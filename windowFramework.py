import playFramework
import pygame


        
pygame.init()

class window:
    def __init__(self, maxWidthWindow, maxHeightWindow):

        self.maxWidthWindow, self.maxHeightWindow = maxWidthWindow, maxHeightWindow

        self.width, self.height = self.maxWidthWindow//2, self.maxHeightWindow//2
        self.window = pygame.display.set_mode((self.width, self.height))

        self.xWindow, self.yWindow = self.width, self.height

        self.clock = pygame.time.Clock()

        self.resolutionDelay = 0
        self.resolutionVelocity = 20

        self.fullScreen = False
        self.endFrame = False

    def updateFrame(self):
        pygame.display.flip()


    def fillFrame(self):
        self.window.fill((0, 0, 0))
        self.clock.tick(60)


    def manage_events(self, loadGame, resolution):
        if not loadGame:
            if resolution == 1:
                self.resolutionDelay += 1
                if self.resolutionDelay > self.resolutionVelocity:
                    self.resolutionDelay = 0
                    self.fullScreen = True

            if resolution == 0:
                self.resolutionDelay += 1
                if self.resolutionDelay > self.resolutionVelocity:
                    self.resolutionDelay = 0
                    self.fullScreen = False


            if self.fullScreen:
                self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            else:
                self.window = pygame.display.set_mode((self.width, self.height))