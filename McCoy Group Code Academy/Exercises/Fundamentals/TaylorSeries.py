"""
Goal: To be able to expand a function as a Taylor Series
Fundamentals: None
Related Exercises: Basis Expansion, Fourier Expansion
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "TaylorSeries1D"
]

## Objects: put all the classes we're defining here
class TaylorSeries1D:
    """
    This is a class that represents a 1D Taylor series expansion of a function
    Construct it like
        fun = TaylorSeries(derivs)
    and use it like
        vals = fun(coords)
    """
    def __init__(self, derivs, center=0, ref=0):
        """
        :param derivs: the derivatives of our functions (the number of derivs. defines the order of the expansion)
        :type derivs: Iterable[float]
        :param center: the point we are expanding around
        :type center: float
        :param ref: the value of the function at the point we're expanding around
        :type ref: float
        """
        ...
    def evaluate(self, coords):
        """
        Takes the set of coords and
        :param coords:
        :type coords:
        :return:
        :rtype:
        """
        # Hint: a Taylor series is an expansion of a function such that f(x) = f(x_e) + sum(1/k!*d^kf/dx^k(x_e)*(x-x_e))
        ...
    def __call__(self, coords):
        return self.evaluate(coords)

if __name__ == '__main__':
    # We'll perform a Taylor series expansion of some function based off of its derivatives
    derivs = [0, 1, 2, 3]
    center = 1
    ref = 0
    series = TaylorSeries1D(derivs, center=center, ref=ref)

    coords = np.linspace(0, 5, 100)
    print(series(coords))