## <a id="McUtils.Plots.Plots.Plot">Plot</a>
The base plotting class to interface into matplotlib or (someday) VTK or another backend
    Builds off of the Graphics system to make a unified and convenient interface to generating plots

### Properties and Methods
```python
data: property
plot_style: property
```
<a id="McUtils.Plots.Plots.Plot.__init__">&nbsp;</a>
```python
__init__(self, *params, method='plot', figure=None, axes=None, subplot_kw=None, plot_style=None, theme=None, **opts): 
```

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
plot(self, *params, **plot_style): 
```

<a id="McUtils.Plots.Plots.Plot.clear">&nbsp;</a>
```python
clear(self): 
```

<a id="McUtils.Plots.Plots.Plot.restyle">&nbsp;</a>
```python
restyle(self, **plot_style): 
```

<a id="McUtils.Plots.Plots.Plot.add_colorbar">&nbsp;</a>
```python
add_colorbar(self, graphics=None, norm=None, **kw): 
```

### Examples
Regular `matplotlib` plotting syntax works:

```python
import numpy as np
from McUtils.Plots import *

grid = np.linspace(0, 2*np.pi, 100)
plot = Plot(grid, np.sin(grid))
plot.show()
```

You can also set a background / axes labels / other options

```python
plot = Plot(grid, np.sin(grid),
    axes_labels = ['x', "sin(x)"],
    background = "red"
    )
```

It's also possible to let `Plot` pick the number of plot points for you:

```python
plot = Plot(lambda x: np.sin(15*x), [0, 2*np.pi])
```

Any valid option to [axes.plot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.plot.html) may also be passed to `Plot`.