## <a id="McUtils.Plots.Interactive.EventHandler">EventHandler</a>


```python
Event: type
```
<a id="McUtils.Plots.Interactive.EventHandler.__init__">&nbsp;</a>
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

<a id="McUtils.Plots.Interactive.EventHandler.bind">&nbsp;</a>
```python
bind(self, **handlers): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ButtonPressedEvent">&nbsp;</a>
```python
ButtonPressedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ButtonReleasedEvent">&nbsp;</a>
```python
ButtonReleasedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.DrawEvent">&nbsp;</a>
```python
DrawEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.KeyPressedEvent">&nbsp;</a>
```python
KeyPressedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.KeyReleasedEvent">&nbsp;</a>
```python
KeyReleasedEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.MoveEvent">&nbsp;</a>
```python
MoveEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.SelectEvent">&nbsp;</a>
```python
SelectEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.ScrollEvent">&nbsp;</a>
```python
ScrollEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.FigureEnterEvent">&nbsp;</a>
```python
FigureEnterEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.FigureLeaveEvent">&nbsp;</a>
```python
FigureLeaveEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.AxesEnterEvent">&nbsp;</a>
```python
AxesEnterEvent(self, handler, **kw): 
```

<a id="McUtils.Plots.Interactive.EventHandler.AxesLeaveEvent">&nbsp;</a>
```python
AxesLeaveEvent(self, handler, **kw): 
```

