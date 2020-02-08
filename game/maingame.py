import pygame

# initialize pygame module
pygame.init()

# create the screen function with 800width and 600height
screen = pygame.display.set_mode((800, 600))

# add a title to the main window
pygame.display.set_caption("SSSSSSpaceeee IIInvaders")
# create an icon variable
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Add a player graphic
playerimg = pygame.image.load('player.png')
# Add a player starting coordinates
playerX = 400
playerY = 550
# player function
def player():
	# puting player on screen, call function after
	# calling the screen in main loop
	screen.blit(playerimg, (playerX, playerY))


# create a loop for the program
running = True
while running:

	# RGB => Red, Green, Blue color to fill bg
	# range from 0 till 255 check color online
	screen.fill((0,0,0))
	
	# write an event for ending game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	player()
	pygame.display.update()


	
