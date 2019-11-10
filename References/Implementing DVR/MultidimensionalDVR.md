<a id="multidimensionaldvr" class="Section" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

# Multidimensional DVR

Assuming one has a separable kinetic energy, DVR in n dimensions is a simple tensor extension of a 1D DVR. We'll reuse the Colbert and Miller kinetic energy and build the potential as usual.

<a id="grid" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Grid

We'll build this to take a set of 1D domains and turn them into a full n-dimensional mesh

```python
import numpy as np
import scipy.sparse as sp

def dvr_grid_1D(domain=(-5, 5), divs=10, **kw):
    '''Calculates a 1D grid'''

    return np.linspace(*domain, divs)
```

```python
def dvr_grid(domain=((-5, -5), (-5, 5)), divs=(10, 10), **kw):
 '''Creates a ND grid from 1D ones'''

 mesh = np.array(np.meshgrid(*map(cm1D.grid, domain, divs), indexing='ij'))
 for i in range(mesh.shape[0]):
     mesh = mesh.swapaxes(i, i+1) # this is clumsy but the single .transpose() call that should have worked wasn't working...

 return mesh
```

<a id="kineticenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Kinetic Energy

We'll use sparse matrix methods and tensor products to build our n-dimensional kinetic energy. First we have our 1D KE:

```python
def dvr_ke_1D(grid, m=1, hb=1):
 '''Computes the kinetic energy for the grid'''

 dx=grid[1]-grid[0] # recomputed here simply to decouple the calling from dvr_grid
 divs=len(grid)
 ke=np.empty((divs, divs))

 coeff=(hb**2)/(2*m*(dx**2))
 # compute the band values for the first row
 b_val_0 = (math.pi**2)/3
 b_vals = np.arange(1, divs) # set up the index numbers
 b_vals = ((-1)**b_vals) * 2/(b_vals**2)


 for i in range(divs):
  if i == 0:
   np.fill_diagonal(ke, b_val_0)
  else:
   np.fill_diagonal(ke[i:], b_vals[i])

 return ke
```

Then we build the n-dimensional extension off of the 1D ones:

```python
def dvr_ke(grid, m=1, hb=1):
 '''Computes n-dimensional kinetic energy for the grid'''
 from functools import reduce

 ndims = grid.shape[-1]
 try:
     iter(m); ms = m
 except TypeError:
     ms = [m]*ndims

 try:
     iter(hb); hbs = hb
 except TypeError:
     hbs = [hb]*ndims

 ndim = grid.shape[-1]
 grids = [ grid[(0, )*i + (...,) + (0, ) * (ndim-i-1) +(i,)] for i in range(ndim) ]
 kes = [ dvr_ke_1D(g, m=m, hb=hb) for g, m, hb in zip(grids, ms, hbs) ]

 kes = map(sp.csr_matrix, kes)

 def _kron_sum(a, b):
     '''Computes a Kronecker sum to build our Kronecker-Delta tensor product expression'''
     n_1 = a.shape[0]
     n_2 = b.shape[0]
     ident_1 = sp.identity(n_1)
     ident_2 = sp.identity(n_2)

     return sp.kron(a, ident_2) + sp.kron(ident_1, b)

 ke = reduce(_kron_sum, kes)
 return ke
```

<a id="potentialenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Potential Energy

Here, we'll again assume  `pot` has been written in order to take advantage of NumPy's vectorized operations, so we simply need to feed in our set of grid points:

```python
def dvr_pe(grid, pot=None):
 '''Computes the potential energy from the gridpoints'''

 from functools import reduce
    from operator import mul

    npts = reduce(mul, grid.shape[:-1], 1)
    gps = np.reshape(grid, (npts, grid.shape[-1]))
    pots = potential_function(gps)
    return sp.diags( [ pots ], [0])
```

<a id="wavefunctions" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Wavefunctions

This now needs to use sparse matrix methods for efficiency:

```python
def dvr_wfns(ke, pe, num_wfns=10):
 """Computes the wavefunctions using sparse methods"""
 import scipy.sparse.linalg as la
 return la.eigsh(hamiltonian, num_wfns, which = 'SM')
```

<a id="alltogether" class="Subsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

## All Together

```python
'''Colbert and Miller DVR in multiple dimensions'''
import numpy as np
import scipy.sparse as sp

def dvr_grid_1D(domain=(-5, 5), divs=10, **kw):
    '''Calculates a 1D grid'''

    return np.linspace(*domain, divs)

def dvr_grid(domain=((-5, -5), (-5, 5)), divs=(10, 10), **kw):
 '''Creates a ND grid from 1D ones'''

 mesh = np.array(np.meshgrid(*map(cm1D.grid, domain, divs), indexing='ij'))
 for i in range(mesh.shape[0]):
     mesh = mesh.swapaxes(i, i+1) # this is clumsy but the single .transpose() call that should have worked wasn't working...

 return mesh

def dvr_ke_1D(grid, m=1, hb=1):
 '''Computes the kinetic energy for the grid'''

 dx=grid[1]-grid[0] # recomputed here simply to decouple the calling from dvr_grid
 divs=len(grid)
 ke=np.empty((divs, divs))

 coeff=(hb**2)/(2*m*(dx**2))
 # compute the band values for the first row
 b_val_0 = (math.pi**2)/3
 b_vals = np.arange(1, divs) # set up the index numbers
 b_vals = ((-1)**b_vals) * 2/(b_vals**2)


 for i in range(divs):
  if i == 0:
   np.fill_diagonal(ke, b_val_0)
  else:
   np.fill_diagonal(ke[i:], b_vals[i])

 return ke

def dvr_ke(grid, m=1, hb=1):
 '''Computes n-dimensional kinetic energy for the grid'''
 from functools import reduce

 ndims = grid.shape[-1]
 try:
     iter(m); ms = m
 except TypeError:
     ms = [m]*ndims

 try:
     iter(hb); hbs = hb
 except TypeError:
     hbs = [hb]*ndims

 ndim = grid.shape[-1]
 grids = [ grid[(0, )*i + (...,) + (0, ) * (ndim-i-1) +(i,)] for i in range(ndim) ]
 kes = [ dvr_ke_1D(g, m=m, hb=hb) for g, m, hb in zip(grids, ms, hbs) ]

 kes = map(sp.csr_matrix, kes)

 def _kron_sum(a, b):
     '''Computes a Kronecker sum to build our Kronecker-Delta tensor product expression'''
     n_1 = a.shape[0]
     n_2 = b.shape[0]
     ident_1 = sp.identity(n_1)
     ident_2 = sp.identity(n_2)

     return sp.kron(a, ident_2) + sp.kron(ident_1, b)

 ke = reduce(_kron_sum, kes)
 return ke


def dvr_pe(grid, pot=None):
 '''Computes the potential energy from the gridpoints'''

 from functools import reduce
    from operator import mul

    npts = reduce(mul, grid.shape[:-1], 1)
    gps = np.reshape(grid, (npts, grid.shape[-1]))
    pots = potential_function(gps)
    return sp.diags( [ pots ], [0])

def dvr_wfns(ke, pe, num_wfns=10):
 """Computes the wavefunctions using sparse methods"""
 import scipy.sparse.linalg as la
 return la.eigsh(hamiltonian, num_wfns, which = 'SM')

def dvr_run(**params):
 '''Runs the entire DVR'''
 grid = dvr_grid(**params)
 ke = dvr_ke(grid, **params)
 pe = dvr_pe(grid, **params)
 wfns = dvr_wfns(ke, pe, **params)

 return wfns


if __name__=='__main__':
 ### parse sys.argv

 dvr_run(**ops)
```
