import pygame 

sprites = pygame.sprite.Group()

class game:
    def __init__(self, window, xWindow, yWindow, fullScreen, loadGame, maxWidth, maxHeight):
        self.goLvl = False
        
        self.window = window
        self.xWindow, self.yWindow = xWindow, yWindow
        self.maxWidthWindow = maxWidth
        self.maxHeightWindow = maxHeight
        self.fullScreen = fullScreen

        pathGame = "images/game/"
        pathPlay = pathGame + "images/"

        self.bg = pygame.image.load(pathPlay+ "bg.png")
        self.xBg, self.yBg = 0, 0

        self.player = pygame.image.load(pathPlay+ "player.png").convert_alpha()
        self.playerSprite = pygame.sprite.Sprite()

        self.playerSprite.rect = self.player.get_rect()


        self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()

        self.windowVelocity = 10
        self.fullScreenVelocity = 20

        self.testSize = 8
        self.range = 1

        if loadGame == False:
            if fullScreen:
                self.playerX, self.playerY = self.maxWidthWindow//2, self.maxHeightWindow//2
                self.playerSprite.rect.x, self.playerSprite.rect.y = self.playerX, self.playerY


            else:
                self.playerX, self.playerY = self.xWindow//2, self.yWindow//2
                self.playerSprite.rect.x, self.playerSprite.rect.y = self.playerX, self.playerY


        sprites.add(self.playerSprite)

    def manage_events(self, loadGame):
        if loadGame: 
            key = pygame.key.get_pressed()

            if key[pygame.K_ESCAPE] or key[pygame.K_BACKSPACE]:
                self.goLvl = True
                self.loadGame = False

            else:
                self.goLvl = False

    def draw(self, loadGame, fullScreen):
        if loadGame:
            key = pygame.key.get_pressed()

            self.bg = pygame.transform.scale(self.bg, (self.maxWidthWindow, self.maxHeightWindow))
            self.window.blit(self.bg, (self.xBg, self.yBg))

            if fullScreen:
                self.player = pygame.transform.scale(self.player, (self.maxWidthWindow//self.testSize, self.maxHeightWindow//self.testSize))
                self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()

                self.playerSprite.image = self.player
                

                if (self.playerSprite.rect.x > 0 and self.playerSprite.rect.x < self.maxWidthWindow - self.playerWidth) and (self.playerSprite.rect.y > 0 and self.playerSprite.rect.y < self.maxHeightWindow - self.playerHeight):
                    if key[pygame.K_RIGHT]:
                        self.playerSprite.rect.x += self.fullScreenVelocity

                    elif key[pygame.K_LEFT]:
                        self.playerSprite.rect.x -= self.fullScreenVelocity

                    elif key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.fullScreenVelocity

                    elif key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.fullScreenVelocity

                    elif key[pygame.K_RIGHT] and key[pygame.K_UP]:
                        self.playerSprite.rect.y += self.fullScreenVelocity
                        self.playerSprite.rect.y += self.fullScreenVelocity

                    if key[pygame.K_RIGHT] and key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.fullScreenVelocity//2
                        self.playerSprite.rect.x += self.fullScreenVelocity//2

                    elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.fullScreenVelocity//2
                        self.playerSprite.rect.x += self.fullScreenVelocity//2

                    elif key[pygame.K_LEFT] and key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.fullScreenVelocity//2
                        self.playerSprite.rect.x -= self.fullScreenVelocity//2

                    elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.fullScreenVelocity//2
                        self.playerSprite.rect.x -= self.fullScreenVelocity//2

                else:
                    if self.playerSprite.rect.x <= 0:
                        self.playerSprite.rect.x = self.range

                    elif self.playerSprite.rect.x >= self.maxWidthWindow - self.playerWidth:
                        self.playerSprite.rect.x = (self.maxWidthWindow - self.playerWidth) - self.range

                    elif self.playerSprite.rect.y <= 0:
                        self.playerSprite.rect.y = self.range

                    elif self.playerSprite.rect.y >= self.maxHeightWindow - self.playerHeight:
                        self.playerSprite.rect.y = (self.maxHeightWindow - self.playerHeight) - self.range


            else:
                self.player = pygame.transform.scale(self.player, (self.xWindow//self.testSize, self.yWindow//self.testSize))
                self.playerWidth, self.playerHeight = self.player.get_width(), self.player.get_height()

                self.playerSprite.image = self.player


                if (self.playerSprite.rect.x > 0 and self.playerSprite.rect.x < self.xWindow - self.playerWidth) and (self.playerSprite.rect.y > 0 and self.playerSprite.rect.y < self.yWindow - self.playerHeight):
                    if key[pygame.K_RIGHT]:
                        self.playerSprite.rect.x += self.windowVelocity

                    elif key[pygame.K_LEFT]:
                        self.playerSprite.rect.x -= self.windowVelocity

                    elif key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.windowVelocity

                    elif key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.windowVelocity

                    if key[pygame.K_RIGHT] and key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.windowVelocity//2
                        self.playerSprite.rect.x += self.windowVelocity//2

                    elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.windowVelocity//2
                        self.playerSprite.rect.x += self.windowVelocity//2

                    elif key[pygame.K_LEFT] and key[pygame.K_UP]:
                        self.playerSprite.rect.y -= self.windowVelocity//2
                        self.playerSprite.rect.x -= self.windowVelocity//2

                    elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
                        self.playerSprite.rect.y += self.windowVelocity//2
                        self.playerSprite.rect.x -= self.windowVelocity//2

                else:
                    if self.playerSprite.rect.x <= 0:
                        self.playerSprite.rect.x = self.range

                    elif self.playerSprite.rect.x >= self.xWindow - self.playerWidth:
                        self.playerSprite.rect.x = (self.xWindow - self.playerWidth) - self.range

                    elif self.playerSprite.rect.y <= 0:
                        self.playerSprite.rect.y = self.range

                    elif self.playerSprite.rect.y >= self.yWindow - self.playerHeight:
                        self.playerSprite.rect.y = (self.yWindow - self.playerHeight) - self.range
        
            #print("player x = " + str(self.playerSprite.rect.x), "player y = " + str(self.playerSprite.rect.y))

#TODO player and game (main play frame) on same class NO!

class enemy:
    def __init__(self, window, xWindow, yWindow, fullScreen, loadGame, maxWidth, maxHeight):

        self.window = window
        self.xWindow, self.yWindow = xWindow, yWindow
        self.maxWidthWindow, self.maxHeightWindow = maxWidth, maxHeight

        self.testSize = 8

        pathGame = "images/game/"
        pathPlay = pathGame + "images/"

        self.enemy = pygame.image.load(pathPlay + "player.png").convert_alpha()
        self.enemySprite = pygame.sprite.Sprite()

        self.enemySprite.rect = self.enemy.get_rect()

        if loadGame == False:
            if fullScreen:
                self.enemyX, self.enemyY = self.maxWidthWindow//2, self.maxHeightWindow//2
                self.enemySprite.rect.x, self.enemySprite.rect.y = self.enemyX, self.enemyY


            else:
                self.enemyX, self.enemyY = self.xWindow//2, self.yWindow//2
                self.enemySprite.rect.x, self.enemySprite.rect.y = self.enemyX, self.enemyY


        sprites.add(self.enemySprite)


    def draw(self, loadGame, fullScreen):
        if loadGame:
            if fullScreen:
                self.enemySprite.image = pygame.transform.scale(self.enemy, (self.maxWidthWindow//self.testSize, self.maxHeightWindow//self.testSize))

                self.enemyX, self.enemyY = self.maxWidthWindow//2, self.maxHeightWindow//2
                self.enemySprite.rect.x, self.enemySprite.rect.y = self.enemyX, self.enemyY

            else:
                self.enemySprite.image = pygame.transform.scale(self.enemy, (self.xWindow//self.testSize, self.yWindow//self.testSize))

                self.enemyX, self.enemyY = self.xWindow//2, self.yWindow//2
                self.enemySprite.rect.x, self.enemySprite.rect.y = self.enemyX, self.enemyY


        #print("enemy x = " + str(self.enemySprite.rect.x), "enemy y = " + str(self.enemySprite.rect.y))

class sprite_framework:
    def __init__(self, window):
        self.window = window

    def draw(self):
        sprites.draw(self.window)

    def collide(self, sprite1, sprite2):
        if pygame.sprite.collide_rect(sprite1, sprite2):
            print("ok!")

        else:
            pass