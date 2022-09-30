import Constants as const
import pygame
from Pipe import pipe 
from NeuralNet.Matrix.Matrix import apply_bounds
from NeuralNet.NeuralNetwork import NeuralNetwork as neural_net

class Bird: 
    # Set init bird values
    def __init__(self):
        self.x = const.game_width / 6
        self.y = const.game_height / 2
        self.downwards_force = 0 # Downwards force will represent how much gravity will change on any given iteration
        self.score = 0
        self.frames_lived = 0
        if const.neural_network_enabled == True:
            self.brain = neural_net(4, const.hidden_nodes, 1)
    
    def copy(self):
        new_bird = Bird()
        new_bird.brain = self.brain.copy()
        return new_bird

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
            self.y = 0
        return self.did_the_bird_hit_the_floor() or pipe.bird_collided(self)

    def did_the_bird_hit_the_ceiling(self):
        return self.y <= 0

    def did_the_bird_hit_the_floor(self):
        return self.y + const.bird_height > const.game_height - const.floor_height

    def draw(self, pygame_screen, bird_img): 
        bird_img = pygame.transform.rotate(bird_img, apply_bounds(self.downwards_force * 10, -80, 80))
        pygame_screen.blit(bird_img, (self.x, self.y))

    def think(self, closest_pipe):
        inputs = []
        inputs.append(self.y / const.game_height)
        inputs.append((closest_pipe.x - self.x + const.bird_width) / const.game_width)
        inputs.append((self.y - closest_pipe.top_height) / const.game_height)
        inputs.append((self.y - (closest_pipe.top_height + const.pipe_gap)) / const.game_height)
        # inputs.append(self.downwards_force / (const.bird_jump_velocity * 1.5)) # Just divide by 10 because that's close-ish to the max value 
        # inputs.append((const.game_height - (self.x - (const.game_height - const.floor_height))) / const.game_height) # How far from the floor
        return self.brain.think(inputs)
        
def init_birds_array():
    birds = []
    if const.neural_network_enabled == False:
        birds.append(Bird())
    else:
        for _ in range(0, const.num_birds): 
            birds.append(Bird())
    return birds