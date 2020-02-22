import pygame as pg
# import mixer to create a sound effects in game
from pygame import mixer
from data.cls import *
import random
from math import sqrt

# initialize pygame module
pg.init()
# main loop variable for quiting
running = True
# create the screen function with 800width and 600height
MainWindow = pg.display.set_mode((800, 600))

# writing a  clock for timing and fps count
clock = pg.time.Clock()
# variable for counting image changes in time
ImgChange = 0
# add a score text on screen, function
score = 0
# number of bullet shot for bullet count and accuracy
ProjectileNumber = 0
Accuracy = 0
# list of all created enemies
Enemies = [Enemy() for i in range(6)]
# list of all bullets shot
Projectiles = [
		Bullet(),
		Bullet()
		]
# creating a player object
Player = Player()

# chose font and font size for text displayed
font = pg.font.Font('freesansbold.ttf', 25)
# add a background image
background = pg.image.load('graphics/BG.png')
# add a bg sound load .wav file for sound
mixer.music.load('sound/bg.wav')
# add a bullet sound at space when bullet is ready
bulletSound = mixer.Sound('sound/pew.wav')
# add a sound on bullet collision with alien
colisionSound = mixer.Sound('sound/explosion.wav')
# play music once, for looping infinitely ad -1 argument
mixer.music.play(-1)

# add a title to the main window
pg.display.set_caption("SSSSSSpaceeee IIInvaders")
# create an icon variable with .display.set_ to set window properties
icon = pg.image.load('graphics/icon.png')
pg.display.set_icon(icon)


def redrawWindow():
	global ImgChange 
	# background img and (0,0) position
	MainWindow.blit(background,(0,0))
	# render font, True value for display, choose RGB color
	scored = font.render("Score : {}".format(score), True, (30,200,20))
	# add on screen scored layer
	MainWindow.blit(scored, (10, 10))
	
	# counting to 5 fps with ImgChange var for changing obj pics
	if ImgChange > 60:
		ImgChange = 0
	# puting player on screen
	# list/ array of images to display in sequence
	MainWindow.blit(Player.img[(ImgChange//15)-1], (Player.X, Player.Y))
	ImgChange += 1
	for Alien in Enemies:
		# put enemie on screen
		Alien.generate(ImgChange, MainWindow)
	for Bullet in Projectiles:
		Bullet.fired(MainWindow)

# player movement function
def PlayerPositionCheck():
	global ProjectileNumber, Projectiles, running
	# write an event for ending game
	for event in pg.event.get():
		# check for event.type, what is happening in game
		if event.type == pg.QUIT:
			running = False
		# Keydown as pressing key function
		# check event for keystroke, if its left or right
		if event.type == pg.KEYDOWN:
			# if key is pressed change the rate of change of position
			if event.key == pg.K_LEFT:
				Player.Xchange = -13
			if event.key == pg.K_RIGHT:
				Player.Xchange = 13
			# fire bullet on SPACE key
			if event.key == pg.K_SPACE:
				#########################
				#PLACE TO ADD A PROJECTILES GENERATION
				########################
				for Bullet in Projectiles:
					# check readines of bullet befor shooting
					if Bullet.state is "ready":
						# play bullet sound saved at begining
						#bulletSound.play()
						# save bullet x coordinate to variable
						Bullet.fire(MainWindow, Player.X, ProjectileNumber)
						# add a projectile to count
						ProjectileNumber += 1
						break
		# Keyup as relising key event
		if event.type == pg.KEYUP:
			# check event.key for pressing left or right
			if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
				Player.Xchange = 0	

	# change position of player
	Player.X += Player.Xchange
	# boundry function for keeping all on screen
	if Player.X < 0:
		Player.X = 0
	elif Player.X > 750:
		Player.X = 750

# create a colision of bullet and enemy
def CheckColision(Alien,Bullet):
	# distance betwen two points>bullet and enemy
	distance = sqrt(pow(Alien.X+Alien.width/2-Bullet.X,2) + \
			pow(Alien.Y+Alien.height/2-Bullet.Y,2))
	if distance < 32:
		return True
		
# aliens movement function for every enemy in list Enemies in line 46
def AlienPositionCheck():
	global score, Enemies, Projectiles
	for Alien in Enemies:
		Alien.X += Alien.Xchange
		if Alien.X < 0:
			Alien.Xchange =	-Alien.Xchange
			Alien.Y += Alien.Ychange
		elif Alien.X >= 750:
			Alien.Xchange = -Alien.Xchange
			Alien.Y += Alien.Ychange

		# check for bullet enemy hit/colision
		for Bullet in Projectiles:
			colision = CheckColision(Alien,Bullet)
			if colision:
				# play sound of colision
				# colisionSound.play()
				# reset bullet
				Bullet.state = "ready"
				Bullet.Y = 500
				# if colision occurs generate new enemy and add a point to score
				Alien.X = random.randint(0, 710)
				Alien.Y = random.randint(20, 100)
				# change alien speed
				Alien.Xchange = random.randint(2,10)
				score += 1
			# after reaching end screen reset state and position of bullet
			if Bullet.Y <= 0:
				Bullet.state = "ready"
				Bullet.Y = 500
			# bullet movement in Y axis after firing
			if Bullet.state is "fired":
				Bullet.fired(MainWindow)
				Bullet.Y -= Bullet.Ychange


# main function for program
def main():
	# create a loop for the program
	global running
	while running:

		# adding fps ration with clock tick
		clock.tick(60)

		# drawing all on screen
		redrawWindow()
		
		#check player position
		PlayerPositionCheck()

		# alien position check
		AlienPositionCheck()

		# update changes on screen each loop
		pg.display.update()

			


# main program body
if __name__ == '__main__':
	
	main()



pg.quit()
	
