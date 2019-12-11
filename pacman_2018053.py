import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

#NAME        : MOHNISH AGRAWAL
#SECTION     : A
#ROLL NUMBER : 2018053
#GROUP       : 5
#DATE        : 20 NOVEMBER 2018


#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,0.1)
RIGHT = (0.1,0)
TOP = (0,-0.1)
LEFT = (-0.1,0)
NONE = (0,0)
rotate=0
x=0
y=0


#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	walls=pygame.image.load("walls_2018053.png").convert()
	screen.blit(walls,pixels)

#Draws a rectangle for the player
def draw_pacman(screen, pos, cycle): 
	pixels = pixels_from_points(pos)
	if 9<=cycle<=12:
		pacman1=pygame.image.load("pacman1_2018053.png").convert()
		if move_direction==LEFT:
			pacman1=pygame.transform.flip(pacman1,x,y)
		else:	
			pacman1=pygame.transform.rotate(pacman1,rotate)
		screen.blit(pacman1,pixels)
	elif 6<=cycle<9:
		pacman2=pygame.image.load("pacman2_2018053.png").convert()
		if move_direction==LEFT:
			pacman2=pygame.transform.flip(pacman2,x,y)
		else:	
			pacman2=pygame.transform.rotate(pacman2,rotate)
		screen.blit(pacman2,pixels)
	elif 3<=cycle<6:
		pacman3=pygame.image.load("pacman3_2018053.png").convert()
		if move_direction==LEFT:
			pacman3=pygame.transform.flip(pacman3,x,y)
		else:	
			pacman3=pygame.transform.rotate(pacman3,rotate)
		screen.blit(pacman3,pixels)
	else:
		pacman4=pygame.image.load("pacman4_2018053.png").convert()
		if move_direction==LEFT:
			pacman4=pygame.transform.flip(pacman4,x,y)
		else:	
			pacman4=pygame.transform.rotate(pacman4,rotate)
		screen.blit(pacman4,pixels)
#To Draw Kong
def draw_kong(screen,pos,cycle2):
	pixels = pixels_from_points(pos)
	kong1 = pygame.image.load("D_K1_2018053.png").convert()
	if cycle>3:
		screen.blit(kong1,pixels)
	else:
		kong2= pygame.transform.flip(kong1,1,0)
		screen.blit(kong2,pixels)

#Enemy's movement
def kong_movement(layout,kong_position,move_direction_kong,arr2,Random):

	if abs(round(kong_position[1])-kong_position[1])<=0.000001 and (abs(round(kong_position[0])-kong_position[0])<=0.00001):
		arr=[1,-1,2,-2]
		if layout[round(kong_position[1])][int(kong_position[0])+1] == 'w':
			arr.remove(1)
		if layout[round(kong_position[1])][int(kong_position[0])-1] == 'w':
			arr.remove(-1)
		if layout[int(kong_position[1])-1][round(kong_position[0])] == 'w':
			arr.remove(2)
		if layout[int(kong_position[1])+1][round(kong_position[0])] == 'w':
			arr.remove(-2)
		arr2=list(arr)

		if -Random in arr and len(arr)>1:
			arr.remove(-Random)
		if len(arr)>0:
			Random=random.choice(arr)
		if Random==0:
			move_direction_kong=NONE
		if Random==1:
			move_direction_kong=RIGHT
		if Random==-1:
			move_direction_kong=LEFT
		if Random==2:
			move_direction_kong=TOP
		if Random==-2:
			move_direction_kong=DOWN	
		if pacman_position[0]==round(kong_position[0]):
			count=0
			if pacman_position[1]<kong_position[1]:
				for i in range(int(pacman_position[1]),int(kong_position[1])):
					if layout[i][int(pacman_position[0])]!='w':
						count+=1
			if pacman_position[1]>kong_position[1]:
				for i in range(int(kong_position[1]),int(pacman_position[1])):
					if layout[i][int(pacman_position[0])]!='w':
						count+=1
			if count==abs(int(pacman_position[1])-int(kong_position[1])):
				if kong_position[1]<pacman_position[1]:
					
					move_direction_kong=DOWN
				if kong_position[1]>pacman_position[1]:
					move_direction_kong=TOP
		elif pacman_position[1]==round(kong_position[1]):
			count=0
			if pacman_position[0]<kong_position[0]:
				for i in range(int(pacman_position[0]),int(kong_position[0])):
					if layout[int(pacman_position[1])][i]!='w':
						count+=1
			if pacman_position[0]>kong_position[0]:
				for i in range(int(kong_position[0]),int(pacman_position[0])):
					if layout[int(pacman_position[1])][i]!='w':
						count+=1
			if count==abs(int(pacman_position[0])-int(kong_position[0])):
				if kong_position[0]>pacman_position[0]:
					move_direction_kong=LEFT
				if kong_position[0]<pacman_position[0]:
					move_direction_kong=RIGHT

	if layout[round(kong_position[1])][int(kong_position[0])+1] == 'w' and move_direction_kong == RIGHT:
		move_direction_kong=NONE
		
	if layout[round(kong_position[1])][int(kong_position[0])] == 'w' and move_direction_kong == LEFT:	
		move_direction_kong=NONE
		
	if layout[int(kong_position[1])+1][round(kong_position[0])] == 'w' and move_direction_kong == DOWN:
		move_direction_kong=NONE
		
	if layout[int(kong_position[1])][round(kong_position[0])] == 'w' and move_direction_kong == TOP:
		move_direction_kong=NONE

	if move_direction_kong==TOP or move_direction_kong==DOWN:
	 	kong_position=(round(kong_position[0]),kong_position[1])
	if move_direction_kong==LEFT or move_direction_kong==RIGHT:
		kong_position=(kong_position[0],round(kong_position[1]))

	return move_direction_kong,arr2,Random,kong_position


