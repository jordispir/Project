import pygame
from win32api import GetSystemMetrics
import playFramework

        
pygame.init()
maxWidthWindow, maxHeightWindow = GetSystemMetrics(0), GetSystemMetrics(1)

class window:
    def __init__(self):
        self.fullScreen = False 
        self.endFrame = False
        
        self.width, self.height = maxWidthWindow//2, maxHeightWindow//2
        self.window = pygame.display.set_mode((self.width, self.height))

        self.xWindow, self.yWindow = self.width, self.height

        self.clock = pygame.time.Clock()

        self.fullScreen = False

        self.loadGamePlayFramework = playFramework.game(self.window, self.xWindow, self.yWindow, self.fullScreen, None)

    def updateFrame(self):
        pygame.display.flip()


    def fillFrame(self):
        self.window.fill((0, 0, 0))
        self.clock.tick(60)


    def manage_events(self, loadGame):
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if not loadGame:
                    if event.key == pygame.K_m:
                        self.fullScreen = True

                    elif event.key == pygame.K_n:
                        self.fullScreen = False


            if self.fullScreen:
                self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            else:
                self.window = pygame.display.set_mode((self.width, self.height))