## <a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface">BaseSurface</a>
Surface base class which can be subclassed for relevant cases

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, data, dimension): 
```

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.evaluate" class="docs-object-method">&nbsp;</a>
```python
evaluate(self, points, **kwargs): 
```
Evaluates the function at the points based off of "data"
- `points`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, gridpoints, **kwargs): 
```

- `gridpoints`: `np.ndarray`
    >No description...
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.minimize" class="docs-object-method">&nbsp;</a>
```python
minimize(self, initial_guess, function_options=None, **opts): 
```
Just calls into `scipy.optimize.minimize` as the default implementation
- `initial_guess`: `np.ndarray`
    >starting position for the minimzation
- `function_options`: `dict | None`
    >No description...
- `opts`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/BaseSurface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/BaseSurface.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Surfaces/BaseSurface/BaseSurface.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Surfaces/BaseSurface/BaseSurface.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/BaseSurface.py?message=Update%20Docs)