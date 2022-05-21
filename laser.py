import pygame
from math import *
from vaisseau import *
pygame.init()

screen = pygame.display.set_mode((1200,800))


class Laser:
    def __init__(self,x , y , vitesse = 10):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.skin =  pygame.image.load("img/laser.png").convert()
        self.xrap = 0
        self.yrap = 0


    def objectif(self,xm , ym):
        y1 = ym-self.y
        x1 = xm-self.x
        self.xrap = (x1*100/(sqrt((x1**2)+(y1**2))))
        self.yrap = 100-self.xrap

    def update(self,screen):


        self.x += (self.xrap/100) * self.vitesse
        self.y += (self.xrap/100) * self.vitesse


