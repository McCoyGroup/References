"""
Goal: The goal of this exercise is to write an implementation of continuous weighting diffusion Monte Carlo.
This guide contains three different options for evaluating the potential. It's not neccessary to write them all out
immediately, but always good to lay out your options. Note: It's easiest if this is done in ATOMIC UNITS.

This also introduces a very basic way to get your simulation into a class based format instead of just a bunch of
functions. If this is confusing at all please reach out with questions and the rest of the group will definitely
answer.

Fundamentals: Numpy101, Data&I/O
Related Exercises: DiscreteDMC.py,
"""

# As with any script we will start by using import statements for any necessary packages
import numpy as np


class Continuous_weight_DMC():

    def __init__(self, dtau, numTimesteps, threshold, numWalkers, initialCoords, masses, potential_func,
                 potential_opts=None):
        '''
        This part of our class sets up the class with all of our wanted parameters for the simulation

        :param dtau: The time step size
        :type dtau: float
        :param numTimesteps: The number of time steps to run the simulation for
        :type numTimesteps: int
        :param threshold: Threshold that low weight walkers will be removed if their weight gets below this
        :type threshold: float
        :param numWalkers:The number of walkers used for the simulation
        :type numWalkers: float
        :param initialCoords: An array of the initial geometry for the system of interest
        :type initialCoords: np.array or list
        :param masses: The appropriate masses for the system (in atomic units)
        :type masses: list
        :param potential_func: The potential being used for the simulation (for now lets just put these functions within the
                       class itself and deal with loading them separately later)
        :type potential_func: str
        :param potential_opts: Options for the potential energy function (None uses the default options)
        :type potential_opts: dict
        '''
        ### Set up the initial parameters for the simulation
        ### include any initial displacements of the coordinates that you want to do, such as multiplying the coords by
        ### 1.05 or something along those lines.
        ### Calculate the sigma value/values appropriate for the system (reminder that this needs the dtau and the masses)
        ### Set up your initial weight array as an array of len(numWalkers) with all entries as 1
        ### Set up an array you can use for your collection of potential energies
        ### Set up a float to collect your Vref value for the simulation

    def displacements(self):
        '''
        Apply the kinetic energy operator to displace our coordinates
        :return:
        :rtype:
        '''
        ### Displace the coordinates (possibly saved as something like self.coords or something along those lines)
        ### of all the walkers using the gaussian distribution that has width equal to sigma (maybe self.sigma)
        ### (np.random.normal is going to be your friend here)

    def potential(self):
        '''
        Get the potential energy of your current set of walkers using your preffered potential energy function
        :return:
        :rtype:
        '''
        ### Use a check to determine what potential to use from whatever you stored as the string in the __init__
        ### Then feed your coordinates to the appropriate potential function and return an array for your potential
        ### an example could be self.V = pot_func_example(self.coords, *self.potential_opts)

    # Starting here we outline 3 different ways to calculate the potential, note not all are neccessary right off the bat,
    # we suggest getting the harmonic oscillator running first, but all are quick functions to write and a fun way to explore
    # parameter space! Plus now we can add conditions into our run function so we can evaluate different potential types with ease!
    @staticmethod
    def HO_potE(coords, frequency=..., re=...):
        """Here we will use a harmonic oscillator function to obtain a potential energy array for our walkers
           :param frequency: the frequency of the vibration (atomic units)
           :type frequency: float
           :param re: Equilibrium distance of vibration (atomic units)
           :type re: float
           :return: Potential energy array
           :rtype: np.array """
        # First solve for the HO potential energy at each of the walkers' coordinates using the appropriate formula for
        # a harmonic oscillator potential

        return potE

    @staticmethod
    def MO_potE(coords, alpha=..., De=..., re=...):
        """Here we will use a morse oscillator to obtain a potential energy array for our walkers
           :param alpha: parameter controlling width of well (atomic units)
           :type alpha: float
           :param De: Dissociation Energy (atomic units)
           :type De: float
           :param re: Equilibrium distance of vibration (atomic units)
           :type re: float
           :return: Potential energy array
           :rtype: np.array"""
        # Solve for the Morse Oscillator potential energy at each of the walkers' coordinates

        return potE

    @staticmethod
    def Pot_E_surface_collab(coords):
        """Here we will use the potential energy surface from a collaborator such as the wonderful CH5 surface from the
        Bowman group"""
        # If you need help interfacing with one of these surfaces please ask a group mate as it is likely that someone
        # else already has

        return potE

    def calc_weights(self):
        '''
        Here you will calculate the weights of the walkers by multiplying the potential energy operator including the
        value of Vref, by the weight of the previous step
        :return:
        :rtype:
        '''
        ### Also add in the killing of low weight walkers whose weight has gotten below the threshold and replace them with
        ### the high weight walker's coordinates and half its weight. Also any other properties of that walker that you
        ### have stored (maybe it's potential energy)

    def vref_calc(self):
        '''
        Use the potential energy and weights of the walkers to calculate the Vref value and save it into your
        self.Vref or appropriate entry
        :return: V_ref
        :rtype: float
        '''
        ### The equation for this is the weighted average of our potential energy (np.average is good here) minus
        ### a correction term that attempts to keep the sum of the weights relatively constant. This term is in the form
        ### of alpha (1/(2*self.dtau)) times the sum of (the current weights - the initial weights) all over the sum of
        ### the initial weights
        ### Return it for collection into an array that can be saved at the end of your simulation

        return V_ref

    def run(self, output):
        '''
        Here is where we will use the DMC algorithm to calculate the ground state wave function and ZPE
        :param output: The output file your would like to use to save your data
        :type output: str
        :return:
        :rtype:
        '''
        ### So the order we want is to call self.displacements, self.potential, self.calc_weights, then self.vref_calc
        ### However, for the first step we will need a vref in order to calculate weights so you can add in a step at
        ### the beginning in order to calculate the intial potential energy and then calculate vref before we get into
        ### the algorithm

        ### Other than that, we loop over the numTimesteps that we set at the beginning, saving the V_ref energies into
        ### an array we can load later

        ### You can also collect any other data you want (and I suggest saving it into npy files or npz files)

        ### If you want to use descendant weighting it might be helpful to add a function that governs keeping track of
        ### a walker's descendants and counting them up at the end. This is usually done by adding an array in __init__
        ### that tells you what number a walker is and who it is descended from. Then after some time calculating the
        ### total weight for each descendant walker. Look into np.bincount (this is a really nice function that can do
        ### this efficiently) Then make sure you reset that descendant array so that the descendant weight doesn't
        ### collapse onto one walker at the end.


