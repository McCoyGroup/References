## <a id="McUtils.Zachary.FunctionExpansions.FunctionExpansion">FunctionExpansion</a>
A class for handling expansions of an internal coordinate potential up to 4th order
    Uses Cartesian derivative matrices and the Cartesian <-> Internal normal mode Jacobian

### Properties and Methods
```python
tensors: property
CoordinateTransforms: type
FunctionDerivatives: type
```
```python
__init__(self, derivatives, transforms=None): 
```

```python
expand(self, coords): 
```
Returns a numerical value for the expanded coordinates
- `coords`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

```python
__call__(self, coords): 
```

```python
get_tensor(self, i): 
```

### Examples
