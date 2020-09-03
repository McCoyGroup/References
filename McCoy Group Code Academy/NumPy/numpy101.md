# Numpy 101

Note: NumPy does not come prepackaged with Python. In order to use NumPy, you will need to either use Anaconda or install NumPy to your Python installation.  To learn how to do that, go back to [Getting Started](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/GettingStarted/IntroToPython.html)


NumPy, at its heart, fixes the fact that python isn't good at managing big blocks of numbers.
To do this, NumPy introduces a core type called an `array`.
We can think of this as an _n_-dimensional matrix.
It can be a 1D matrix (a vector), a 2D matrix (just a regular matrix), a 3D matrix (a vector of 2D matrices), etc.
These _n_-D matrices are usually called _tensors_, so be ready to see that terminology in guides and tutorial outside of this.

### A Very Brief Introduction to Arrays

NumPy array creation is very easy, but a defining feature is that it is a fixed size, i.e. if you want to update a vector's size, you need to reassign the variable. Here, we use `np.zeros` to initialize a 1D array of length 10.

```console?lang=python&prompt=>>>
>>> import numpy as np
>>> example_array = np.zeros((2,5,3))
>>> print(example_array)

[[[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]]
```

Note that the default data type for each element in the array is a 64-bit floating point number, also known as a `double` in other languages.  

For multidimensional arrays, you can supply a `tuple` to the `np.zeros()` function:

```console?lang=python&prompt=>>>
>>> import numpy as np
>>> example_array = np.zeros((2,5,3))
>>> print(example_array)

[[[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]]
```

As you can see, the first "axis", `axis=0` is the depth-wise axis, the second axis `axis=1` specifies the number of rows, and the last axis `axis=2` specifies the number of columns. There are plenty of ways to create arrays, you can see more of them [here](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/NumPy/numpyFunctions.html).

Once you have an array, you can index it much a Python list, but with greater flexibility

```console?lang=python&prompt=>>>
>>> import numpy as np
>>> tiny_array = np.array([[0,1,2],[3,4,5]]) # the creation of a hard-coded numpy array with a list of lists
>>> print(tiny_array[0, 0])
0
>>> print(tiny_array[0, 1])
1
>>> print(tiny_array[1, 0])
3
>>> print(tiny_array[1, -1]) #-1 means "last" in Python
5
>>> print(tiny_array[0, :]) #a bare ":" means everything 
[0,1,2]
>>> print(tiny_array[0]) #if an axis after the first one is not specified, it defaults to : 
[0,1,2]
>>> print(tiny_array[:, 1]) #This slices columns 
[1,4]
>>> print(tiny_array.shape) #This returns the tuple associated with the indices of the numpy array
(2,3)
```

### Example and Performance Considerations

NumPy performs best when no looping is involved.  This is because, as one goes past 1000s of operations to 10 000+ operations, NumPy has a bunch of built-in functions that are significantly faster than anything one could write using Python looping. These functions are reffered to as *Vectorized* operations.  They are written in C by the friendly NumPy developers.  The most basic example of this can be seen in performing matrix addition. 

```python
import numpy as np
example_array = np.random.random((10000,50,3)) #works like np.zeros, but instead of filling the array with 0 if fills it with a random number between 0 and 1
example_array_2 = np.random.random((10000,50,3))

#pythonic way
res_array = np.zeros(example_array.shape) #.shape allows us to get the tuple of an already initialized array
for i in range(len(example_array)): #len() of a numpy array defaults to the length of axis=0
 for j in range(len(example_array[i])):
  for k in range(len(example_array[i,j])):
   res_array[i,j,k] = example_array[i,j,k] + example_array_2[i,j,k]

#numpy way
res_array = example_array + example_array2

#equivalent numpy way
res_array = np.add(example_array, example_array2)
```

Not only is the NumPy fewer lines of code and much less error prone, it also will perform much, much faster than the pure Python way.
If you are coming from another programming language, you may be wary of the fact that `res_array` was not initialized before we assigned an array to it. 
This is a subtle, important point about NumPy: a lot of memory management happens under the hood & a lot of it is done with [mutable state](https://www.interviewcake.com/concept/java/mutable) for efficiency. 
Keep this in mind while coding and hopefully you will not be bitten by some of the subtle bugs that have gotten the rest of us with this.

NumPy & its sister package [SciPy](https://www.scipy.org/) are huge programs with tons of very, very useful functions.
In fact, if you need to implement something, it's worth checking the NumPy & SciPy docs (or checking Stack Overflow) to make sure that someone hasn't already implemented it. 
Basically, if you need to code something up, make sure there isn't a NumPy function that can already do it! 
To see a partial set of functions that the McCoy group finds useful, check out our [List of Useful NumPy Functions](numpyFunctions.md). 

Next, we suggest doing the [Intro to NumPy](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/Exercises/) Fundamental exercise. 

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/numpy101.md)
