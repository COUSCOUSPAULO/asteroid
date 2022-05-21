from math import *
import pygame
from laser import *

pygame.init()

screen = pygame.display.set_mode((1200,800))

class Vaisseau:
    def __init__(self,x,y,angle = 0,skin = pygame.image.load("img/vseau2.png").convert(),vitesse = 3):
        self.x = x
        self.y = y
        self.angle = angle
        self.skin = skin
        self.vitesse = vitesse
        

    def tor(self):
        if self.y < 0:
            self.y = 800
        if self.y > 800:
            self.y = 0
        if self.x < 0:
            self.x = 1200
        if self.x > 1200:
            self.x = 0




    def mouvement(self,pressed,screen,event):
        if pressed[pygame.K_a]:
            self.x -= self.vitesse
        
        if pressed[pygame.K_d]:
            self.x += self.vitesse
        if pressed[pygame.K_w]:
            self.y -= self.vitesse
        if pressed[pygame.K_s]:
            self.y += self.vitesse


    def tire(self,screen,event):
        xm, ym = pygame.mouse.get_pos()

        tire = Laser(self.x + 40, self.y + 40)
        screen.blit(tire.skin, (self.x, self.y))
        tire.objectif(xm, ym)
        event.append(tire)
        return tire