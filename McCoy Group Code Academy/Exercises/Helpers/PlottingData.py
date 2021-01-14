"""
Goal: This fundamental should get you experience with plotting functions and data
Related: All of the Plotting sections in McCode Academy
"""

## Imports: put all import statments here

import numpy as np
import matplotlib.pyplot as plt, matplotlib.figure as mplfig, matplotlib.axes as mplax

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "Plotter"
]

## Objects: put all the classes we're defining here
class Plotter:
    """
    A very simple plotter that makes the object-oriented matplotlib interface
    a little bit cleaner to work with.

    We use it by first making a Plotter() and then calling that object's `plot_*` methods
    """
    def __init__(self):
        self.figure, self.axes = plt.subplots()
    def plot_function(self, f, x_min, x_max, npoints=100, **styles):
        """
        :param f: the function to plot
        :param x_min: the minimum point to plot in x
        :param x_max: the maximum point to plot in x
        :param npoints: the number of points to use
        :param styles: curve styling, if you want it
        """
        x_data = np.linspace(x_min, x_max, npoints)
        self.plot_curve(x_data, f(x_data), **styles)
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
        :param x_data: the x points for your curve
        :param y_data: the y points for your curve
        :param styles: point styling, if you want it
        """
        y_data = np.asarray(y_data)
        if 'colors' not in styles:
            styles['colors'] = ['red']*len(x_data)
        self.axes.vlines(x_data, np.zeros(y_data.shape), y_data, **styles)
    def show(self):
        plt.show()

## Run Script: put the script we'd want to run from the command line here
if __name__ == '__main__':
    gaussian_plot = Plotter()
    gaussian_function = lambda x,sigma=1,x0=0: np.exp(-(x-x0)**2/sigma)
    gaussian_plot.plot_function(gaussian_function, -5, 5)
    gaussian_plot.show()

    line_plot = Plotter()
    x_points = np.linspace(-2, 2, 25)
    line_plot.plot_lines(x_points, gaussian_function(x_points))
    line_plot.show()