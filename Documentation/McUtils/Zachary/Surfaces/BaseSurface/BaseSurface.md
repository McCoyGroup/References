## <a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface">BaseSurface</a>
Surface base class which can be subclassed for relevant cases

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.__init__">&nbsp;</a>
```python
__init__(self, data, dimension): 
```

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.evaluate">&nbsp;</a>
```python
evaluate(self, points, **kwargs): 
```
Evaluates the function at the points based off of "data"
- `points`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.__call__">&nbsp;</a>
```python
__call__(self, gridpoints, **kwargs): 
```

- `gridpoints`: `np.ndarray`
    >No description...
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.BaseSurface.minimize">&nbsp;</a>
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
