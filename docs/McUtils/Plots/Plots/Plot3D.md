## <a id="McUtils.Plots.Plots.Plot3D">Plot3D</a>
A base class for 3D plots

<a id="McUtils.Plots.Plots.Plot3D.__init__">&nbsp;</a>
```python
__init__(self, func, xrange, yrange, plot_style=None, method='plot_surface', colorbar=None, figure=None, axes=None, subplot_kw=None, **opts): 
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

<a id="McUtils.Plots.Plots.Plot3D.plot">&nbsp;</a>
```python
plot(self, func, xrange, yrange, **plot_style): 
```

<a id="McUtils.Plots.Plots.Plot3D.add_colorbar">&nbsp;</a>
```python
add_colorbar(self, **kw): 
```

