## <a id="McUtils.Zachary.Surfaces.BaseSurface.LinearFitSurface">LinearFitSurface</a>
A surface built off of a LinearExpansionSurface, but done by fitting.
The basis selection

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.BaseSurface.LinearFitSurface.__init__">&nbsp;</a>
```python
__init__(self, points, basis=None, order=4, dimension=None): 
```

- `points`: `np.ndarray`
    >a set of points to fit to
- `basis`: `Iterable[function] | None`
    >a basis of functions to use (defaults to power series)

<a id="McUtils.Zachary.Surfaces.BaseSurface.LinearFitSurface.evaluate">&nbsp;</a>
```python
evaluate(self, points, **kwargs): 
```

- `points`: `Any`
    >No description...
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.LinearFitSurface.minimize">&nbsp;</a>
```python
minimize(self, initial_guess=None, function_options=None, **opts): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/LinearFitSurface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/LinearFitSurface.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/BaseSurface.py?message=Update%20Docs)