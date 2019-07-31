## <a id="McUtils.Plots.Plots.Plot">Plot</a>


### Properties and Methods
<a id="McUtils.Plots.Plots.Plot.__init__">&nbsp;</a>
```python
__init__(self, *params, method='plot', figure=None, axes=None, subplot_kw=None, plot_style=None, colorbar=None, **opts): 
```
Creates a 1D plot on 2D axes
- `params`: `Any`
    >_empty_ or _x_, _y_ arrays or _function_, _xrange_
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

<a id="McUtils.Plots.Plots.Plot.plot">&nbsp;</a>
```python
plot(self, func, xrange, **plot_style): 
```

<a id="McUtils.Plots.Plots.Plot.add_colorbar">&nbsp;</a>
```python
add_colorbar(self, **kw): 
```

### Examples
