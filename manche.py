import random

from asteroid import *
from laser import *
from pygame import *
from settings import *
from vaisseau import *
from boss import *
from ennemi import *


def randomspawn(event,score): # Fonction qui va faire apparaitre de maniere aleatoire les asteroides
    if score < 1000:
        n = random.randrange(0, 150)
        if n == 42:
            aste = Asteroid(random.randrange(0, 1200), 4)
            event.append(aste)

    if score >= 1000 and score < 5000:
        n = random.randrange(0, 150)
        if n == 42:
            aste = Asteroid(random.randrange(1, 1150), 0, 5)
            event.append(aste)
        if n == 78:
            aste = Asteroid(0, random.randrange(1, 750), 5)
            event.append(aste)
        if n == 114:
            roll = random.randrange(1,3)
            if roll == 1:
                missile = Ennemihor(0, random.randrange(20, 780))
                event.append(missile)
            else:
                missile = Ennemiver(random.randrange(20, 1180), 0)
                event.append(missile)

    if score >= 5000 and score <= 10000:
        test = 0
        for object in event:
            if isinstance(object,Boss):
                pass
            else:
                test += 1
        if test == len(event):
            boss = Boss()
            event.append(boss)
        else:
            print(test,len(event))
    if score > 10000:
        n = random.randrange(0, 150)
        if n == 42:
            aste = Asteroid(random.randrange(50,1150), 0, 5.5)
            event.append(aste)
        if n == 78:
            aste = Asteroid(0, random.randrange(1,750), 5.5)
            event.append(aste)
        if n == 12:
            missile = Ennemihor(0,random.randrange(20,780))
            event.append(missile)
        if n == 50:
            missile = Ennemiver(random.randrange(20,1180),0)
            event.append(missile)



def checkhitbox(event): # Fonction qu va definir les interactions entre asteroid
        score = 0
        for obj in event:
            for other in event:
                if isinstance(obj,Vaisseau) and isinstance(other,Asteroid):
                    if obj.rect.colliderect(other.rect):
                
                
                       
                
                        obj.vie -= 1
                        if obj.vie <= 0:
                                gameover(screen)
                        else :
                            try:
                                event.remove(other)
                            except:
                                pass
                if isinstance(obj,Vaisseau) and isinstance(other,Asteroidmini):
                    if obj.rect.colliderect(other.rect):
                        obj.vie -= 1
                        if obj.vie <= 0:
                            gameover(screen)
                        else:
                            try:
                                event.remove(other)
                            except:
                                pass
                
                if isinstance(obj,Vaisseau) and isinstance(other,Boss):
                    if obj.rect.colliderect(other.rect):
                        obj.vie -= 1
                        if obj.vie <= 0:
                            gameover(screen)
                        else:
                            try:
                                event.remove(other)
                            except:
                                pass
                if isinstance(obj,Vaisseau) and isinstance(other,Laser):
                    if obj.rect.colliderect(other.rect) and other.team == 1:
                        obj.vie -= 1
                        if obj.vie <= 0:
                            gameover(screen)
                        else:
                            try:
                                event.remove(other)
                            except:
                                pass
                if isinstance(obj,Boss) and isinstance(other,Laser):
                    if obj.rect.colliderect(other.rect) and other.team == 0:
                        obj.vie -= 1
                        if obj.vie <= 0:
                            event.remove(obj)
                            score += 5001
                        else:
                            try:
                                event.remove(other)
                            except:
                                pass
                if isinstance(obj,Vaisseau) and (isinstance(other,Ennemiver) or isinstance(other,Ennemihor)):
                    if obj.rect.colliderect(other.rect):
                        obj.vie -= 1
                        if obj.vie <= 0:
                            gameover(screen)
                
                
                        else:
                            try:
                                event.remove(other)
                            except:
                                pass
                
                if (isinstance(obj, Ennemiver) or isinstance(obj, Ennemihor))  and isinstance(other, Laser):  # si un laser touche un missile
                    if obj.rect.colliderect(other.rect):
                
                        try:
                            event.remove(other)
                            event.remove(obj)
                        except:
                            pass
                        score += 80  # + 80 points au score du joueur

                if isinstance(obj, Laser) and (isinstance(other, Asteroid) or isinstance(other, Asteroidmini)):
                    if obj.rect.colliderect(other.rect) and obj.team == 0:
                        try:
                            other.remove(event)
                            event.remove(obj)

                        except:
                            pass
                        score += 20  # + 20 points au score du joueur

        return score

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
