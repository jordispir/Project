import pygame
from win32api import GetSystemMetrics

class options:
    def __init__(self, window, xWindow, yWindow, fullScreen):
        self.pathOptions = "images/menu/options/"
        self.pathSound = self.pathOptions + "sound/"
        self.pathButton = self.pathOptions + "buttons/"
        self.pathResolution = self.pathOptions + "resolutions/"
        self.pathArrow = self.pathOptions + "arrow/"

        maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)
        self.windowWidth, self.heighWindow = xWindow, yWindow

        self.fullScreen = fullScreen

        self.backGround = pygame.image.load(self.pathOptions + "bg.png").convert_alpha()
        self.bgX, self.bgY = 0, 0

        try:
            self.soundTest = pygame.mixer.Sound("images/menu/options/sound_effects/testSoundEffect.mp3")

        except:
            print("respositorio faltante sound test")

        self.sound0 = pygame.image.load(self.pathSound + "sound0.png").convert_alpha()
        self.sound20 = pygame.image.load(self.pathSound + "sound20.png").convert_alpha()
        self.sound40 = pygame.image.load(self.pathSound + "sound40.png").convert_alpha()
        self.sound60 = pygame.image.load(self.pathSound + "sound60.png").convert_alpha()
        self.sound80 = pygame.image.load(self.pathSound + "sound80.png").convert_alpha()
        self.sound100 = pygame.image.load(self.pathSound + "sound100.png").convert_alpha()

        self.soundBarWidth, self.soundBarHeight = self.sound0.get_width(), self.sound0.get_height()
        self.soundBarFullScreenX, self.soundBarFullScreenY = maxWidthWindow//2 - self.soundBarWidth//2, maxHeightWindow//3
        self.soundBarWindowX, self.soundBarWindowY = self.windowWidth//2 - self.soundBarWidth//4, self.heighWindow//3

        self.changeValues = False

        self.window = window

        self.volume0 = True 
        self.volume20 = False
        self.volume40 = False
        self.volume60 = False
        self.volume80 = False
        self.volume100 = False

        self.goLvl = False

        self.backButton60 = pygame.image.load(self.pathButton + "back_button60.png").convert_alpha()
        self.backButton70 = pygame.image.load(self.pathButton + "back_button70.png").convert_alpha()
        self.backButton80 = pygame.image.load(self.pathButton + "back_button80.png").convert_alpha()
        self.backButton90 = pygame.image.load(self.pathButton + "back_button90.png").convert_alpha()
        self.backButton100 = pygame.image.load(self.pathButton + "back_button100.png").convert_alpha()

        self.backButton60Width, self.backButton60Height = self.backButton60.get_width(), self.backButton60.get_height()
        self.backButton80Width, self.backButton80Height = self.backButton80.get_width(), self.backButton80.get_height()
        self.backButton100Width, self.backButton100Height = self.backButton100.get_width(), self.backButton100.get_height()

        self.sonido = 0
        self.contChange = 0
        self.contChangeButtonDelay = 0
        self.contChangeButton = 0
        self.timeDelay = 10

        self.reverseArrow = False
        self.reverse = False

        self.resolutionFullScreen = pygame.image.load(self.pathResolution + "resolutionFullScreen.png").convert_alpha()
        self.resolutionFullScreenWidth, self.resolutionFullScreenHeight = self.resolutionFullScreen.get_width(), self.resolutionFullScreen.get_height()

        self.resolutionWindow = pygame.image.load(self.pathResolution + "resolutionWindow.png").convert_alpha()
        self.resolutionWindowWidth, self.resolutionWindowHeight = self.resolutionWindow.get_width(), self.resolutionWindow.get_height()

        self.resolutionWindow = pygame.transform.scale(self.resolutionWindow, (self.resolutionFullScreenWidth//2, self.resolutionFullScreenHeight//2))

        self.arrowList = [pygame.image.load(self.pathArrow + "arrow100.png").convert_alpha(), 
                        pygame.image.load(self.pathArrow + "arrow75.png").convert_alpha(),
                        pygame.image.load(self.pathArrow + "arrow50.png").convert_alpha(),
                        pygame.image.load(self.pathArrow + "arrow25.png").convert_alpha(),
                        pygame.image.load(self.pathArrow + "arrow0.png").convert_alpha()]

        self.arrowWidth, self.arrowHeight = self.arrowList[0].get_width(), self.arrowList[0].get_height()

        self.arrowWidthWindow, self.arrowHeightWindow = self.arrowWidth // 4, self.arrowHeight // 4

        self.contArrow = 0
        self.contArrowDelay = 0
        self.arrowContChange = 0

        self.arrowListYWindow = [self.soundBarWindowY, self.soundBarWindowY + self.soundBarHeight]
        self.arrowListYFullScreen= [self.soundBarFullScreenY, self.soundBarFullScreenY + (self.soundBarHeight * 2)]

        self.arrowChangeDelay = 0
        self.arrowListPosition = 0

        self.arrowChangeVelocity = 5

        self.resolutionPosition = 0

        self.resolutionChangeVelocity = 1
        self.resolutionChangeDelay = 0

    def draw(self, fullScreen):

        if fullScreen:
            self.changeValues = True
            maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

        else:
            self.changeValues = False
            maxWidthWindow, maxHeightWindow = self.windowWidth, self.heighWindow

        if self.changeValues: 
            self.sound0 = pygame.transform.scale(self.sound0, (self.soundBarWidth, self.soundBarHeight))
            self.sound20 = pygame.transform.scale(self.sound20, (self.soundBarWidth, self.soundBarHeight))
            self.sound40 = pygame.transform.scale(self.sound40, (self.soundBarWidth, self.soundBarHeight))
            self.sound60 = pygame.transform.scale(self.sound60, (self.soundBarWidth, self.soundBarHeight))
            self.sound80 = pygame.transform.scale(self.sound80, (self.soundBarWidth, self.soundBarHeight))
            self.sound100 = pygame.transform.scale(self.sound100, (self.soundBarWidth, self.soundBarHeight))

            self.arrow = pygame.transform.scale(self.arrowList[self.contArrow], (self.arrowWidth // 2, self.arrowHeight // 2))
            self.backGround = pygame.transform.scale(self.backGround, (maxWidthWindow, maxHeightWindow))

            self.window.blit(self.backGround, (self.bgX, self.bgY))

            if self.sonido == 0:
                self.volume0 = True
                self.window.blit(self.sound0, (self.soundBarFullScreenX, self.soundBarFullScreenY))
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 1:
                self.volume20 = True
                self.window.blit(self.sound20, (self.soundBarFullScreenX, self.soundBarFullScreenY))
                self.volume0 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 2:
                self.volume40 = True
                self.window.blit(self.sound40, (self.soundBarFullScreenX, self.soundBarFullScreenY)) 
                self.volume0 = False
                self.volume20 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            
            if self.sonido == 3:
                self.volume60 = True
                self.window.blit(self.sound60, (self.soundBarFullScreenX, self.soundBarFullScreenY))
                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (self.soundBarFullScreenX, self.soundBarFullScreenY))
                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume100 = False

            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (self.soundBarFullScreenX, self.soundBarFullScreenY))
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


            self.contArrowDelay += self.arrowChangeVelocity
            if self.contArrowDelay > 20: 
                if not (self.reverseArrow):
                    self.contArrow += 1
                    self.contArrowDelay = 0

                else:
                    self.contArrow -= 1
                    self.contArrowDelay = 0

            if self.contArrow == 4:
                self.reverseArrow = True

            if self.contArrow == 0:
                self.reverseArrow = False

            if self.arrowListPosition == 0:
                xArrow, yArrow = self.soundBarFullScreenX - self.arrowWidth, self.arrowListYFullScreen[self.arrowListPosition]
                self.window.blit(self.arrow, (xArrow, yArrow))

            elif self.arrowListPosition == 1:
                xArrow, yArrow = self.soundBarFullScreenX - self.arrowWidth, self.arrowListYFullScreen[self.arrowListPosition]
                self.window.blit(self.arrow, (xArrow, yArrow))

            self.window.blit(self.resolutionFullScreen, (maxWidthWindow//2 - self.soundBarWidth//2, (maxHeightWindow//3) + self.soundBarHeight * 2))


        else:
            self.sound0 = pygame.transform.scale(self.sound0, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound20 = pygame.transform.scale(self.sound20, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound40 = pygame.transform.scale(self.sound40, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound60 = pygame.transform.scale(self.sound60, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound80 = pygame.transform.scale(self.sound80, (self.soundBarWidth//2, self.soundBarHeight//2))
            self.sound100 = pygame.transform.scale(self.sound100, (self.soundBarWidth//2, self.soundBarHeight//2))

            self.arrow = pygame.transform.scale(self.arrowList[self.contArrow], (self.arrowWidthWindow, self.arrowHeightWindow))

            self.backGround = pygame.transform.scale(self.backGround, (self.windowWidth, self.heighWindow))
            self.window.blit(self.backGround, (self.bgX, self.bgY))

            if self.sonido == 0:
                self.volume0 = True
                self.window.blit(self.sound0,  (self.soundBarWindowX, self.soundBarWindowY))
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 1:
                self.volume20 = True
                self.window.blit(self.sound20,  (self.soundBarWindowX, self.soundBarWindowY))
                self.volume0 = False
                self.volume020 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False

            if self.sonido == 2:
                self.volume40 = True
                self.window.blit(self.sound40, (self.soundBarWindowX, self.soundBarWindowY))
                self.volume0 = False
                self.volume20 = False
                self.volume60 = False
                self.volume80 = False
                self.volume100 = False
            
            if self.sonido == 3:
                self.volume60 = True
                self.window.blit(self.sound60, (self.soundBarWindowX, self.soundBarWindowY))
                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume80 = False
                self.volume100 = False


            if self.sonido == 4:
                self.volume80 = True
                self.window.blit(self.sound80, (self.soundBarWindowX, self.soundBarWindowY))
                self.volume0 = False
                self.volume20 = False
                self.volume40 = False
                self.volume60 = False
                self.volume100 = False


            if self.sonido == 5:
                self.volume100 = True
                self.window.blit(self.sound100, (self.soundBarWindowX, self.soundBarWindowY))
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
                self.window.blit(self.backButton100, (self.windowWidth - 100, self.heighWindow - 100))

            elif self.contChangeButton == 1:
                self.window.blit(self.backButton90, (self.windowWidth - 95, self.heighWindow - 95))

            elif self.contChangeButton == 2:
                self.window.blit(self.backButton80, (self.windowWidth - 90, self.heighWindow - 90))

            elif self.contChangeButton == 3:
                self.window.blit(self.backButton70, (self.windowWidth - 85, self.heighWindow - 85))
                       
            elif self.contChangeButton == 4:
                self.window.blit(self.backButton60, (self.windowWidth - 80, self.heighWindow - 80))

            elif self.contChangeButton == 5:
                self.window.blit(self.backButton70, (self.windowWidth - 85, self.heighWindow - 85))
       
            elif self.contChangeButton == 6:
                self.window.blit(self.backButton80, (self.windowWidth - 90, self.heighWindow - 90))
       
            elif self.contChangeButton == 7:
                self.window.blit(self.backButton90, (self.windowWidth - 95, self.heighWindow - 95))

            self.window.blit(self.resolutionWindow, (self.soundBarWindowX, self.soundBarWindowY  + self.soundBarHeight))

            self.contArrowDelay += self.arrowChangeVelocity
            if self.contArrowDelay > 20: 
                if not (self.reverseArrow):
                    self.contArrow += 1
                    self.contArrowDelay = 0

                else:
                    self.contArrow -= 1
                    self.contArrowDelay = 0

            if self.contArrow == 4:
                self.reverseArrow = True

            if self.contArrow == 0:
                self.reverseArrow = False

            if self.arrowListPosition == 0:
                xArrow, yArrow = self.soundBarWindowX - self.arrowWidthWindow - self.arrowWidthWindow // 2, self.arrowListYWindow[self.arrowListPosition]
                self.window.blit(self.arrow, (xArrow, yArrow))

            elif self.arrowListPosition == 1:
                xArrow, yArrow = self.soundBarWindowX - self.arrowWidthWindow - self.arrowWidthWindow // 2, self.arrowListYWindow[self.arrowListPosition]
                self.window.blit(self.arrow, (xArrow, yArrow))

        if self.volume0:
            try:
                self.soundTest.stop()
            except:
                pass

        if self.volume20:
            try:
                self.soundTest.set_volume(0.2)
                self.soundTest.play()
            except:
                pass

        if self.volume40:
            try:
                self.soundTest.set_volume(0.4)
                self.soundTest.play()
            except:
                pass

        if self.volume60: 
            try:
                self.soundTest.set_volume(0.6)
                self.soundTest.play()
            except:
                pass

        if self.volume80: 
            try:
                self.soundTest.set_volume(0.8)
                self.soundTest.play()
            except:
                pass

        if self.volume100: 
            try:
                self.soundTest.set_volume(1)
                self.soundTest.play()
            except:
                pass

    def manage_events(self, fullScreen):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.arrowChangeDelay += 1

            if self.arrowChangeDelay > 20:
                self.arrowListPosition += 1
                self.arrowChangeDelay = 0


        elif key[pygame.K_UP]:
            self.arrowChangeDelay += 1

            if self.arrowChangeDelay > 20:
                self.arrowListPosition -= 1
                self.arrowChangeDelay = 0


        if self.arrowListPosition > 1:
            self.arrowListPosition = 0

        elif self.arrowListPosition < 0:
            self.arrowListPosition = 1

        if self.arrowListPosition == 0:
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

        elif self.arrowListPosition == 1:
            if key[pygame.K_RIGHT]:
                if self.resolutionPosition != 1:
                    self.resolutionChangeDelay += 1

                    if self.resolutionChangeDelay == self.resolutionChangeVelocity:
                        self.resolutionPosition += 1
                        self.resolutionChangeDelay = 0


            elif key[pygame.K_LEFT]:
                if self.resolutionPosition > 0:
                    self.resolutionChangeDelay += 1

                    if self.resolutionChangeDelay == self.resolutionChangeVelocity:
                        self.resolutionPosition -= 1
                        self.resolutionChangeDelay = 0



            if self.resolutionPosition > 1:
                self.resolutionPosition = 0

            elif self.resolutionPosition < 0:
                self.resolutionPosition = 1
                

             #print(self.resolutionChangeDelay, self.resolutionPosition) 


        if key[pygame.K_ESCAPE] or key[pygame.K_BACKSPACE]:
            self.goLvl = True

        else:
            self.goLvl = False

        if self.sonido > 5:
            self.sonido = 5

        if self.sonido < 0:
            self.sonido = 0


        #print(self.arrowListPosition)
