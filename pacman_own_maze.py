#
# NAME :Ｃｈａｎｇ　Ｈｏｎｇ　Ｙｕａｎ
# ID: 20561464
#
import turtle
import math
import random

# Setup the turtle window
turtle.setup(800, 700)
turtle.title("COMP1021 - Pacman")
turtle.bgcolor("black")

# Setup the turtle
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Define the ghost information
ghost_size = 30
ghost_speed = 6
ghost_start_x = 0
ghost_start_y = 0
ghosts = []
number_of_ghost = 10
colors = [ "red", "Aqua", "pink", "Lawngreen", "Salmon", "Navy", "Olive", "Chocolate", "Darkmagenta", "Turquoise"] 
# Define the game timing (30 frames per second)
frame_time = 1000 // 30

# Define the maze information
maze_x       = -300
maze_y       = -270
maze_columns = 21
maze_rows    = 19

# Define the tile information
tile_size = 30

# Define the food information
food_size  = 10

# Define the pacman information
pacman_size  = 30
pacman_speed = 6
pacman_x     = 0
pacman_y     = 0

# Create the variables for the pacman movement
current_move = ""   # This is the current movement
next_move = ""      # This is the next movement


# Maze of the game
#   + : wall
#   . : food
#   o : power food
#   P : starting position of pacman
#   G : starting position of ghosts
maze = [
	#012345678901234567890 - total 21 columns
	"+++++++++o+o+++++++++", # 0
	"+...................+", # 1
	"+......+++++++......+", # 2
	"+oooooo+..G...oooooo+", # 3
	"+......+............+", # 4
	"+......+............+", # 5
	"+oooooo+++++++oooooo+", # 6
	"+...................+", # 7
	"+......+.....+......+", # 8
	"+oooooo+.....+oooooo+", # 9
	"+......+++++++......+", # 10
	"+......+.....+......+", # 11
	"+oooooo+.....+oooooo+", # 12
	"o...................o", # 13
	"+......+.....+......+", # 14
	"+oooooo+..P..+oooooo+", # 15
	"+......+++++++......+", # 16
	"+.........+.........+", # 17
	"+++++++++o+o+++++++++"  # 18 - total 19 rows
]
win_condition = 0
point = 0

#
# Task 1 - Draw the maze


for i in range(maze_columns):
	for j in range(maze_rows):
		# Get the tile
		tile = maze[j][i]

		# Task 1.1 - Locate the tile and move to the tile position
		#
		# - Find the x, y position of the tile in the turtle window
		# - Put the turtle to the tile position
		tile_x = maze_x + i * tile_size
		tile_y = maze_y + (maze_rows - j -1) * tile_size
		turtle.goto(tile_x, tile_y)
		# Task 1.2 - Draw the tiles according to the tile symbol
		#
		# - Draw the tiles for walls, food and power food
		# - Initialize the position of pacman
		if tile == "+": #wall
			turtle.shape("square")
			turtle.color("blue", "black")
			turtle.shapesize(tile_size/20, tile_size/20, 3)
			turtle.stamp()
		
		elif tile == ".":#food
			
			turtle.pencolor("yellow")
			turtle.dot(food_size/2)
			win_condition += 1
		
		elif tile == "o": #power_food
			turtle.pencolor("white")
			turtle.dot(food_size)		
			win_condition += 5
		elif tile == "P": #pacman
			pacman_x = tile_x
			pacman_y = tile_y
			
		elif tile == "G":
			ghost_start_x = tile_x
			ghost_start_y = tile_y
		

# Task 2.1 - Create the pacman turtle
#
# - Use turtle.Turtle() to make your pacman
# - Make a yellow turtle circle shape as your pacman
# - Put your pacman at the starting position
pp = turtle.Turtle()
pp.up()
pp.goto(pacman_x, pacman_y)


#create ghosts
for i in range(number_of_ghost):
	ghost = { "turtle": turtle.Turtle(), "move" : " "}
	ghost["turtle"].pencolor(colors[i])
	ghost["turtle"].up()
	ghost["turtle"].goto(ghost_start_x, ghost_start_y)
	ghost["turtle"].hideturtle()
	ghosts.append(ghost)

#score

score = turtle.Turtle()
turtle.goto(maze_x - tile_size/2, maze_y + tile_size*(maze_rows-0.5))
turtle.pencolor("yellow")
turtle.write("score:", font=("Arial", 25, "bold"))
score.goto(maze_x - tile_size/2, maze_y + tile_size*(maze_rows-0.5))
score.hideturtle()
score.pencolor("yellow")
score.write("0", font=("Arial", 25, "bold"))


# Task 2.2 - Handle the movement keys
#
# - Complete the down, left and right movement keys for the pacman
#   (the up movement has been given to you)

# Handle the "Up" key for moving up
def move_up():
	global next_move
	next_move = "up"

def move_down():
	global next_move
	next_move = "down"

