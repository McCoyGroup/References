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
```python
__init__(self, *args, figure=None, axes=None, subplot_kw=None, parent=None, non_interactive=None, **opts): 
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

```python
bind_events(self, *handlers, **events): 
```

```python
create_animation(self, *args, **opts): 
```

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

```python
__getattr__(self, item): 
```

```python
copy_axes(self): 
```
Copies the axes object
- `:returns`: `matplotlib.axes.Axes`
    >No description...

```python
refresh(self): 
```
Refreshes the axes
- `:returns`: `_`
    >No description...

```python
copy(self): 
```
Creates a copy of the object with new axes and a new figure
- `:returns`: `_`
    >No description...

```python
show(self, reshow=True): 
```

```python
clear(self): 
```

```python
to_png(self): 
```

### Examples
