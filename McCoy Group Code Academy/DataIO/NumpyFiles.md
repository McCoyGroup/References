# Python Specific File Types

Okay, so by now you have probably figured out that we are all _pretty big_ fans of Python. So it shouldn't a big surprise that we pass along/save/archive data in Python specific files. 
There are two types `*.npy` and `*.npz` that we commonly use. 

Note: these types of files can only be written/read by NumPy. If you want to exchange data between languages, look into using a standard text format like [JSON](https://docs.python.org/3/library/json.html).
{: .alert .alert-warning}

## .npy Files 

A `*.npy` is a file extensition specifically for storing NumPy arrays. 
This file type is able to save all the information required to reconstruct the same NumPy array on any computer, i.e. it knows the `dtype` and `shape` information of the array.  
This comes in handy particulary when you are passing data around between group members or have worked up a large set of data and want to save it for later.

### How to Use: 

* In order to create one of these files you will make use of the `np.save()` command. Read about it [here](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
* In order to read one of these files you will make use of the `np.load()` command. Read more [here](https://numpy.org/doc/stable/reference/generated/numpy.load.html)


## .npz Files

A `*.npz` is a file extensition for storing _multiple_ NumPy arrays or variable values. 
With these files, you can store multiple arrays that don't neccessarily have to have the same shape. This comes in handy when you need to send/save data, parameters, results, etc all together. 
These files are essentially "zipped" `.npy` files where the file name of the npy is constructed by some key. 

### How to Use:

* In order to create one of these files you will make use of the `np.savez()` command. Read about it [here](https://numpy.org/doc/stable/reference/generated/numpy.savez.html)
* In order to read one of these files you will make use of the same `np.load()` command as you would for a `*.npy`. Read more [here](https://numpy.org/doc/stable/reference/generated/numpy.load.html)


## An Example
If I wanted to store the results of a [DVR](https://mccoygroup.github.io/References/References/Basis%20Set%20Methods/BasicDVR.html) calculation along with the parameters to make it easily reproducible, I would do something like: 
```python
grid = ... # type: np.ndarray
wfns = ... # type: np.ndarray
energies = ... # type: np.ndarray
params = ... # type: dict

np.savez("DVRSpectrum_harmonic.npz", grid=grid, energies=energies, wavefunctions=wfns, params=params)
```

Alternatively, if I recieved the file `DVRSpectrum_harmonic.npz` and wanted to get the data back out, I'd load it in like
```python
data = np.load("DVRSpectrum_harmonic.npz")
```

then were I not sure what was in the file I could check the keys similarly to a `dict` by
```console?lang=python&&prompt=>>>
>>> print(data.keys())
['grid', 'energies', 'wavefunctions', 'params']
```

and so if I just wanted the DVR parameters I'd access them like
```console?lang=python&&prompt=>>>
>>> params_dict = data["params"]
{...}
```

<span class="text-muted">Next:</span>
 [Gaussian, an Intro](GaussianIntro.md)<br/>
<span class="text-muted">Previous:</span>
 [Exporting Data Out](ExportingDataOut.md)
 

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/NumpyFiles.md)

