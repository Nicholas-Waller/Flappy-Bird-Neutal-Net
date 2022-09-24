game_width = 500
game_height = 800
framerate = 60

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
background_colour = (25, 33, 150)
bird_colour = (255, 255, 0)
grass_green = (124, 252, 0)
pipe_colour = (0, 255, 0)

# Bird properties
bird_radius = 25
# This setting deals with how "sensitive" the bird is to the pipes. 
# This is because the bird collision is treated as rectangular, not circular. 
# The bird's hitbox will be it's radius - margin, treated as a rectangle
bird_margin = 0
# Drawing properties
floor_height = 20

# Pipe properties
pipe_gap = 200
pipe_speed = 3
pipe_frequency = 150 # After how many frames should a new pipe be created
pipe_width = 50
