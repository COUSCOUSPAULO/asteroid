from math import *
import pygame
from laser import *

pygame.init()

screen = pygame.display.set_mode((1200,800))

class Vaisseau:
    def __init__(self,x,y,angle = 0,skin = pygame.image.load("img/vseau2.png").convert(),vitesse = 5):
        self.x = x
        self.y = y
        self.angle = angle
        self.skin = skin
        self.vitesse = vitesse
        self.rect = self.skin.get_rect(x = self.x,y = self.y)

    def tor(self):
        if self.rect[1] < 0:
            self.rect[1] = 800
        if self.rect[1] > 800:
            self.rect[1] = 0
        if self.rect[0] < 0:
            self.rect[0] = 1200
        if self.rect[0] > 1200:
            self.rect[0] = 0




    def mouvement(self,pressed,screen,event):
        if pressed[pygame.K_a]:
            self.rect[0] -= self.vitesse
        
        if pressed[pygame.K_d]:
            self.rect[0] += self.vitesse
        if pressed[pygame.K_w]:
            self.rect[1] -= self.vitesse
        if pressed[pygame.K_s]:
            self.rect[1] += self.vitesse


    def tire(self,screen,event):
        xm, ym = pygame.mouse.get_pos()

        tire = Laser(self.rect[0] + 40, self.rect[1] + 40)
        screen.blit(tire.skin, self.rect)
        tire.objectif(xm, ym)
        event.append(tire)
        return tire

