Regular `matplotlib` plotting syntax works:

```python
import numpy as np
from McUtils.Plots import *

grid = np.linspace(0, 2*np.pi, 100)
plot = Plot(grid, np.sin(grid))
plot.show()
```

You can also set a background / axes labels / other options

```python
plot = Plot(grid, np.sin(grid),
    axes_labels = ['x', "sin(x)"],
    background = "red"
    )
```

It's also possible to let `Plot` pick the number of plot points for you:

```python
plot = Plot(lambda x: np.sin(15*x), [0, 2*np.pi])
```

Any valid option to [axes.plot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.plot.html) may also be passed to `Plot`.