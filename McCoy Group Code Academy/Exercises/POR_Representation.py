""" Goal: The goal of this exercise is to write a implementation of the Particle on a Ring Basis Set Representation
using Fourier series expansion coefficients.
We will use ideas from: Numpy101, Expanding a Function as a Fourier Series, ...
After this, recommended next steps are: Calculate POR wavefunctions, ...
"""

# As with any script we will start by using import statements for any necessary packages
import numpy as np

def pullCoefficents():
    """
    This function should load in your Fourier series expansion coefficients from a text file
    (in which case you would want params like filename or dirname)
    or call to the functions you have in place for calculating them.
    (in which case you want params like function_data or expansion_form)
    :return: V_coeffs, B_coeffs
    :rtype: tuple of np.array s
    """
    return V_coeffs, B_coeffs

def calcHamiltonian(V_coeffs, B_coeffs, Klength=None):
    """
    Here we will calculate the Hamiltonian in the POR basis
    :param V_coeffs: coefficients of the Potential Energy ([0] from pullCoefficients)
    :type V_coeffs: np.array
    :param B_coeffs: coefficients of the Effective Rotation Constant ([1] from pullCoefficients)
    :type B_coeffs: np.array
    :param Klength: amount of K values to calculate
    :type Klength: int
    :return: Hamiltonian (size: (2*Klength + 1, 2*Klength + 1))
    :rtype: np.ndarray
    """
    # Here is a fun little bonus trick:
    if Klength is None:
        Klength = len(V_coeffs)  # This makes sure that Klength has a value and your code won't break
    # As you are playing with this you will notice that Klength has to be larger than this to get eigenvalues to stablize.

    # Here allocate an array the size of the FULL hamiltonian (remember it is described from -k to k including 0)

    # Fill the array in whatever way you are comfortable with. Remember there are unique expressions for the on diagonal
    # and off diagonal terms

    return Hamiltonian

def evaluateHam(Hamiltonian):
    """
    Here we will solve for the eigenvalues and eigenvectors of the function.
    :param Hamiltonian: result of calcHamiltonian
    :type: np.ndarray
    :return: a dictionary of eigenvalues and eigenvectors (results)
    :rtype: dict
    """
    # Remember np.eigh() ?
    return results

def run():
    """
    Remember our friend the run function? This should string together all of the above functions so that someone could
    easily call to this one function and get the results of EvaluateHam
    :return: results
    :rtype: dict
    """
    return results

if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line
    run()
