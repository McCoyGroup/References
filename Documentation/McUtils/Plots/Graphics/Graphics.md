## <a id="McUtils.Plots.Graphics.Graphics">Graphics</a>
A mini wrapper to matplotlib.pyplot to create a unified interface I know how to work with

### Properties and Methods
```python
default_style: dict
```
<a id="McUtils.Plots.Graphics.Graphics.set_options" class="docs-object-method">&nbsp;</a>
```python
set_options(self, axes_labels=None, plot_label=None, plot_range=None, plot_legend=None, frame=None, ticks=None, scale=None, padding=None, spacings=None, ticks_style=None, image_size=None, aspect_ratio=None, background=None, colorbar=None, prolog=None, epilog=None, **parent_opts): 
```

<a id="McUtils.Plots.Graphics.Graphics.plot_label" class="docs-object-method">&nbsp;</a>
```python
@property
plot_label(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.plot_legend" class="docs-object-method">&nbsp;</a>
```python
@property
plot_legend(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.axes_labels" class="docs-object-method">&nbsp;</a>
```python
@property
axes_labels(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.frame" class="docs-object-method">&nbsp;</a>
```python
@property
frame(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.plot_range" class="docs-object-method">&nbsp;</a>
```python
@property
plot_range(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.ticks" class="docs-object-method">&nbsp;</a>
```python
@property
ticks(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.ticks_style" class="docs-object-method">&nbsp;</a>
```python
@property
ticks_style(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.scale" class="docs-object-method">&nbsp;</a>
```python
@property
scale(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.aspect_ratio" class="docs-object-method">&nbsp;</a>
```python
@property
aspect_ratio(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.image_size" class="docs-object-method">&nbsp;</a>
```python
@property
image_size(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.padding" class="docs-object-method">&nbsp;</a>
```python
@property
padding(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.padding_left" class="docs-object-method">&nbsp;</a>
```python
@property
padding_left(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.padding_right" class="docs-object-method">&nbsp;</a>
```python
@property
padding_right(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.padding_top" class="docs-object-method">&nbsp;</a>
```python
@property
padding_top(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.padding_bottom" class="docs-object-method">&nbsp;</a>
```python
@property
padding_bottom(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.spacings" class="docs-object-method">&nbsp;</a>
```python
@property
spacings(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.background" class="docs-object-method">&nbsp;</a>
```python
@property
background(self): 
```

<a id="McUtils.Plots.Graphics.Graphics.colorbar" class="docs-object-method">&nbsp;</a>
```python
@property
colorbar(self): 
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

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Graphics/Graphics.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Graphics/Graphics.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Plots/Graphics/Graphics.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Plots/Graphics/Graphics.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Graphics.py?message=Update%20Docs)