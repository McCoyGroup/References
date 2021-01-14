"""
Goal: This fundamental should get you acquanited with plotting harmonic and morse oscillator potentials
"""

## Imports: put all import statments here

import numpy as np
import matplotlib.pyplot as plt

## Exports: put all the names things we might want to use in other scripts here

__all__ = ["plot_HO_pot", "plot_MO_pot"]


## Functions: put all the functions we're defining here
def HO_pot(disp, mass, omega, eq_disp):
    """
    :param disp: An array of displacements in atomic units
    :type disp: np.ndarray
    :param mass: The reduced mass of the system
    :type mass: float
    :param omega: The frequency in atomic units
    :type omega: float
    :param eq_disp: The equilibrium value of the potential, in atomic units
    :type eq_disp: float
    :return: The values of the potential at each of the disps values
    :rtype: np.array
    """

    ...
    return pot_vals


def MO_pot(disp, mass, omega, omega_x, eq_disp):
    """
    :param disp: An array of displacements in atomic units
    :type disp: np.ndarray
    :param mass: The reduced mass of the system
    :type mass: float
    :param omega: The frequency in atomic units
    :type omega: float
    :param omega: The "Anharmonicity" atomic units
    :type omega: float
    :param eq_disp: The equilibrium value of the potential, in atomic units
    :type eq_disp: float
    :return: The values of the potential at each of the disps values
    :rtype: np.array

    Calculate De and Alpha from omega and omega_x
    https://www.sciencedirect.com/science/article/abs/pii/S0009261410015460?via%3Dihub
    """
    ...
    return pot_vals


def plot_pot(disps, pot_vals, plt_title, savefig_filename):
    """
    :param disp: Our displacements in Angstroms
    :type disp: np.ndarray
    :param pot_vals: The potential values in wavenumbers
    :type pot_vals: np.ndarray
    :param plt_title: The title that will display at the top of the plot
    :type plt_title: str
    :param savefig_filename: The filename of the plot that you will be saved to the current working directory.
    :type savefig_filename: str

    Must have arguments in angstroms and wavenumbers
    """
    # Params updates so that the font size is larger and font is akin to arial, and you can use Latex formatting :).
    # See more here: https://matplotlib.org/3.3.1/tutorials/text/mathtext.html
    params = {'text.usetex': False,
              'mathtext.fontset': 'dejavusans',
              'font.size': 14}
    plt.rcParams.update(params)
    fig, ax = plt.subplots()
    ...
    fig.savefig(...)
    plt.close()


## Run Script: put the script we'd want to run from the command line here
if __name__ == '__main__':
    # Harmonic Oscillator:
    # V = 0.5 * k * (r-re)**2 = 0.5 * mass * (omega**2) * (r-re)**2

    # Morse Oscillator:
    # https://www.sciencedirect.com/science/article/abs/pii/S0009261410015460?via%3Dihub
    # V = De*((1-np.exp(-alpha*(r-re))))**2
    # Where alpha = sqrt(mass*(omega ** 2)/(2*De))

    # mass is the reduced mass of the system,
    # omega is the frequency,
    # De is the dissociation energy
    # r is the displacement,
    # and re is the eq. displacement

    # DO CALCULATIONS IN ATOMIC UNITS, PLOT IN WAVENUMBERS AND ANGSTROMS
    # hbar = 1
    amu_to_au = 1.000000000000000000 / 6.02213670000e23 / 9.10938970000e-28  # conversion
    cm_to_au = 4.55634e-6
    angstr_to_au = 1 / 0.529177

    # Base potential Data for O-H stretch
    # After you have this working for an O-H stretch, play with these parameters! for example look at a C-H or O-O or C-O stretch
    mass_O = 15.99491561957 * amu_to_au
    mass_H = 1.00782503223 * amu_to_au
    reduced_mass = (mass_O * mass_H) / (mass_O + mass_H)
    omega = 3600. * cm_to_au

    # Harmonic Oscillator
    displacements = np.linspace(-2, 2, 10000)  # center around 0
    pots = HO_pot(disp=displacements,
                  mass=reduced_mass,
                  omega=omega,
                  eq_disp=0.0)
    plot_pot(disps=displacements / angstr_to_au,
             pot_vals=pots / cm_to_au,
             plt_title='Harmonic Oscillator Potential',
             savefig_filename='HO_pot')

    # Morse Oscillator
    displacements = np.arange(-1, 3, 0.005)  # center around 0
    omega_x = 750 * cm_to_au
    pots = MO_pot(disp=displacements,
           mass=reduced_mass,
           omega=omega,
           omega_x=omega_x,
           eq_disp=0.0)

    plot_pot(disps=displacements / angstr_to_au,
             pot_vals=pots / cm_to_au,
             plt_title='Morse Oscillator Potential',
             savefig_filename='MO_pot')
