## <a id="McUtils.Zachary.Surfaces.Surface.MultiSurface">MultiSurface</a>
A _reallly_ simple extension to the Surface infrastructure to handle vector valued functions,
    assuming each vector value corresponds to a different Surfaces

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.Surface.MultiSurface.__init__">&nbsp;</a>
```python
__init__(self, *surfs): 
```

- `surfs`: `Iterable[Surface]`
    >a set of Surface objects to use when evaluating

<a id="McUtils.Zachary.Surfaces.Surface.MultiSurface.__call__">&nbsp;</a>
```python
__call__(self, gridpoints, **kwargs): 
```

### Examples
