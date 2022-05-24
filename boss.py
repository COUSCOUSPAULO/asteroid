import pygame
import random
from laser import *

class Boss:
    def __init__(self):
        """Classe définissant un boss caractérisé par :
    - son skin
    - s
    - sa vie """
        self.skin = pygame.image.load("img/boss.png") # image du boss
        self.rect = self.skin.get_rect(x = 500,y = 50 ) # hitbox ?
        self.vie = 100 # vie du boss

    def update(self,score,event):
        """Fonction permetant au boss de tirer prnant en parametres :
         le score 
         l'event"""
        roll = random.randrange(1,17) # nbre au hazard entre 1 et 17
        if roll == 1: # si le nbre est 1
            tire = Laser(self.rect[0]+100,self.rect[1]+25,team = 1) # le boss recoit l'odre de tirer 
            tire.objectif(event[0].rect[0], event[0].rect[1])
            event.append(tire) # il tire

