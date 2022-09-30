import pygame # Use this module for the main window
import Constants as const
import Bird
import Pipe as pipe
import os
import NeuralNet.Matrix.MatrixTest as matrix_test_runner
from time import sleep
from NeuralNet.Evolve import create_new_generation as new_gen

def main():
    current_generation, max_score, max_gen = 1, 0, 1

    verify_matrix_integrity()
    pygame_font_style, pygame_screen, bird_img = init_pygame_settings()

    birds = Bird.init_birds_array() # Create the array of birds if the neural network is enabled. 

    pipes, dead_birds = [], []
    game_running = True
    frames_total_count = 0

    while game_running: 
        for _ in range(const.speed_multiplier):
            if game_running:
                if frames_total_count % const.pipe_frequency == 0: 
                    pipes.append(pipe.pipe()) # Create a new pipe
                frames_total_count += 1
                move_pipes(pipes)

                if const.neural_network_enabled == True:
                    game_running = neural_network_game_cycle(birds, dead_birds, pipes)
                    if len(birds) == 0:
                        frames_total_count = 0
                        max_score, max_gen = (dead_birds[-1].score, current_generation) if dead_birds[-1].score >= max_score else (max_score, max_gen)
                        current_generation += 1
                        birds = new_gen(dead_birds)
                        pipes, dead_birds = [], []
                else: 
                    const.speed_multiplier = 1
                    game_running = game_cycle(birds[0], pipes)

        # Make sure draw_screen is outside of the speed multiplier. If it is in, speed_multiplier is useless. 
        draw_screen(pygame_screen, pipes, birds, bird_img, pygame_font_style)

    pygame.quit()

def neural_network_game_cycle(birds, dead_birds, pipes): 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False

    closest_pipe = pipes[0] if pipes[0].x + const.pipe_width > birds[0].x or len(pipes) == 1 else pipes[1]
    scored = pipes[0].passed_pipe(birds[0].x)

    i = 0
    while i < len(birds):
        bird = birds[i]
        bird.apply_gravity()

        result = bird.think(closest_pipe)
        if result.matrix[0][0] > const.network_sensitivity:
            bird.flap()

        bird.score += 1 if scored else 0
        if bird.hit_something(pipes[0]):
            dead_birds.append(bird)
            del birds[i]
            i -= 1
        else:
            bird.frames_lived += 1
        i += 1

    return True

# Returns whether the game is in a valid, playable state or not, True or False
def game_cycle(bird, pipes):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
            if const.neural_network_enabled == False:
                bird.flap()

    bird.score += int(pipes[0].passed_pipe(bird.x)) # int(bool) will return 1 if true, 0 if false
    bird.apply_gravity()
    if bird.hit_something(pipes[0]): 
        return False

    return True
    
def verify_matrix_integrity(): 
    if const.neural_network_enabled == True:
        print("----------Testing Matrix Library for Code Integrity------------")
        matrix_test_runner.run_tests()
        print("Tests passed! Starting Flappy Bird Neural Net") 

def init_pygame_settings(): 
    pygame.init()
    pygame.font.init()
    pygame_font_style = pygame.font.SysFont('Comic Sans MS', 30)
    pygame_screen = pygame.display.set_mode([const.game_width + (const.menu_width if const.neural_network_enabled else 0), const.game_height])
    pygame.display.set_caption("Neural Network Flappy Bird")
    # Load the bird image ----------------------------
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    bird_img = pygame.image.load(os.path.join(sourceFileDir, "sprites", "Bird.png"))
    bird_img = pygame.transform.scale(bird_img, (const.bird_width, const.bird_height))
    return pygame_font_style, pygame_screen, bird_img

def move_pipes(pipes):
    for pipe in pipes:
        pipe.move()
        if pipe.off_screen() == True: 
            del pipes[0]

def draw_screen(pygame_screen, pipes, birds, bird_img, pygame_font_style):
    """Draws all of the objects required for the game creation, and the sleeps for the appropriate amount of time and flips the display

    Args:
        pygame_screen: The screen to draw the game's objects on
        pipes: A list of the pipes to draw
        birds: A list of birds to draw
        bird_img: The pygame bird image to draw
        pygame_font_style: The pygame font object that defines the properties of how the game is drawn

    Returns: None
    """
    pygame_screen.fill(const.background_colour)
    for pipe in pipes:
        pipe.draw(pygame_screen)
    for bird in birds:
        bird.draw(pygame_screen, bird_img)
    pygame.draw.rect(pygame_screen, const.grass_green, (0, const.game_height - const.floor_height, const.game_width, const.floor_height))
    if const.neural_network_enabled == False:
        text = pygame_font_style.render(f"Score: {birds[0].score}", False, const.white)
        pygame_screen.blit(text, (10, 10))
    else:
        pygame.draw.rect(pygame_screen, const.white, (const.game_width, 0, const.menu_width, const.game_height))
        pygame.draw.line(pygame_screen, const.black, (const.game_width, 0), (const.game_width, const.game_height), 2) # Border
    sleep(1.0 / const.framerate)
    pygame.display.flip()


main()
