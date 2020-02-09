import pygame

# initialize pygame module
pygame.init()

# create the screen function with 800width and 600height
screen = pygame.display.set_mode((800, 600))

# add a background image
background = pygame.image.load('BG.png')

# add a title to the main window
pygame.display.set_caption("SSSSSSpaceeee IIInvaders")
# create an icon variable
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Add a player graphic, position, function to put on screen
playerimg = pygame.image.load('player.png')
# Add a player starting coordinates
playerX = 400
playerY = 520
# rate of change of position of a player
playerX_change = 0

# player function
def player(x, y):
	# puting player on screen, call function after
	# calling the screen in main loop
	screen.blit(playerimg, (x, y))


# Add a enemy graphic, position, function to put on screen
enemyimg = pygame.image.load('enemy.png')
# Add a enemy starting coordinates
enemyX = 400
enemyY = 20
# rate of change of position of a enemy
enemyX_change = 5
enemyY_change = 50

# enemy function
def enemy(x, y):
	# puting enemy on screen, call function after
	# calling the screen in main loop
	screen.blit(enemyimg, (x, y))


# create a loop for the program
running = True
while running:

	# RGB => Red, Green, Blue color to fill bg
	# range from 0 till 255 check color online
	screen.fill((0,0,0))
	# add a bg img after loading the screen
	screen.blit(background,(0,0))

	
	# write an event for ending game
	for event in pygame.event.get():
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
		# Keyup as relising key
		if event.type == pygame.KEYUP:
			# check event.key for pressing left or right
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0	

	# change position of player and enemy
	playerX += playerX_change
	enemyX += enemyX_change

	# boundry function for keeping all on screen
	if playerX < 0:
		playerX = 0
	elif playerX > 750:
		playerX = 750
	if enemyX < 0:
		enemyX_change =	5
		enemyY += enemyY_change
	elif enemyX >= 750:
		enemyX_change = -5
		enemyY += enemyY_change

	# call player and enemy func/ create p and e char
	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()


	
