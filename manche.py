import random

from asteroid import *
from laser import *
from pygame import *

def randomspawn(event): # Fonction qui va faire apparaitre de maniere aleatoire les asteroides
    n = random.randrange(0,200)
    if n == 42 :
        aste = Asteroid(random.randrange(0,1200), 0)
        event.append(aste)




def checkhitbox(event): # Fonction qu va definir les interactions entre asteroides/ petits asteroides et laser
    score = 0 # le score de base du joueur est de 0

    for obj in event: # tant qu'il y a des objets (asteroides)
        for other in event:


            if isinstance(obj,Asteroid) and isinstance(other,Laser): # si un laser touche un asteroide
                if obj.rect.colliderect(other.rect):

                    event.remove(other) # remove le laser 
                    event.remove(obj) # remove l'asteroide
                    other.__del__(event) 
                    obj.__del__(event)
                    score += 60 # + 60 points au score du joueur


            if isinstance(obj,Asteroidmini) and isinstance(other,Laser): # si un laser touche un petit asteroide
                if obj.rect.colliderect(other.rect):
                    event.remove(other)# remove le laser 
                    event.remove(obj)# remove le petit asteroide
                    other.__del__(event)
                    obj.__del__(event)
                    score += 10 # + 10 points au score du joueur

            if isinstance(obj,Asteroidmini) and isinstance(other,Laser):
                if obj.rect.colliderect(other.rect):
                    event.remove(other)
                    event.remove(obj)
                    other.__del__(event)
                    obj.__del__(event)
                    score += 10


    return score