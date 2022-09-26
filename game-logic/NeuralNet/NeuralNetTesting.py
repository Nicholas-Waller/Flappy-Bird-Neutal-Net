# This file is just used for basic testing of the Neural Network. The output will be random and therefore
# No assertions will take place. However, you can test the various functions using this file. 
from NeuralNetwork import NeuralNetwork

inputs = [0.1, 0.5, 0.68, 0.04, 0.95]

nn = NeuralNetwork(5, 3, 1)
output = nn.think(inputs)

output.print_matrix("Output Matrix")
