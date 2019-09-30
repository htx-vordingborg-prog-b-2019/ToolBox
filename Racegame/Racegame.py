import pygame
import time
import random

pygame.init()

class game:
    def __init__(self):
        #her indsætter farverne i rbg
        self.grey=(110, 110, 110)
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(200,0,0)
        self.green=(0,200,0)
        self.blue=(0,0,200)
        self.bright_red=(255,0,0)
        self.bright_green=(0,255,0)
        self.bright_blue=(0,0,255)
        self.size = window_width, window_hight = 800, 600
        #så displayer vi surfacet
        self.gd=pygame.display.set_mode(size)
        self.car_image=pygame.image.load('Bil.png')
        self.car1=pygame.transform.scale(car_image, (100,100))
        self.clock=pygame.time.Clock()
        car(self)

    def car(self,x,y):
        screen.blit(car1,(x,y))
        self.pygame.display.update()
        gameloop(self)


    def gameloop(self):
        self.x_change = 0
        self.lead_y = 0
        self.x = 300
        self.y = 490
        self.block =  10
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
        #dette skaber en fejl nedenunder
        screen.fill(self.black)
        car(self,x,y)
        clock.tick(60)
        pygame.display.update()

pygame.quit()
quit()
