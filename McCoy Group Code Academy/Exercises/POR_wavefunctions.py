"""
Goal: The goal of this exercise is to calculate and plot Particle on a Ring Wavefunctions
We will use ideas from: Particle on A Ring Basis Set Representation
After this, recommended next steps are: ...
"""

# As with any script we will start by using import statements for any necessary packages
import numpy as np
import matplotlib.pyplot as plt
import POR_Representation

# here we will import the script we have for the POR Representation so we can calculate the eigenvectors

def PORwavefunctions(eigenvectors, theta):
    """

    :param eigenvectors:
    :type eigenvectors:
    :param theta:
    :type theta:
    :return:
    :rtype:
    """

    return wavefunction_values

def plotResults(theta):
    """
    Here we will make some pretty plots with our nice results, we will overlay the wavefunctions
    (at their given energies) over the potential energy curve. Think about how you can use what you have in 
    POR_Representation to your advantage here. 
    :param theta: x-values your potential is evaluated over (probably a range of values from 0 to 2 pi)
    :type theta: np.array
    :return: a plot of the results
    :rtype: 
    """
    # you will probably want to stat this function with first a call to the run funtion in POR_Representations
    
    # also you will probably want a call to PORwavefunctions ...
    
    # this will probably end with something like plt.show() or plt.savefig()
    
if __name__ == '__main__':
    # adding this makes it so you can get the plots/values (if you chose to return any)
    #  if you chose to run the script in the command line
    theta = np.arange()  # don't forget to fill this in!
    plotResults(theta)
