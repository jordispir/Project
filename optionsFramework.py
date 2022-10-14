
import pygame
from win32api import GetSystemMetrics


class options:
    def __init__(self, window, xWindow, yWindow, fullScreen):
        self.pathOptions = "imagenes/menu/options/"
        self.pathSound = self.pathOptions + "sound/"

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

            if self.sonido == 1:
                self.volume20 = True
                self.window.blit(self.sound20, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))


            if self.sonido == 2:
                self.volume40 = True
                self.window.blit(self.sound40, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

            
            if self.sonido == 3:
                self.volume60 = True
                self.window.blit(self.sound60, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))


            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))


            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3))

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


            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))


            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (self.xWindow//2 - self.soundBarWidth//4, self.yWindow//3))

        if self.volume0:
            self.soundTest.stop()

            self.volume0 = False
            self.volume20 = False
            self.volume40 = False
            self.volume60 = False
            self.volume80 = False
            self.volume100 = False

        if self.volume20:
            self.volume0 = False

            self.soundTest.play()
            self.soundTest.set_volume(20)


        if self.volume40: 
            self.volume0 = False
            self.volume20 = False
            self.volume60 = False
            self.volume80 = False
            self.volume100 = False

            self.soundTest.play()
            self.soundTest.set_volume(40)

        if self.volume60: 
            self.volume20 = False
            self.volume40 = False
            self.volume80 = False
            self.volume100 = False

            self.soundTest.play()
            self.soundTest.set_volume(60)

        if self.volume80: 
            self.volume0 = False
            self.volume20 = False
            self.volume40 = False
            self.volume60 = False
            self.volume100 = False

            self.soundTest.play()
            self.soundTest.set_volume(80)

        if self.volume100: 
            self.volume0 = False
            self.volume20 = False
            self.volume40 = False
            self.volume60 = False
            self.volume80 = False 

            self.soundTest.play()
            self.soundTest.set_volume(100)

        print(self.volume20, self.volume40)

    def manage_events(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.contChange += 1

            if self.contChange > 10:
                self.sonido += 1
                self.contChange = 0


        if key[pygame.K_LEFT]:
            self.contChange += 1

            if self.contChange > 10:
                self.sonido -= 1
                self.contChange = 0

        if self.sonido > 5:
            self.sonido = 5

        if self.sonido < 0:
            self.sonido = 0

