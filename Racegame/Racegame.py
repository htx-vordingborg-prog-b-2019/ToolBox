import pygame
import time
import random
pygame.init()

class gameMec():
    def __init__(self):
        self.xChange = 0
        self.lead_y = 0
        self.xCar = 300
        self.yCar = 490
        self.block = 10
        self.gameOver = False
        self.gV = gameVisuals()
        self.gd = gV.gd

    def genericMessage(self,size,message,color2,x,y):
        self.font = pygame.font.SysFont(None,size)
        self.screenText = self.font.render(message,True,color2)
        self.gd.blit(self.screenText, (x, y))

    def genericButton(self,x,y,message,color1,color2):
        self.mousePos = pygame.mouse.get_cursor()
        self.mouseClick = pygame.mouse.get_pressed()
        if self.mousePos > self.x and self.mousePos < self.x+100:

        pygame.draw.rect(self.gd, color1, [x, y, 100, 40])
        gM.genericMessage(55,message,color2,x,y)
        pygame.display.update()

    def gameLoop(self):
        while self.gameOver == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Xchange = -self.block
                    elif event.key == pygame.K_RIGHT:
                        self.Xchange = +self.block
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.Xchange = 0
            self.xCar += self.Xchange
            self.gV.carLoad(self.xCar,self.yCar)
            pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

class gameVisuals():
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
        self.gameOver = False


    def gameIntro(self):
        while self.gameOver == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.background = pygame.image.load('Placeholder.png')
            self.gd.blit(self.background, (0,0))
            gM.genericButton(350, 200,'PLAY', self.red, self.black)
            pygame.display.update()

    def carLoad(self,x,y):
        self.gd.fill(self.black)
        self.gd.blit(self.car1,(x,y))
        pygame.display.update()
        self.clock.tick(60)


gV = gameVisuals()
gM = gameMec()
gV.gameIntro()
#gM.gameLoop()
