import pygame
from pygame.locals import *
from vaisseau import *
from laser import *

pygame.init()

screen = pygame.display.set_mode((1200,800))
fond = pygame.image.load("img/Stars.png").convert()

clock = pygame.time.Clock()

vseau = Vaisseau(600,400)


screen.blit(fond, (0,0))
screen.blit(vseau.skin,(vseau.x,vseau.y))

event1= []



cont = True
while cont:
    screen.blit(fond, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            cont=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                laser = vseau.tire(screen,event1)
                screen.blit(laser.skin,(laser.x,laser.y))
    for i in event1:
        if i.x < 0 or i.x > 1200:
            event1.remove(i)
        i.update(screen)
        screen.blit(i.skin, (i.x, i.y))

    pressed = pygame.key.get_pressed()
    vseau.mouvement(pressed,screen,event1)

    dt = clock.tick(30)

    vseau.tor()


    screen.blit(vseau.skin,(vseau.x,vseau.y))


    pygame.display.flip()