## <a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion">FunctionExpansion</a>
A class for handling expansions of an internal coordinate potential up to 4th order
Uses Cartesian derivative matrices and the Cartesian <-> Internal normal mode Jacobian

### Properties and Methods
```python
expand_function: method
tensors: property
CoordinateTransforms: type
FunctionDerivatives: type
```
<a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion.__init__">&nbsp;</a>
```python
__init__(self, derivatives, transforms=None, center=None, ref=0, weight_coefficients=True): 
```

- `derivatives`: `Iterable[np.ndarray | Tensor]`
    >Derivatives of the function being expanded
- `transforms`: `Iterable[np.ndarray | Tensor] | None`
    >Jacobian and higher order derivatives in the coordinates
- `center`: `np.ndarray | None`
    >the reference point for expanding aobut
- `ref`: `float | np.ndarray`
    >the reference point value for shifting the expansion
- `weight_coefficients`: `bool`
    >whether the derivative terms need to be weighted or not

<a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion.get_expansions">&nbsp;</a>
```python
get_expansions(self, coords, squeeze=True): 
```

- `coords`: `np.ndarray | CoordinateSet`
    >Coordinates to evaluate the expansion at
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion.expand">&nbsp;</a>
```python
expand(self, coords, squeeze=True): 
```
Returns a numerical value for the expanded coordinates
- `coords`: `np.ndarray`
    >No description...
- `:returns`: `float | np.ndarray`
    >No description...

<a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion.__call__">&nbsp;</a>
```python
__call__(self, coords, **kw): 
```

<a id="McUtils.Zachary.Taylor.FunctionExpansions.FunctionExpansion.get_tensor">&nbsp;</a>
```python
get_tensor(self, i): 
```
Defines the overall tensors of derivatives
- `i`: `order of derivative tensor to provide`
    >No description...
- `:returns`: `Tensor`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FunctionExpansions/FunctionExpansion.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FunctionExpansions/FunctionExpansion.md)