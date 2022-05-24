#!/usr/bin/python3
""" Module to divide a matrix of numbers by a given number """


def matrix_divided(matrix, div):
    """Function that returns a new matrix with the result of the
        division between the numbers in a matrix and the divisor
        Raises various error messages
    """

    new_matrix = list(map(list, matrix))
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    list_len = len(matrix[0])

    if len(matrix) == 1:
        raise IndexError("list index out of range")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        if len(matrix[i]) != list_len:
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if type(new_matrix[i][j]) not in [int, float]:
                raise TypeError(error_msg)
            test_var = new_matrix[i][j]
            try:
                int(test_var)
            except ValueError:
                raise TypeError(error_msg)
            new_matrix[i][j] = new_matrix[i][j] / div
            new_matrix[i][j] = round(new_matrix[i][j], 2)

    return new_matrix
