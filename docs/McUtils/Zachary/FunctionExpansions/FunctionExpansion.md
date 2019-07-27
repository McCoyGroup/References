## <a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion">FunctionExpansion</a>
A class for handling expansions of an internal coordinate potential up to 4th order
    Uses Cartesian derivative matrices and the Cartesian <-> Internal normal mode Jacobian

```python
tensors: property
CoordinateTransforms: type
FunctionDerivatives: type
```
<a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion.__init__">&nbsp;</a>
```python
__init__(self, derivatives, transforms=None): 
```

<a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion.expand">&nbsp;</a>
```python
expand(self, coords): 
```
Returns a numerical value for the expanded coordinates
- `coords`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion.__call__">&nbsp;</a>
```python
__call__(self, coords): 
```

<a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion.get_tensor">&nbsp;</a>
```python
get_tensor(self, i): 
```

