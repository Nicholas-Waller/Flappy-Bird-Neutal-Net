import pygame
import Constants as const
from NeuralNet.Matrix.Matrix import apply_bounds as bound
class Slider: 
    def __init__(self, position_of_slider, min_val, max_val, step_size, init_val, title, func):
        self.x = position_of_slider[0]
        self.y = position_of_slider[1]
        self.w = position_of_slider[2]
        self.h = position_of_slider[3]
        self.min_val = min_val
        self.max_val = max_val + 1
        self.max_steps = (max_val - min_val) / step_size
        self.step_size = step_size
        self.current_step = bound(round(self.max_steps * (init_val / max_val)), 1, self.max_steps)
        self.margin = const.slider_margin
        self.func = func
        self.title = title

    def draw(self, pygame_screen, font_style): 
        slider_x = bound(self.x + self.margin + (self.w / (self.max_steps / self.current_step)), self.x, self.x + self.w - (self.w / 10) - self.margin) 
        pygame.draw.rect(pygame_screen, const.black, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(pygame_screen, const.white, (slider_x, self.y + const.slider_margin, self.w / 10, self.h - self.margin * 2))
        text = font_style.render(self.title, False, const.black)
        pygame_screen.blit(text, (self.x + self.w + 20, self.y))
        text = font_style.render(f"{self.get_val()}", False, const.black)
        pygame_screen.blit(text, (const.menu_width + const.game_width - 50, self.y))

    def get_val(self): 
        return int(self.min_val + (self.step_size * (self.current_step - 1)))

    def check_slider_status(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0] != 0:
            if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.w:
                if mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.h:
                    mouse_x_relative = (mouse_pos[0] - self.x) / self.w
                    # mouse_x_relative gives you a percentage way through the slider, set current_step to 
                    self.current_step = bound(round(((self.max_val - self.min_val) * mouse_x_relative) / self.step_size), 1, self.max_steps)


### Below are defined many functions used by Flappy.py to allow easier editing of the slider values

def edit_speed_multiplier(val):
    const.speed_multiplier = val

def edit_num_birds(val): 
    const.num_birds = val

def edit_pipe_gap(val):
    const.pipe_gap = val

def edit_pipe_freq(val): 
    const.pipe_frequency = val

def edit_bird_jump_velocity(val): 
    const.bird_jump_velocity = val

def edit_mutation_chance(val):
    const.mutation_chance = val / 100

def edit_mutation_factor(val):
    const.mutation_factor = val / 100
