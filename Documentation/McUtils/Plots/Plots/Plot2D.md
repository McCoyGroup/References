## <a id="McUtils.Plots.Plots.Plot2D">Plot2D</a>
A base class for plots of 3D data but plotted on 2D axes

### Properties and Methods
```python
__init__(self, *params, plot_style=None, method='contour', colorbar=None, figure=None, axes=None, subplot_kw=None, **opts): 
```

- `params`: `Any`
    >either _empty_ or _x_, _y_, _z_ arrays or _function_, _xrange_, _yrange_
- `plot_style`: `dict | None`
    >the plot styling options to be fed into the plot method
- `method`: `str`
    >the method name as a string
- `figure`: `Graphics | None`
    >the Graphics object on which to plot (None means make a new one)
- `axes`: `None`
    >the axes on which to plot (used in constructing a Graphics, None means make a new one)
- `subplot_kw`: `dict | None`
    >the keywords to pass on when initializing the plot
- `colorbar`: `None | bool | dict`
    >whether to use a colorbar or what options to pass to the colorbar
- `opts`: `Any`
    >options to be fed in when initializing the Graphics

### Examples
