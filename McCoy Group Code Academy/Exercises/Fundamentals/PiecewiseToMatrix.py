"""
Goal: This fundamental should get you comfortable with building a matrix from a piecewise expression
Fundamentals: Filling a Matrix
Related: The NumPy section in McCode Academy
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "fill_piecewise"
]

## Functions: put all the functions we're defining here
def fill_piecewise(conditions, nrows, ncolumns):
    """
    :param conditions: a set of piecewise conditions expressed as functions on j and result functions on i,j
    :type conditions: list[(function, function)]
    :param nrows: the number of rows
    :type nrows: int
    :param ncolumns: the number of columns
    :type ncolumns: int
    """
    my_array = ...
    for i in range(...):
        for j in range(...):
            for cond in conditions:
                if cond[0](j) == i:
                    ...[i, j] = cond[1](i, j)
    return ...

## Run Script: put the script we'd want to run from the command line here
if __name__ == '__main__':
    # here's an example to get the representation of x in a harmonic oscillator basis
    harmonic_x = [
        (lambda j: j+1, lambda i,j: np.sqrt(i/2)),
        (lambda j: j-1, lambda i,j: np.sqrt(j/2))
    ]
    harm_mat = fill_piecewise(harmonic_x, 50, 50)