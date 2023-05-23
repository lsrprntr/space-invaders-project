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
    screen = None
    aliens = []
    
    def __init__(self,width,height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))


start = game(800,600)