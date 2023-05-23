import pygame
import random
import math

class Player():
    def __init__(self):
        self.lives=3
        self.x = 0
        self.y = 0
        return
    def moveleft(self):
        self.x -= 1
        return
    def moveright(self):
        self.x += 1
        return
    def lives():
        return
    def checkhit():
        return
    def fire():
        return
    
class Rocket():
    def __init__(self,x,y):
        self.x = x
        self.y = y


    

class Game():
    
    def __init__(self,width,height):
        #initializes the pygame engine
        pygame.init() 
        #screen size
        self.screen = pygame.display.set_mode((width, height))
        #details
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load('images/ship.png')
        pygame.display.set_icon(icon)
        self.screen.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        
        #background = pygame.image.load('background.png') #background if needed, default black empty
        
        # define a variable to control the main loop
        running = True
        while running:

        # event handling, gets all event from the event queue
            for event in pygame.event.get():
                print(event)
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    running = False
            
            aliens = [Enemy(self,30,30)] #aliens list will generate later
            for alien in aliens:
                alien.draw()

            #update screen    
            pygame.display.flip()


class Enemy(): 
    def __init__(self,game,x,y):
        self.lives = 1
        self.x = x
        self.y = y
        self.game = game
    
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0,0,255),
                         pygame.Rect(self.x,self.y,20,20))

    
    def fire():
        return
    def death():
        return
    def checkhit():
        return
    

if __name__ == '__main__':
    game = Game(800, 600)
#start = Game(800,600)