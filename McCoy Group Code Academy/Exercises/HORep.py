"""
Goal: To find the energies of a 1D system using a harmonic oscillator representation
Fundamentals: Filling out a Matrix, Turning a Piecewise Formula into a Matrix
Related Exercises: Anything basis set related
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "kinetic_energy",
    "potential_energy",
    "energies_and_wavefunctions"
]

## Functions: put all the functions we're defining here

def kinetic_energy(mass=1, hbar=1, omega=1, basis_size=25):
    """
    Creates the representation for the kinetic energy of the system at hand
    For convenience, here's the momentum squared formula (assuming j>=i; the j<i case is left up to you)
        <i|p^2|j> = hbar*mass*omega/2 * (-np.sqrt(j*(j-1)) if j==i+2 else 2*i+1 if i==j else 0 )

    :param mass: the mass of our system
    :type mass: float or int
    :param hbar: the value of hbar in the units we've chosen to use; atomic units (hbar=1) are recommended
    :type hbar: float or int
    :param omega: the frequency of the oscillator we're using for our basis
    :type omega: float or int
    :return:
    :rtype:
    """

    # make use of the Filling a Matrix and Turning a Piecewise Formula into a Matrix fundamentals

    return kinetic_energy_matrix

def potential_energy(coefficients, mass=1, hbar=1, omega=1, basis_size=25):
    """
    Creates the representation for the potential energy of the system at hand
    We assume the the potential energy is in a power series, that is we assume as an operator it has the form
        pot(x) = sum([c*(x**n) for n, c in enumerate(coefficients)])

    For convenience, the matrix element for x is
        <i|x|j> = np.sqrt(2/(hbar*mass*omega)) * np.sqrt(j)

    :param coefficients: the power series coefficients for the potential
    :type coefficients: list of float
    :param mass: the mass of our system
    :type mass: float or int
    :param hbar: the value of hbar in the units we've chosen to use; atomic units (hbar=1) are recommended
    :type hbar: float or int
    :param omega: the frequency of the oscillator we're using for our basis
    :type omega: float or int
    :return:
    :rtype:
    """

    # First obtain a representation for `X` on its own, then use the series representation to build a representation
    #   for the total potential
    # Keep in mind that (x**n) != np.mat_pow(x, n) [you want the latter]

    return potential_energy_matrix


def energies_and_wavefunctions(coefficients, mass=1, hbar=1, omega=1, basis_size=25):
    """
    Takes the kinetic_energy and potential_energy defined before and creates a Hamiltonian
    Then diagonalizes this to get energies and wavefunctions

    :param coefficients: the power series coefficients for the potential
    :type coefficients: list of float
    :param mass: the mass of our system
    :type mass: float or int
    :param hbar: the value of hbar in the units we've chosen to use; atomic units (hbar=1) are recommended
    :type hbar: float or int
    :param omega: the frequency of the oscillator we're using for our basis
    :type omega: float or int
    :return:
    :rtype:
    """

    # Recall H = T + V
    hamiltonian_matrix = ...
    # now look at the NumPy 101 tutorial for a function that gives you eigenvalues and eigenvectors
    # of a real symmetric (i.e. Hermitian) matrix
    energies, wavefunction_coeffs = ...
    return energies, wavefunction_coeffs

## Run Script: put the script we'd want to run through PyCharm or from the command line here

if __name__ == '__main__':
    # We want to avoid any kind of 'hard-coding' of parameters in our code, since that's apt to give you hard
    # to find bugs and make it harder for other people to read your code (and other people will almost certainly
    # need to read your code)

    # we'll start by assuming our potential is 0*x + (x**2) + .1*(x**3) + .001*(x**4)
    series_coeffs = [0, 1, .1, .001]
    hbar = 1
    mass = 1
    omega = 1
    basis_size = 25
    energies, wfn_coeffs = energies_and_wavefunctions(series_coeffs,
                                                      mass=mass,
                                                      hbar=hbar,
                                                      omega=omega,
                                                      basis_size=basis_size
                                                      )