from NeuralNet.Matrix.Matrix import Matrix
import math

class NeuralNetwork:
    
    # Note, in this case, the output_node_count will always be 1. 
    # This isn't hard coded just so this code can be slightly more reusable
    def __init__(self, input_nodes, hidden_count, output_node_count):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_count 
        self.output_nodes = output_node_count
        self.weights_input_hidden = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_input_hidden.randomize()
        self.weights_hidden_output = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_hidden_output.randomize()

        self.bias_hidden = Matrix(self.hidden_nodes, 1)
        self.bias_output = Matrix(self.output_nodes, 1)
        self.bias_hidden.randomize()
        self.bias_output.randomize()
    
    def copy(self):
        new_network = NeuralNetwork(self.input_nodes, self.hidden_nodes, self.output_nodes)
        new_network.weights_input_hidden = Matrix(self.weights_input_hidden)
        new_network.weights_hidden_output = Matrix(self.weights_hidden_output)
        new_network.bias_hidden = Matrix(self.bias_hidden)
        new_network.bias_output = Matrix(self.bias_output)
        return new_network

    def think(self, inputs):
        inputs_as_matrix = Matrix(inputs)
        hidden_result = self.weights_input_hidden.multiply(inputs_as_matrix)
        hidden_result.addition(self.bias_hidden)
        hidden_result.apply_activation_function(math.tanh)
        output_result = self.weights_hidden_output.multiply(hidden_result)
        output_result.addition(self.bias_output)
        output_result.apply_activation_function(math.tanh)
        return output_result
 
    def mutate(self, val, chance): 
        self.weights_input_hidden.mutate(val, chance)
        self.weights_hidden_output.mutate(val, chance)
        self.bias_hidden.mutate(val, chance)
        self.bias_output.mutate(val, chance)
