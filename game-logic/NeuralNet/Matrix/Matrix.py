import random

class Matrix: 
    def __init__(self, *args): 
        self.rows = 0
        self.cols = 0
        self.matrix = None
        if isinstance(args[0], int):
            self.rows = args[0]
            self.cols = args[1]
            self.init_matrix()
        elif isinstance(args[0], Matrix):
            prevMatrix = args[0]
            self.rows = prevMatrix.rows
            self.cols = prevMatrix.cols
            self.matrix = [ [ prevMatrix.matrix[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ]
        elif isinstance(args[0], type([])): # If it's an array, ONLY an array (corresponding to a matrix) was passed in.
            matrix = args[0]
            self.rows = len(matrix)
            self.cols = len(matrix[0])
            self.matrix = [ [ matrix[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ]

    # Init the matrix to random numbers between 0 and 1
    def init_matrix(self):
        self.matrix = [ [ 0 for y in range( self.cols ) ] for x in range( self.rows ) ]

    def randomize(self):
        self.matrix = [ [ random.random() for y in range( self.cols ) ] for x in range( self.rows ) ]

    # Set all values in the matrix to 'n', used for testing
    def set_all_vals_to_number(self, n):
        self.matrix = [ [ n for y in range( self.cols ) ] for x in range( self.rows ) ]

    # Print the matrix
    def print_matrix(self, matrix_name):
        print(f"{matrix_name} Properties:")
        print(f"  Matrix Rows: {self.rows}\n  Matrix Columns: {self.cols}")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in self.matrix]))
        print("") # Print a new line 

    # Add either
    #  1. 2 Matrices of the same size together
    #  2. A single value to every element of a matrix (eg. if m1.matrix = [1, 2, 3], m1.addition(1) would set m1.matrix = [2, 3, 4])
    def addition(self, *args):
        if isinstance(args[0], Matrix):
            if args[0].rows == self.rows and args[0].cols == self.cols:
                self.matrix = [ [ args[0].matrix[i][j] + self.matrix[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ]
            else:
                print("ERROR: ADDITION NOT BEING PERFORMED DUE TO INVALID MATRIX SIZES")
                print(f"Rows of (M1, M2): ({self.rows}, {args[0].rows}")
                print(f"Cols of (M1, M2): ({self.cols}, {args[0].cols}")
        elif isinstance(args[0], int):
            self.matrix = [ [ args[0] + self.matrix[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ]

    # Multiply either returns
    #  1. The result of matrix multiplication between 2 matrices. The rows of A must be equal to the columns of B.
    #     Note: This takes advantage of temporal locality. 
    #  2. The matrix multiplied by a static integer. 
    def multiply(self, *args):
        if isinstance(args[0], Matrix):
            if self.rows != args[0].cols:
                print("Rows of A do not match cols of B")
                return []
            matrix = args[0]
            newMatrix = Matrix(self.rows, matrix.cols)
            newMatrix.print_matrix("DEBUG")
            for i in range(self.rows):
                for k in range(self.cols):
                    for j in range(matrix.cols):
                        newMatrix.matrix[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
            return newMatrix

        elif isinstance(args[0], int):
            return [ [ args[0] * self.matrix[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ]
        

