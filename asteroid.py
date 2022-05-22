import pygame
import vaisseau
import laser
import random

vitesselist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7]


class Asteroid:
     """Classe définissant un asteroide caractérisé par :
    - sa position x
    - sa position y
    - sa vitesse """
    def __init__(self,x,y,vitesse = 4): # Methode constructeur
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/asteroid.png").convert()
        self.direction_x = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction x
        self.direction_y = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction y
        self.rect = self.skin.get_rect(x = self.x,y = self.y)


    def update(self):
        self.tor()
        self.rect[0] += self.direction_x * self.vitesse
        self.rect[1] += self.direction_y * self.vitesse


    def tor(self):
        if self.rect[1] < 0:
            self.rect[1] = 800
        if self.rect[1] > 800:
            self.rect[1] = 0
        if self.rect[0] < 0:
            self.rect[0] = 1200
        if self.rect[0] > 1200:
            self.rect[0] = 0

    def __del__(self,event):
        for i in range(4):
            asteroidmini = Asteroidmini(self.rect[0],self.rect[1],random.randrange(9,13))
            event.append(asteroidmini)

        del self


class Asteroidmini:
     """Classe définissant un petit asteroide caractérisé par :
    - sa position x
    - sa position y
    - sa vitesse """
    def __init__(self,x,y,vitesse = 4): # Methode constructeur
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/asteroid_petit.png").convert()
        self.direction_x = vitesselist[random.randrange(0,13)]
        self.direction_y = vitesselist[random.randrange(0,13)]
        self.rect = self.skin.get_rect(x = self.x,y = self.y)


    def update(self):
        self.tor()
        self.rect[0] += self.direction_x * self.vitesse
        self.rect[1] += self.direction_y * self.vitesse

    def tor(self):
        if self.rect[1] < 0:
            self.rect[1] = 800
        if self.rect[1] > 800:
            self.rect[1] = 0
        if self.rect[0] < 0:
            self.rect[0] = 1200
        if self.rect[0] > 1200:
            self.rect[0] = 0

    def __del__(self,event):
        del self