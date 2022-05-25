from math import *
import pygame

pygame.init()

screen = pygame.display.set_mode((1200,800))

class Vaisseau:
    def __init__(self,x,y,angle = 0,skin = pygame.image.load("img/vseau.png").convert(),vitesse = 0.2):
        self.x = x
        self.y = y
        self.angle = angle
        self.skin = skin
        self.vitesse = vitesse


    def tor(self):
        if self.y < 0:
            self.y = 800
        if self.y > 800:
            self.y = 0
        if self.x < 0:
            self.x = 1200
        if self.x > 1200:
            self.x = 0

    def rotation(self,move):
        if move == "left":
            self.angle += 0.1 % 2*pi
        if move =="Right":
            self.angle -= 0.1 % 2*pi


    def mouvement(self,pressed):
        if pressed[pygame.K_a]:
            self.x -= self.vitesse
        if pressed[pygame.K_d]:
            self.x += self.vitesse
        if pressed[pygame.K_w]:
            self.y -= self.vitesse
        if pressed[pygame.K_s]:
            self.y += self.vitesse
