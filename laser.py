import pygame
from math import *
from vaisseau import *
pygame.init()

screen = pygame.display.set_mode((1200,800))


class Laser:

    def __init__(self,x , y , team = 0,vitesse = 10):
        """Classe définissant un laser caractérisé par :
            - sa position x
            - sa position y
            - sa vitesse """
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.skin =  pygame.image.load("img/laser.png")
        self.xrap = 0
        self.yrap = 0
        self.rect = self.skin.get_rect(x = self.x,y = self.y)
        self.team = team

    def objectif(self,xm , ym): 
        """Fonction permetant de donner la direction du laser en prenant en para :
         - la coo x de la souris 
         - la coo y de la souris"""
        y1 = ym-self.rect[1]
        x1 = xm-self.rect[0]
        univect  = sqrt(x1**2 + y1**2) # On fait pytagore des deux veceteurs x,y de directions du laser
        self.xrap = x1/univect
        self.yrap = y1/univect

    def update(self,score,event):


        self.rect[0] += self.xrap * self.vitesse
        self.rect[1] += self.yrap * self.vitesse
        if self.rect[0] < 0 or self.rect[0] > 1200: # si le laser quitte l'ecran par la gauche ou la droite il disparait
            try:
                event.remove(self)
            except:
                pass
        if self.rect[1] < 0 or self.rect[1] > 800: # si le laser quitte l'ecran par le bas ou le haut il disparait
            try:
                event.remove(self)
            except:
                pass
    def remove(self,event):
        event.remove(self)

