# This file deals strictly with the process of checking a generation's status, and making a new generation if needed
import Constants as const
from random import random as rand_num

def create_new_generation(dead_birds):
    print(len(dead_birds))
    total = 0
    for bird in dead_birds:
        total += bird.frames_lived
    print(total)
    birds = []
    for _ in range(const.num_birds):
        temp_bird = pick_a_bird(dead_birds, total) 
        temp_bird_mutated = temp_bird.copy()
        temp_brain = temp_bird_mutated.brain
        temp_brain.mutate(const.max_mutation, const.mutation_chance)
        temp_bird_mutated.brain = temp_brain
        birds.append(temp_bird_mutated)
    return birds

def pick_a_bird(dead_birds, total):
    """ Takes all of dead_birds and picks a bird with a bias towards the birds that lived longer
        Returns: The bird it has picked"""
    # Generate the total frames lived for all birds combined

    # Take a random number, and keep subtracting the bird's score until that random number is < 0
    # Take the bird that made the score < 0, and return it
    random = rand_num()
    i = 0
    while random > 0: 
        random -= dead_birds[i].frames_lived / total
        i += 1
    i -= 1

    return dead_birds[i]
