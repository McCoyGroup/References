"""
Goal: To be able to ingest the data stored in a
Fundamentals: Making a Class, Interpolating a 1D Function
Related Exercises: Colbert-Miller DVR
"""

## Imports: put all import statments here

import numpy as np
import matplotlib.pyplot as plt

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "Plotter",
    "DVRSpectrumGenerator"
]

## Objects: put all the classes we're defining here
class Plotter:
    """
    A very simple plotter that makes the object-oriented matplotlib interface
    a little bit cleaner to work with.
    We've filled in most of this for you, but you get to figure out how the
    `plot_lines` method should work
    """
    def __init__(self):
        self.figure, self.axes = plt.subplots()
    def plot_curve(self, x_data, y_data, **styles):
        """
        :param x_data: the x points for your curve
        :param y_data: the y points for your curve
        :param styles: curve styling, if you want it
        """
        self.axes.plot(x_data, y_data, **styles)
    def plot_points(self, x_data, y_data, **styles):
        """
        :param x_data: the x points for your curve
        :param y_data: the y points for your curve
        :param styles: point styling, if you want it
        """
        self.axes.scatter(x_data, y_data, **styles)
    def plot_lines(self, x_data, y_data, **styles):
        """
        Plots a bunch of vertical lines. You get to implement this one yourself

        :param x_data: the x points for your curve
        :param y_data: the y points for your curve
        :param styles: point styling, if you want it
        """
        ...
    def show(self):
        plt.show()

class DVRSpectrumGenerator:
    """
    An object that should take an inputs file and a set of results
    and provide you with a way to calculate intensities
    """
    def __init__(self, inputs_file, dvr_results):
        """
        :param inputs_file: npz file with inputs for a DVR calculation; has keys 'coords', 'potential', 'mu_x', 'mu_y', 'mu_z'
        :type inputs_file: str
        :param dvr_results: npz file with results from a DVR calculation; has keys 'energies', 'wavefunctions', 'params'
        :type dvr_results: str
        """
        # Here's an an example of how you can store the files you're loading from
        self.inputs_file = inputs_file
        self.results_file = dvr_results
        # Now it's up to you to do actually attach the data you'll need to your object
        ...

    def get_transition_moments(self):
        """
        :return: the transition moments from the ground state calculated from the data we loaded in
        :rtype: np.ndarray
        """
        # Hint: recall that the transition moment can be calculateed
        #       as a simple dot product for a DVR
        ...

    def get_frequencies(self):
        """
        :return: the transition frequencies calculated from the data we loaded in
        :rtype: np.ndarray
        """
        ...

    def get_intensities(self):
        """
        :return: the transition frequencies calculated from the data we loaded in
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
