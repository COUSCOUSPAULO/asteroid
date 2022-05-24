import pygame
import random


class Ennemiver:
    def __init__(self,x,y):
        """Classe définissant un boss caractérisé par :
    - son y
    - son x"""
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/ennemiver.png") # image enemi vertical
        self.rect = self.skin.get_rect(x = self.x,y = self.y ) # hitbox


    def update(self,score,event):
        self.rect[1] += 6
        self.tor()

    def tor(self):
        # commentaire du tor a deja ete fait dans la classe vaisseau
        if self.rect[1] < 0:
            self.rect[1] = 800
        if self.rect[1] > 800:
            self.rect[1] = 0
        if self.rect[0] < 0:
            self.rect[0] = 1200
        if self.rect[0] > 1200:
            self.rect[0] = 0

class Ennemihor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/ennemihor.png") # image enemi horizontal
        self.rect = self.skin.get_rect(x=self.x, y=self.y)

    def update(self, score, event):
        self.rect[0] += 6
        self.tor()

    def tor(self):
        if self.rect[1] < 0:
            self.rect[1] = 800
        if self.rect[1] > 800:
            self.rect[1] = 0
        if self.rect[0] < 0:
            self.rect[0] = 1200
        if self.rect[0] > 1200:
            self.rect[0] = 0