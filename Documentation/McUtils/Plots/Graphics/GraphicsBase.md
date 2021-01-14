## <a id="McUtils.Plots.Graphics.GraphicsBase">GraphicsBase</a>
The base class for all things Graphics
Defines the common parts of the interface with some calling into matplotlib

### Properties and Methods
```python
opt_keys: set
```
<a id="McUtils.Plots.Graphics.GraphicsBase.__init__" class="docs-object-method">&nbsp;</a>
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

<a id="McUtils.Plots.Graphics.GraphicsBase.event_handlers" class="docs-object-method">&nbsp;</a>
```python
@property
event_handlers(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.animated" class="docs-object-method">&nbsp;</a>
```python
@property
animated(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.bind_events" class="docs-object-method">&nbsp;</a>
```python
bind_events(self, *handlers, **events): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.create_animation" class="docs-object-method">&nbsp;</a>
```python
create_animation(self, *args, **opts): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.set_options" class="docs-object-method">&nbsp;</a>
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

<a id="McUtils.Plots.Graphics.GraphicsBase.prolog" class="docs-object-method">&nbsp;</a>
```python
@property
prolog(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.epilog" class="docs-object-method">&nbsp;</a>
```python
@property
epilog(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.__getattr__" class="docs-object-method">&nbsp;</a>
```python
__getattr__(self, item): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.copy_axes" class="docs-object-method">&nbsp;</a>
```python
copy_axes(self): 
```
Copies the axes object
- `:returns`: `matplotlib.axes.Axes`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.refresh" class="docs-object-method">&nbsp;</a>
```python
refresh(self): 
```
Refreshes the axes
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.opts" class="docs-object-method">&nbsp;</a>
```python
@property
opts(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.copy" class="docs-object-method">&nbsp;</a>
```python
copy(self): 
```
Creates a copy of the object with new axes and a new figure
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.prep_show" class="docs-object-method">&nbsp;</a>
```python
prep_show(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.show" class="docs-object-method">&nbsp;</a>
```python
show(self, reshow=True): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.close" class="docs-object-method">&nbsp;</a>
```python
close(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.clear" class="docs-object-method">&nbsp;</a>
```python
clear(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.savefig" class="docs-object-method">&nbsp;</a>
```python
savefig(self, where, format='png', **kw): 
```
Saves the image to file
- `where`: `Any`
    >No description...
- `format`: `Any`
    >No description...
- `kw`: `Any`
    >No description...
- `:returns`: `str`
    >file it was saved to (I think...?)

<a id="McUtils.Plots.Graphics.GraphicsBase.to_png" class="docs-object-method">&nbsp;</a>
```python
to_png(self): 
```
Used by Jupyter and friends to make a version of the image that they can display, hence the extra 'tight_layout' call
- `:returns`: `_`
    >No description...

<a id="McUtils.Plots.Graphics.GraphicsBase.add_colorbar" class="docs-object-method">&nbsp;</a>
```python
add_colorbar(self, graphics=None, norm=None, cmap=None, size=(20, 200), tick_padding=40, **kw): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Graphics/GraphicsBase.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Graphics/GraphicsBase.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Plots/Graphics/GraphicsBase.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Plots/Graphics/GraphicsBase.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Graphics.py?message=Update%20Docs)