"""
Goal: This fundamental should get you comfortable with filling out a matrix from an expression
Related: The NumPy section in McCode Academy
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "fill_array"
]

## Functions: put all the functions we're defining here
def fill_array(expression, nrows, ncolumns):
    """
    :param expression: a function that takes two indices (i, j) and returns a value
    :param nrows: the number of rows
    :type nrows: int
    :param ncolumns: the number of columns
    :type ncolumns: int
    """
    my_array = ...
    for i in range(...):
        for j in range(...):
            ...[i, j] = expression(i, j)
    return ...

## Run Script: put the script we'd want to run from the command line here
if __name__ == '__main__':
    # here's an example to get the representation of x in a harmonic oscillator basis
    def harmonic_x(i, j):
        """
        returns the matrix elements for a harmonic oscillator
        """
        if i == j + 1:
            return np.sqrt(i/2)
        elif i == j - 1:
            return np.sqrt(j/2)
        else:
            return 0
    harm_mat = fill_array(harmonic_x, 50, 50)