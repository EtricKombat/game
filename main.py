import pygame

# initialize the pygame
pygame.init()

#create the screen
screen =pygame.display.set_mode((800,600))


#Title and icon
pygame.display.set_caption("Pilot Ayana A.K.A Chuchini")
icon = pygame.image.load('ayana.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('cloak.png')
playerX = 370
playerY = 180


def player(x,y):
	screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:
	

	screen.fill((0, 0, 0))
	playerX -= 0.3
	playerY -= 0.4	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# RGB - Red , Green , Blue	
	player(playerX,playerY)	
	pygame.display.update()





