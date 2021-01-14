"""
Goal: To be able to expand a function as a series if given series coefficients
Fundamentals: None
Related Exercises: Taylor Series, Fourier Expansion
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "BasisExpansion1D"
]

## Objects: put all the classes we're defining here
class BasisExpansion1D:
    """
    This is a class that represents a 1D series expansion of a function in terms of a set of basis functions
    This generalizes both the notion of a Taylor series or a Fourier series to any abritrary basis

    Construct it like
        fun = BasisExpansion1D(coeffs, basis)
    and use it like
        vals = fun(coords)
    """
    def __init__(self, coeffs, basis):
        """
        :param coeffs: the expansion coefficients in the basis
        :type coeffs: Iterable[float]
        :param basis: the basis functions we're using for our expansion
        :type basis: Iterable[basis]
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
        # Hint: evaluate your basis functions dot them into the coefficients
        ...
    def __call__(self, coords):
        return self.evaluate(coords)

if __name__ == '__main__':
    # We'll perform an effective Taylor series expansion, but with only even valued powers
    derivs = [1, 1/2, 3]
    center = 1
    basis = [
        lambda x: 1,
        lambda x,c=center: 1/2*(x-c)**2,
        lambda x,c=center: 1/24*(x-c)**4
    ]
    series = BasisExpansion1D(derivs, basis)

    coords = np.linspace(0, 5, 100)
    print(series(coords))