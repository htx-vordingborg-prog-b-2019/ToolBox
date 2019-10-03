import pygame
import time
import random
pygame.init()

class gameMec():
    def __init__(self):
        print('gameloop')
        self.x_change = 0
        self.lead_y = 0
        self.x = 300
        self.y = 490
        self.block = 10
        self.game_over = False
        self.V = Visuals()

    def gameLoop(self):
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change = -self.block
                    elif event.key == pygame.K_RIGHT:
                        self.x_change = +self.block
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.x_change = 0
            self.x += self.x_change
            self.V.carLoad(self.x,self.y)
            pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

class Visuals():
    def __init__(self):
        #her indsætter vi farver i rbg
        self.grey = (110, 110, 110)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (200,0,0)
        self.green = (0,200,0)
        self.blue = (0,0,200)
        self.bright_red = (255,0,0)
        self.bright_green = (0,255,0)
        self.bright_blue = (0,0,255)
        #så displayer vi surfacet
        self.size = window_width, window_hight = 800, 600
        self.gd = pygame.display.set_mode(self.size)
        self.car_image = pygame.image.load('Bil.png')
        self.car1 = pygame.transform.scale(self.car_image, (100,100))
        self.clock = pygame.time.Clock()

    def gameIntro():
        #while k.
        self.background = pygame.image.load('navn')
        self.gd.blit(background, (0,0))
        pygame.display.update()

    def carLoad(self,x,y):
        self.gd.fill(self.black)
        self.gd.blit(self.car1,(x,y))
        pygame.display.update()
        self.clock.tick(60)



k = gameMec()
k.gameLoop()
#pygame.quit()
#quit()
