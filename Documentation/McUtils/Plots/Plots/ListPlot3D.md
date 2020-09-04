## <a id="McUtils.Plots.Plots.ListPlot3D">ListPlot3D</a>
Convenience 3D plotting class that handles the interpolation first

### Properties and Methods
<a id="McUtils.Plots.Plots.ListPlot3D.__init__">&nbsp;</a>
```python
__init__(self, *params, plot_style=None, method='contour', colorbar=None, figure=None, axes=None, subplot_kw=None, interpolate=True, **opts): 
```

- `params`: `Any`
    >either _empty_ or and array of (_x_, _y_, _z_) points
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
- `interpolate`: `bool`
    >whether to interpolate the data or not
- `opts`: `Any`
    >options to be fed in when initializing the Graphics

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Plots/ListPlot3D.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Plots/ListPlot3D.md)