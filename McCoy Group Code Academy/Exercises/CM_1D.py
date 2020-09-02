""" Goal: The goal of this exercise is to write a implementation of the Colbert-Miller DVR on the range of -inf to inf. 
This guide contains three different options for evaluating the potential. It's not neccessary to write them all out immediately, 
but always good to lay out your options. Note: You will want all of this to be set up to work in ATOMIC UNITS. 

Fundamentals: Intro to npy/npz Files, Filling out a Matrix, and the NumPy 101 Section. 
Related Exercises: Other Basis Set Representations, Multi Dimensional DVR, or Spectrum Generation. 
"""

# Imports: put all import statments here
import numpy as np
import matplotlib.pyplot as plt

## Exports: put all the names of things we might want to use in other scripts here

__all__ = [run_DVR]

def dvr_grid(domain, NumGP):
    """ Here we will set up the grid for our DVR. 

        :param domain: the start and stop of your grid (start, stop)
                       If you are having a hard time seeing convergence of your wavefunctions (they are not
                       at 0 at the endpoints) making your grid longer (adjust start and stop!) is one way to fix this!
        :type domain: tuple
        :param NumGP: the number of points along your grid,
                      change this number and see how quickly (or not) your results converge!
                      This convergence is of your energies, we are looking for stable numbers
                      that do not change when you continue to add more points. 
        :type NumGP: int
        :return: grid
        :rtype: np.array
        """
    
    return grid

def CM_kinE(grid, mu):
    """ Here we will calculate the kinetic energy at each grid point. Remember Equation A7? Based on 
        this equation, you will probably want to allocate an array and fill it using loops :)

        :param grid: the grid created by dvr_grid (atomic units)
        :type grid: np.array
        :param mu: The reduced mass of your system (atomic units)
        :type mu: float
        :return: Kinetic energy array
        :rtype: np.array
    """

    return kinE

# Starting here we outline 3 different ways to calculate the potential, note not all are neccessary right off the bat, 
# we suggest getting the harmonic oscillator running first, but all are quick functions to write and a fun way to explore
# parameter space! Plus now we can add conditions into our run function so we can evaluate different potential types with ease!
def HO_potE(grid, mass=..., frequency=..., re=...):
    """Here we will use a harmonic oscillator function to create the matrix representation of the potential energy.
       :param grid: the grid created by dvr_grid (atomic units)
       :type grid: np.array
       :param mass: The reduced mass of your system (atomic units) 
       *Note: this mass is the same as the mu you will use in the kinetic energy function, but since your potential will 
       not always rely on mass so you do want to define them twice. 
       :type mass: float
       :param frequency: the frequency of the vibration (atomic units)
       :type frequency: float
       :param re: Equilibrium distance of vibration (atomic units)
       :type re: float
       :return: Potential energy array
       :rtype: np.array """
    # First solve for the HO potential energy at each grid point
    # Then project your results into the matrix representation!
    # Remember: The potential matrix is 0 for all terms off the diagonal for any type of potential in DVR
    
    return potE

def MO_potE(grid, alpha=..., De=..., re=...):
    """Here we will use a morse oscillator to create the matrix representation of the potential energy.
       :param grid: the grid created by dvr_grid (atomic units) (basically your range of displacements)
       :type grid: np.array
       :param alpha: parameter controlling width of well (atomic units)
       :type alpha: float
       :param De: Dissociation Energy (atomic units)
       :type De: float
       :param re: Equilibrium distance of vibration (atomic units)
       :type re: float
       :return: Potential energy array
       :rtype: np.array"""
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
    # How will you set up your key/value pairs for your results dictionary?
    # First suggestion would be: {"grid":grid, "energies":eigenvalues, "wavefunctions":eigenvectors}
    # If something else feels more logical, add more key/value pairs!
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

def runDVR(domain, NumGP, mu, potential_function, potential_options):
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
    results = ...
    # returning results is good when you are passing this to oher functions, but if you just need to run the DVR once and then 
    # manipulate the data (more likely), you probably just want to save the results. In order to keep this clean, we want to use
    # an npz file, and also save the parameters so we can recreate it. Here is a suggestion, but make what feels right for you.
    param_dict = {"domain": domain, 
                  "numberpoints": NumGP, 
                  "mass": mu}
    np.savez("myDVRresults.npz", params=param_dict, grid=results["grid"], energies=results["energies"], wavefunctions=results["wavefunctions"])
    # Can you think of a way (maybe adding parameters to run function and using format strings *hint hint*) to make these
    # data file names more descriptive? Probably add a system name, maybe some of the parameters or the units used in the file?
    return results

if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line
    
    # Here are some sample parameters to try:
    # First, let's start with H2 as our system. We've filled in the potential options for you (in ATOMIC UNITS) so you can try the 
    # harmonic oscillator and morse oscillator. These values are from NIST, so (hopefully) you should be able
    # to replicate this dictionary for other diatomics as well! Also to start, we will use a domain of (-5, 5) and 100 DVR grid points.
    
    H2PotOptsDict = { "mass": 918.59073,  # mass electron
                      "frequency" : 0.0200534,  # Hartree
                      "re" : 1.40112,  # bohr
                      "alpha" : 1.00779,  # 1/bohr
                      "De" : 0.18186,  # Hartree
                    }
    
    run(domain=(-5, 5), NumGP=100, potential_function='HarmonicOscillator', potential_options=H2PotOptsDict)
    
    # If this is working, for the harmonic oscillator you should have energies: [0.0098886  0.02883656 0.04667887 0.06341553 0.07904654] (Hartree)
    # and for the Morse oscillator the energies should look like: [0.0100267  0.0300801  0.05013349 0.07018689 0.09024029] (Hartree)
    
    # Once code is working, play around with it!
    # Find some suggestions for "exploring the parameter space" in the DVR Reference!
    # Basically, the idea is to build intution, so play around with the parameters (domain and number of grid points) and the potential (harmonic, morse, 
    # or electonic structure) and see what happens. 
    
 
