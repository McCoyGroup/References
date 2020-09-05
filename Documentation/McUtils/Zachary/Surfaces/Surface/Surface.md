## <a id="McUtils.Zachary.Surfaces.Surface.Surface">Surface</a>
This actually isn't a concrete implementation of BaseSurface.
Instead it's a class that _dispatches_ to an implementation of BaseSurface to do its core evaluations (plus it does shape checking)

### Properties and Methods
```python
detect_base: method
```
<a id="McUtils.Zachary.Surfaces.Surface.Surface.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, data, dimension=None, base=None, **metadata): 
```

- `data`: `Any`
    >No description...
- `dimension`: `Any`
    >No description...
- `base`: `None | Type[BaseSurface]`
    >No description...
- `metadata`: `Any`
    >No description...

<a id="McUtils.Zachary.Surfaces.Surface.Surface.minimize" class="docs-object-method">&nbsp;</a>
```python
minimize(self, initial_guess=None, function_options=None, **opts): 
```
Provides a uniform interface for minimization, basically just dispatching to the BaseSurface implementation if provided
- `initial_guess`: `np.ndarray | None`
    >initial starting point for the minimization
- `function_options`: `None | dict`
    >No description...
- `opts`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.Surface.Surface.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, gridpoints, **kwargs): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces/Surface/Surface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces/Surface/Surface.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/Surface.py?message=Update%20Docs)