import pygame
import time
import random
pygame.init()

class game():
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
        print('init')
        #car(self,x,y)

    def car(self,x,y):
        print('car start')
        self.gd.blit(self.car1,(x,y))
        pygame.display.update()
        print('car end')

    def gameloop(self):
        print('gameloop')
        self.x_change = 0
        self.lead_y = 0
        self.x = 300
        self.y = 490
        self.block = 10
        self.game_over = False
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
            self.gd.fill(self.black)
            self.clock.tick(60)
            pygame.display.update()

game()
pygame.quit()
quit()
