import pygame
from win32api import GetSystemMetrics


class game:
    def __init__(self, window, xWindow, yWindow, fullScreen, loadGame):
        self.goLvl = False
        self.window = window

        self.xWindow, self.yWindow = xWindow, yWindow

        self.changeValues = False

        self.fullScreen = fullScreen

        pathImagen = "imagenes/"
        pathMenu = "menu/"
        pathPlay = pathImagen + pathMenu + "play/"
        pathPlayImagenes = pathPlay + "images/"

        self.bg = pygame.image.load(pathPlayImagenes + "bg.png")
        self.xBg, self.yBg = 0, 0

        self.player = pygame.image.load(pathPlayImagenes + "player.png")
        self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()

        self.testSize = 8
        self.velocidad = 20
        self.range = 1
            
        self.maxWidthWindow, self.maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

        if not loadGame:
            if fullScreen:
                maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

                self.playerX, self.playerY = maxWidthWindow//2, maxHeightWindow//2


            else:
                self.changeValues = False
                maxWidthWindow, maxHeightWindow = self.xWindow, self.yWindow

                self.playerX, self.playerY = self.xWindow//2, self.yWindow//2

    def manage_events(self, loadGame):
        if loadGame: #loadGame tiene devolver el valor a windowFramework.
            key = pygame.key.get_pressed()

            if key[pygame.K_ESCAPE] or key[pygame.K_BACKSPACE]:
                self.goLvl = True
                self.loadGame = False

            else:
                self.goLvl = False


    def draw(self, loadGame, fullScreen):
        if loadGame:
            key = pygame.key.get_pressed()

            if self.changeValues or fullScreen:
                print("FULL")
                self.changeValues = True
                self.bg = pygame.transform.scale(self.bg, (self.maxWidthWindow, self.maxHeightWindow))
                self.player = pygame.transform.scale(self.player, (self.maxWidthWindow//self.testSize, self.maxHeightWindow//self.testSize))
                self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()
                
                self.window.blit(self.bg, (self.xBg, self.yBg))

                self.window.blit(self.player, (self.playerX, self.playerY))

                if (self.playerX > 0 and self.playerX < self.maxWidthWindow - self.playerWidth) and (self.playerY > 0 and self.playerY < self.maxHeightWindow - self.playerHeight):
                    if key[pygame.K_RIGHT]:
                        self.playerX += self.velocidad

                    elif key[pygame.K_LEFT]:
                        self.playerX -= self.velocidad

                    elif key[pygame.K_UP]:
                        self.playerY -= self.velocidad

                    elif key[pygame.K_DOWN]:
                        self.playerY += self.velocidad

                else:
                    if self.playerX <= 0:
                        self.playerX = self.range

                    elif self.playerX >= self.maxWidthWindow - self.playerWidth:
                        self.playerX = (self.maxWidthWindow - self.playerWidth) - self.range

                    elif self.playerY <= 0:
                        self.playerY = self.range

                    elif self.playerY >= self.maxHeightWindow - self.playerHeight:
                        self.playerY = (self.maxHeightWindow - self.playerHeight) - self.range


            else:
                if not fullScreen:
                    print("NO FULL")
                    self.bg = pygame.transform.scale(self.bg, (self.maxWidthWindow, self.maxHeightWindow))
                    self.player = pygame.transform.scale(self.player, (self.xWindow//self.testSize, self.yWindow//self.testSize))
                    self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()

                    self.window.blit(self.bg, (self.xBg, self.yBg))
                    self.window.blit(self.player, (self.playerX, self.playerY))


                    if (self.playerX > 0 and self.playerX < self.xWindow - self.playerWidth) and (self.playerY > 0 and self.playerY < self.yWindow - self.playerHeight):
                        if key[pygame.K_RIGHT]:
                            self.playerX += self.velocidad

                        elif key[pygame.K_LEFT]:
                            self.playerX -= self.velocidad

                        elif key[pygame.K_UP]:
                            self.playerY -= self.velocidad

                        elif key[pygame.K_DOWN]:
                            self.playerY += self.velocidad

                    else:
                        if self.playerX <= 0:
                            self.playerX = self.range

                        elif self.playerX >= self.xWindow - self.playerWidth:
                            self.playerX = (self.xWindow - self.playerWidth) - self.range

                        elif self.playerY <= 0:
                            self.playerY = self.range

                        elif self.playerY >= self.yWindow - self.playerHeight:
                            self.playerY = (self.yWindow - self.playerHeight) - self.range



            #print(self.playerY, self.yWindow- self.playerHeight)

            #print(self.playerX, self.playerY)

                    