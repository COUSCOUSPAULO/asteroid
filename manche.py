import random

from asteroid import *
from laser import *
from pygame import *

def randomspawn(event):
    n = random.randrange(0,200)
    if n == 42 :
        aste = Asteroid(random.randrange(0,1200), 0)
        event.append(aste)




def checkhitbox(event):
    score = 0

    for obj in event:
        for other in event:


            if isinstance(obj,Asteroid) and isinstance(other,Laser):
                if obj.rect.colliderect(other.rect):

                    event.remove(other)
                    event.remove(obj)
                    other.__del__(event)
                    obj.__del__(event)
                    score += 60


            if isinstance(obj,Asteroidmini) and isinstance(other,Laser):
                if obj.rect.colliderect(other.rect):
                    event.remove(other)
                    event.remove(obj)
                    other.__del__(event)
                    obj.__del__(event)
                    score += 10

            if isinstance(obj,Asteroidmini) and isinstance(other,Laser):
                if obj.rect.colliderect(other.rect):
                    event.remove(other)
                    event.remove(obj)
                    other.__del__(event)
                    obj.__del__(event)
                    score += 10


    return score