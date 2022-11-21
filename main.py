import pygame, tkinter 
import windowFramework, menuFramework, optionsFramework, playFramework

pygame.init()

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.maxHeightWindow = self.root.winfo_screenheight()
        self.maxWidthWindow = self.root.winfo_screenwidth()


    def mainLoop(self):
        loadGame = False
        window_frame = windowFramework.window(self.maxWidthWindow, self.maxHeightWindow)
        menu_frame = menuFramework.menu(window_frame.window, window_frame.width, window_frame.height, window_frame.fullScreen, self.maxWidthWindow, self.maxHeightWindow)
        options_frame = optionsFramework.options(window_frame.window, window_frame.width, window_frame.height, window_frame.fullScreen, self.maxWidthWindow, self.maxHeightWindow)
        play_frame = playFramework.game(window_frame.window, window_frame.xWindow, window_frame.yWindow, window_frame.fullScreen, loadGame, self.maxWidthWindow, self.maxHeightWindow)
        enemy_frame = playFramework.enemy(window_frame.window, window_frame.xWindow, window_frame.yWindow, window_frame.fullScreen, loadGame, self.maxWidthWindow, self.maxHeightWindow)
        sprite_frame = playFramework.sprite_framework(window_frame.window)

        while not window_frame.endFrame:
            window_frame.fillFrame()

            window_frame.manage_events(loadGame, options_frame.resolutionPosition)

            if options_frame.goLvl or play_frame.goLvl or not menu_frame.goLvl:  #options_frame.goLvl = False, menu_frame_goLvl = True
                menu_frame.manage_events()
                menu_frame.draw(window_frame.fullScreen)
            
            if menu_frame.contYArrow == 0 and menu_frame.goLvl:
                loadGame = True
                options_frame.goLvl = False

                play_frame.manage_events(loadGame)
                play_frame.draw(loadGame, window_frame.fullScreen)
                enemy_frame.draw(loadGame, window_frame.fullScreen)

                sprite_frame.draw()
                sprite_frame.collide(play_frame.playerSprite, enemy_frame.enemySprite)

            if menu_frame.contYArrow == 1 and menu_frame.goLvl:
                play_frame.goLvl = False

                options_frame.manage_events(window_frame.fullScreen)
                options_frame.draw(window_frame.fullScreen)


            if menu_frame.contYArrow == 2 and menu_frame.goLvl:
                window_frame.endFrame = True

            loadGame = False
            window_frame.updateFrame()


main().mainLoop()

