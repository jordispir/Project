from re import I
import pygame
from win32api import GetSystemMetrics
        
class window:
    def __init__(self):
        self.fullScreen = False 
        self.endFrame = False

        self.widthWindow, self.heightWindow = GetSystemMetrics(0), GetSystemMetrics(1)
        
        self.width, self.height = self.widthWindow, self.heightWindow
        self.window = pygame.display.set_mode((self.width, self.height))

        self.xWindow, self.yWindow = 800, 800

        self.clock = pygame.time.Clock()


        self.pathImagen = "imagenes/"
        self.arrow = pygame.image.load(self.pathImagen + "arrow.png")

        self.yArrowList = [200, 400, 600]

        self.contYArrow = 0

    def updateFrame(self):
        pygame.display.flip()


    def fillFrame(self):
        self.window.fill((255, 255, 255))
        self.clock.tick(30)

    def receive_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.fullScreen = True

                elif event.key == pygame.K_n:
                    self.fullScreen = False

                elif event.key == pygame.K_ESCAPE:
                    self.endFrame = True

        if self.fullScreen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        else:
            self.window = pygame.display.set_mode((self.width, self.height))

    

    def getEvent(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.contYArrow += 1

        if key[pygame.K_UP]:
            self.contYArrow -= 1


        if self.contYArrow > 2:
            self.contYArrow = 0

        if self.contYArrow < 0:
            self.contYArrow = 2

    def draw(self):
        xArrow, yArrow = 0, self.yArrowList[self.contYArrow]
        self.window.blit(self.arrow, (xArrow, yArrow))

frame = window()


while not frame.endFrame:
    frame.receive_events()
    frame.getEvent()
    frame.draw()
    frame.updateFrame()
