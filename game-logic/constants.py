game_width = 500
game_height = 800
menu_width = 500
framerate = 60

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
background_colour = (25, 33, 150)
bird_colour = (255, 255, 0)
grass_green = (124, 252, 0)
pipe_colour = (0, 255, 0)

# Bird properties
bird_width = 40
bird_height = 40
bird_gravity_multiplier = 1
bird_jump_velocity = 8 # Abstract value representing how high the bird is able to jump

# Drawing properties
floor_height = 20
slider_margin = 2

# Pipe properties
pipe_gap = 200
pipe_speed = 3
pipe_frequency = 150 # After how many frames should a new pipe be created
pipe_width = 50

# Neural Network
neural_network_enabled = True
network_sensitivity = 0.7  # A value between 0 and 1. This value represents how confident the bird has to be to flap. Eg if it's 72% confident it should flap, sensitivity should be 0.72 or below
mutation_factor = 0.1 # The max mutation any given element in an iteration can have. Recommended max is 0.1
mutation_chance = 0.1
hidden_nodes = 5
num_birds = 500
speed_multiplier = 10
