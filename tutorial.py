#Testing file to the first game

import pygame,sys
from pygame.locals import *

# Initialization of pygame
pygame.init()

# Creation of a window
window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Game Test")

color = (70,80,150)
colorBkw = pygame.Color(0,0,0)

# Showing the window
while True:
	window.fill(colorBkw)
#	pygame.draw.line(window,color,(60,80),(160,100),4)
#	pygame.draw.circle(window,(150,150,40),(180,190),20)
	pygame.draw.rect(window,(120,70,70),(0,0,100,50))
#	pygame.draw.polygon(window,(0,120,200),((140,0),(291,106),(237,277),(56,277),(0,106)))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.update()

