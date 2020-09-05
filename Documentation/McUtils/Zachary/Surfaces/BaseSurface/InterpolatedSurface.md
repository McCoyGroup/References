## <a id="McUtils.Zachary.Surfaces.BaseSurface.InterpolatedSurface">InterpolatedSurface</a>
A surface that operates by doing an interpolation of passed mesh data

### Properties and Methods
<a id="McUtils.Zachary.Surfaces.BaseSurface.InterpolatedSurface.__init__">&nbsp;</a>
```python
__init__(self, xdata, ydata=None, dimension=None, **opts): 
```

<a id="McUtils.Zachary.Surfaces.BaseSurface.InterpolatedSurface.evaluate">&nbsp;</a>
```python
evaluate(self, points, **kwargs): 
```
We delegate all the dirty work to the Interpolator so hopefully that's working...
- `points`: `Any`
    >No description...
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Surfaces.BaseSurface.InterpolatedSurface.minimize">&nbsp;</a>
```python
minimize(self, initial_guess=None, function_options=None, **opts): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/InterpolatedSurface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces/BaseSurface/InterpolatedSurface.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/BaseSurface.py?message=Update%20Docs)