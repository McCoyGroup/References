# Code Exercises

Like anything else, coding takes time and effort to get good at.
And like many other things, it's also got an opinionated, sometimes virulent practitioner base.
To help you along and to (hopefully) spare you some of the toxicitiy of the internet, we've collected samples for some of the fundamentals of what we do.
These samples are scripts where the logical structure of a program is provided as a reference so that you can build off of it/fill it out and get a working implementation that follows python best practices.

### General Layout

We've written this in the way we feel best represents good python code.
Obviously with anything code-style related, there are differences in opinion, but our feeling is that this layout will serve you well.
We think the structure we're showing here will help you if you choose to switch to a language like Java or C++ and will also serve you well if you try to find a job outside of academic chemistry research.
{: .alert .alert-success}

We'll take [`Template.py`](Template.py) to look at the basic structure of these samples.
The file will auto-download when you click on the link, so open it in PyCharm or [view it on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Template.py).

If we look at the file we see it's got basically five chunks to it

1. Module description (docstring): describes what this module should be doing. It's good to get in the habit of writing these, since it means other people can start using your code without you having to explain how everything works all the time. When we write samples we're always gonna have module doc string.
2. Imports: it's good practice to put `import` statements at the top of your file (unless you have a specific reason not to). This lets other people know what your code depends on without having to dig.
3. Exports: when other people read your code we want to make it clear which functions and classes are actually meant for public consumption and which ones are just meant to be used inside the module itself. We put the names of all the public functions and methods in the `__all__` variable.
4. Classes and Functions: the actual meat-and-potatoes of what we're writing. Aim to write more classes than functions, but whatever gets your logic across the cleanest is best.
5. Run Script: if you're writing code that's only intended to be used from other code you don't need this, but if you want to run your code from the command line, it's good to separate out the definitions (i.e the prior 4 sections) from the runtime. To do that we put the run script inside a block wrapped with `if __name__ == '__main__':`

## Exercise List

We've split our list of exercises up so that they roughly match the layout we have in our [References](../../References).
If you'd like to brush up on your python or object-oriented programming, give the [Getting Started](../GettingStarted) guide a look.
Most of these will make use of `numpy`, so if you aren't totally comfortable with that check out our [Numpy 101](../NumPy) intro.

We recommend downloading the whole set of exercises [here](https://github.com/McCoyGroup/References/raw/gh-pages/McCoy%20Group%20Code%20Academy/Exercises.zip) so that you can use the [Helpers](https://github.com/McCoyGroup/References/tree/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Helpers) and [Data](https://github.com/McCoyGroup/References/tree/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Data) we've included for you.
If you just want to look at an individual exercise, though, each one is just a `.py` file that downloads automatically, but if you'd prefer you can also view them on GitHub.
{: .alert .alert-success}


### Fundamentals

These will be referenced inside the exercises, but don't feel like you need to work through all of them right now.
{: .alert .alert-warning}
* [Intro to NumPy](Fundamentals/IntroToNumpy.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/IntroToNumpy.py))
* [Intro to npy/npz Files](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/DataIO/NumpyFiles.html)
* [Reading/Writing an XYZ file](Fundamentals/XYZWriter.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/XYZWriter.py))
* [Plotting Harmonic and Morse Oscillator Potentials](Fundamentals/PlotOscillators.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/PlotOscillators.py))
* [Filling out a Matrix](Fundamentals/FillingAMatrix.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/FillingAMatrix.py))
* [Turning a Piecewise Formula into a Matrix](Fundamentals/PiecewiseToMatrix.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/PiecewiseToMatrix.py))
* [Performing a Change of Basis](Fundamentals/ChoB.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/ChoB.py))
* [Fitting to a Fourier Expansion](Fundamentals/FourierExpansion.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Fundamentals/FourierExpansion.py))




### Basis Set Methods

* [Particle in a Box Representation](PIBRep.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/PIBRep.py))
* [Harmonic Oscillator Representation](HORep.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/HORep.py))
* [Colbert-Miller 1D DVR](CM_1D.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/CM_1D.py))

### Monte Carlo Methods

* [Discrete Weighting DMC](DiscreteDMC.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/DiscreteDMC.py))
* [Continuous Weighting DMC](ContinuousDMC.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/ContinuousDMC.py))
* [Importance Sampling](ImpSamp.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/ImpSamp.py))

### Spectrum Generation

* [General Basis Set Spectra](BasisSetSpectrum.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/BasisSetSpectrum.py))
* [DVR Spectra](DVRSpectrum.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/DVRSpectrum.py))
* [Adiabatic Spectra](AdiabaticSpectrum.py) ([View on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/AdiabaticIntensities.py))

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/index.md)
