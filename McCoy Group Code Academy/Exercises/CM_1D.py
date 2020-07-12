""" Goal: The goal of this exercise is to write a implementation of the Colbert-Miller DVR on the range of -inf to inf.
First, we will start with the describing H2 and OH stretches as Harmonic Oscillators, then as Morse Oscillators,
then using data from an Electronic Structure Calculation.
We will use ideas from: Numpy 101, Data&I/O, ...
After this, recommended next steps are: ... 
"""
# As with any script we will start by using import statements for any necessary packages
import numpy as np
import matplotlib.pyplot as plt

def dvr_grid(domain, NumGP):
    """ Here we will set up the grid for our DVR, you want it to be a little larger than the relevant range of your
        system to ensure convergence of your wavefunctions.

        :param domain: the start and stop of your grid (start, stop)
        :type domain: tuple
        :param NumGP: the number of points along your grid,
                      change this number and see how quickly (or not) your results converge!
        :type NumGP: int
        :return: grid
        :rtype: np.array
        """
    return grid

def CM_kinE(grid, mu):
    """ Here we will calculate the kinetic energy at each grid point.

        :param grid: the grid created by dvr_grid (atomic units)
        :type grid: np.array
        :param mu: The reduced mass of your system (atomic units)
        :type mu: int
        :return: Kinetic energy array
        :rtype: np.array
    """

    return kinE

def HO_potE(grid):
    """Here we will use a harmonic oscillator to create the matrix representation of the potential energy."""
    # Remember: The potential matrix is 0 for all terms off the diagonal...
    return potE

def MO_potE(grid):
    """Here we will use a morse oscillator to create the matrix representation of the potential energy."""
    return potE

def ES_potE(data):
    """Here we will load in a Gaussian Data file and then create the matrix representation of the potential energy."""
    # Remember our friend np.diag() ?
    return potE

def evaluateHam(kinE, potE):
    """ Here we will combine our kinetic and potential matrices into our Hamiltionain and
        then solve for eigenvalues and eigenvalues

        :param kinE: our Matrix Representation of Kinetic Energy (atomic units)
        :type kinE: np.array
        :param potE: our Matrix Representation of Potential Energy (atomic units)
        :type potE: np.array
        :return: a dictionary of eigenvalues and eigenvectors (results)
        :rtype: dict
    """
    # Remember np.eigh() ?
    return results

def plot_wavefunctions(grid, potE, results):
    """Here we will make some pretty plots with our nice results, we will overlay the wavefunctions
      (at their given energies) over the potential energy curve.

      :param grid: the grid created by dvr_grid (atomic units)
      :type grid: np.array()
      :param potE: our Matrix Representation of Potential Energy (atomic units)
      :type potE: np.array()
      :param results: a dictionary of eigenvalues and eigenvectors
      :type results: dict
      :return: plots of the results
      :rtype:
    """
    # We probably don't want to look at these in atomic units... Do you have a Converter class to use?
    # what matplotlib tricks do you remember to make this nice? (and have axis labels)

def run():
    """ You can use this function to gather all your functions to calculate the results in such a way that you only need
        to call this function. Maybe it returns the results dictionary too and you can use it in other scripts?"""
    return results

if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line
    run()  

