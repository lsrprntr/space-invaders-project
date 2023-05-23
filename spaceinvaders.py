import pygame
import random
import math

class player():
    def __init__(self):
        self.lives=3
        return
    def moveleft(self):
        return
    def moveright(self):
        return
    def lives():
        return
    def checkhit():
        return
    def fire():
        return

class enemy(player): 
    def __init__(self):
        self.lives = 1
        return
    def fire():
        return
    def death():
        return
    def checkhit():
        return
    

class game():
    
    def __init__(self,width,height):
        #initializes the pygame engine
        pygame.init() 
        #screen size
        self.screen = pygame.display.set_mode((width, height))

        #details
        pygame.display.set_caption("Space Invaders")
        #icon = pygame.image.load('ufo.png')
        #pygame.display.set_icon(icon)
        #background = pygame.image.load('background.png') #background if needed, default black empty


        self.clock = pygame.time.Clock()

        # define a variable to control the main loop
        running = True
        while running:
        # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    running = False
        


start = game(800,600)