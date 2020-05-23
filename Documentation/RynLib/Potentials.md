# Potentials

RynLib has a very flexible system for using potentials. 
It was written originally to allow for hyper-distributed calling of Entos, but now can work with pretty much any potential, compiled or not.

## Installing a Prebuilt Potential

One of the big benefits of the container architecture is the portability of what gets built. For many use cases, a potential will already have been created. If that's the case, we can compress it and get it out of the container on one platform via

```ignorelang
rynlib pot export NAME DEST
```

and then we can install it on a different platform with

```ignorelang
rynlib pot import NAME SRC
```

These are just `zip`/`unzip` operations so you can certainly also do them by hand if you prefer

## Compiling a Potential

### Directly Compiling the Potential

Since we need to call the potential inside the container environment, we need a way to compile the potential inside the container.

As an example, let's imagine we want to work with a harmonic oscillator. Maybe we have the source as `HarmonicOscillator.cpp`

```c++
double HarmonicOscillator(std::vector<std::vector<double> > coords, std::vector<std::string> atoms, double force_constant, double re) {
    // compute HO from coords, force_constant, and re
    ...
    return pot;
}
```

We need to decide how we want this to compile, which we set up by either creating a `Makefile` or a file called `build.sh`. 
Inside the container one or other other of these will be called, with `make` being prioritized.

By default, the code expects that this will make a library called `libHarmonicOscillator.so`, but if this isn't the case we can specify the name in our configuration file.
The only available compiler is `gcc/g++/gfortran` so be aware of this when writing your build script.

### Using f2py

Because [f2py]() is such a common use case, we added support for calling into a general python potential. 
_In general_, we don't recommend it, since it requires an extra layer of indirection and so will be somewhat slower than using a directly compiled potential, but it would have been negligent to leave it out. 

In this case, again, we provide a `Makefile`, but this file will call into `f2py` and return a proper python extension library.

Then we will write a package on the _python_ side that will load our potential from this and which will be defined like

```python
def _potential(walkers, atoms, extra_args):
    """
    :param walkers: the walkers to evaluate the potential over
    :type walkers: np.ndarray
    :param atoms: the atom symbols for the walker coordinates
    :type atoms: list[str]
    :param extra_args: a tuple of any extra bools, ints, and floats to be passed in
    :type extra_args: tuple
    """
    ...
```

the name _does_ have to be `_potential`, but if people also think it's really ugly it could definitely be changed

All of the data will get farmed out to the different cores when doing this.

### Using a Precompiled Binary

If you know the binary you have will work with the container, you can pass it in directly. In this case we simply have to turn off the `requires_make` flag.

### Loading the Potential

When getting a potential into the container, we use the command

```ignorelang
rynlib pot add src
```

The _source_ should be where our potential is stored, so either the directory containing the source or the potential binary.

The _config\_file_ holds the parameters for the potential. 
For the most part it just makes sense to look at one of the examples, since there are an overwhelming number of options.
At some point in the future, once the API has stabilized, I'll go back and document the options here.

## Creating a Wrapper

To make the potential accessible from python, we need to make a smaller wrapper around it.

The basic idea is to expose a function through a `PyCapsule` object that can be fed into the caller. 
The caller is written in C++ and expects the function it's calling to expose a specific type-signature.

### Using the Automatic Wrapper

For most cases, the automatic wrapper will suffice. In this case, in the potential's `config.py` we just need to expose something like

```python
config = dict(
    wrap_potential=True, # tells the loader that it needs to build an automatic wrapper
    function_name='HarmonicOscillator', # the name of the function we're calling on the C++ side
    arguments=(('re', 'float'), ('k', 'float')), # the arguments to be fed in
    requires_make=True, # letting the loader know that the underlying C++ src code needs to be compiled, e.g. using the Makefile you provided
    linked_libs=['HarmonicOscillator'] # the name of the compiled library we link in
)
```

Here's a listing of all of the options specific to the automatic wrapper

* `function_name` - this is a string telling us what the function we're wrapping is called
* `arguments` - this is the set of arguments that go in to the potential, each argument will have a name and will conform to the "argument spec" defined below
* `shim_script` - this is a string that gets inserted directly into the wrapper function after the arguments are loaded, which makes it possible to do things like create a temporary buffer to fill in
* `raw_array_potential` - this specifies whether the potential expects to get a flat set of coordinates or not

Of these, by far the most subtle is the `arguments`. The reason for this is two-fold. 

First off, by default `coords` and `atoms` are passed into the call unless you actively specify one or the other, e.g. if you say

```python
arguments = (('re', 'float'), ('k', 'float'))
```

this turns into

```python
arguments = ("coords", "atoms", ('re', 'float'), ('k', 'float'))
```

but if you say

```python
arguments = ("coords", ('re', 'float'), ('k', 'float'))
```

no transmogrification is done. 

This possible annoyance and subtlety was done to make the thing I thought was common easy. This may have been a mistake.

The second subtlety has everything to do with C++ and to explain it I think it will be easiest to describe the full possible argument spect

### Wrapping Your Own Potential

The caller allows for two flavors of call signatures, the first is "modern" potentials that allow for a multi-dimensional array of coordinates

```c++
double pot(
  std::vector<std::vector<double> > coords, std::vector<std::string> atoms, 
  std::vector<bool> extra_bools, std::vector<int> extra_ints, std::vector<float> extra_floats);
```

The second flavor differs only in that it expects a flat array of coordinate data and allows the called function to deal with it

```c++
double pot(
  std::vector<double> coords, std::vector<std::string> atoms, 
  std::vector<bool> extra_bools, std::vector<int> extra_ints, std::vector<float> extra_floats);
```

The option passed to the `PotentialCaller` is `raw_array_potential=True` to pass data in this flat manner.

Usually, this wrapper function will be no more than a stub that is used to call some other program, e.g. this wrapper that I use for calling into the [TTM family of water potentials](https://sites.uw.edu/wdbase/database-of-water-clusters/).

```c++
double TTM_ttm(
  std::vector<double> coords, std::vector<std::string> atoms,
  std::vector<bool> extra_bools, std::vector<int> extra_ints, std::vector<float> extra_floats
  ) {

    // Load the number of waters and the chosen model for the TTM potential (
    int nwaters = extra_ints[0];
    int imodel = extra_ints[1];
    // Copy data into a single array
    double* raw_coords = coords.data();
    
    // The potential itself needs an extra array to write the derivatives to, even though we don't use it
    double derivs[nwaters*9];
    double energy = -1000.;
    // calling ttm from Fortran module ttm_mod
    if (imodel==3) {
        __ttm3f_mod_MOD_ttm3f(&nwaters, raw_coords, derivs, &energy);
    } else {
        __ttm2f_mod_MOD_ttm2f(&nwaters, raw_coords, derivs, &energy, &imodel);
    };

    return energy / 627.5094740631; // Convert kcal/mol to Hartree

}
```

After doing that we need to

* Put the call signature for this function and the called functions from the library in the corresponding `.hpp` file
* Wrap this up in a `PyCapsule`
* Expose these things via the python extension module boilerplate

None of this requires much thought, so I've provided some helpful boilerplate [here](https://github.com/McCoyGroup/RynLib/tree/master/RynUtils/C%2B%2B%20Common/Boilerplate)

