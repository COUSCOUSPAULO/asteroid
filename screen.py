import pygame
from pygame.locals import *
from vaisseau import *


pygame.init()

screen = pygame.display.set_mode((1200,800))
fond = pygame.image.load("img/Stars.png").convert()

vseau = Vaisseau(600,400)

screen.blit(fond, (0,0))
screen.blit(vseau.skin,(vseau.x,vseau.y))




cont = True
while cont:
    for event in pygame.event.get():
        if event.type == QUIT:
            cont=False

    pressed = pygame.key.get_pressed()
    vseau.mouvement(pressed)

    vseau.tor()

    screen.blit(fond, (0, 0))
    screen.blit(vseau.skin,(vseau.x,vseau.y))

    pygame.display.flip()