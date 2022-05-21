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
        self.rect = self.skin.get_rect(x = self.x,y = self.y)

    def objectif(self,xm , ym):
        y1 = ym-self.rect[1]
        x1 = xm-self.rect[0]
        univect  = sqrt(x1**2 + y1**2)
        self.xrap = x1/univect
        self.yrap = y1/univect

    def update(self):


        self.rect[0] += self.xrap * self.vitesse
        self.rect[1] += self.yrap * self.vitesse

    def __del__(self,event):
        del self