def move_right():
	global next_move
	next_move = "right"
	
def move_left():
	global next_move
	next_move = "left"
	
def draw_pacman(a, b):
	global v 
	
	pp.down()
	if v == 0:
		pp.fillcolor("yellow")
	else :
		pp.fillcolor("green")
	pp.setheading(a + 90 * b)
	pp.begin_fill()
	pp.fd(pacman_size/2)
	pp.lt(90)
	pp.circle(pacman_size/2, 360 - 2*a)
	pp.lt(90)
	pp.fd(pacman_size/2)
	pp.end_fill()
	pp.up()
	
v = 0	

def invincable():
		global v
		v = 1
		turtle.onkeypress(normal, "c")
def normal():
		global v
		v = 0
		turtle.onkeypress(invincable, "c")
def draw_ghost(number, direction):
	ghosts[number]["turtle"].setheading(0)
	ghosts[number]["turtle"].color(colors[number])
	ghosts[number]["turtle"].dot(ghost_size)
	ghosts[number]["turtle"].pencolor("white")
	ghosts[number]["turtle"].up()
	ghosts[number]["turtle"].fd(ghost_size/4)
	ghosts[number]["turtle"].dot(ghost_size/2)
	ghosts[number]["turtle"].lt(direction * 90)
	ghosts[number]["turtle"].fd(ghost_size/8)
	ghosts[number]["turtle"].pencolor("red")
	ghosts[number]["turtle"].dot(ghost_size/4)
	ghosts[number]["turtle"].fd(-ghost_size/8)
	ghosts[number]["turtle"].rt(direction*90)
	
	ghosts[number]["turtle"].fd(-ghost_size/2)
	ghosts[number]["turtle"].pencolor("white")
	ghosts[number]["turtle"].dot(ghost_size/2)
	ghosts[number]["turtle"].lt(direction * 90)
	ghosts[number]["turtle"].fd(ghost_size/8)
	ghosts[number]["turtle"].pencolor("red")
	ghosts[number]["turtle"].dot(ghost_size/4)
	ghosts[number]["turtle"].fd(-ghost_size/8)
	ghosts[number]["turtle"].rt(direction*90)
	

# Set up the key press events
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_left, "Left")
# Need to use listen for key events to work
turtle.listen()


