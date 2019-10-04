import pygame
import time
import random
pygame.init()

class gameMec():
    def __init__(self):
        self.xChange = 0
        #xChange er en potentiel ændring i x koordinatet
        #self.lead_y = 0 ???????
        self.xCar = 300
        #bilens x koordinat
        self.yCar = 490
        #bilens y koordinat
        self.block = 10
        #en konstant som bilen skal kunne flytte sig med senere
        self.gameOver = False
        #en variabel der skal hjælpe med at lukke pygame korrekt
        self.gV = gameVisuals()
        #en variabel der kalder på klassen gameVisuals
        self.gd = gV.gd
        #her kalder vi variablen gd som egentligt ligger i gameVisuals og derfor er der skravet gV foran

    def genericMessage(self,size,message,color1,color2,x,y):
        #her bruges der rigtigt mange parametrer som bruges senere i funktionen
        if self.buttonCreation == True:
        #her checker vi om buttonCreation er true for at finde ud af om vi skal lave tekst eller tekst til en knap
            self.buttonCreation = False
            #her gør vi buttonCreation falsk fordi vi har checket og der er blevet besluttet at vi skal lave en knap
            if x<self.mousePos[0]<x+100 and y<self.mousePos[1]<y+40:
            #her checker vi om musens position er indenfor kassens x og y koordinater
                self.font = pygame.font.SysFont(None,size)
                #her laver vi en font og størrelsen bliver defineret af parameteren size
                self.screenText = self.font.render(message,True,color1)
                #her laver vi teksten og gemmer i en variabel. beskeden kommer fra parameteren message og farven fra color1
                self.gd.blit(self.screenText, (x, y))
                #her bruger vi variablen gd sammen med funktionen blit til så at sige printe variablen screentext^^ på skærmen
                #og der bruges et x og y koordinat fra parameteret til at bestemme tekstens position
            else:
                self.font = pygame.font.SysFont(None,size)
                self.screenText = self.font.render(message,True,color2)
                self.gd.blit(self.screenText, (x, y))
                #her gøres det samme som ovenover, forskellen er blot farven
                #grunden til det samme gøres igen er at der så sker en farveændring når musen kører over knappen
        else:
            self.font = pygame.font.SysFont(None,size)
            self.screenText = self.font.render(message,True,color2)
            self.gd.blit(self.screenText, (x, y))
            #her laver vi igen bare noget tekst, forskellen er at dette tekst ikke er beregnet til at være
            #i en knap, derfor kan det ikke skifte farve når musen kører hen over
            pygame.display.update()
            #her opdaterer vi vores display sådan så vi nu viser teksten, tegningen eller andet


    def genericButton(self,x,y,message,color1,color2,onClick):
        #igen er der mange parametrer som vi skal bruge i funktionen
        self.mousePos = pygame.mouse.get_pos()
        self.mouseClick = pygame.mouse.get_pressed() #ændre lokation?
        self.buttonCreation = True
        #her sætter vi buttonCreation=sand. dette gøres fordi denne funktion kun bliver kaldt når vi laver en knap
        #og så kan genericMessage() se at vi laver en knaptekst
        if x<self.mousePos[0]<x+100 and y<self.mousePos[1]<y+40:
        #her laver vi det samme som i genericMessage, altså chekker vi om musen kører over knappen
            pygame.draw.rect(self.gd, color2, [x, y, 100, 40])
            #her tegner vi en kasse med farve 2, x og y fra parameteret. Bredden og højden af kassen er fastsat til 100x40
            gM.genericMessage(55,message,color1,color2,x,y)
            #Her skaber vi en besked til vores knap ved at kalde på genericMessage med parametrer og strørrelsen (size) er fastsat
            if self.mouseClick == (1,0,0):
                onClick()
        else:
            pygame.draw.rect(self.gd, color1, [x, y, 100, 40])
            gM.genericMessage(55,message,color1,color2,x,y)
        pygame.display.update()
        #opdatering

    def gameLoop(self):
        while self.gameOver == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.xChange = -self.block
                    elif event.key == pygame.K_RIGHT:
                        self.xChange = +self.block
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.xChange = 0
            self.xCar += self.xChange
            if self.xCar < 0:
                self.xCar = 0
            elif self.xCar > 700:
                self.xCar = 700
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
            gM.genericButton(350, 200,'PLAY', self.red, self.black, gM.gameLoop)
            pygame.display.update()

    def carLoad(self,x,y):
        self.gd.fill(self.black)
        self.gd.blit(self.car1,(x,y))
        self.clock.tick(60)
        pygame.display.update()


gV = gameVisuals()
gM = gameMec()
gV.gameIntro()
#gM.gameLoop()
