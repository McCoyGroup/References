"""
Goal: To be able to ingest the data stored in a file and use it to plot a DVR spectrum, using DVR
Fundamentals: Making a Class
Related Exercises: Colbert-Miller DVR
"""

## Imports: put all import statments here

import numpy as np
from Helpers.PlottingData import Plotter # We'll use the Plotter object from the PlottingData fundamental
# The `from Helpers.PlottingData` is just here to indicate that PlottingData is in the Helpers folder
# If you download it to the same directory as this file, you will have to change that import line to `from PlottingData import Plotter`
from Helpers.Interpolating1D import Interpolator1D
from Helpers.FittingToAPolynomial import FittedPolynomial


## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "DVRSpectrumGenerator"
]

## Objects: put all the classes we're defining here

class DVRSpectrumGenerator:
    """
    An object that should take an inputs file and a set of results
    and provide you with a way to calculate intensities
    """
    def __init__(self, inputs_file, dvr_results, num_wfns=5, dipole_type='interpolated'):
        """
        :param inputs_file: npz file with inputs for a DVR calculation; has keys 'coords', 'potential', 'dipoles'
        :type inputs_file: str
        :param dvr_results: npz file with results from a DVR calculation; has keys 'energy', 'wavefunctions', 'params'
        :type dvr_results: str
        :param num_wfns: the number of wavefunctions to calculate transition intensities for
        :param dipole_type: the kind of dipole moment we want to use; possible values 'interpolated', 'linear', 'quadratic'
        """
        # Here's an an example of how you can store the files you're loading from
        self.inputs_file = inputs_file
        self.results_file = dvr_results
        # Now it's up to you to do actually attach the data you'll need to your object
        ...

    def get_interpolated_dipole_moment(self):
        """
        :return: the interpolated dipole moment function
        :rtype: Interpolator1D
        """
        # Hint: the Interpolator1D class we've loaded in is built for this
        ...
    def get_linear_dipole_moment(self):
        """
        :return: a linear approximated dipole moment function
        :rtype: FittedPolynomial
        """
        # Hint: the FittedPolynomial class we've loaded in is built for this
        ...
    def get_quadratic_dipole_moment(self):
        """
        :return: a quadratic approximated dipole moment function
        :rtype: FittedPolynomial
        """
        # Hint: the FittedPolynomial class we've loaded in is built for this
        ...
    def get_dipole_moment(self):
        """
        :return: the dipole functions we're going to use
        :rtype:
        """
        if self.dipole_mode == "interpolated":
            return self.get_interpolated_dipole_moment()
        elif self.dipole_mode == 'linear':
            return self.get_linear_dipole_moment()
        elif self.dipole_mode == 'quadratic':
            return self.get_linear_dipole_moment()
        else:
            raise ValueError("bad dipole type '{}'".format(self.dipole_mode))
    def get_transition_moments(self):
        """
        :return: the transition moments from the ground state calculated from the data we loaded in
        :rtype: np.ndarray
        """
        # Hint: recall that the transition moment can be calculated as a  dot product for a DVR
        ...

    def get_frequencies(self):
        """
        :return: the transition frequencies calculated from the data we loaded in
        :rtype: np.ndarray
        """
        # might be helpful that the Hartree to Wavenumber conversion is 219474.631363
        ...

    def get_intensities(self):
        """
        :return: the intensities calculated from the results of get_transition_moments() and get_frequencies().
                 You may want to add a argument here for calculating intensities with different units.
        :rtype: np.ndarray
        """
        ...

    def plot_spectrum(self, plot=None, **styles):
        """
        :param plot: an existing plot to plot this spectrum on _or_ `None` to make a new spectrum
        :type plot: Plotter | None
        :param styles: styles for this plot
        :return: a plot of the spectrum
        :rtype: Plotter
        """
        if plot is None:
            plot = Plotter()
        plot.plot_lines(self.get_frequencies(), self.get_intensities(), **styles)
        return plot

if __name__ == '__main__':
    # We've provided you with some sample data from prior DVR runs
    # We have both input data, anharmonic data, and harmonic data
    inputs_file = "Data/DVRSpectrum_inputs.npz"
    anharmonics_file = "Data/DVRSpectrum_anharmonic.npz"
    harmonics_file = "Data/DVRSpectrum_harmonic.npz"

    anharmonic = DVRSpectrumGenerator(inputs_file, anharmonics_file)
    anh_spec = anharmonic.plot_spectrum()
    anh_spec.show()

    anharmonic = DVRSpectrumGenerator(inputs_file, anharmonics_file)
    harm_spec = anharmonic.plot_spectrum()
    harm_spec.show()

    ####################################################################
    #####                       ADVENTURE TIME                     #####
    ####################################################################
    # At this point, you should go explore for yourself
    # Optimally, you'd go back to your DVR implementation and
    #   use that to generate a bunch of new input & results files
    # You should also go back and do a direct comparison of the
    #   anharmonic and harmonic spectra. To do this, note that we wrote
    #   `plot_spectrum` so that it can take an existing plot and plot
    #   a new plot on top of that plot
