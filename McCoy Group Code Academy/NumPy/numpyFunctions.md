# Listing of Helpful Numpy Functions

This is a listing of functions in [numpy](https://www.numpy.org/)/[scipy](https://www.scipy.org/) that members of the group have found particularly useful.
The idea isn't to be a complete listing nor to provide detailed documentation.
Rather we're hoping that this will serve as a jumping off point for you to investigate for yourself
and keep you from feeling like you're drowning in the docs.

We've provided the broad topics, _General_, _DMC_, and _DVR_, _Optimization_

### General
* [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html): creates an array of evenly spaced values over a given interval
* [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html): creates an array of evenly spaced values of a given number over a given interval
* [average](https://numpy.org/doc/stable/reference/generated/numpy.average.html): takes the average of an array
* [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html): returns the indices of the sorted array
* [argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html): returns the indices of the maximum element
* [argwhere/where](https://numpy.org/doc/stable/reference/generated/numpy.where.html): return either indices (argwhere) or elements (where) chosen that fulfill a certain condition.
* [logical operations](https://numpy.org/doc/stable/reference/routines.logic.html#logical-operations): returns elementwise truth values of an array given two conditions using logical_and, logical_xor, etc.
* [sort/lexsort](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html): sort will sort elements along a specified axis, lexsort allows you to do nested sorting (sort by array a, then array b)


### Numerical
* [exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html): calculates the exponential
* [power](https://numpy.org/doc/stable/reference/generated/numpy.power.html): raises a value to a given power (NumPy equivalent of `**`) 
* [pi](https://numpy.org/doc/stable/reference/constants.html?highlight=pi#numpy.pi): returns the value of pi
* [rad2deg/deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html): converts to and from degrees/radians.
* Also look at other constants numpy knows [here](https://numpy.org/doc/stable/reference/constants.html)

### Arrays
* [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html): creates a new array full of the value `0`
* [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html): creates a new array full of the value `1`
* [eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html): creates an identity matrix of whatever size you need
* [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html): creates a numpy array (useful for making lists into numpy arrays)
* [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html): reshapes an array
* [delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html): deletes specified elements of an array
* [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html): tranposes the elements of an array
* [diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html): either brodcasts a 1D array to the diagional of a 2D array or pulls the diagonal of a 2D array
* [column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html): stacks 1D arrays column-wise into a 2D array
* [concatentate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html): concatenate arrays along  a specified axis
* [in1d](https://numpy.org/doc/stable/reference/generated/numpy.in1d.html?highlight=in1d#numpy.in1d): checks if elements of one array are in another
* [flip](https://numpy.org/doc/stable/reference/generated/numpy.flip.html): returns the reversed array. Last element is first, etc.

### Linear Algebra
* [dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html): computes a dot product of 2 arrays
* [inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html): computes the inner porduct of 2 arrays
* [outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html): computes the outer product of 2 arrays
#### numpy.linalg
_Note: If you use `import numpy as np` in order to call these functions you will need to use `np.linalg.norm`. 
Or, you can do `import numpy.linalg as la` and do `la.norm`_
* [norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html): gets the norm of a vector
* [eigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html): computes the eigenvalues and eigenvectors of a Hermitian matrix
* For more see [here](https://numpy.org/doc/stable/reference/routines.linalg.html)

### <Your Tag Here>

## DMC
* [random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html): generates a random number between two inputs
* [random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html): generates a random number chosen from a normal (gaussian) distribution.
* [unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html): how many unique elements in an array, can return counts and/or indices.  Good for discrete  descendant weighting.

## DVR

...

## Optimization

...

---

### Adding to the List

If you want to add to the list, feel free.
All we're gonna ask is that you follow a basic template.
First decide which of the existing headings your function should go under, then add your function using Markdown like
```lang-none
* [<name of function>](<URL of documentation page>): brief description of what it does
```

At this point in time, that's all we're asking, but the hope is that it'll keep entropy at bay.

<span class="text-muted">Next:</span>
 [Usage Examples](Examples.md)<br/>
<span class="text-muted">Previous:</span>
 [NumPy 101](Numpy101.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/numpyFunctions.md)
