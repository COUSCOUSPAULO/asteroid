import pygame
import random
from laser import *

class Boss:
    def __init__(self):
        self.skin = pygame.image.load("img/boss.png")
        self.rect = self.skin.get_rect(x = 500,y = 50 )
        self.vie = 50

    def update(self,score,event):
        roll = random.randrange(1,17)
        if roll == 1:
            tire = Laser(self.rect[0]+100,self.rect[1]+25,team = 1)
            tire.objectif(event[0].rect[0], event[0].rect[1])
            event.append(tire)

