# Flappy Bird Neural Network

This is my second attempt at creating a basic neural network to play the classic game "Flappy Bird". The neural network uses the "NEAT" technique. This means that a large amount of birds are created, and the ones that preform the best have a significantly higher chance of reproducing. Eventually, in theory, the birds should have "evolved" in order to play the game to a super-human level. No backpropogation takes place using this method, as there's no "expected result". (AKA, this is just simulating evolution, rather than properly "training" the bird) 

## Setup
Run ./setup.sh. This will either prompt you that 
 - pip install pygame was successful 
 - pip install pygame failed. It will then prompt you to go to python.org to install python. 
Set up the constants in Constants.py. The ones that should be known about are listed below, but notably: 
 - neural_network_enabled should be set to your desired setting. False just plays a single game where, when you die, the game is over. Mouse click over the screen to jump. 
Run ./summon.sh

## Constants
All constants for the game are defined in game-logic/Constants.py. There are a few notable ones to mention

| Name of Constant        | Description                                                                            | Default Value |
| :---                    |    :----:                                                                              |          ---: |
| Game Height             | This is the height of the game screen                                                  | 500           |
| Game Width              | This is the width of the game screen                                                   | 800           |
| Menu Width  | This is the width of the menu. It is recommended you do not make this value lower since many values in the menu are hard coded | 500
| Framerate               | This is the framerate that the game is played at. Note: Other vars might need adjusted | 60            |
| Bird Width              | This is the width of the bird                                                          | 40            |
| Bird Height             | This is the height of the bird                                                         | 40            |
| Bird Gravity Multiplier | This is used in case you make the screen taller. Use this to make the bird fall faster | 1.0           |
| Bird Jump Velocity      | This is an arbitrary value which defines how "powerful" the birds jump is.             | 8             |
| Pipe Gap                | This is the gap, in pixels between the top pipe and the bottom pipe                    | 175           |
| Pipe Speed              | This is how many pixels the pipe moves on any given frame                              | 3             |
| Pipe Frequency               | This is how many frames that will occur before a new pipe is created                   | 150           |
| Pipe Width              | This is how wide each given pipe is, in pixels                                         | 50            |
| Neural Network Enabled | ***This defines whether or not the neural network will be used. Please set the value to your desired value*** | False
| Network Sensitivity | This is a value between 0 and 1, which defines how confident any given bird has to be to flap. Eg. 0.7 means that the bird must be 70% sure it has to jump for it to jump. | 0.7
| Mutation Factor | The max mutation any given element can have to any given weight when the weights are being mutated | 0.1
| Mutation Chance | The chance that a mutation will occur after all birds are dead | 0.1
| Hidden Nodes | The amount of hidden nodes that the given network will have. | 5
| Num Birds | The number of birds to duplicate after all birds are dead. Note: The higher the value, the more laggy the game will be | 500
| Speed multiplier | How much faster the game will go when the neural network is enabled. Used for quick evolution | 1

## Notes
 - It is known that the sliders are not the most responsive. Sadly, due to Pygame not having an easy built-in slider, I had to custom make a slider. The values/positionings are slightly off, and this is known. 
 - There are some fun ways to tweak the neural network on the fly. Some examples are training a bird on a really easy version of the game (increasing pipe gap and decreasing pipe frequency) and then modifying the game to be significantly harder once they get good at that version. You can also set the mutation factor and mutation chance higher to see how much faster the birds evolve at a given mutation chance/factor. There are tons of interesting expirements regarding evolution that you can do with the code :)
 - You can also try setting the number of birds to duplicate to 1. You will note that, although it will take forever, it should in theory, eventually learn. After setting it to 1, get a bird that is horrible. Now, set the number of birds to duplicate to a much higher value. It's interesting to see how all of the birds simulate the same behaviour, but then eventually, they start to differ in behaviour. 

## Possible Improvements / Bugs Known / New Features I want to Implement
 - Update slider to be more responsive.
 - Implement multithreading for the matrix calculations that the birds are doing so that the game doesn't lag as severly when there are a large amount of birds.
 - Allow a "get a good bird instantly" (basically run the simulation with the current settings without drawing anything to the screen).
 - Allow a "save best bird of generation to file to load for later" feature. Potentially even letting the birds have their own name. 