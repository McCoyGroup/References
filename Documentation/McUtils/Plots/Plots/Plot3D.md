## <a id="McUtils.Plots.Plots.Plot3D">Plot3D</a>
A base class for 3D plots

### Properties and Methods
<a id="McUtils.Plots.Plots.Plot3D.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *params, plot_style=None, method='plot_surface', colorbar=None, figure=None, axes=None, subplot_kw=None, **opts): 
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

<a id="McUtils.Plots.Plots.Plot3D.plot" class="docs-object-method">&nbsp;</a>
```python
plot(self, *params, **plot_style): 
```

<a id="McUtils.Plots.Plots.Plot3D.add_colorbar" class="docs-object-method">&nbsp;</a>
```python
add_colorbar(self, **kw): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Plots/Plot3D.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Plots/Plot3D.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Plots/Plots/Plot3D.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Plots/Plots/Plot3D.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Plots.py?message=Update%20Docs)