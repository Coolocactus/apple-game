import pygame
import time
import random


pygame.init()
fenetreHauteur = 1280
fenetreLargeur = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
fond = pygame.image.load("assets/background1.png")
fond = pygame.transform.scale(fond,(fenetreHauteur, fenetreLargeur))

class player():
    def __init__(self):
        self.co_x = 0
        self.score = 0
        self.skin = pygame.image.load("assets/panier1.png")
        self.speed = 5
    def move_left(self):
        self.co_x -= self.speed
    def move_right(self):
        self.co_x += self.speed
    def gain_score(self,how_much):
        self.score += how_much

class apple():
    def __init__(self):
        self.co_x = random.randint(0,1280) 
        self.co_y = -15
        self.speed = 2
        self.skin = pygame.image.load("assets/apple1.png")
        self.skin = pygame.transform.scale(self.skin,(100, 100))
    
    def tomber(self):
        self.co_y += self.speed
        if self.co_y > 720:
            self.co_x = random.randint(0,1280)
            self.co_y = 0
    def collision(self):
        self.afficher()
        self.collide = rectPlayer.collidepoint(self.co_x,self.co_y)
        if self.collide: 
            player1.gain_score(1)
            return self
    def afficher(self):
        self.rectPomme = self.skin.get_rect()   #affichage Pomme
        self.rectPomme.center = self.co_x,self.co_y
        screen.blit(self.skin,self.rectPomme)
        self.tomber()

pomme = []
def création_pomme(): #create an apple with a one-in-a-hundred chance
    global pomme
    chance_création = random.randint(1,100)
    if chance_création == 1:
        pomme1 = apple()
        pomme.append(pomme1)
            
player1 = player() #creation of the player 

#main programe
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        

    création_pomme()
    print(len(pomme))
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(fond,(0,0))

    
    rectPlayer = player1.skin.get_rect()   # player actualisation
    rectPlayer.center = player1.co_x,600
    screen.blit(player1.skin,rectPlayer)
    
    
    apple_suppr = [] #list of apple to remove
    for i in range(len(pomme)): 
        apple_suppr_add = pomme[i].collision() #return the name of the apple if the apple touch the player
        if apple_suppr_add != None:
            apple_suppr.append(apple_suppr_add) #add the apple to the list 
    for j in range(len(apple_suppr)):
        pomme.remove(apple_suppr[j])#pourquoi ne pas le suppreimer directement au dessue ????  # Parce que sinon index out of range vu que ça regarde le nombre de pomme au début


    keys = pygame.key.get_pressed() #detecte the imput 
    #movement 
    if keys[pygame.K_q]:
        player1.move_left()
    if keys[pygame.K_d]:
        player1.move_right()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
