from NeuralNet.Matrix.Matrix import Matrix

def run_tests():
    test_copy()
    test_addition()
    test_static_multiply()
    test_matrix_multiplication()

def test_copy(): 
    print("Copy Matrix 1 into Matrix 2 and assert that they have the same value")
    matrix = Matrix(3, 3)
    matrix.set_all_vals_to_number(1)
    matrix.print_matrix("Matrix 1")
    newMatrix = Matrix(matrix)
    newMatrix.print_matrix("Matrix 2")
    assert(matrix.matrix == newMatrix.matrix)
    matrix = Matrix([1, 2, 3, 4, 5])
    matrix.print_matrix("Matrix from array")
    assert(matrix.matrix == [[1], [2], [3], [4], [5]])

def test_addition():
    expected_matrix = [[15, 15, 15], [15, 18, 21], [15, 15, 15]]
    expected_matrix2 = [[19, 19, 19], [19, 22, 25], [19, 19, 19]]
    print("\n\n------------TEST MATRIX ADDITION--------------\n")
    matrix1 = Matrix(3, 3)
    matrix1.set_all_vals_to_number(12)
    matrix1.print_matrix("Matrix 1")
    matrix2 = Matrix(3, 3)
    matrix2.set_all_vals_to_number(3)
    matrix2.matrix[1] = [3, 6, 9]
    matrix2.print_matrix("Matrix 2")
    matrix1.addition(matrix2)
    matrix1.print_matrix("Matrix 1 + Matrix 2")
    assert(matrix1.matrix == expected_matrix)
    matrix1.addition(4)
    matrix1.print_matrix("Matrix 1 + Matrix 2 + 4 to each element")
    assert(matrix1.matrix == expected_matrix2)

def test_static_multiply():
    expected_matrix = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    print("\n\n------------TEST MATRIX SCALAR MULTIPLICATION--------------\n")
    matrix1 = Matrix(3, 3)
    matrix1.set_all_vals_to_number(5)
    matrix1.print_matrix("Matrix 1")
    matrix1 = Matrix(matrix1.multiply(2))
    matrix1.print_matrix("2(Matrix 1)")
    assert(matrix1.matrix == expected_matrix)

def test_matrix_multiplication():
    matrix1 = [[2, 3, 4], [0, 1, 5]]
    matrix2 = [[1, 0], [9, 5], [1, 3]]
    expected_result = [[33, 27], [14, 20]]
    print("\n\n------------TEST MATRIX MULTIPLICATION--------------\n")
    m1 = Matrix(matrix1)
    m2 = Matrix(matrix2)
    m1.print_matrix("Matrix 1")
    m2.print_matrix("Matrix 2")
    result = m1.multiply(m2)
    result.print_matrix("Resulting matrix from the matrix multiplication between m1 and m2")
    assert(result.rows == 2)
    assert(result.cols == 2)
    assert(result.matrix == expected_result)
