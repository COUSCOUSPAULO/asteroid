import pygame
from pygame.locals import *
from vaisseau import *
from laser import *
from asteroid import *
from manche import *

pygame.init()

screen = pygame.display.set_mode((1200,800)) # taille de l'ecran
fond = pygame.image.load("img/Stars.png").convert() # image de fond

clock = pygame.time.Clock()

vseau = Vaisseau(600,400) # endroit de spawn du vaisseau


screen.blit(fond, (0,0))
screen.blit(vseau.skin,(vseau.x,vseau.y))

event1= [vseau]
score = 0 


cont = True
while cont:
    screen.blit(fond, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            cont=False
        if event.type == pygame.MOUSEBUTTONDOWN: # si clique droit
            if event.button == 1: 
                laser = vseau.tire(screen,event1)
                screen.blit(laser.skin,laser.rect) # vaisseau tire
    for i in event1:

        i.update(score,event1) # update du score
        screen.blit(i.skin, i.rect)

    score += checkhitbox(event1) # score ancient + score de l'evenement qui vient de se produire
    randomspawn(event1,score)


    pressed = pygame.key.get_pressed()
    vseau.mouvement(pressed,screen,event)
    vseau.tor()


    dt = clock.tick(30) # determine le temps


    drawscore(screen,score) # ecran de fin
    vseau.drawlife()



    pygame.display.flip()