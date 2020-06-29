# Code Exercises

Like anything else, coding takes time and effort to get good at.
And like many other things, it's also got an opinionated, sometimes virulent practitioner base.
To help you along and to (hopefully) spare you some of the toxicitiy of the internet, we've collected samples for some of the fundamentals of what we do.
These samples are scripts where the logical structure of a program is provided as a reference so that you can build off of it/fill it out and get a working implementation that follows python best practices.

We'll take [`Template.py`](Template.py) to look at the basic structure of these samples.
The file will auto-download when you click on the link, so open it in PyCharm or [view it on GitHub](https://github.com/McCoyGroup/References/blob/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Template.py).

If we look at the file we see it's got basically five chunks to it

1. Module description (docstring): describes what this module should be doing. It's good to get in the habit of writing these, since it means other people can start using your code without you having to explain how everything works all the time. When we write samples we're always gonna have module doc string.
2. Imports: it's good practice to put `import` statements at the top of your file (unless you have a specific reason not to). This lets other people know what your code depends on without having to dig.
3. Exports: when other people read your code we want to make it clear which functions and classes are actually meant for public consumption and which ones are just meant to be used inside the module itself. We put the names of all the public functions and methods in the `__all__` variable.
4. Classes and Functions: the actual meat-and-potatoes of what we're writing. Aim to write more classes than functions, but whatever gets your logic across the cleanest is best.
5. Run Script: if you're writing code that's only intended to be used from other code you don't need this, but if you want to run your code from the command line, it's good to separate out the definitions (i.e the prior 4 sections) from the runtime. To do that we put the run script inside a block wrapped with `if __name__ == '__main__':`

### List

With that said, here's the list of exercises to work through. Don't feel obligated to do them all right away or in order. But do remember they are here as your research projects expand and evolve. 

* Expand a Function as a Fourier Series
* Apply a change of basis to a Hamiltonian
* [Colbert-Miller 1D DVR](CM_1D.py)
* Colbert-Miller Multidimensional DVR
* Calculate Adiabatic Potentials
* Calculate Franck-Condon Transition Intensities
* Calculate Intensities with a Linear Dipole
* Anderson DMC
* Reyonolds DMC

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/Examples/index.md)
