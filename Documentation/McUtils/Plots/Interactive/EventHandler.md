## <a id="McUtils.Plots.Interactive.EventHandler">EventHandler</a>


### Properties and Methods
```python
Event: type
```
<a id="McUtils.Plots.Interactive.EventHandler.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, figure, on_click=None, on_release=None, on_draw=None, on_key_press=None, on_key_release=None, on_move=None, on_select=None, on_resize=None, on_scroll=None, on_figure_entered=None, on_figure_left=None, on_axes_entered=None, on_axes_left=None): 
```
Creates an EventHandler on a Figure that handles most interactivity stuff
- `figure`: `GraphicsBase`
    >No description...
- `on_click`: `Any`
    >No description...
- `on_release`: `Any`
    >No description...
- `on_draw`: `Any`
    >No description...
- `on_key_press`: `Any`
    >No description...
- `on_key_release`: `Any`
    >No description...
- `on_move`: `Any`
    >No description...
- `on_select`: `Any`
    >No description...
- `on_resize`: `Any`
    >No description...
- `on_scroll`: `Any`
    >No description...
- `on_figure_entered`: `Any`
    >No description...
- `on_figure_left`: `Any`
    >No description...
- `on_axes_entered`: `Any`
    >No description...
- `on_axes_left`: `Any`
    >No description...

<a id="McUtils.Plots.Interactive.EventHandler.bind" class="docs-object-method">&nbsp;</a>
```python
bind(self, **handlers): 
```

<a id="McUtils.Plots.Interactive.EventHandler.handlers" class="docs-object-method">&nbsp;</a>
```python
@property
handlers(self): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ButtonPressedEvent" class="docs-object-method">&nbsp;</a>
```python
ButtonPressedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ButtonReleasedEvent" class="docs-object-method">&nbsp;</a>
```python
ButtonReleasedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.DrawEvent" class="docs-object-method">&nbsp;</a>
```python
DrawEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.KeyPressedEvent" class="docs-object-method">&nbsp;</a>
```python
KeyPressedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.KeyReleasedEvent" class="docs-object-method">&nbsp;</a>
```python
KeyReleasedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.MoveEvent" class="docs-object-method">&nbsp;</a>
```python
MoveEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.SelectEvent" class="docs-object-method">&nbsp;</a>
```python
SelectEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ScrollEvent" class="docs-object-method">&nbsp;</a>
```python
ScrollEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.FigureEnterEvent" class="docs-object-method">&nbsp;</a>
```python
FigureEnterEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.FigureLeaveEvent" class="docs-object-method">&nbsp;</a>
```python
FigureLeaveEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.AxesEnterEvent" class="docs-object-method">&nbsp;</a>
```python
AxesEnterEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.AxesLeaveEvent" class="docs-object-method">&nbsp;</a>
```python
AxesLeaveEvent(self, handler, **kw): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Interactive/EventHandler.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Interactive/EventHandler.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Plots/Interactive/EventHandler.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Plots/Interactive/EventHandler.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Interactive.py?message=Update%20Docs)