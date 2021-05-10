import pygame
from pygame.locals import *

'''define fps'''
clock = pygame.time.Clock()
fps = 60

'''Creating the screen'''
screen_width = 800
screen_height = 600

'''Caption and Icon'''
screen = pygame.display.set_mode((screen_width,  screen_height))
pygame.display.set_caption('Space Shooter')

'''load image'''
bg = pygame.image.load('backgroundSPACE.png')

'''used blit fucntion to display  img '''
def draw_bg():
    screen.blit(bg, (0, 0))

'''create spaceship  class'''
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load('SHIP.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,  y]

run = True
while run:
    clock.tick(fps)
    '''draw background'''
    draw_bg()


    '''event handlers'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.QUIT()

