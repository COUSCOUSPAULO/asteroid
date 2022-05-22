from math import *
import pygame
from laser import *
from settings import *

pygame.init()

screen = pygame.display.set_mode((1200,800))

class Vaisseau:
    def __init__(self,x,y,angle = 0,skin = pygame.image.load("img/vseau2.png"),vitesse = 7):
        self.x = x
        self.y = y
        self.angle = angle
        self.skin = skin
        self.vitesse = vitesse
        self.rect = self.skin.get_rect(x = self.x,y = self.y)
        self.level = 0

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

        tire = Laser(self.rect[0] + 40 , self.rect[1] + 40 )
        screen.blit(tire.skin, self.rect)
        tire.objectif(xm, ym)
        event.append(tire)
        return tire

    def update(self,score):
        self.levelmeth(score)

    def levelmeth(self,score):
        if score >= 100 and self.level < 1:
            self.level = 1
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
                if event.type == pygame.K_c:
                    pause = False
                    screen.blit(image_yl, (40, 40))

            


            pygame.display.update()