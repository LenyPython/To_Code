import pygame as pg
import random
from math import sqrt

# creating an enemy class
class Enemy:
	def __init__(self):
		# Add a enemy graphics from files
		self.img = [
				pg.image.load('graphics/enemy/enemy-1.png'),
				pg.image.load('graphics/enemy/enemy-2.png'),
				pg.image.load('graphics/enemy/enemy-3.png'),
				pg.image.load('graphics/enemy/enemy-4.png'),
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
	def generate(self, num, window):
		window.blit(self.img[(num//15)-1], (self.X, self.Y))

# creatin a player class object
class Player:
	def __init__(self):
		# Add a player graphic, position, function to put on screen
		self.img = [
				pg.image.load('graphics/player/player-1.png'),
				pg.image.load('graphics/player/player-2.png'),
				pg.image.load('graphics/player/player-3.png'),
				pg.image.load('graphics/player/player-4.png'),
				]

		# Add a player starting coordinates
		self.X = 400
		self.Y = 520
		# adding number of bullets available
		self.ammo = 2
		# rate of change of position of a player
		self.Xchange = 0

# creating a projectalies class for bullets
class Bullet:
	def __init__(self):
		# Add a bullet graphic
		self.img = pg.image.load('graphics/bullet.png')
		# Add a bullet starting coordinates
		self.X = 0
		self.Y = 500
		# rate of change of position of a bullet
		self.Ychange = 2
		# add a state for ready to shoot or not
		# two states, 'fired' for moving bullet and 'ready' for no bullet 
		self.state = "ready"
	# initialiaze bullet on screen
	def fire(self, window, x, position):
		# for bullet position shot from gun 1 or 2
		if position%2 == 0:
			gunNumber = 0
		else:
			gunNumber = 58
		# set bullet X value plus gun position
		self.X = x + gunNumber
		# take global value of bullet and change it when fire
		self.state = "fired"
		# put bullet on screen
		window.blit(self.img,(self.X, self.Y))
	# bullet flight function
	def fired(self, window):
		if self.state == 'fired':
			window.blit(self.img, (self.X, self.Y))
		


