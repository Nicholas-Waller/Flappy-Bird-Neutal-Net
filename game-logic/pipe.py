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

    def off_screen(self):
        return self.x + const.pipe_width < 0

    def bird_collided(self, bird):
        # Convert the "circle" into a rectangle for collision
        x = bird.x - const.bird_radius + const.bird_margin
        y = bird.y - const.bird_radius + const.bird_margin
        w = 2 * const.bird_radius - 2 * const.bird_margin
        h = w

        if x + w >= self.x and x <= self.x + const.pipe_width: # Check if the bird is within the pipe width
            if y < self.topHeight:
                print("hit top pipe")
                return True
            elif y + h > self.topHeight + const.pipe_gap: 
                print("hit bottom pipe")
                return True
        return False
