import pygame
import random
import math

class Player():
    def __init__(self,game):
        self.game = game
        self.lives=3
        self.x = self.game.width/2 - 13
        self.y = self.game.height - 25

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0, 0, 255),
                         pygame.Rect(self.x, self.y, 25, 25))
        

    
class Rocket():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class Game():

    def __init__(self,width,height):
        #initializes the pygame engine
        pygame.init() 
        #screen size
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        #details
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load('images/ship.png')
        pygame.display.set_icon(icon)
        #background = pygame.image.load('background.png') #background if needed, default black empty

        self.screen.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        aliens = [] #aliens list will generate later
        alien = Enemy(self,30,30)
        aliens.append(alien)

        players = []
        player = Player(self)
        players.append(player)

        # define a variable to control the main loop
        running = True
        while running:
            self.screen.fill((0, 0, 0)) #resets screen to blank
            pressed = pygame.key.get_pressed()
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                print(event)
                reset = 1
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and reset == 1:
                        player.x += 5
                        print(player.x)
                    elif event.key == pygame.K_LEFT and reset == 1:
                        player.x -= 5
                    reset = 0


            #aliens draw loop
            for alien in aliens:
                alien.draw()
            
            #player draw loop
            for ship in players:
                ship.draw()
                

            #update screen    
            pygame.display.flip()


class Enemy(): 
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.game = game
        self.direction = random.randint(0,1)
        self.size = 20
    
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0,255,0), #RGB color
                         pygame.Rect(self.x,self.y,20,20))
        
        if self.direction == 1:
            self.x += 1
        else:
            self.x -= 1
        if self.x > self.game.width - self.size or self.x < 0:
            if self.direction == 1:
                self.direction = 0
            else:
                self.direction = 1
            self.y += 30


    
    def fire():
        return
    def death():
        return
    def checkhit():
        return
    

if __name__ == '__main__':
    game = Game(800, 600)
#start = Game(800,600)