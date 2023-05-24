import pygame
import random

class Game():

    def __init__(self,width,height,difficulty=1):
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

        self.aliens = [] #aliens list will auto generate later
        self.rockets = [] #rocket list

        self.difficulty = difficulty
        print("Difficulty: ", difficulty)
        gen = EnemyGenerator(self)
        for i in range(difficulty):
            gen.spawn(10,i)
        print("Aliens spawned: ",len(self.aliens))

        player = Player(self)

        # MAIN LOOP VARIABLE
        running = True
        while running:
            #BLANK SCREEN
            self.screen.fill((0, 0, 0)) 
            #QUIT event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.rockets.append(Rocket(self,player.x,player.y))
            #WINNING EVENT INCREASE DIFFICULTY
            if len(self.aliens) == 0:
                self.displaytext("YOU WON!")
                self.difficulty += 1
                self.restart(self.difficulty)
            #player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.x +=2
            if keys[pygame.K_LEFT]:
                player.x -=2

            #aliens draw loop
            for alien in self.aliens:
                alien.draw()
                alien.checkhit(self)
            
            #player draw loop
            player.draw()
            if player.collisioncheck(self):
                self.displaytext("YOU DIED!")
                self.restart()
            
            for rocket in self.rockets:
                rocket.draw()
                
            #UPDATE SCREEN   
            pygame.display.flip()
    
    def displaytext(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 60)
        textsurface = font.render(text, False, (255, 0, 0))
        coords = textsurface.get_rect(center=(self.width//2,self.height//2))
        self.screen.blit(textsurface, coords)
    
    def restart(self,difficulty=1):
        self.aliens.clear()
        self.rockets.clear()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    game = Game(800,600,difficulty)
                    
class Player():
    def __init__(self,game):
        self.game = game
        self.lives = 3
        self.x = self.game.width/2 - 13
        self.y = self.game.height - 25
        self.size = 15

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0, 0, 255),
                         pygame.Rect(self.x, self.y, self.size, self.size))
        if self.x > self.game.width - self.size:
            self.x = self.game.width - self.size
        if self.x < 0:
            self.x = 0
            
    def collisioncheck(self,game):
        for alien in game.aliens:
            if (alien.x < self.x + self.size and
                alien.x > self.x - self.size and
                alien.y < self.y + self.size and
                alien.y > self.y - self.size):
                self.lives -= 1
                return True
            else:
                return False
            
class Enemy(): 
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.game = game
        self.direction = random.randint(0,1)
        self.size = 25
        self.speed = 1
    
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0,255,0), #RGB color
                         pygame.Rect(self.x,self.y,self.size,self.size))
        if self.direction == 1:
            self.x += self.speed
        else:
            self.x -= self.speed
        if self.x > self.game.width - self.size or self.x < 0:
            if self.direction == 1:
                self.direction = 0
            else:
                self.direction = 1
            self.y += 30
            self.speed *= 1.17

    def checkhit(self,game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                rocket.x > self.x and
                rocket.y < self.y + self.size and
                rocket.y > self.y ):
                game.rockets.remove(rocket)
                game.aliens.remove(self)


class EnemyGenerator():
    def __init__(self,game):
        self.x,self.y = (30,30)
        self.game = game

    def spawn(self,number = 1,row = 0):
        for a in range(number):
            x = random.randint(30,self.game.width-30)
            y = self.y + 30 * row
            self.game.aliens.append(Enemy(self.game,x,y))

class Rocket():
    def __init__(self,game,x,y):
        self.x = x + 6
        self.y = y - 8
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (255,0,0), #RGB color
                         pygame.Rect(self.x,self.y,3,8))
        self.y -= 2
        if self.y < 0:
            self.game.rockets.remove(self)

if __name__ == '__main__':
    game = Game(800, 600)

#start = Game(800,600)