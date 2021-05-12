import pygame
import os
from pygame.locals import *

screen_width = 800
screen_height = 600

'''define fps'''
clock = pygame.time.Clock()
fps = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

'''Caption and Icon'''
screen = pygame.display.set_mode((screen_width,  screen_height))
pygame.display.set_caption('Space Fight')

'''load image'''
bg = pygame.image.load('backgroundSPACE.png')

SPACESHIP_IMG = pygame.image.load('SHUTTLE.png')
SPACESHIP_IMG = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

SPACESHIP_IMG2 = pygame.image.load('SPACESHIP.png')
SPACESHIP_IMG2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG2, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)




'''used blit function to display  img '''
def draw_bg():
    screen.blit(bg, (0, 0))
    screen.blit(SPACESHIP_IMG, (100, 100))
    screen.blit(SPACESHIP_IMG2, (600, 100))





run = True
while run:
    clock.tick(fps)
    '''draw background  in  main window'''
    draw_bg()


    '''event handlers'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.QUIT()

