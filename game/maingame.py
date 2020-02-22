import pygame
# import mixer to create a sound effects in game
from pygame import mixer
import random
from math import sqrt

# initialize pygame module
pygame.init()

# create the screen function with 800width and 600height
screen = pygame.display.set_mode((800, 600))

# writing a  clock for timing and fps count
clock = pygame.time.Clock()

# add a background image
background = pygame.image.load('graphics/BG.png')
# add a bg sound load .wav file for sound
mixer.music.load('sound/bg.wav')
# add a bullet sound at space when bullet is ready
bulletSound = mixer.Sound('sound/pew.wav')
# add a sound on bullet collision with alien
colisionSound = mixer.Sound('sound/explosion.wav')
# play music once, for looping infinitely ad -1 argument
mixer.music.play(-1)

# add a title to the main window
pygame.display.set_caption("SSSSSSpaceeee IIInvaders")
# create an icon variable with .display.set_ to set window properties
icon = pygame.image.load('graphics/icon.png')
pygame.display.set_icon(icon)

# Add a player graphic, position, function to put on screen
playerimg = [
		pygame.image.load('graphics/player/player-1.png'),
		pygame.image.load('graphics/player/player-2.png'),
		pygame.image.load('graphics/player/player-3.png'),
		pygame.image.load('graphics/player/player-4.png'),
		]

# Add a player starting coordinates
playerX = 400
playerY = 520
# rate of change of position of a player
playerX_change = 0

# add a score text on screen, function
score = 0
# chose font and font size for text displayed
font = pygame.font.Font('freesansbold.ttf', 25)
def viewScore():
	# render font, True value for display, choose RGB color
	scored = font.render("Score : {}".format(score), True, (30,200,20))
	# add on screen scored layer
	screen.blit(scored, (10, 10))

# creating an enemy class
class Enemy:
	def __init__(self):
		# Add a enemy graphics from files
		self.img = [
				pygame.image.load('graphics/enemy/enemy-1.png'),
				pygame.image.load('graphics/enemy/enemy-2.png'),
				pygame.image.load('graphics/enemy/enemy-3.png'),
				pygame.image.load('graphics/enemy/enemy-4.png'),
				]
		# add enemy height and width
		self.width = 64
		self.height = 64
		# rate of change of position of a enemy
		self.Xchange = random.randint(2,10)
		self.Ychange = 50
		# Add a enemy starting coordinates
		self.X = random.randint(0, 710)
		self.Y = random.randint(0,50)
	# puting enemy in window, call function after
	def generate(self, num):
		screen.blit(self.img[(num//15)-1], (self.X, self.Y))
		
# list of all created enemies
Enemies = [Enemy() for i in range(6)]


# Add a bullet graphic
bulletimg = pygame.image.load('graphics/bullet.png')
# Add a bullet starting coordinates
bulletX = 0
bulletY = 500
# rate of change of position of a bullet
bulletY_change = 20
# add a state for ready to shoot or not
# two states, 'fired' for moving bullet and 'ready' for no bullet 
bullet_state = "ready"
# initialiaze bullet on screen
def fire(x):
	# take global value of bullet and change it when fire
	global bullet_state
	bullet_state = "fired"
	# put bullet on screen
	screen.blit(bulletimg,(x+58,bulletY))

# create a colision of bullet and enemy
def check_colision(x1,x2,y1,y2):
	# distance betwen two points>bullet and enemy
	distance = sqrt(pow(x1-x2,2) + pow(y1-y2,2))
	if distance < 35:
		return True

# variable for counting image changes in time
ImgChange = 0
# background img and (0,0) position
def redrawWindow(playerX, playerY):
	global ImgChange 
	screen.blit(background,(0,0))
	# counting to 5 fps with ImgChange var for changing obj pics
	if ImgChange > 60:
		ImgChange = 0
	# puting player on screen
	# list/ array of images to display in sequence, for now just 0 index
	screen.blit(playerimg[(ImgChange//15)-1], (playerX, playerY))
	ImgChange += 1
	for Alien in Enemies:
		# put enemie on screen
		Alien.generate(ImgChange)


# create a loop for the program
running = True
while running:

	# adding fps ration with clock tick
	clock.tick(60)

	# drawing all on screen
	redrawWindow(playerX, playerY)
	
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
				playerX_change = -13
			if event.key == pygame.K_RIGHT:
				playerX_change = 13
			# fire bullet on SPACE key
			if event.key == pygame.K_SPACE:
				# check readines of bullet befor shooting
				if bullet_state is "ready":
					# play bullet sound saved at begining
					#bulletSound.play()
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
	# bullet movement in Y axis after firing
	if bullet_state is "fired":
		fire(bulletX)
		bulletY -= bulletY_change
	# after reaching end screen reset state and position of bullet
	if bulletY <= 0:
		bullet_state = "ready"
		bulletY = 500

	# boundry function for keeping all on screen
	if playerX < 0:
		playerX = 0
	elif playerX > 750:
		playerX = 750

	# aliens movement function for list Enemies in line 46
	for Alien in Enemies:
		Alien.X += Alien.Xchange
		if Alien.X < 0:
			Alien.Xchange =	-Alien.Xchange
			Alien.Y += Alien.Ychange
		elif Alien.X >= 750:
			Alien.Xchange = -Alien.Xchange
			Alien.Y += Alien.Ychange
		# check for bullet enemy hit/colision
		colision = check_colision(Alien.X, bulletX, Alien.Y, bulletY)
		if colision:
			# play sound of colision
			# colisionSound.play()
			# reset bullet
			bullet_state = "ready"
			bulletY = 500
			# if colision occurs generate new enemy and add a point to score
			Alien.X = random.randint(0, 710)
			Alien.Y = random.randint(20, 100)
			# change alien speed
			Alien.Xchange = random.randint(2,10)
			score += 1

	# call score function to put score on screen
	viewScore()

	pygame.display.update()


pygame.quit()
	
