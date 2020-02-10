import pygame
import random
from math import sqrt

score = 0
# initialize pygame module
pygame.init()

# create the screen function with 800width and 600height
screen = pygame.display.set_mode((800, 600))

# add a background image
background = pygame.image.load('BG.png')

# add a title to the main window
pygame.display.set_caption("SSSSSSpaceeee IIInvaders")
# create an icon variable with .display.set_ to set window properties
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Add a player graphic, position, function to put on screen
playerimg = pygame.image.load('player.png')
# Add a player starting coordinates
playerX = 400
playerY = 520
# rate of change of position of a player
playerX_change = 0
# puting player on screen, call function after
# calling the screen in main loop
def player(x, y):
	screen.blit(playerimg, (x, y))

# creating an enemy class
class Enemy:
	def __init__(self):
		# Add a enemy graphic, position, function to put on screen
		self.enemyimg = pygame.image.load('enemy.png')
		# rate of change of position of a enemy
		self.enemyX_change = 5
		self.enemyY_change = 50
		# Add a enemy starting coordinates
		self.enemyX = random.randint(0, 710)
		self.enemyY = random.randint(10,100)
# random enemy
randAlien = Enemy()
	
# puting enemy on screen, call function after
# calling the screen in main loop
def enemy(alien):
	screen.blit(alien.enemyimg, (alien.enemyX, alien.enemyY))

# Add a bullet graphic
bulletimg = pygame.image.load('bullet.png')
# Add a bullet starting coordinates
bulletX = 0
bulletY = 500
# rate of change of position of a bullet
bulletY_change = 10
# add a state for ready to shoot or not
# two states, 'fired' for moving bullet and 'ready' for no bullet 
bullet_state = "ready"
# initialiaze bullet on screen
def fire(x):
	# take global value of bullet and change it when fire
	global bullet_state
	bullet_state = "fired"
	# put bullet on screen
	screen.blit(bulletimg,(x+43,bulletY))

# create a colision of bullet and enemy
def check_colision(x1,x2,y1,y2):
	# distance betwen two points>bullet and enemy
	distance = sqrt(pow(x1-x2,2) + pow(y1-y2,2))
	if distance < 35:
		return True

# create a loop for the program
running = True
while running:

	# RGB => Red, Green, Blue color to fill bg
	# range from 0 till 255 check color online
	screen.fill((0,0,0))
	# add a bg img after loading the screen, with 
	# background img and (0,0) position
	screen.blit(background,(0,0))

	
	# write an event for ending game
	for event in pygame.event.get():
		# check for event.type, what is happening in game
		if event.type == pygame.QUIT:
			running = False
		# Keydown as pressing key function
		# check event for keystroke, if its left or right
		if event.type == pygame.KEYDOWN:
			# if key is pressed change the rate of change of position
			if event.key == pygame.K_LEFT:
				playerX_change = -8
			if event.key == pygame.K_RIGHT:
				playerX_change = 8
			# fire bullet on SPACE key
			if event.key == pygame.K_SPACE:
				# check readines of bullet befor shooting
				if bullet_state is "ready":
					# save bullet x coordinate to variable
					bulletX = playerX
					fire(bulletX)
		# Keyup as relising key event
		if event.type == pygame.KEYUP:
			# check event.key for pressing left or right
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0	

	# change position of player and enemy
	playerX += playerX_change
	randAlien.enemyX += randAlien.enemyX_change
	# bullet movement in Y axis after firing
	if bullet_state is "fired":
		fire(bulletX)
		bulletY -= bulletY_change
	# after reaching end screen reset state and position of bullet
	if bulletY <= 0:
		bullet_state = "ready"
		bulletY = 500

	# check for bullet enemy hit/colision
	colision = check_colision(randAlien.enemyX, bulletX, randAlien.enemyY, bulletY)
	if colision:
		# reset bullet
		bullet_state = "ready"
		bulletY = 500
		# if colision occurs generate new enemy and add a poit to score
		randAlien.enemyX = random.randint(0, 710)
		randAlien.enemyY = random.randint(20, 100)
		score += 1
		print(score)


	# boundry function for keeping all on screen
	if playerX < 0:
		playerX = 0
	elif playerX > 750:
		playerX = 750
	if randAlien.enemyX < 0:
		randAlien.enemyX_change =	5
		randAlien.enemyY += randAlien.enemyY_change
	elif randAlien.enemyX >= 750:
		randAlien.enemyX_change = -5
		randAlien.enemyY += randAlien.enemyY_change

	# call player and enemy func/ create player and enemy char
	player(playerX, playerY)

	enemy(randAlien)
	pygame.display.update()


	