if __name__ == '__main__':
    # adding this makes it so you can get this results dictionary if you chose to run the script in the command line

    # Here are some sample parameters to try:
    # First, let's start with an H2 stretch as our system. We've filled in the potential options for you
    # (in ATOMIC UNITS) so you can try the harmonic oscillator and morse oscillator. These values are from NIST,
    # so (hopefully) you should be able to replicate this dictionary for other diatomics as well!

    H2PotOptsDict = {
        "frequency": 0.0200534,  # Hartree
        "re": 1.40112,  # bohr
        "alpha": 1.00779,  # 1/bohr
        "De": 0.18186,  # Hartree
    }

    params = {
        "dtau": 1,
        "numTimesteps": 10000,
        "threshold": 1 / 5000,
        "numWalkers": 5000,
        "initialCoords": [1.40],
        "masses": [918.59073],
        "potential_func": 'Harmonic Oscillator',
        "potential_opts": H2PotOptsDict
    }

    sim = Continuous_weight_DMC(*params)
    sim.run('file_where_the_results_can_go')

    ## If this is working, for the harmonic oscillator you should have a ground state energy = 0.0098886 Hartree
    ## and for the Morse oscillator the energy should look like: 0.0100267 Hartree

    # Once code is working, play around with it!
    # Try varying numWalkers, numTimesteps, dtau, initialCoords, threshold
    # There is a lot here to vary so explore to get comfortable with this type of simulation and please reach out with
    # questions
