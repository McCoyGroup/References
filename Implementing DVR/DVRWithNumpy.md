<a id="numpy1ddvr" class="Section" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

# NumPy 1D DVR

We'll take the 1D DVR done in  [Colbert and Miller DVR](Colbert%20and%20Miller.html) but make it  *much* more efficient by using NumPy

<a id="grid" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Grid

We discretize as before, but use NumPy functions for do this more efficiently

```python
'''Colbert and Miller DVR on the [-inf, inf] domain using NumPy'''
import numpy as np

def dvr_grid(domain=(-5, 5), divs=10, **kw):
    '''Calculates the grid'''

    return np.linspace(*domain, divs)
```

<a id="kineticenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Kinetic Energy

The kinetic energy is constant along bands, so we can use this property to fill out our matrix more quickly.

```python
def kinetic_energy(grid, m=1, hb=1, **kw):
    '''Computes the kinetic energy for the grid'''

    dx=grid[1]-grid[0] # recomputed here simply to decouple the calling from dvr_grid
    divs=len(grid)
    ke=np.empty((divs, divs))

    coeff=(hb**2)/(2*m*(dx**2))
    # compute the band values for the first row
    b_val_0 = coeff*(math.pi**2)/3
    col_rng = np.arange(1, divs+1) # the column indices -- also what will be used for computing the off diagonal bands
    row_rng = np.arange(0, divs) # the row indices -- computed once and sliced
    b_vals = coeff * ((-1)**col_rng) * 2 / (col_rng**2)

    for i in range(divs):
        if i == 0:
            np.fill_diagonal(ke, b_val_0)
        else:
            col_inds = col_rng[i-1:-1]#+(i-1)
            row_inds = row_rng[:-i]
            ke[row_inds, col_inds] = b_vals[i-1]
            ke[col_inds, row_inds] = b_vals[i-1]

    return ke
```

<a id="potentialenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Potential Energy

Here, we'll assume  `pot` has been written in order to take advantage of NumPy's vectorized operations and hence should be called with our entire grid fed in.

```python
def dvr_pe(grid, pot=None):
 '''Computes the potential energy from the gridpoints'''

 return np.diag(pot(grid))
```

<a id="wavefunctions" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

### Wavefunctions

This already used NumPy so we won't change anything here.

```python
def dvr_wfns(ke, pe):
 '''Computes the wavefunctions'''

 return np.linalg.eig(ke+pe)
```

<a id="alltogether" class="Subsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

## All Together

```python
'''Colbert and Miller DVR on the [-inf, inf] domain using NumPy'''
import numpy as np

def dvr_grid(domain=(-5, 5), divs=10, **kw):
    '''Calculates the grid'''

    return np.linspace(*domain, divs)

def kinetic_energy(grid, m=1, hb=1, **kw):
    '''Computes the kinetic energy for the grid'''

    dx=grid[1]-grid[0] # recomputed here simply to decouple the calling from dvr_grid
    divs=len(grid)
    ke=np.empty((divs, divs))

    coeff=(hb**2)/(2*m*(dx**2))
    # compute the band values for the first row
    b_val_0 = coeff*(math.pi**2)/3
    col_rng = np.arange(1, divs+1) # the column indices -- also what will be used for computing the off diagonal bands
    row_rng = np.arange(0, divs) # the row indices -- computed once and sliced
    b_vals = coeff * ((-1)**col_rng) * 2 / (col_rng**2)

    for i in range(divs):
        if i == 0:
            np.fill_diagonal(ke, b_val_0)
        else:
            col_inds = col_rng[i-1:-1]#+(i-1)
            row_inds = row_rng[:-i]
            ke[row_inds, col_inds] = b_vals[i-1]
            ke[col_inds, row_inds] = b_vals[i-1]

    return ke

def dvr_pe(grid, pot=None):
 '''Computes the potential energy from the gridpoints'''

 return np.diag(pot(grid))

def dvr_wfns(ke, pe):
 '''Computes the wavefunctions'''

 return np.linalg.eig(ke+pe)

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
