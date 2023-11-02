from os import system
import pygame
pygame.init()

import sys

screen=pygame.display.set_mode((288,512))
# clock=pygame.time.clock()
bg_surface=pygame.image.load("Game Image/background-night.png")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.blit(bg_surface,(0,0))
    # clock.tick(120)