## <a id="McUtils.Zachary.Interpolator.Extrapolator">Extrapolator</a>
A general purpose that takes your data and just extrapolates it.
This currently only exists in template format.
As I do more work with the Surface stuff I'm sure this will get filled out more.
One big target is to use

### Properties and Methods
<a id="McUtils.Zachary.Interpolator.Extrapolator.__init__">&nbsp;</a>
```python
__init__(self, extrapolation_function, warning=False, **opts): 
```

- `extrapolation_function`: `None | function`
    >the function to handle extrapolation off the interpolation grid
- `warning`: `bool`
    >whether to emit a message warning about extrapolation occurring
- `opts`: `Any`
    >the options to feed into the extrapolator call

<a id="McUtils.Zachary.Interpolator.Extrapolator.find_extrapolated_points">&nbsp;</a>
```python
find_extrapolated_points(self, gps, vals, extrap_value=nan): 
```
Currently super rough heuristics to determine at which points we need to extrapolate
- `gps`: `Any`
    >No description...
- `vals`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Interpolator.Extrapolator.extrap2d">&nbsp;</a>
```python
extrap2d(self, gps, vals, extrap_kind='linear'): 
```
Takes a regular grid and creates a function for interpolation/extrapolation.
        :param gps: x, y data
        :type gps: ndarray
        :param vals: z data
        :type vals: ndarray
        :param extrap_kind: type of interpolation to do ('cubic' | 'linear' | 'nearest' | ...)
        :type extrap_kind: str
        :param fillvalues: if true, outer edges are filled with last data point extending out.
         Otherwise extrapolates according to extrap_kind (default)
- `fillvalues`: `bool`
    >No description...
- `:returns`: `function`
    >pf: function fit to grid points for evaluation.

<a id="McUtils.Zachary.Interpolator.Extrapolator.apply">&nbsp;</a>
```python
apply(self, gps, vals, extrap_value=nan): 
```

<a id="McUtils.Zachary.Interpolator.Extrapolator.__call__">&nbsp;</a>
```python
__call__(self, *args, **kwargs): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Interpolator/Extrapolator.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Interpolator/Extrapolator.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Interpolator.py?message=Update%20Docs)