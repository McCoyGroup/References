## <a id="McUtils.Plots.Graphics.GraphicsBase">GraphicsBase</a>
The base class for all things Graphics
Defines the common parts of the interface with some calling into matplotlib

### Properties and Methods
```python
opt_keys: set
event_handlers: property
animated: property
prolog: property
epilog: property
opts: property
```
<a id="McUtils.Plots.Graphics.GraphicsBase.__init__">&nbsp;</a>
```python
__init__(self, *args, figure=None, tighten=False, axes=None, subplot_kw=None, parent=None, image_size=None, padding=None, aspect_ratio=None, non_interactive=None, mpl_backend=None, theme=None, prop_manager=<class 'McUtils.Plots.Properties.GraphicsPropertyManager'>, theme_manager=<class 'McUtils.Plots.Styling.ThemeManager'>, managed=None, **opts): 
```

- `args`: `Any`
    >No description...
- `figure`: `matplotlib.figure.Figure | None`
    >No description...
- `axes`: `matplotlib.axes.Axes | None`
    >No description...
- `subplot_kw`: `dict | None`
    >No description...
- `parent`: `GraphicsBase | None`
    >No description...
- `opts`: `Any`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.bind_events">&nbsp;</a>
```python
bind_events(self, *handlers, **events): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.create_animation">&nbsp;</a>
```python
create_animation(self, *args, **opts): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.set_options">&nbsp;</a>
```python
set_options(self, event_handlers=None, animated=None, prolog=None, epilog=None, **opts): 
```
Sets options for the plot
- `event_handlers`: `Any`
    >No description...
- `animated`: `Any`
    >No description...
- `opts`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.__getattr__">&nbsp;</a>
```python
__getattr__(self, item): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.copy_axes">&nbsp;</a>
```python
copy_axes(self): 
```
Copies the axes object
- `:returns`: `matplotlib.axes.Axes`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.refresh">&nbsp;</a>
```python
refresh(self): 
```
Refreshes the axes
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.copy">&nbsp;</a>
```python
copy(self): 
```
Creates a copy of the object with new axes and a new figure
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.prep_show">&nbsp;</a>
```python
prep_show(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.show">&nbsp;</a>
```python
show(self, reshow=True): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.clear">&nbsp;</a>
```python
clear(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.savefig">&nbsp;</a>
```python
savefig(self, where, format='png', **kw): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.to_png">&nbsp;</a>
```python
to_png(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.add_colorbar">&nbsp;</a>
```python
add_colorbar(self, graphics=None, norm=None, cmap=None, size=(20, 200), tick_padding=40, **kw): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Graphics/GraphicsBase.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Graphics/GraphicsBase.md)