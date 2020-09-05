## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix">FiniteDifferenceMatrix</a>
Defines a matrix that can be applied to a regular grid of values to take a finite difference

### Properties and Methods
```python
weights: property
order: property
npts: property
mesh_spacing: property
only_core: property
only_center: property
mode: property
dtype: property
matrix: property
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.__init__">&nbsp;</a>
```python
__init__(self, finite_difference_data, npts=None, mesh_spacing=None, only_core=False, only_center=False, mode='sparse', dtype='float64'): 
```

- `finite_difference_data`: `FiniteDifferenceData`
    >No description...
- `npts`: `Any`
    >No description...
- `mesh_spacing`: `Any`
    >No description...
- `only_core`: `Any`
    >No description...
- `only_center`: `Any`
    >No description...
- `mode`: `Any`
    >No description...

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.fd_matrix">&nbsp;</a>
```python
fd_matrix(self): 
```
Builds a 1D finite difference matrix for a set of boundary weights, central weights, and num of points
        Will look like:
            b1 b2 b3 ...
            w1 w2 w3 ...
            0  w1 w2 w3 ...
            0  0  w1 w2 w3 ...
                 ...
                 ...
                 ...
                    .... b3 b2 b1
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)