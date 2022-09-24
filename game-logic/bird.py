import constants as const
import pipe 
import pygame

class bird: 
    # Set init bird values
    def __init__(self):
        self.x = const.game_width / 6
        self.y = const.game_height / 2
        self.downwards_force = 0 # Downwards force will represent how much gravity will change on any given iteration
    
    def flap(self):
        self.downwards_force = 8
    
    def apply_gravity(self):
        self.y -= self.downwards_force
        self.downwards_force -= 0.25
        if self.downwards_force > 0:
            self.downwards_force -= 0.1

    def hit_something(self, pipe):
        if self.did_the_bird_hit_the_ceiling(): 
            self.downwards_force *= -1
        return self.did_the_bird_hit_the_floor() or pipe.bird_collided(self)

    def did_the_bird_hit_the_ceiling(self):
        return self.y - const.bird_radius <= 0

    def did_the_bird_hit_the_floor(self):
        return self.y + const.bird_radius > const.game_height - const.floor_height

    def draw(self, pygame_screen): 
        pygame.draw.circle(pygame_screen, const.bird_colour, (self.x, self.y), const.bird_radius)
