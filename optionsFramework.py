import pygame
from win32api import GetSystemMetrics


class options:
    def __init__(self, window, xWindow, yWindow, fullScreen):
        self.pathOptions = "imagenes/menu/options/"
        self.pathSound = self.pathOptions + "sound/"
        self.pathButton = self.pathOptions + "buttons/"

        self.xWindow, self.yWindow = xWindow, yWindow

        self.fullScreen = fullScreen

        self.soundTest = pygame.mixer.Sound("imagenes/menu/options/sound_effects/testSoundEffect.mp3")

        self.sound0 = pygame.image.load(self.pathSound + "sound0.png").convert_alpha()
        self.sound20 = pygame.image.load(self.pathSound + "sound20.png").convert_alpha()
        self.sound40 = pygame.image.load(self.pathSound + "sound40.png").convert_alpha()
        self.sound60 = pygame.image.load(self.pathSound + "sound60.png").convert_alpha()
        self.sound80 = pygame.image.load(self.pathSound + "sound80.png").convert_alpha()
        self.sound100 = pygame.image.load(self.pathSound + "sound100.png").convert_alpha()

        self.soundBarWidth, self.soundBarHeight = self.sound0.get_width(), self.sound0.get_height()

        self.changeValues = False

        #self.arrow = pygame.image.load(pathImagen + "arrow.png").convert_alpha()
        #self.arrowWidth, self.arrowHeight = self.arrow.get_width(), self.arrow.get_height()
        
        self.window = window

        self.sonido = 0

        self.contChange = 0

        self.volume0 = True 
        self.volume20 = False
        self.volume40 = False
        self.volume60 = False
        self.volume80 = False
        self.volume100 = False

        self.goLvl = False

        self.backButtonX, self.backButtonY = 100, 100
        
        
        self.backButton60 = pygame.image.load(self.pathButton + "back_button60.png").convert_alpha()
        self.backButton70 = pygame.image.load(self.pathButton + "back_button70.png").convert_alpha()
        self.backButton80 = pygame.image.load(self.pathButton + "back_button80.png").convert_alpha()
        self.backButton90 = pygame.image.load(self.pathButton + "back_button90.png").convert_alpha()
        self.backButton100 = pygame.image.load(self.pathButton + "back_button100.png").convert_alpha()

        self.backButton60Width, self.backButton60Height = self.backButton60.get_width(), self.backButton60.get_height()
        self.backButton80Width, self.backButton80Height = self.backButton80.get_width(), self.backButton80.get_height()
        self.backButton100Width, self.backButton100Height = self.backButton100.get_width(), self.backButton100.get_height()

        self.contChangeButtonDelay = 0
        self.contChangeButton = 0

        self.reverse = False

        self.timeDelay = 10

    def draw(self, fullScreen):
        if fullScreen:
            self.changeValues = True
            maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

        else:
            self.changeValues = False
            maxWidthWindow, maxHeightWindow = self.xWindow, self.yWindow


        if self.changeValues: 
            self.sound0 = pygame.transform.scale(self.sound0, (self.soundBarWidth, self.soundBarHeight))
            self.sound20 = pygame.transform.scale(self.sound20, (self.soundBarWidth, self.soundBarHeight))
            self.sound40 = pygame.transform.scale(self.sound40, (self.soundBarWidth, self.soundBarHeight))
            self.sound60 = pygame.transform.scale(self.sound60, (self.soundBarWidth, self.soundBarHeight))
            self.sound80 = pygame.transform.scale(self.sound80, (self.soundBarWidth, self.soundBarHeight))
            self.sound100 = pygame.transform.scale(self.sound100, (self.soundBarWidth, self.soundBarHeight))


            if self.sonido == 0:
                self.volume0 = True
                self.window.blit(self.sound0, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 1:
                self.volume20 = True
                self.window.blit(self.sound20, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume0 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False


            if self.sonido == 2:
                self.volume40 = True
                self.window.blit(self.sound40, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            
            if self.sonido == 3:
                self.volume60 = True
                self.window.blit(self.sound60, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume80 = False
                self.volume100 = False


            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume100 = False

            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False

            self.contChangeButtonDelay += 1 

            if self.contChangeButtonDelay > self.timeDelay:

                if self.reverse == False:
                    self.contChangeButton += 1

                if self.reverse:
                    self.contChangeButton -= 1

                self.contChangeButtonDelay = 0


            if self.contChangeButton >= 7:
                self.reverse = True

            if self.contChangeButton <= 0:
                self.reverse = False


            if self.contChangeButton == 0:
                self.window.blit(self.backButton100, (maxWidthWindow - 100, maxHeightWindow - 100))


            elif self.contChangeButton == 1:
                self.window.blit(self.backButton90, (maxWidthWindow - 95, maxHeightWindow - 95))

            elif self.contChangeButton == 2:
                self.window.blit(self.backButton80, (maxWidthWindow - 90, maxHeightWindow - 90))

            elif self.contChangeButton == 3:
                self.window.blit(self.backButton70, (maxWidthWindow - 85, maxHeightWindow - 85))
                       
            elif self.contChangeButton == 4:
       
                self.window.blit(self.backButton60, (maxWidthWindow - 80, maxHeightWindow - 80))

            elif self.contChangeButton == 5:
                self.window.blit(self.backButton70, (maxWidthWindow - 85, maxHeightWindow - 85))
       
            elif self.contChangeButton == 6:
                self.window.blit(self.backButton80, (maxWidthWindow - 90, maxHeightWindow - 90))
       
            elif self.contChangeButton == 7:
                self.window.blit(self.backButton90, (maxWidthWindow - 95, maxHeightWindow - 95))
        else:
            self.sound0 = pygame.transform.scale(self.sound0, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound20 = pygame.transform.scale(self.sound20, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound40 = pygame.transform.scale(self.sound40, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound60 = pygame.transform.scale(self.sound60, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound80 = pygame.transform.scale(self.sound80, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound100 = pygame.transform.scale(self.sound100, (self.soundBarWidth//2, self.soundBarHeight//2))

            if self.sonido == 0:
                self.volume0 = True
                self.window.blit(self.sound0, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))
            
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 1:
                self.volume20 = True
                self.window.blit(self.sound20, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

                self.volume0 = False
                self.volume020 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 2:
                self.volume40 = True
                self.window.blit(self.sound40, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            
            if self.sonido == 3:
                self.volume60 = True
                self.window.blit(self.sound60, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume80 = False
                self.volume100 = False


            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume100 = False


            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False



            self.contChangeButtonDelay += 1 

            if self.contChangeButtonDelay > self.timeDelay:

                if self.reverse == False:
                    self.contChangeButton += 1

                if self.reverse:
                    self.contChangeButton -= 1

                self.contChangeButtonDelay = 0


            if self.contChangeButton >= 7:
                self.reverse = True

            if self.contChangeButton <= 0:
                self.reverse = False


            if self.contChangeButton == 0:
                self.window.blit(self.backButton100, (self.xWindow - 100, self.yWindow - 100))


            elif self.contChangeButton == 1:
                self.window.blit(self.backButton90, (self.xWindow - 95, self.yWindow - 95))

            elif self.contChangeButton == 2:
                self.window.blit(self.backButton80, (self.xWindow - 90, self.yWindow - 90))

            elif self.contChangeButton == 3:
                self.window.blit(self.backButton70, (self.xWindow - 85, self.yWindow - 85))
                       
            elif self.contChangeButton == 4:
       
                self.window.blit(self.backButton60, (self.xWindow - 80, self.yWindow - 80))

            elif self.contChangeButton == 5:
                self.window.blit(self.backButton70, (self.xWindow - 85, self.yWindow - 85))
       
            elif self.contChangeButton == 6:
                self.window.blit(self.backButton80, (self.xWindow - 90, self.yWindow - 90))
       
            elif self.contChangeButton == 7:
                self.window.blit(self.backButton90, (self.xWindow - 95, self.yWindow - 95))




        if self.volume0:
            #print("0")
            self.soundTest.stop()

        if self.volume20:
            print("20")

            self.soundTest.set_volume(0.2)
            self.soundTest.play()

        if self.volume40: 
            print("40")

            self.soundTest.set_volume(0.4)
            self.soundTest.play()

        if self.volume60: 
            print("60")

            self.soundTest.set_volume(0.6)
            self.soundTest.play()

        if self.volume80: 
            print("80")

            self.soundTest.set_volume(0.8)
            self.soundTest.play()

        if self.volume100: 
            print("100")

            self.soundTest.set_volume(1)
            self.soundTest.play()

        #print(self.volume20, self.volume40)


    def manage_events(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.contChange += 1

            if self.contChange > 10:
                self.sonido += 1
                self.contChange = 0


        elif key[pygame.K_LEFT]:
            self.contChange += 1

            if self.contChange > 10:
                self.sonido -= 1
                self.contChange = 0

        elif key[pygame.K_ESCAPE] or key[pygame.K_BACKSPACE]:
            self.goLvl = True

        else:
            self.goLvl = False

        if self.sonido > 5:
            self.sonido = 5

        if self.sonido < 0:
            self.sonido = 0

