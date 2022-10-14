import pygame
from win32api import GetSystemMetrics

class menu:
    def __init__(self, window, xWindow, yWindow, fullScreen):
        pathImagen = "imagenes/"
        pathMenu = "menu/"
        pathRectangulo = pathImagen + pathMenu + "main/"
        pathPlay = pathRectangulo + "play/"
        pathExit = pathRectangulo + "exit/"
        pathOptions = pathRectangulo + "options/"

        self.rectanguloPlayNotSelected = pygame.image.load(pathPlay + "playNotSelected.png").convert_alpha()
        self.heightRectangulo = self.rectanguloPlayNotSelected.get_height()

        self.xWindow, self.yWindow = xWindow, yWindow
        self.changeValues = False

        self.fullScreen = fullScreen
        
        if self.fullScreen:
            maxHeightWindow = GetSystemMetrics(1)

        else:
            maxHeightWindow = self.yWindow

        self.rectanguloPlayOnSelected = pygame.image.load(pathPlay + "playOnSelected.png").convert_alpha()
        self.rectanguloPlayNotSelected = pygame.image.load(pathPlay + "playNotSelected.png").convert_alpha()

        self.rectanguloExitOnSelected = pygame.image.load(pathExit + "exitOnSelected.png").convert_alpha()
        self.rectanguloExitNotSelected = pygame.image.load(pathExit + "exitNotSelected.png").convert_alpha()

        self.rectanguloOptionsOnSelected = pygame.image.load(pathOptions + "optionsOnSelected.png").convert_alpha()
        self.rectanguloOptionsNotSelected = pygame.image.load(pathOptions + "optionsNotSelected.png").convert_alpha()

        #------------------------------
        #-----------------------------

        self.arrow = pygame.image.load(pathImagen + "arrow.png").convert_alpha()
        self.arrowWidth, self.arrowHeight = self.arrow.get_width(), self.arrow.get_height()
        
        self.window = window

        self.xRectangulo = 0
        self.yListRectangulo = [(maxHeightWindow / 4) - self.heightRectangulo/2,  ((maxHeightWindow / 4) * 2) - self.heightRectangulo/2, 
                    ((maxHeightWindow / 4) * 3) - self.heightRectangulo/2]

        self.contYArrow = 0
        self.contChange = 0

        self.yArrowList = [(maxHeightWindow / 4) - self.heightRectangulo/2,  ((maxHeightWindow / 4) * 2) - self.heightRectangulo/2, 
                    ((maxHeightWindow / 4) * 3) - self.heightRectangulo/2]


    def draw(self, fullscreen):
        if fullscreen:
            self.changeValues = True
            maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

        else:
            self.changeValues = False 
            maxWidthWindow, maxHeightWindow = self.xWindow, self.yWindow
        #------------------------------

        if self.changeValues:
            #print("full screen")
            self.heightRectangulo = self.rectanguloPlayNotSelected.get_height() // 2
            self.arrow = pygame.transform.scale(self.arrow, (self.arrowWidth, self.arrowHeight))
            self.arrowWidth, self.arrowHeight = self.arrow.get_width(), self.arrow.get_height()

            rectanguloPlayOnSelected = pygame.transform.scale(self.rectanguloPlayOnSelected, (maxWidthWindow, self.heightRectangulo))
            rectanguloPlayNotSelected = pygame.transform.scale(self.rectanguloPlayNotSelected, (maxWidthWindow, self.heightRectangulo))

            rectanguloOptionsNotSelected = pygame.transform.scale(self.rectanguloOptionsNotSelected, (maxWidthWindow, self.heightRectangulo))
            rectanguloOptionsOnSelected = pygame.transform.scale(self.rectanguloOptionsOnSelected, (maxWidthWindow, self.heightRectangulo))

            rectanguloExitOnSelected = pygame.transform.scale(self.rectanguloExitOnSelected, (maxWidthWindow, self.heightRectangulo))
            rectanguloExitNotSelected = pygame.transform.scale(self.rectanguloExitNotSelected, (maxWidthWindow, self.heightRectangulo))

        else:
            #print("window")
            self.heightRectangulo = self.rectanguloPlayNotSelected.get_height() // 4
            self.arrow = pygame.transform.scale(self.arrow, (self.arrowWidth//2, self.arrowHeight//2))

            rectanguloPlayOnSelected = pygame.transform.scale(self.rectanguloPlayOnSelected, (self.xWindow, self.heightRectangulo))
            rectanguloPlayNotSelected = pygame.transform.scale(self.rectanguloPlayNotSelected, (self.xWindow, self.heightRectangulo))

            rectanguloOptionsNotSelected = pygame.transform.scale(self.rectanguloOptionsNotSelected, (self.xWindow, self.heightRectangulo))
            rectanguloOptionsOnSelected = pygame.transform.scale(self.rectanguloOptionsOnSelected, (self.xWindow, self.heightRectangulo))

            rectanguloExitOnSelected = pygame.transform.scale(self.rectanguloExitOnSelected, (self.xWindow, self.heightRectangulo))
            rectanguloExitNotSelected = pygame.transform.scale(self.rectanguloExitNotSelected, (self.xWindow, self.heightRectangulo))

        #-----------------------------
        
        self.yListMenu = [(maxHeightWindow / 4) - self.heightRectangulo/2,  ((maxHeightWindow / 4) * 2) - self.heightRectangulo/2, 
                    ((maxHeightWindow / 4) * 3) - self.heightRectangulo/2]
        #-----------------------------

        xArrow, yArrow = 0, self.yListMenu[self.contYArrow] 

        if self.contYArrow == 0:
            self.window.blit(rectanguloPlayOnSelected, (self.xRectangulo, self.yListMenu[0]))
            self.window.blit(rectanguloOptionsNotSelected, (self.xRectangulo, self.yListMenu[1]))
            self.window.blit(rectanguloExitNotSelected, (self.xRectangulo, self.yListMenu[2]))

        if self.contYArrow == 1:
            self.window.blit(rectanguloOptionsOnSelected, (self.xRectangulo, self.yListMenu[1]))
            self.window.blit(rectanguloPlayNotSelected, (self.xRectangulo, self.yListMenu[0]))
            self.window.blit(rectanguloExitNotSelected, (self.xRectangulo, self.yListMenu[2]))

        if self.contYArrow == 2:
            self.window.blit(rectanguloExitOnSelected, (self.xRectangulo, self.yListMenu[2]))
            self.window.blit(rectanguloPlayNotSelected, (self.xRectangulo, self.yListMenu[0]))
            self.window.blit(rectanguloOptionsNotSelected, (self.xRectangulo, self.yListMenu[1]))

        self.window.blit(self.arrow, (xArrow, yArrow))

    def manage_events(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.contChange += 1

            if self.contChange > 10: #10 must be a variable. 
                self.contYArrow += 1
                self.contChange = 0

        if key[pygame.K_UP]:
            self.contChange += 1

            if self.contChange > 10:
                self.contYArrow -= 1
                self.contChange = 0

        if self.contYArrow > 2:
            self.contYArrow = 0

        if self.contYArrow < 0:
            self.contYArrow = 2