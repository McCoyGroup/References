## <a id="McUtils.Plots.Graphics.Graphics">Graphics</a>
A mini wrapper to matplotlib.pyplot to create a unified interface I know how to work with

### Properties and Methods
```python
default_style: dict
plot_label: property
plot_legend: property
axes_labels: property
frame: property
plot_range: property
ticks: property
ticks_style: property
scale: property
aspect_ratio: property
image_size: property
padding: property
padding_left: property
padding_right: property
padding_top: property
padding_bottom: property
spacings: property
background: property
colorbar: property
```
<a id="McUtils.Plots.Graphics.Graphics.set_options">&nbsp;</a>
```python
set_options(self, axes_labels=None, plot_label=None, plot_range=None, plot_legend=None, frame=None, ticks=None, scale=None, padding=None, spacings=None, ticks_style=None, image_size=None, aspect_ratio=None, background=None, colorbar=None, prolog=None, epilog=None, **parent_opts): 
```

### Examples
The `Graphics` object is a simple interface to the [matplotlib.figure.Figure
](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) class. 
This is bound to the `figure` attribute of the object.

```python
from McUtils.Plots import *

g = Graphics()
type(g.figure)

# Out: matplotlib.figure.Figure
```

Each `Graphics` object also binds an [matplotlib.axes.Axes](https://matplotlib.org/3.1.1/api/axes_api.html#the-axes-class) object.
Because of this, the framework is set up so that multiple `Graphics` objects can
 use the same underlying `figure`:
 
 ```python
g = Graphics()
f = Graphics(figure=g)
g.figure is f.figure

# Out: True
```

Usually one won't use `Graphics` on its own, but will instead use on of the
other plotting functions, such as `Plot` or `ContourPlot` to create a
`Graphics` object.

___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Graphics/Graphics.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Graphics/Graphics.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Graphics.py?message=Update%20Docs)