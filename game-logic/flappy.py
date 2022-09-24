import pygame # Use this module for the main window
import constants as const
import bird as flappy_bird
import pipe
from time import sleep

def main():
    pygame.init()
    bird = flappy_bird.bird()
    pygame_screen = pygame.display.set_mode([const.game_width, const.game_height])

    pipes = []
    game_running = True
    i = 0
    while game_running: 
        print(len(pipes))
        game_running = game_cycle(pygame_screen, bird, i % const.pipe_frequency == 0, pipes)
        sleep(1 / const.framerate) # Update the game {framerate} times a second
        pygame.display.flip()
        i += 1
    pygame.quit()


# Returns whether the game is in a valid, playable state or not, True or False
def game_cycle(pygame_screen, bird, create_new_pipe, pipes):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
            bird.flap()

    if create_new_pipe == True: 
        pipes.append(pipe.pipe()) # Create a new pipe

    if bird.hit_something(pipes[0]): 
        return False

    bird.apply_gravity()

    pygame_screen.fill(const.background_colour)

    for p in pipes: 
        p.move()
        p.draw(pygame_screen)
        if p.off_screen() == True:
            del pipes[0]

    pygame.draw.rect(pygame_screen, const.grass_green, (0, const.game_height - const.floor_height, const.game_width, const.floor_height))
    bird.draw(pygame_screen)
    return True
    
main()
