import pygame # Use this module for the main window
import constants as const

pygame.init()

pygame_screen = pygame.display.set_mode([const.gameWidth, const.gameHeight])

game_running = True

while game_running: 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            game_running = False

    pygame_screen.fill((255, 255, 255))

    pygame.draw.circle(pygame_screen, const.birdColour, (250, 250), 30)

    pygame.display.flip()

pygame.quit