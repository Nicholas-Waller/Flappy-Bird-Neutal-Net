# Flappy Bird Neural Network

This is my second attempt at creating a basic neural network to play the classic game "Flappy Bird". The neural network uses the "NEAT" technique. This means that a large amount of birds are created, and the ones that preform the best have a significantly higher chance of reproducing. Eventually, in theory, the birds should have "evolved" in order to play the game to a super-human level. No backpropogation takes place using this method, as there's no "expected result". (AKA, this is just simulating evolution, rather than properly "training" the bird) 

## Constants
All constants for the game are defined in game-logic/Constants.py. There are a few notable ones to mention

| Name of Constant        | Description                                                                            | Default Value |
| :---                    |    :----:                                                                              |          ---: |
| Game Height             | This is the height of the game screen                                                  | 500           |
| Game Width              | This is the width of the game screen                                                   | 800           |
| framerate               | This is the framerate that the game is played at. Note: Other vars might need adjusted | 60            |
| Bird Width              | This is the width of the bird                                                          | 40            |
| Bird Height             | This is the height of the bird                                                         | 40            |
| Bird Gravity Multiplier | This is used in case you make the screen taller. Use this to make the bird fall faster | 1.0           |
| Bird Jump Velocity      | This is an arbitrary value which defines how "powerful" the birds jump is.             | 8             |
| Pipe Gap                | This is the gap, in pixels between the top pipe and the bottom pipe                    | 175           |
| Pipe Speed              | This is how many pixels the pipe moves on any given frame                              | 3             |
| Pipe Freq               | This is how many frames must take place before a new pipe is created                   | 150           |
| Pipe Width              | This is how wide each given pipe is, in pixels                                         | 50            |

## Notes
It is known that the sliders are not the most responsive. Sadly, due to Pygame not having an easy built-in slider, I had to custom make a slider. The values/positionings are slightly off, and this is known. 

## Possible Improvements / Bugs Known
 - Update slider to be more responsive.
 - Implement multithreading for the matrix calculations that the birds are doing so that the game doesn't lag as severly when there are a large amount of birds.
 - When updating "pipe freq", it may make the pipe come to you significantly faster than expected, or significantly slower, depending on the current frame count. 
 - When updating "pipe gap", the gap will not apply visually to the current pipe, but it will apply in practice. E.g. if you update the gap to be larger, it might look like the birds clip through the pipe because they're assuming that the pipe has a larger gap than it does. 