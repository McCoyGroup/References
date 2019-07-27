## <a id=McUtils.Plots.Plots.Plot2D>Plot2D</a>
A base class for plots that are 3D but plotted on 2D Graphics

<a id=McUtils.Plots.Plots.Plot2D.__init__>&nbsp;</a>
```python
__init__(self, func, xrange, yrange, plot_style=None, method='contour', colorbar=None, figure=None, axes=None, subplot_kw=None, **opts): 
```
Creates a 3D plot on 2D axes
- `func`: `Any`
    >either a func to apply or an array of x-values
- `xrange`: `Any`
    >either an xrange spec or an array of y-values
- `yrange`: `Any`
    >either a yrange spec or an array of z-values
- `method`: `str`
    >the method to be used to plot the data
- `opts`: `Any`
    >No description...

<a id=McUtils.Plots.Plots.Plot2D.plot>&nbsp;</a>
```python
plot(self, func, xrange, yrange, **plot_style): 
```

<a id=McUtils.Plots.Plots.Plot2D.add_colorbar>&nbsp;</a>
```python
add_colorbar(self, **kw): 
```

