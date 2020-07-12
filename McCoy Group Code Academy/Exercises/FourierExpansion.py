""" Goal: The goal of this exercise is to write a set of functions to flexibly expand a function using a Fourier series.
We will use ideas from: Numpy 101
After this, recommended next steps are: Particle on A Ring Basis Set Representation and Calculate POR wavefunctions
"""

# As with any script we will start by using import statements for any necessary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def cosExpansion(theta, coeffs):
    """
    Here we are going to describe an expansion in cos,
    you should think about ways to make it flexible in the order of the expansion,
    but it is okay to start with just defining it as a specific order say 4th or 6th.
    :param theta: x-values (probably a range of values from 0 to 2 pi)
    :type theta: np.array
    :param coeffs: expansion coefficents, ultimately you will use this function to calculate the expanded curve.
    :type coeffs: np.array
    :return: the values of the function evaluated at x
    :rtype: np.array
    """
    # here we are going to implement a little trick, but note that if you want this function to do anything other than
    # a 4th order expansion in cos, you will have to adjust it.
    return coeffs[0] + coeffs[1]*np.sin(x) + coeffs[2]*np.sin(2*x) + coeffs[3]*np.sin(3*x) + coeffs[4]*np.sin(4*x)


def CalculateCoefficents(function_data, expansion_form):
    """
    Here you should use something like optimize.curve_fit
    (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) in order to calculate the
    coefficients in the expansion
    :param function_data: a [numPts, 2] array of data to be fit
    :type function_data: np.ndarray
    :param expansion_form: the function defining your expansion
    :type expansion_form: function
    :return: expansion coefficents
    :rtype: np.array
    """

    return coeffs

def plot_curves(theta):
    """
    What good is calculating a bunch of stuff and not looking at it? So here we are going to write out a quick
    function to calculate and plot our expansion. Note: you could also think of this as a "run" type function.
    :param theta: x-values (probably a range of values from 0 to 2 pi)
    :type theta: np.array
    :return: the values of the function evaluated at x
    :rtype: np.array
    """

    # this will probably end with something like plt.show() or plt.savefig()
    return values

if __name__ == '__main__':
    # adding this makes it so you can get the plots/values if you chose to run the script in the command line
    theta = np.arange()  # don't forget to fill this in!
    plot_curves(theta)
