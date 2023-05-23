import pygame
import random

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
        self.screen.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        #background = pygame.image.load('background.png')
        
        aliens = [] #aliens list will auto generate later
        alien = Enemy(self,30,30)
        aliens.append(alien)


        player = Player(self)
        

        # MAIN LOOP VARIABLE
        running = True
        while running:
            #BLANK SCREEN
            self.screen.fill((0, 0, 0)) 
            
            #QUIT event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.x +=1
            if keys[pygame.K_LEFT]:
                player.x -=1

            #aliens draw loop
            for alien in aliens:
                alien.draw()
            
            #player draw loop
            player.draw()
                
            #UPDATE SCREEN   
            pygame.display.flip()

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
    
    def collisioncheck(self):
        
        self.lives -= 1

        
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

class Generator():
    def __init__(self,game):
        self.x,self.y = (30,30)
        self.game = game
    
class Rocket():
    def __init__(self,x,y):
        self.x = x
        self.y = y   


if __name__ == '__main__':
    game = Game(800, 600)

#start = Game(800,600)