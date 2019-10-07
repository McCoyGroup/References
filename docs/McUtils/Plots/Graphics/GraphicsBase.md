## <a id="McUtils.Plots.Graphics.GraphicsBase">GraphicsBase</a>
The base class for all things Graphics
    Defines the common parts of the interface with some calling into matplotlib

### Properties and Methods
```python
opt_keys: set
event_handlers: property
animated: property
modified: type
opts: property
```
<a id="McUtils.Plots.Graphics.GraphicsBase.__init__">&nbsp;</a>
```python
__init__(self, *args, figure=None, axes=None, subplot_kw=None, parent=None, **opts): 
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
set_options(self, event_handlers=None, animated=None, **opts): 
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

<a id="McUtils.Plots.Graphics.GraphicsBase.show">&nbsp;</a>
```python
show(self): 
```

<a id="McUtils.Plots.Graphics.GraphicsBase.clear">&nbsp;</a>
```python
clear(self): 
```

### Examples
