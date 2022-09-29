from random import random
import pygame
import constants as const

# Misleading, but this is a SET of pipes, top and bottom.
class pipe:
    def __init__(self):
        self.x = const.game_width + 100 # Start the pipe off of the screen + a little bit
        self.top_height = random() * (const.game_height - const.pipe_gap - 50) # Make bottom pipe MINIMUM 50 pixels - floor_height
        self.bottom_height = const.game_height - self.top_height - const.pipe_gap
        self.scored = False

    def draw(self, pygame_screen):
        pygame.draw.rect(pygame_screen, const.pipe_colour, (self.x, 0, const.pipe_width, self.top_height))
        pygame.draw.rect(pygame_screen, const.pipe_colour, (self.x, const.game_height - self.bottom_height, const.pipe_width, self.bottom_height))

    def move(self):
        self.x -= const.pipe_speed

    def off_screen(self):
        return self.x + const.pipe_width < 0

    def bird_collided(self, bird):
        # Convert the "circle" into a rectangle for collision
        x = bird.x
        y = bird.y
        w = const.bird_width
        h = const.bird_height

        if x + w >= self.x and x <= self.x + const.pipe_width: # Check if the bird is within the pipe width
            if y < self.top_height:
                print("hit top pipe")
                return True
            elif y + h > self.top_height + const.pipe_gap: 
                print("hit bottom pipe")
                return True
        return False

    def passed_pipe(self, x):
        if (x > self.x and not self.scored):
            self.scored = True
            return True
        return False