#Draws a circle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pixels=(pixels[0]+16,pixels[1]+16)
	pygame.draw.circle(screen, COIN_COLOR, pixels ,5)

#Uitlity functions
def add_to_pos(pos, pos2):
	return (round(pos[0],1)+round(pos2[0],1), round(pos[1],1)+round(pos2[1],1))

def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((640,672), 0, 32)
background = pygame.surface.Surface((640,672)).convert()
pygame.display.set_caption("PACMAN")

pacman=pygame.image.load("pacman3_2018053.png").convert()

#Initializing variables
layout = loadtxt('layout_2018053.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
kong_position =(8,9)
kong_position_2nd =(9,9)
kong_position_3=(10,9)
kong_position_4=(11,9)
background.fill((0,0,0))


coin=0
for col in range(cols):
	for row in range(rows):
		value = layout[row][col]
		if value == 'c':
			coin+=1
			
text=pygame.image.load("text_box_2018053.png").convert()
score=0
cycle=12
cycle2=6
cycle3=1
move_direction_kong = NONE
move_direction_kong_2nd=NONE
move_direction_kong_3=NONE
move_direction_kong_4=NONE
Random_4=0
Random_3=0
Random_2nd=0
move_direction = NONE 
Random=-2
arr2=[]
arr3=[]
arr4=[]
arr5=[]
lives=4
start_menu=pygame.image.load("start_menu_2018053.png")
start=False
lose=pygame.image.load("lose_2018053.png")
clock=pygame.time.Clock()
end=False
counter=3
time_passed=0
win=pygame.image.load("win_2018053.png")
wall_open=0

# Main game loop
while True:
	all_path=[0,1,2,3]
	clock.tick(35)
	time_passed+=35
	wall_open+=35
	startf=pygame.font.SysFont('freesans',30,True)

	# pygame.time.delay(40)
	for event in pygame.event.get():
	 	if event.type == QUIT:
	 		exit()
	 	if event.type == pygame.K_p:
	 		start=True

	while not start:
		screen.blit(start_menu,(0,0))
		startfont=startf.render("Press P to Play",True,(255,255,255))
		screen.blit(startfont,(100,400))
		startfont=startf.render('Press Q to Quit',True,(255,255,255))
		screen.blit(startfont,(100,440))
		pygame.display.update()
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
		 	if event.type == QUIT:
		 		exit()
		if keys[pygame.K_p]:
			start = True
		if keys[pygame.K_q]:
			exit()


	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  	#In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos)

	#Draw the player and enemy
	draw_pacman(screen, pacman_position, cycle)
	draw_kong(screen, kong_position, cycle2)
	draw_kong(screen,kong_position_2nd,cycle2)
	draw_kong(screen,kong_position_3,cycle2)
	draw_kong(screen,kong_position_4,cycle2)

	score_text="Score : "+str(score*10)
	myfont= pygame.font.SysFont('TemuInlineGrunge_2018053.otf',28,
		True,True)
	font=myfont.render(score_text,False,(127,117,18))
	screen.blit(text,(260,0))
	screen.blit(font,(270,5))

	position_lives=0
	for i in range(lives):
		screen.blit(pacman,(576-position_lives,640))
		position_lives+=40
	pygame.display.update()
	counter_pos=0
	while counter!=-1:
		time=startf.render(str(counter),True,(0,0,0))
		if counter==0:
			time=startf.render("Go!",True,(0,0,0))
		screen.blit(time,(1+counter_pos,1))
		counter-=1
		counter_pos+=32
		time_passed+=1000
		pygame.display.update()
		pygame.time.delay(1000)

	if cycle<=12:
		cycle-=1
	if cycle==0:
		cycle=12
	if cycle2<=6:
		cycle2-=1
	if cycle2==0:
		cycle2=6

	pygame.display.update()
	kong_position=add_to_pos(kong_position,move_direction_kong)
	kong_position_2nd=add_to_pos(kong_position_2nd,move_direction_kong_2nd)
	kong_position_3=add_to_pos(kong_position_3,move_direction_kong_3)
	kong_position_4=add_to_pos(kong_position_4,move_direction_kong_4)

	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
	#Update player position based on movement.
	keys=pygame.key.get_pressed()
	if keys[pygame.K_s]:
		move_direction = DOWN
		rotate=-90
	if keys[pygame.K_w]:
		move_direction = TOP
		rotate=90
	if keys[pygame.K_a]:
		move_direction = LEFT
		x=1
		y=0
	if keys[pygame.K_d]:
		move_direction = RIGHT
		rotate=0

	#TO close the wall so the enemies dont get into the box
	if wall_open>1995:	
		move_direction_kong,arr2,Random,kong_position=kong_movement(layout,kong_position,move_direction_kong,arr2,Random)
		move_direction_kong_2nd,arr3,Random_2nd,kong_position_2nd=kong_movement(layout,kong_position_2nd,move_direction_kong_2nd,arr3,Random_2nd)
		move_direction_kong_3,arr4,Random_3,kong_position_3=kong_movement(layout,kong_position_3,move_direction_kong_3,arr4,Random_3)
		move_direction_kong_4,arr5,Random_4,kong_position_4=kong_movement(layout,kong_position_4,move_direction_kong_4,arr5,Random_4)


	if (int(kong_position[0]),int(kong_position[1])) not in [(8,9),(9,9),(10,9),(11,9),(9,8),(10,8)] and (int(kong_position_2nd[0]),int(kong_position_2nd[1])) not in [(8,9),(9,9),(10,9),(11,9),(9,8),(10,8)] and (int(kong_position_3[0]),int(kong_position_3[1])) not in [(8,9),(9,9),(10,9),(11,9),(9,8),(10,8)] and (int(kong_position_4[0]),int(kong_position_4[1])) not in [(8,9),(9,9),(10,9),(11,9),(9,8),(10,8)]:
		layout[8][9]='w'
		layout[8][10]='w'

	#Determines the lives of the player left and displays the lose menu if the player loses
	if round(kong_position[0])==round(pacman_position[0]) and round(kong_position[1])==round(pacman_position[1]) or round(kong_position_2nd[0])==round(pacman_position[0]) and round(kong_position_2nd[1])==round(pacman_position[1]) or round(kong_position_3[0])==round(pacman_position[0]) and round(kong_position_3[1])==round(pacman_position[1]) or round(pacman_position[0])==round(kong_position_4[0]) and round(pacman_position[1])==round(kong_position_4[1]):
		lives-=1
		layout[8][9]='.'
		layout[8][10]='.'
		wall_open=0
		kong_position=(8,9)
		move_direction_kong=NONE
		kong_position_2nd=(9,9)
		move_direction_kong_2nd=NONE
		kong_position_3=(10,9)
		move_direction_kong_3=NONE
		kong_position_4=(11,9)
		move_direction_kong_4=NONE
		counter=3
		pygame.display.update()
		if lives==0:
			screen.blit(lose,(0,0))
			time_passed=round(time_passed/1000)
			min=time_passed//60
			if time_passed%60==0:
				elapsed_time=str(min)+":00"
			else:
				elapsed_time=str(min)+":"+str("%02d"%(time_passed-min*60))
			elap_time=startf.render("Elapsed Time- "+elapsed_time,True,(19,193,22))
			score2=startf.render("Final Score- "+str(score*10),True,(19,193,22))
			screen.blit(elap_time,(100,440))
			screen.blit(score2,(100,480))
			pygame.display.update()
			while not end:
				keys = pygame.key.get_pressed()
				for event in pygame.event.get():
				 	if event.type == QUIT:
				 		exit()
				if keys[pygame.K_r]:
					pacman_position=(1,1)
					end = True
					score=0
					lives=4
					layout = loadtxt('layout_2018053.txt', dtype=str)
					rows, cols = layout.shape
					time_passed=0
				if keys[pygame.K_q]:
					exit()
		end=False
		continue

	#adding constraints to pacman movements so that it does not pass through walls
	pacman_position1 = add_to_pos(pacman_position, move_direction)

	if layout[round(pacman_position1[1])][int(pacman_position1[0])+1] == 'w' and move_direction == RIGHT:
		continue
	if layout[round(pacman_position1[1])][int(pacman_position1[0])] == 'w' and move_direction == LEFT:
		continue
	if layout[int(pacman_position1[1])+1][round(pacman_position1[0])] == 'w' and move_direction == DOWN:
		continue
	if layout[int(pacman_position1[1])][round(pacman_position1[0])] == 'w' and move_direction == TOP:
		continue

	if move_direction==TOP or move_direction==DOWN:
	 	pacman_position=(round(pacman_position1[0]),pacman_position1[1])
	if move_direction==LEFT or move_direction==RIGHT:
		pacman_position=(pacman_position1[0],round(pacman_position1[1]))

	if layout[round(pacman_position[1])][round(pacman_position[0])]=='c':
		score+=1
		layout[round(pacman_position[1])][round(pacman_position[0])]='.'


	pygame.display.update()

	#if player wins, display win menu
	if score == coin : 
		wall_open=0
		layout[8][9]='.'
		layout[8][10]='.'
		screen.blit(win,(0,0))
		time_passed=round(time_passed/1000)
		min=time_passed//60
		if time_passed%60==0:
			elapsed_time=str(min)+":00"
		else:
			elapsed_time=str(min)+":"+str("%02d"%(time_passed-min*60))
		win_text=startf.render("YOU WIN NERD!",True,(19,193,22))
		elap_time=startf.render("Elapsed Time- "+elapsed_time,True,(19,193,22))
		score2=startf.render("Final Score- "+str(score*10),True,(19,193,22))
		screen.blit(win_text,(100,100))
		screen.blit(elap_time,(100,150))
		screen.blit(score2,(100,190))
		pygame.display.update()
		while not end:
			keys = pygame.key.get_pressed()
			for event in pygame.event.get():
			 	if event.type == QUIT:
			 		exit()
			if keys[pygame.K_r]:
				pacman_position=(1,1)
				move_direction=NONE
				kong_position=(8,9)
				move_direction_kong=NONE
				pacman_position=(1,1)
				kong_position_2nd=(9,9)
				move_direction_kong_2nd=NONE
				kong_position_3=(10,9)
				move_direction_kong_3=NONE
				kong_position_4=(11,9)
				move_direction_kong_4=NONE
				counter=3
				end = True
				score=0
				lives=4
				layout = loadtxt('layout_2018053.txt', dtype=str)
				rows, cols = layout.shape
				time_passed=0
			if keys[pygame.K_q]:
				exit()
		end=False
		continue

	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array

	#Update the display
	#Wait for a while, computers are very fast.