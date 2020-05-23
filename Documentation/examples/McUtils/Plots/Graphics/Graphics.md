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