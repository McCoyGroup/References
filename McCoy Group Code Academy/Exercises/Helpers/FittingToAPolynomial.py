"""
Goal: This fundamental should get you experience with fitting data to a polynomials
Related: ...
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "FittedPolynomial"
]

## Objects: put all the classes we're defining here
class FittedPolynomial:
    """
    A simple class that represents a 1D fitted polynomial.
    All you need to fill in is the function `get_polynomial_fit`, everything else
    exists to make this a convenient function for you to work with.
    """
    def __init__(self, x_data, y_data, order):
        self.fit_coefficients, self.fit_error = self.get_polynomial_fit(x_data, y_data, order)
    def get_polynomial_fit(self, x_data, y_data, order):
        """
        :param x_data: the x values for your data
        :param y_data: the y values for your data
        :param order: the order of the fit (i.e. 1 for linear)
        """
        ...
    def evaluate_polynomial(self, x_points):
        """
        Evaluates the fitted polynomial at the passed points
        :param x_points:
        """
        return np.polyval(self.fit_coefficients, x_points)
    def __call__(self, x_points):
        return self.evaluate_polynomial(x_points)

## Run Script: put the script we'd want to run from the command line here

if __name__ == '__main__':
    # We'll test how well a randomly perturbed parabola fits
    x_data = np.linspace(-10, 10, 100)
    perturb = np.random.rand(100) / 10
    y_data = 1/2*x_data+perturb + 5*(x_data+perturb)**2
    poly = FittedPolynomial(x_data, y_data, 2)
    print("Fit Coefficients: {} Unperturbed Coefficients: {}".format(
        poly.fit_coefficients,
        [1/2, 5]
    ))
    print("Residue: {}".format(
        poly(x_data) - y_data
    ))