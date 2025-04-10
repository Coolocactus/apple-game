import pygame
import time
import random


pygame.init()
fenetreHauteur = 1280
fenetreLargeur = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
fond = pygame.image.load("assets\background1.png")
fond = pygame.transform.scale(fond,(fenetreHauteur, fenetreLargeur))

class player():
    def __init__(self):
        self.co_x = 0
        self.score = 0
        self.skin = pygame.image.load("assets\panier1.png")
        self.speed = 5
    def move_left(self):
        self.co_x -= self.speed
    def move_right(self):
        self.co_x += self.speed
    def gain_score(self,how_much,pomme):
        if pomme.not_been_touched == True:
            self.score += how_much
            pomme.not_been_touched = False

class apple():
    def __init__(self,id):
        self.co_x = random.randint(0,1280) 
        self.co_y = -15
        self.speed = 2    
        self.timer = random.randint(1,5000)
        self.start = False
        self.id = id
        pygame.time.set_timer(id, self.timer)    
        self.skin = pygame.image.load("assets\apple1.png")
        self.skin = pygame.transform.scale(self.skin,(100, 100))
        self.not_been_touched = True
        self.rectPomme = None
        self.collide = False
    
    def tomber(self):
        self.co_y += self.speed
        if self.co_y > 720:
            self.co_x = random.randint(0,1280)
            self.co_y = 0
    def collision(self):
        if self.start:
            self.collide = rectPlayer.collidepoint(self.co_x,self.co_y)
            if self.collide: 
                player1.gain_score(1,self)
            print(player1.score)
            if self.not_been_touched == True:
                self.afficher()
            else:
                self.__init__(self.id)
    def afficher(self):
        self.rectPomme = self.skin.get_rect()   #affichage Pomme
        self.rectPomme.center = self.co_x,self.co_y
        screen.blit(self.skin,self.rectPomme)
        self.tomber()
        
player1 = player()
pomme1 = apple(1)
pomme2 = apple(2)
pomme3 = apple(3)
pomme4 = apple(4)
pomme5 = apple(5)
pomme6 = apple(6)
pomme7 = apple(7)
pomme8 = apple(8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 2:  #Donne a chacune des pommes l'odre de bouger
            pomme2.start = True
        if event.type == 3:
            pomme3.start = True
        if event.type == 4:
            pomme4.start = True
        if event.type == 5:
            pomme5.start = True
        if event.type == 6:
            pomme6.start = True
        if event.type == 7:
            pomme7.start = True
        if event.type == 8:
            pomme8.start = True
         #if event.type == pygame.USEREVENT:


    # fill the screen with a color to wipe away anything from last frame
    screen.blit(fond,(0,0))

    rectPlayer = player1.skin.get_rect()   # Panier
    rectPlayer.center = player1.co_x,600
    screen.blit(player1.skin,rectPlayer)
    
    pomme1.collision() #GÃ¨re a la fois les pommes qui tombent , la collision et l'affichage
    pomme2.collision()
    pomme3.collision()
    pomme4.collision()
    pomme5.collision()
    pomme6.collision()
    pomme7.collision()
    pomme8.collision()




    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_q]:
        player1.move_left()
    if keys[pygame.K_d]:
        player1.move_right()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
