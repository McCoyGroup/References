## <a id="McUtils.Plots.Interactive.EventHandler">EventHandler</a>


### Properties and Methods
```python
handlers: property
Event: type
```
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

```python
bind(self, **handlers): 
```

```python
ButtonPressedEvent(self, handler, **kw): 
```

```python
ButtonReleasedEvent(self, handler, **kw): 
```

```python
DrawEvent(self, handler, **kw): 
```

```python
KeyPressedEvent(self, handler, **kw): 
```

```python
KeyReleasedEvent(self, handler, **kw): 
```

```python
MoveEvent(self, handler, **kw): 
```

```python
SelectEvent(self, handler, **kw): 
```

```python
ScrollEvent(self, handler, **kw): 
```

```python
FigureEnterEvent(self, handler, **kw): 
```

```python
FigureLeaveEvent(self, handler, **kw): 
```

```python
AxesEnterEvent(self, handler, **kw): 
```

```python
AxesLeaveEvent(self, handler, **kw): 
```

### Examples