# This is the game main loop, which is mainly used to:
#
# - Determine the movement of pacman
# - Determine if pacman hits a wall or food
d = 0
m = int()
gap =  5
def game_loop():
	global current_move, next_move
	global pacman_x, pacman_y
	global m
	global d
	global gap
	global point
	
	n = 0
	pp.clear()
	# Task 2.4 - Handle the pacman next move
	#
	# - Update the condition of the following if statement so that
	#   pacman can only move along the rows and columns of the maze
	if next_move != "" and (pacman_x - maze_x)% tile_size == 0 and  (pacman_y - maze_y)% tile_size == 0:
		current_move = next_move
		next_move = ""


	# Task 2.3 - Find the pacman new position
	#
	# - Complete the down, left and right moves
	#   (the up move has been given to you)
	if current_move == "up":
		new_x = pacman_x
		new_y = pacman_y + pacman_speed
		d = 1
		#current_move = ""
	elif current_move == "down":
		new_x = pacman_x
		new_y = pacman_y - pacman_speed
		d = 3
		#current_move = ""
	elif current_move == "right":
		new_x = pacman_x + pacman_speed
		new_y = pacman_y
		d = 0
		#current_move = ""
	elif current_move == "left":
		new_x = pacman_x - pacman_speed
		new_y = pacman_y 
		d = 2
		#current_move = ""
	else:
		new_x = pacman_x
		new_y = pacman_y
	
	
	#
	# Task 3 - Handle the collision of pacman, food and walls
	#
	for i in range(maze_columns):
		for j in range(maze_rows):
			# Get the tile
			tile = maze[j][i]

			# Task 3.1 - Locate the tile and calculate the distance
			#
			# - Find the x, y position of the tile in the turtle window
			# - Find the distance between pacman and the tile in dx, dy
			dx = math.fabs(new_x - (maze_x + i * tile_size))
			dy = math.fabs(new_y - (maze_y + (maze_rows - j -1) * tile_size))

			# Task 3.2 - Collision detection
			#
			# - If pacman collides with any wall, stop pacman from moving
			# - If pacman collides with any food, eat the food (remove the food)
			if dx < (pacman_size + tile_size) / 2 and dy < (pacman_size + tile_size) / 2 and tile == "+":
				new_x = pacman_x
				new_y = pacman_y
				
			if dx < (pacman_size + food_size/2) / 2 and dy < (pacman_size + food_size/2) / 2 and tile == ".":
				maze[j] = maze[j][:i]+" "+ maze[j][i+1:]
				turtle.goto(maze_x + i * tile_size, maze_y + (maze_rows - j -1) * tile_size)
				turtle.pencolor("black")	
				turtle.dot(food_size/2)
				point += 1
			if dx < (pacman_size + food_size) / 2 and dy < (pacman_size + food_size) / 2 and tile == "o":
				maze[j] = maze[j][:i]+" "+ maze[j][i+1:]
				maze[j] = maze[j][:i]+" "+ maze[j][i+1:]
				turtle.goto(maze_x + i * tile_size, maze_y + (maze_rows - j -1) * tile_size)
				turtle.pencolor("black")	
				turtle.dot(food_size)
				point += 5
				
	#invisable tunnel
	if  maze_x > new_x :
		new_x = new_x + (maze_columns-1) * tile_size
	elif  maze_x + (maze_columns-1) * tile_size < new_x :
		new_x = maze_x
	elif maze_y > new_y:
		new_y = maze_y +( maze_rows-1) * tile_size
	elif  maze_y + (maze_rows-1) * tile_size < new_y :
		new_y = maze_y


	# Task 2.3 - Move the pacman
	#
	# - Move pacman to the new position
	# - Update pacman_x and pacman_y
	
	pp.goto(new_x, new_y)			
	pacman_x = new_x
	pacman_y = new_y
	
	if m == 30 :
		gap = -5
	if m == 0:
		gap = 5
		
		
		
	draw_pacman(m, d)
	m  = m + gap
	
	pp.hideturtle()
	
	# move the ghost
	for ghost in ghosts:
		ghost_x = ghost["turtle"].xcor()
		ghost_y = ghost["turtle"].ycor()
		ghost_current_move = ghost["move"]
		move_list = []
		ghost["turtle"].clear()
		g_d = int()
		
		if ghost_current_move == "up":
			ghost_x = ghost_x
			ghost_y = ghost_y + ghost_speed
			g_d = 1
		
		elif ghost_current_move == "down":
			ghost_x = ghost_x
			ghost_y = ghost_y - ghost_speed
			g_d = 3
		
		elif ghost_current_move == "right":
			ghost_x  = ghost_x + ghost_speed
			ghost_y = ghost_y
			g_d = 0
		
		elif ghost_current_move == "left":
			ghost_x  = ghost_x - ghost_speed
			ghost_y = ghost_y
			g_d = 2
		
		elif ghost_current_move == " ":
			ghost_x  = ghost_x
			ghost_y = ghost_y
		ghost["turtle"].goto(ghost_x, ghost_y)
		
		draw_ghost(n, g_d)
		n += 1
		ghost["turtle"].goto(ghost_x, ghost_y)
		if (ghost_x - maze_x) % tile_size == 0 and (ghost_y - maze_y) % tile_size == 0:
			i = int((ghost_x - maze_x) / tile_size)
			j = int(-1*((ghost_y - maze_y) / tile_size)  + maze_rows - 1)
			
			#look left
			if maze[j][i-1] != "+" and i > 0:
				move_list.append("left")
			#look right
			if i < 20:
			
				if maze[j][i+1] != "+" :
					move_list.append("right")
			#look up
			if j < 18:
				if maze[j+1][i] != "+" :
					move_list.append("down")
			#look down
			if maze[j-1][i] != "+" and j > 0:
				move_list.append("up")
				
			
			if len(move_list) > 1:
				if ghost_current_move == "right" and "left" in move_list:
					move_list.remove("left")
				elif ghost_current_move == "left"and "right" in move_list:
					move_list.remove("right")
				elif ghost_current_move == "up"and "down" in move_list:
					move_list.remove("down")
				elif ghost_current_move == "down"and "up" in move_list:
					move_list.remove("up")
			
			
			ghost["move"] = random.choice(move_list)		
			
			
			
	score.goto(maze_x - tile_size/2+110, maze_y + tile_size*(maze_rows-0.5))	
	score.clear()
	score.write(point, point, font=("Arial", 25, "bold"))
		
	
	# Update the window content
	turtle.update()
	
	#end game condition
		#ghost catch the pacman
	for ghost in ghosts:
		ghost_x = ghost["turtle"].xcor()
		ghost_y = ghost["turtle"].ycor()
		dx = math.fabs(pacman_x - ghost_x)
		dy = math.fabs(pacman_y - ghost_y)
		dd = math.sqrt(dx**2+ dy**2)
		if dd < (pacman_size + ghost_size)/2 and v == 0:
			turtle.goto(-180, 0)
			turtle.pencolor("red")
			turtle.write("Game over!!!", font=("Arial", 50, "bold"))
			return
	
	if point == win_condition:
		turtle.goto(-150, 0)
		turtle.pencolor("White")
		turtle.write("You Win!!!", font=("Arial", 50, "bold"))
		return
	
	
	# Keep on running the game loop
	turtle.ontimer(game_loop, frame_time)
# cheat key
turtle.listen()
turtle.onkeypress(invincable, "c")	
# Start the game loop
game_loop()

turtle.done()
