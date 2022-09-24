from random import random
import pygame
import constants as const

# Misleading, but this is a SET of pipes, top and bottom.
class pipe:

    def __init__(self):
        self.x = const.game_width + 100 # Start the pipe off of the screen + a little bit
        self.topHeight = random() * (const.game_height - const.pipe_gap - 50) # Make bottom pipe MINIMUM 50 pixels - floor_height
        self.bottomHeight = const.game_height - self.topHeight - const.pipe_gap

    def draw(self, pygame_screen):
        pygame.draw.rect(pygame_screen, const.pipe_colour, (self.x, 0, const.pipe_width, self.topHeight))
        pygame.draw.rect(pygame_screen, const.pipe_colour, (self.x, const.game_height - self.bottomHeight, const.pipe_width, self.bottomHeight))

    def move(self):
        self.x -= const.pipe_speed