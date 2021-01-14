"""
Goal: The goal of this exercise is to write a implementation of the Particle on a Ring Basis Set Representation
using Fourier series expansion coefficients.
We will use ideas from: Numpy101, Expanding a Function as a Fourier Series, ...
Related Exercises: Calculate POR wavefunctions, ...
"""

# As with any script we will start by using import statements for any necessary packages
import numpy as np

def pullCoefficents():
    """
    This function should load in your Fourier series expansion coefficients from a text file
    (in which case you would want params like filename or dirname)
    or call to the functions you have in place for calculating them.
    (in which case you want params like function_data or expansion_form)
    Or to get started, you can manually enter a set of coefficients to use. 
    :return: V_coeffs, B_coeffs
    :rtype: tuple of np.array s
    """
    return V_coeffs, B_coeffs

def calcHamiltonian(V_coeffs, B_coeffs, BasisSize=None):
    """
    Here we will calculate the Hamiltonian in the POR basis
    :param V_coeffs: coefficients of the Potential Energy ([0] from pullCoefficients)
    :type V_coeffs: np.array
    :param B_coeffs: coefficients of the Effective Rotation Constant ([1] from pullCoefficients)
    :type B_coeffs: np.array
    :param BasisSize: amount of Basis Functions to use
    :type BasisSize: int
    :return: Hamiltonian (size: (2*BasisSize + 1, 2*BasisSize + 1))
    :rtype: np.ndarray
    """
    # Here is a fun little bonus trick:
    if BasisSize is None:
        BasisSize = len(V_coeffs)  # This makes sure that BasisSize has a value and your code won't break
    # As you are playing with this you will notice that BasisSize has to be larger than this to get eigenvalues to stablize.

    # Here allocate an array the size of the FULL hamiltonian (remember it is described from -k (BasisSize) to k (BasisSize) including 0)

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

def run(BasisSize=None, filename=None):
    """
    Remember our friend the run function? This should string together all of the above functions so that someone could
    easily call to this one function and get the results of EvaluateHam 
    *Note that this is not a complete list of variables, do what works for you*
    :param BasisSize: amount of Basis Functions to use
    :type BasisSize: int
    :param filename: The name of the text file that holds your coefficents (if that is how you have written the function)
    :return: results
    :rtype: dict
    """
    if filename is None:
        
    else: 
        
    return results

if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line
    filename = ...
    BasisSize = ...
    run(BasisSize, filename)
