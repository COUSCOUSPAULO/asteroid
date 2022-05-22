from math import *
import pygame
from laser import *
from settings import *
from bonus import *


pygame.init()

screen = pygame.display.set_mode((1200,800))

class Vaisseau:
    def __init__(self,x,y,angle = 0,skin = pygame.image.load("img/vseau2.png"),vitesse = 7):
        """Classe définissant un vaisseau caractérisé par :
    - sa position x
    - sa position y
    - son angle par rapport a sa position de départ
    - son skin
    - sa vitesse """
        self.x = x
        self.y = y
        self.angle = angle
        self.skin = skin
        self.vitesse = vitesse
        self.rect = self.skin.get_rect(x = self.x,y = self.y)
        self.level = 0
        self.vie = 3

    def tor(self): # pour que le vaisseau ne sorte jamais du jeu, si il va de gauche a droite et "sors" du jeu par la doite il reapparait par la gauche
        if self.rect[1] < 0: # pour le cote gauche
            self.rect[1] = 800
        if self.rect[1] > 800: # pour le cote droit
            self.rect[1] = 0
        if self.rect[0] < 0: # pour en haut
            self.rect[0] = 1200
        if self.rect[0] > 1200:# pour en bas
            self.rect[0] = 0




    def mouvement(self,pressed,screen,event): # fonction nous permetant de faire bouger le vaisseau en appuyant sur les touches du clavier.
        if pressed[pygame.K_a]: # on appuis sur a on va a gauche
            self.rect[0] -= self.vitesse
        if pressed[pygame.K_d]:# on appuis sur d on va a droite
            self.rect[0] += self.vitesse
        if pressed[pygame.K_w]:# on appuis sur w on va en haut
            self.rect[1] -= self.vitesse
        if pressed[pygame.K_s]:# on appuis sur s on va en bas
            self.rect[1] += self.vitesse


    def tire(self,screen,event):
        xm, ym = pygame.mouse.get_pos() # la postion de la souris est la direction dans la quelle va partir le laser

        tire = Laser(self.rect[0] + 40 , self.rect[1] + 40 )
        screen.blit(tire.skin, self.rect)
        tire.objectif(xm, ym)
        event.append(tire) # le tire est executé
        return tire

    def update(self,score,event):
        self.levelmeth(score)

    def levelmeth(self,score):
        if score >= 1000 and self.level < 1: # si on a plus de 100 de score et qu'on est pas encore lvl 1
            self.level = 1 # on passe lvl 1
            self.amelioration()
        if score >= 5000 and self.level < 2:
            self.level = 2
            self.amelioration()
        if score >= 10000 and self.level < 3:
            self.level = 3
            self.amelioration()
        if score >= 20000 and self.level < 4:
            self.level = 4
            self.amelioration()
        if score >= 40000 and self.level < 5:
            self.level = 5 # on passe lvl 1
            self.amelioration()
        if score >= 100000 and self.level < 6:
            self.level = 6
            self.amelioration()
        if score >= 500000 and self.level < 7:
            self.level = 7
            self.amelioration()

    def amelioration(self):
        pause = True

        image_yl = police.render("Level up: 1 amélioration possible", 1, (255, 255, 255))
        screen.blit(image_yl, (40, 40))





        while pause == True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_p]:
                pause = False
            if pressed[pygame.K_1]:
                pause = False
                bonuslife(self)
            if pressed[pygame.K_2]:
                pause = False
                bonusvitesse(self)

            image_bonusvie = police.render("1: + 1 vie",1,(255,255,255))
            screen.blit(image_bonusvie,(40,100))

            image_bonusvitesse = police.render("2: + 5% de vitesse",1,(255,255,255))
            screen.blit(image_bonusvitesse,(40,200))

            screen.blit(image_yl, (40, 40))
            


            pygame.display.flip()
    def drawlife(self):
        image_vie = police.render("Vie: " + str(self.vie), 1, (255, 255, 255))
        screen.blit(image_vie, (1000, 50))