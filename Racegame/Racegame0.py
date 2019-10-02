import pygame
import time
import random
pygame.init()


        #her indsætter vi farver
grey = (110, 110, 110)
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
        #så displayer vi surfacet
size = window_width, window_hight = 800, 600
gd = pygame.display.set_mode(size)
car_image = pygame.image.load('Bil.png')
car1 = pygame.transform.scale(car_image, (100,100))
clock = pygame.time.Clock()
        #car(self,x,y)

def carLoad(x,y):
    gd.blit(car1,(x,y))
    pygame.display.update()

def gameLoop():
    x_change = 0
    lead_y = 0
    x = 300
    y = 490
    block = 10
    game_over = False
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block
                elif event.key == pygame.K_RIGHT:
                    x_change = +block
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gd.fill(grey)
        carLoad(x,y)
        clock.tick(60)
        pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
gameLoop()
#pygame.quit()
#quit()
