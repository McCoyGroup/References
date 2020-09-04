## <a id="McUtils.Zachary.FittableModels.LinearFitBasis">LinearFitBasis</a>
Provides a container to build bases of functions for fitting.
    Asks for a generator for each dimension, which is just a function that takes an integer and returns a basis function at that order.
    Product functions are taken up to some max order

### Properties and Methods
```python
functions: property
names: property
order: property
```
<a id="McUtils.Zachary.FittableModels.LinearFitBasis.__init__">&nbsp;</a>
```python
__init__(self, *generators, order=3): 
```

- `generators`: `Iterable[function]`
    >the generating functions for the bases in each dimenion
- `order`: `int`
    >the maximum order for the basis functions (currently turning off coupling isn't possible, but that could come)

<a id="McUtils.Zachary.FittableModels.LinearFitBasis.construct_basis">&nbsp;</a>
```python
construct_basis(self): 
```

<a id="McUtils.Zachary.FittableModels.LinearFitBasis.<lambda>">&nbsp;</a>
```python
<lambda>(x, k): 
```

<a id="McUtils.Zachary.FittableModels.LinearFitBasis.<lambda>">&nbsp;</a>
```python
<lambda>(x, n): 
```

### Examples
