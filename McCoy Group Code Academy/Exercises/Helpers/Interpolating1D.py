"""
Goal: This fundamental should get you experience with interpolation
Related: ...
"""

## Imports: put all import statments here

import scipy.interpolate as interp

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "Interpolator1D"
]

## Objects: put all the classes we're defining here
class Interpolator1D:
    """
    A simple class that represents a 1D interpolation of a function
    Really, it's just an interface to stuff that's already in scipy.interpolate,
    so if you don't want to bother with it, that's cool by us.
    We leave it here since you can extend it _beyond_ what's already in scipy.interpolate
    to support stuff like extrapolation, getting derivatives, etc.

    We'll build our interpolation like

        interp = Interpolator1D(x_data, y_data)

    then call it on a different set of x values (say the grid points from a DVR calculation) like

        vals = interp(new_x_vals)
    """
    def __init__(self, x_data, y_data, method=None, **kwargs):
        if method is None:
            method = self.interp1d
        self.kw = kwargs
        self.interp_function = method(x_data, y_data, **kwargs)
    @classmethod
    def interp1d(cls, x_data, y_data, fill_value = 0, bounds_error = False, **kwargs):
        return interp.interp1d(x_data, y_data, fill_value=fill_value, bounds_error=bounds_error, **kwargs)
    def __call__(self, x_points):
        return self.interp_function(x_points)

## Run Script: put the script we'd want to run from the command line here

if __name__ == '__main__':
    # We'll test how well an interpolated parabola works
    import numpy as np

    x_data = np.linspace(-10, 10, 100)
    y_data = 1/2*x_data + 5*x_data**2
    int_fun = Interpolator1D(x_data, y_data)
    print("Residue: {}".format(
        int_fun(x_data) - y_data
    ))