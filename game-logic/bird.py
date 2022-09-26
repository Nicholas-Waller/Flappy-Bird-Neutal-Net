import constants as const
import os
import pygame
from NeuralNet.Matrix.Matrix import apply_bounds


class bird: 
    # Set init bird values
    def __init__(self):
        self.x = const.game_width / 6
        self.y = const.game_height / 2
        self.downwards_force = 0 # Downwards force will represent how much gravity will change on any given iteration
        self.score = 0
    
    def flap(self):
        self.downwards_force = const.bird_jump_velocity * const.bird_gravity_multiplier
    
    def apply_gravity(self):
        self.y -= self.downwards_force
        self.downwards_force -= 0.25 * const.bird_gravity_multiplier
        # In order to enforce stronger gravity when jumping than falling
        if self.downwards_force > 0: 
            self.downwards_force -= 0.1 * const.bird_gravity_multiplier

    def hit_something(self, pipe):
        if self.did_the_bird_hit_the_ceiling(): 
            self.downwards_force *= -1 # If it hit the ceiling, reverse it's gravitational direction
        return self.did_the_bird_hit_the_floor() or pipe.bird_collided(self)

    def did_the_bird_hit_the_ceiling(self):
        return self.y <= 0

    def did_the_bird_hit_the_floor(self):
        return self.y + const.bird_height > const.game_height - const.floor_height

    def draw(self, pygame_screen): 
        sourceFileDir = os.path.dirname(os.path.abspath(__file__))
        birdImg = pygame.image.load(os.path.join(sourceFileDir, "sprites", "Bird.png"))
        birdImg = pygame.transform.scale(birdImg, (const.bird_width, const.bird_height))
        birdImg = pygame.transform.rotate(birdImg, apply_bounds(self.downwards_force * 10, -80, 80))
        pygame_screen.blit(birdImg, (self.x, self.y))
