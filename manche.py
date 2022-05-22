import random

from asteroid import *
from laser import *
from pygame import *
from settings import *
from vaisseau import *

def randomspawn(event): # Fonction qui va faire apparaitre de maniere aleatoire les asteroides
    n = random.randrange(0,150)
    if n == 42 :
        aste = Asteroid(random.randrange(0,1200), 0)
        event.append(aste)




def checkhitbox(event): # Fonction qu va definir les interactions entre asteroides/ petits asteroides et laser
    score = 0 # le score de base du joueur est de 0

    for obj in event: # tant qu'il y a des objets (asteroides)
        for other in event:


            if isinstance(obj,Asteroid) and isinstance(other,Laser): # si un laser touche un asteroide
                if obj.rect.colliderect(other.rect):

                    try: # si il n'y a pas d'erreur dans le code
                        other.remove(event)
                        obj.remove(event)
                    except: # si il y a erreur
                        pass
                    score += 60 # + 60 points au score du joueur


            if isinstance(obj,Asteroidmini) and isinstance(other,Laser): # si un laser touche un petit asteroide
                if obj.rect.colliderect(other.rect):

                    try:# si il n'y a pas d'erreur dans le code
                        other.remove(event)
                        obj.remove(event)
                    except:# si il y a erreur
                        pass
                    score += 10 # + 10 points au score du joueur

            if isinstance(obj,Vaisseau) and isinstance(other,Asteroid): # si le vaisseau et un asteroide entre en collision
                if obj.rect.colliderect(other.rect):


                    gameover(screen,score) # on perd

            if isinstance(obj,Vaisseau) and isinstance(other,Asteroidmini):# si le vaisseau et un petit asteroide entre en collision
                if obj.rect.colliderect(other.rect):

                    screen.blit(pygame.image.load("img/laser.png"),(obj.rect))
                    gameover(screen,score) # on perd


    return score # apres avoir perdu le score est return

def drawscore(screen,score,x = 50 ,y = 50): # fonction d'affichage du score
    image_score = police.render("score: " + str(score),1,(255,255,255))
    screen.blit(image_score,(x,y))


def gameover(screen,score): # quand on perd

    image_yl = police2.render("Game Over",1,(255,0,0)) #ecriture game over
    screen.blit(image_yl,(400,400)) # affichée (position)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(image_yl, (400, 400))
        drawscore(screen,score,550,650)

        pygame.display.update()
