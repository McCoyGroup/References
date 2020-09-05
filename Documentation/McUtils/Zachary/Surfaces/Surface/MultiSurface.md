## <a id="McUtils.Zachary.Surfaces.Surface.MultiSurface">MultiSurface</a>
A _reallly_ simple extension to the Surface infrastructure to handle vector valued functions,
assuming each vector value corresponds to a different Surfaces

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.Surface.MultiSurface.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *surfs): 
```

- `surfs`: `Iterable[Surface]`
    >a set of Surface objects to use when evaluating

<a id="McUtils.Zachary.Surfaces.Surface.MultiSurface.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, gridpoints, **kwargs): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces/Surface/MultiSurface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces/Surface/MultiSurface.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/Surface.py?message=Update%20Docs)