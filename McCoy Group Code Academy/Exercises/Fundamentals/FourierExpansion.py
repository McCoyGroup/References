"""
Goal: To be able to expand a function as a Fourier series
Fundamentals: None
Related Exercises: Taylor Series, Basis Expansion
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "FourierSeries1D"
]

## Objects: put all the classes we're defining here
class FourierSeries1D:
    """
    This is a class that represents a 1D Fourier series expansion of a function
    A Fourier series is defined in terms of a reference value (r0), a length (L), & two sets of coefficients (c_k & sk_) by

        f(x) = r0/2 + sum(c_k/L cos(2Pi/L  k), k=1...) + sum(s_k/L sin(2Pi/L  k), k=1...)

    Construct it like
        fun = FourierSeries1D(cos_coeffs, sin_coeffs)
    and use it like
        vals = fun(coords)
    """
    def __init__(self, cos_coeffs, sin_coeffs, center=0, ref=0, length=2*np.pi):
        """
        :param cos_coeffs: the coefficients to multiply into the cos part of the series
        :type cos_coeffs: Iterable[float]
        :param sin_coeffs: the coefficients to multiply into the sin part of the series
        :type sin_coeffs: Iterable[float]
        :param center: the point we are expanding around
        :type center: float
        :param ref: the value of the function at the point we're expanding around
        :type ref: float
        :param length: the length of the pox in the series
        :type length: float
        """
        ...
    def evaluate(self, coords):
        """
        Takes a set of coords and returns a Fourier series approximation of it
        :param coords:
        :type coords:
        :return:
        :rtype:
        """
        ...
    def __call__(self, coords):
        return self.evaluate(coords)

if __name__ == '__main__':
    # We'll perform a Fourer series expansion of some function based off of a set of randomly chosen coefficients
    c_k = [0, 1, 2, 3]
    s_k = [-0, -1, -2, -3]
    center = 1
    ref = 0
    length = 5*np.pi
    series = FourierSeries1D(c_k, s_k, center=center, ref=ref, length=length)

    coords = np.linspace(0, 5, 100)
    print(series(coords))
