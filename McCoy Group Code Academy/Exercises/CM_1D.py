""" Goal: The goal of this exercise is to write a implementation of the Colbert-Miller DVR on the range of -inf to inf. 
This guide contains three different options for evaluating the potential. It's not neccessary to write them all out immediately, 
but always good to lay out your options. 
We will use ideas from: Numpy 101, Data&I/O, ...
After this, recommended next steps are: Other Basis Set Representations, Multi Dimensional DVR, Spectrum Generation, ...  
"""
# As with any script we will start by using import statements for any necessary packages
import numpy as np
import matplotlib.pyplot as plt

def dvr_grid(domain, NumGP):
    """ Here we will set up the grid for our DVR, you want it to be a little larger than the relevant range of your
        system to ensure convergence of your wavefunctions. (do you want to remember this or do you want the 
        function to handle it?)

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
    """ Here we will calculate the kinetic energy at each grid point. Remember Equation A7?

        :param grid: the grid created by dvr_grid (atomic units)
        :type grid: np.array
        :param mu: The reduced mass of your system (atomic units)
        :type mu: int
        :return: Kinetic energy array
        :rtype: np.array
    """

    return kinE
# Starting here we outline 3 different ways to calculate the potential, note not all are neccessary right off the bat, 
# we suggest getting the harmonic oscillator running first, but all are quick functions to write and a fun way to explore
# parameter space! Plus now we can add conditions into our run function so we can evaluate different potential types with ease!
def HO_potE(grid, mass=..., frequency=...):
    """Here we will use a harmonic oscillator function to create the matrix representation of the potential energy."""
    # First solve for the HO energy at each grid point
    # Then project your results into the matrix representation!
    #    Remember: The potential matrix is 0 for all terms off the diagonal for any type of potential in DVR
    return potE

def MO_potE(grid, alpha=..., De=...):
    """Here we will use a morse oscillator to create the matrix representation of the potential energy."""
    # First solve for the MO energy at each grid point
    # Then project your results into the matrix representation!
    # Remember our friend np.diag() ?
    return potE

def ES_potE(data):
    """Here we will load in a Gaussian Data file and then create the matrix representation of the potential energy."""
    # Here you will probably need to do some I/O. Not ready for that? That's okay come back to this later
    # and just start with the analytic forms for now.
    # Remember our friend np.diag() ?
    return potE

def evaluateHam(kinE, potE):
    """ Here we will combine our kinetic and potential matrices into our Hamiltionain and
        then solve for eigenvalues and eigenvalues. Remember H = T + V

        :param kinE: our Matrix Representation of Kinetic Energy (atomic units)
        :type kinE: np.array
        :param potE: our Matrix Representation of Potential Energy (atomic units)
        :type potE: np.array
        :return: a dictionary of eigenvalues and eigenvectors (results)
        :rtype: dict
    """
    # Remember np.eigh() ? Remind yourself how to index into the outputs!
    # How will you set up your key/value pairs for your results dictionary? What feels most logical to you?
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
    # Don't forget about your units!! Do you know what they are? Do you know what you want to look at them in?
    # If you've previously written a Converter class now might be a good time to bring that in! (an import inside a function perhaps?)
    # what matplotlib tricks do you remember to make this nice? (and have axis labels)

def run(domain, NumGP, potential_function, potential_options):
    """ You can use this function to gather all your functions to calculate the results in such a way that you only need
        to call this function. We've added some suggested arguments and tips, but feel free to make it your own!
        As you are doing so, think about what would make it easiest to use in other scripts?
        :param domain: the start and stop of your grid (start, stop)
        :type domain: tuple
        :param NumGP: the number of points along your grid,
                      change this number and see how quickly (or not) your results converge!
        :type NumGP: int
        :param potential_function: the grid created by dvr_grid (atomic units)
        :type potential_function: np.array()
        :param potential_options: a dictionary filled with differnet potential options, i.e
               potential_options["mass"] = mass used in HO function or
               potential_options["De"] = Dissociation energy in Morse oscillator function
               Note: it doesn't need to hold them all, just the ones you need for the function you are testing!
        :type potential_options: dict
        """
    grid = dvr_grid(domain, NumGP)
    if potential_function == "HarmonicOscillator":
        potentialE = HO_potE(grid, potential_options["mass"], potential_options["frequency"])
    elif potential_function == "MorseOscillator":
        potentialE = MO_potE(...)
    elif potential_function == "ElectronicStructureData":
        potentialE = ES_potE(...)
    else:
        raise Exception("I can't evaluate that potential energy function.")
    # now that you have a grid and potential set up, what's  next?
    return results

if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line
    
    # Here are some sample parameters to try:
    #   First, let's start with a harmonic oscillator of mass 1 with frequency 3, giving us a pot_func like
    #   Let's try running this with a grid_range from [-5, 5] with 100 DVR points
    #   If all is going well, you should get energies that look like [1.5, 4.5, 7.5, ...]
    
    mass=1
    frequency=3
    PotOpsDict = { "mass": mass,
                  "frequency" : frequency, 
                  ...}
    
    run(domain=(-5, 5), NumGP=100, potential_function='HarmonicOscillator', potential_options=PotOpsDict)
    
    # Now that you know your code is working, play around with it!
    # Find parameters appropriate for, e.g., an OH stretch in a water molecule,
    #   or HCl, or HF.
    # The idea is to build intution, so play around with the parameters and the potential and see what happens
    
    

