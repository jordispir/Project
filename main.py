import pygame
import windowFramework, menuFramework, optionsFramework


pygame.init()

window_frame = windowFramework.window()
menu_frame = menuFramework.menu(window_frame.window,window_frame.width, window_frame.height, window_frame.fullScreen)
options_frame = optionsFramework.options(window_frame.window, window_frame.width, window_frame.height, window_frame.fullScreen)


while not window_frame.endFrame:
    window_frame.fillFrame()
    window_frame.manage_events()
    #menu_frame.manage_events()
    #menu_frame.draw(window_frame.fullScreen)
    options_frame.manage_events()
    options_frame.draw(window_frame.fullScreen)
    window_frame.updateFrame()


