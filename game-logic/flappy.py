import pygame # Use this module for the main window
import constants as const
from bird import bird as Bird
import pipe
import os
import NeuralNet.Matrix.MatrixTest as testRunner
from NeuralNet.Matrix.Matrix import Matrix
from time import sleep
from random import random as rand_num

def main():
    current_generation = 1
    max_score = 0
    max_gen = 0
    if const.neural_network_enabled == True:
        print("----------Testing Matrix Library for Code Integrity------------")
        testRunner.run_tests()
        print("Tests passed! Starting Flappy Bird Neural Net") 
    pygame.init()
    pygame.font.init()
    font_style = pygame.font.SysFont('Comic Sans MS', 30)
    birds = []
    if const.neural_network_enabled == False:
        birds.append(Bird())
    else:
        for i in range(0, const.num_birds): 
            birds.append(Bird())
    pygame_screen = pygame.display.set_mode([const.game_width, const.game_height])

    pipes = []
    game_running = True
    i = 0
    dead_birds = []
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    bird_img = pygame.image.load(os.path.join(sourceFileDir, "sprites", "Bird.png"))
    bird_img = pygame.transform.scale(bird_img, (const.bird_width, const.bird_height))
    while game_running: 
        game_running = game_cycle(pygame_screen, birds, i % const.pipe_frequency == 0, pipes, bird_img, dead_birds)
        if len(birds) > 0:
            text = font_style.render(f"Score: {birds[0].score}", False, const.white)
            pygame_screen.blit(text, const.text_placement)
            text = font_style.render(f"Max score is {max_score if birds[0].score < max_score else birds[0].score} on generation {max_gen if birds[0].score < max_score else current_generation}/{current_generation}", False, const.white)
            pygame_screen.blit(text, (10, const.game_height - 40))

        sleep(1.0 / const.framerate) # Update the game {framerate} times a second
        pygame.display.flip()
        i += 1
        if const.neural_network_enabled == True and len(birds) == 0:
            highest_score_of_gen = dead_birds[len(dead_birds) - 1].score
            max_score, max_gen = (highest_score_of_gen, current_generation) if highest_score_of_gen >= max_score else (max_score, max_gen)
            pipes = []
            i = 0
            current_generation += 1
            next_generation(dead_birds, birds)
    pygame.quit()


# Returns whether the game is in a valid, playable state or not, True or False
def game_cycle(pygame_screen, birds, create_new_pipe, pipes, bird_img, dead_birds):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
            if const.neural_network_enabled == False:
                birds[0].flap()
    if create_new_pipe == True: 
        pipes.append(pipe.pipe()) # Create a new pipe

    closest_pipe = pipes[0] if pipes[0].x + const.pipe_width > birds[0].x else pipes[1]
    try:
        if closest_pipe == pipes[1]:
            print("Best pipe is pipes[1]")
    except:
        i = 0
    i = 0
    scored = pipes[0].passed_pipe(birds[0].x)
    while i < len(birds):

        bird = birds[i]
        if const.neural_network_enabled == True:
            result = bird.think(closest_pipe)
            if result.matrix[0][0] > const.network_sensitivity:
                bird.flap()

        bird.frames_lived = bird.frames_lived + 1
        bird.score += 1 if scored else 0
        bird.apply_gravity()
        if bird.hit_something(pipes[0]): 
            if const.neural_network_enabled == False:
                return False
            else:
                dead_birds.append(bird)
                del birds[i]
                i -= 1
        i += 1
    

    pygame_screen.fill(const.background_colour)

    for p in pipes: 
        p.move()
        p.draw(pygame_screen)
        if p.off_screen() == True:
            del pipes[0]

    pygame.draw.rect(pygame_screen, const.grass_green, (0, const.game_height - const.floor_height, const.game_width, const.floor_height))
    for bird in birds:
        bird.draw(pygame_screen, bird_img)
    return True
    
def next_generation(dead_birds, birds):
    total = 0
    for bird in dead_birds:
        total += bird.frames_lived

    for i in range(const.birds_to_duplicate):
        temp_bird = pick_a_bird(dead_birds, total)
        for j in range(int(const.num_birds / const.birds_to_duplicate)):
            temp_bird_mutated = temp_bird.copy()
            temp_brain = temp_bird_mutated.brain
            temp_brain.mutate(const.max_mutation, const.mutation_chance)
            temp_bird_mutated.brain = temp_brain
            birds.append(temp_bird_mutated)

def pick_a_bird(birds, total):
    random = rand_num()
    i = 0
    while random > 0: 
        random -= birds[i].frames_lived / total
        i += 1
    i -= 1

    return birds[i]

main()
