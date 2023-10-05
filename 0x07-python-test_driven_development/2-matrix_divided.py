#!/usr/bin/python3
'''
divides all elements of a matrix.
This module contains a function, matrix_divided(matrix, div)
,that takes two integers or floats as arguments and returns
their division as an integer.
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix by a number and returns a new matrix.
    '''
    try:
        if not isinstance(matrix, list) or not all(
           isinstance(row, list) for row in matrix):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        row_size = len(matrix[0])
        if any(len(row) != row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

        result_matrix = []
        for row in matrix:
            new_row = [round(element / div, 2) for element in row]
            result_matrix.append(new_row)
    except (TypeError, ZeroDivisionError) as e:
        raise e

    return result_matrix
