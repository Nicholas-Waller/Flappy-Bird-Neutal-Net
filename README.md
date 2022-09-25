# Flappy Bird Neural Network

This is my second attempt at creating a basic neural network to play the classic game "Flappy Bird". The neural network uses the "NEAT" technique. This means that a large amount of birds are created, and the ones that preform the best have a significantly higher chance of reproducing. Eventually, in theory, the birds should have "evolved" in order to play the game to a super-human level. 

## Constants
All constants for the game are defined in game-logic/constants.py. There are a few notable ones to mention

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