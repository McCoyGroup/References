# Potentials

RynLib has a very flexible system for using potentials. 
It was written originally to allow for hyper-distributed calling of Entos, but now can work with pretty much any potential, compiled or not.

## Installing a Potential

Before we can use a potential, we need to get it into the system and accessible. There are two ways to go about this.

### Installing a Prebuilt Potential

One of the big benefits of the container architecture is the portability of what gets built. For many use cases, a potential will already have been created. If that's the case, we can compress it and get it out of the container on one platform via

```ignorelang
rynlib pot export NAME DEST
```

and then we can install it on a different platform with

```ignorelang
rynlib pot import NAME SRC
```

These are just `zip`/`unzip` operations so you can certainly also do them by hand if you prefer

### Installing a New Potential

If no prebuilt potential exists, we'll need to add and compile one ourselves. To start, we'll focus on the adding part.
When getting a potential into the container, we use the command

```ignorelang
rynlib pot add NAME SRC
```

_NAME_ is the name we'll reference the potential by inside RynLib, _SRC_ should be where our potential is stored.
Inside _SRC_, we expect two (maybe three) things
* The source code for the potential (or a precompiled binary to call)
* A config file detailing the configuration of the potential (see the examples)
* Optional: a test file to use as the default when testing the potential (see the section on testing)

## Calling a Potential

Once we have a potential installed, `RynLib` is able to load it by name. This is done through the `PotentialManager` class

```python
pm = PotentialManager()
pot = pm.load_potential("<NAME>")
```

With the potential loaded, we can call it like

```python
pot(coords, atoms, *parameters)
```

or if we've supplied an `arguments` spec, we can use the associated names, like

```python
pot(coords, atoms, **parameters)
```

### Binding arguments

If the same arguments will be used over-and-over, it can be convenient to bind them to the potential. 
Both the atoms and the parameters can be bound this way. If we choose to do this, we run like so

```python
pot.bind_atoms(atoms)
pot.bind_args(parameters)
pot(coords)
```

## Running a Test

Potentials can also be run using a test config file, the parameters in this one are

```python
config = dict(
    atoms= [...], # atom spec
    coordinates = [
        ... # list of coordinate
    ],
    parameters=dict(...), # parameters (experimental support for kwargs)
    walkers_per_core=..., # when testing with MPI/threading, how many configurations to put on each core
    steps_per_propagation=..., # when testing with MPI/threading, how many steps to propagate the configurations forward
    random_seed=..., # when testing with MPI/threading, the random seed for the displacement, for reproducibility
)
```

Then when we call this, we use

```shell
rynlib [-n MPI_JOBS] pot test[-mpi] NAME --input=</container/path/to/test.py>
```



## Compiling a Potential

The hardest part of working with potentials in RynLib is figuring out how to get them to compile. 
I've built out tooling to make this process _easier_, but I don't have a way to make it automatic (and such a thing literally cannot exist).

To help make this easier, I've detailed the many ways a potential can be compiled. I recommend initially skipping this section and going to the discussion of the automatic wrapper, since that should serve for 90% of cases.


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
* `fortran_potential` - a convenience flag that let's the templator know that everything should be set up so that Fortran can work with the data

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

The second subtlety has everything to do with C++ and to explain it I think it will be easiest to describe the full possible argument spec.

Any given argument has four parameters (and if given as a tuple this is how they should be passed)

* `name` -- pretty simply the name of the argument that will go into the code, this is the least important argument except for four special names `coords`, `raw_coords`, `atoms`, and `energy`; these are effectively reserved
* `dtype` -- the type of the argument; for most simple arguments, this is just the _string_ form of the python type. If the argument will be passed in as a parameter it _must_ be either a `float`, `int`, or `bool`.
* `ref` -- whether the argument should be _passed by reference_ or not; this is the fundamental subtlety mentioned earlier. In C/C++ arguments can be passed by _value_ (in which case they are copied) or passed by _reference_ (in which case the underlying memory is passed). Python is entirely pass-by-reference, C++ defaults to pass-by-value. Fortran, however, expects everything to be passed by reference.
* `extra` -- whether this argument should be passed from the python side or will be defined in the `shim_script`; most of the time this parameter doesn't need to be filled out, but it doesn't necessarily hurt to fill it out.

These can either be passed as a `tuple` (in this order), or as a `dict`. The arguments specified will also be used by `Potential` to validate any calls made.

Here is an example of a more complicated setup used to compile the `TTM2.1-F` potential

```python
config = dict(
    wrap_potential=True,
    function_name='__ttm2f_mod_MOD_ttm2f',
    shim_script="double derivs[nwaters*3*3]; // allocate space for the derivatives",
    arguments=(
        ('nwaters', 'int'),
        dict(name='raw_coords', dtype="FlatCoordinates"),
        dict(name='derivs', dtype="double*", ref=False, extra=False),
        dict(name='energy', dtype="double", ref=True, extra=False),
        ('imodel', 'int')
    ),
    requires_make=True,
    fortran_potential=True,
    transpose_call=False
)
```

We see here how the `raw_coords` argument can be used (it will always have the type `FlatCoordinates`, which is an alias for `double*`). 

Because of the way the potential is set up, we also have an argument that has to be defined in the `shim_script`, which is

```c++
double derivs[nwaters*3*3]; // allocate space for the derivatives
```

this provides a place for Fortran to write the derivatives to.

The function call itself is into a function called `__ttm2f_mod_MOD_ttm2f`, which is the name Fortran gives to the function `ttm2f` which lives in the Fortran module `ttm2f_mod`.

Since this is labeled as a `fortran_potential`, the `nwaters` and `imodel` arguments actually end up being passed by reference (the `ref` gets inserted automatically). But because of the way the function is defined on the Fortran side, both C++ and Fortran have the same ordering for the memory, so we also need to specify that `transpose_call=False` (this is an argument that gets fed to the caller).

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

None of this requires much thought, so I've provided some helpful boilerplate [here](https://github.com/McCoyGroup/RynLib/tree/master/RynUtils/C%2B%2B%20Common/Boilerplate). There are a number of places where you will need to Find/Replace stuff, though.

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/RynLib/Potentials.md)