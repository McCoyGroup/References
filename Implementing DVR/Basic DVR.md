<a id="basic-dvr" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

# Basic DVR

A discrete variable representation is a way to solve the Schrödinger equation in a simple, grid-based way. It has four basic functions:

* Grid

* Kinetic Energy

* Potential Energy

* Wavefunctions

Of these, the only ones that will significantly vary from DVR to DVR are the grid and the kinetic energy. Everything else is pretty standardized.

A good primer on the mathematical foundations of DVR can be found  [here](http://www.pci.uni-heidelberg.de/tc/usr/mctdh/lit/NumericalMethods.pdf) . There is also a nice review paper on DVR by Light and Carrington  [here](http://light-group.uchicago.edu/dvr-rev.pdf) .

The basic motivating idea is to provide a basis that in effect discretizes the domain over which the wavefunctions and which diagonalizes the representation of the potential energy.

### Grid

DVR solves the Schrödinger equation on a grid, so the first thing we need is a function to set up the appropriate grid. To make this grid we take in a grid domain, e.g.  ```[0, 1]``` , and a number of grid points, say  ```15``` . If we were to make a script  ```basic_dvr.py```  this would look like:

```python
'''basic_dvr.py is a template DVR'''

def dvr_grid(domain, divs):
	'''Discretizes domain into divs number of point'''
	# subdivide domain
```

### Kinetic Energy

This is the complicated part in a DVR. Various strategies may be taken for creating an expression for the kinetic energy, but in the optimal case they will only have a dependence on the grid of choice. So we could add this to our script like so:

```python
def dvr_ke(grid, **params):
	'''Computes the kinetic energy for the grid (based on the chosen basis)'''
	# calculate kinetic energy based on grid and system parameters passed as dict
```

### Potential Energy

This is what makes DVR so attractive. By choosing the appropriate basis we can get a representation of the potential that is diagonal and thus depends only on the grid points. A template can look like:

```python
def dvr_pe(grid, **params):
	'''Computes the potential energy from the gridpoints'''
	# make diagonal matrix base on value of the potential at the gridpoints 
```

### Wavefunctions

In the most general case, the wavefunctions are simply the eigenvalues of the kinetic energy plus the potential energy. Optimizations can be done to take only the smallest-n eigenvalues or in higher dimensions to use sparse matrix methods, but at the base level this will always look like:

```python
def dvr_wfns(ke, pe):
	'''Computes the wavefunctions'''
	# compute eigensystem of ke+pe
```

<a id="concrete-example" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

## Concrete Example

A concrete example of this based on a DVR developed by  [Colbert and Miller](http://xbeams.chem.yale.edu/~batista/v572/ColbertMiller.pdf)  can be found  [here](Colbert and Miller.md) .