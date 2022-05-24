import pygame
import vaisseau
import laser
import random

vitesselist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7] # liste de 14 vitesse aleatoire pour les asteroides


class Asteroid:
    def __init__(self,x,y,vitesse = 4): # Methode constructeur
        """Classe définissant un asteroide caractérisé par :
    - sa position x
    - sa position y
    - sa vitesse """
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/asteroid.png").convert() # skin asteroide
        self.direction_x = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction x
        self.direction_y = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction y
        self.rect = self.skin.get_rect(x = self.x,y = self.y)


    def update(self):
        self.tor()
        self.rect[0] += self.direction_x * self.vitesse
        self.rect[1] += self.direction_y * self.vitesse


    def tor(self): # fonction qui fait en sorte que les ateroides qui passent à gauche dans le jeu ressortent a droite
        # commentaire du tor a deja ete fait dans la classe vaisseau 
        """Fonction permetant de faire passe le vaiseau de en haut a en bas :
         """
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
    def __init__(self,x,y,vitesse = 4): # Methode constructeur
        """Classe définissant un petit asteroide caractérisé par :
    - sa position x
    - sa position y
    - sa vitesse """
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.skin = pygame.image.load("img/asteroid_petit.png").convert() # skin asteroide
        self.direction_x = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction x
        self.direction_y = vitesselist[random.randrange(0,13)] # vitesse aleatoire dans la direction y
        self.rect = self.skin.get_rect(x = self.x,y = self.y)


    def update(self):
        self.tor()
        self.rect[0] += self.direction_x * self.vitesse
        self.rect[1] += self.direction_y * self.vitesse

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

    def __del__(self,event):
        del self