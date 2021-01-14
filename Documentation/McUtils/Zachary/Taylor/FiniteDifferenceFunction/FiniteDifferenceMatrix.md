## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix">FiniteDifferenceMatrix</a>
Defines a matrix that can be applied to a regular grid of values to take a finite difference

### Properties and Methods
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.__init__" class="docs-object-method">&nbsp;</a>
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

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.npts" class="docs-object-method">&nbsp;</a>
```python
@property
npts(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.mesh_spacing" class="docs-object-method">&nbsp;</a>
```python
@property
mesh_spacing(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.only_core" class="docs-object-method">&nbsp;</a>
```python
@property
only_core(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.only_center" class="docs-object-method">&nbsp;</a>
```python
@property
only_center(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.mode" class="docs-object-method">&nbsp;</a>
```python
@property
mode(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.dtype" class="docs-object-method">&nbsp;</a>
```python
@property
dtype(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.matrix" class="docs-object-method">&nbsp;</a>
```python
@property
matrix(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.fd_matrix" class="docs-object-method">&nbsp;</a>
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
- `:returns`: `np.ndarray | sp.csr_matrix`
    >fd_mat

### Examples
## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix">FiniteDifferenceMatrix</a>
Defines a matrix that can be applied to a regular grid of values to take a finite difference

### Properties and Methods
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.__init__" class="docs-object-method">&nbsp;</a>
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

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.npts" class="docs-object-method">&nbsp;</a>
```python
@property
npts(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.mesh_spacing" class="docs-object-method">&nbsp;</a>
```python
@property
mesh_spacing(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.only_core" class="docs-object-method">&nbsp;</a>
```python
@property
only_core(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.only_center" class="docs-object-method">&nbsp;</a>
```python
@property
only_center(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.mode" class="docs-object-method">&nbsp;</a>
```python
@property
mode(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.dtype" class="docs-object-method">&nbsp;</a>
```python
@property
dtype(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.matrix" class="docs-object-method">&nbsp;</a>
```python
@property
matrix(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceMatrix.fd_matrix" class="docs-object-method">&nbsp;</a>
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
- `:returns`: `np.ndarray | sp.csr_matrix`
    >fd_mat

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)

___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)