# Examples

One of the best ways to learn how to do new things is to look at examples of how _other_ people did them.
To that effect, we've included little examples of how you can do stuff with NumPy, both in a straightforward way and in an optimized way.
To quantify the effects of these optimization, we'll use the `Timer` object we discussed in the [Getting Started guide](../GettingStarted/AnotherClassExample.md).


### Filling a Matrix

We're going to fill a `10x10` matrix with numbers from `0...99`.

#### Straightforward Way

We can just loop through and provide a number for each position
```python
import numpy as np
mat = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        mat[i, j] = i*10 + j
```

#### Optimized Way

This can be done much more easily using `np.arange` and `np.reshape`
```python
import numpy as np
mat = np.reshape(np.arange(100), (10, 10))
```

#### Timing Comparison

At small sizes, both are fast

```python
import numpy as np
with Timer("Straightforward Way"):
    mat = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            mat[i, j] = i * 10 + j

with Timer("Optimized Way"):
    mat = np.reshape(np.arange(100), (10, 10))
## Out:
# Straightforward Way: took 7e-05s
# Optimized Way: took 4e-05s
```

as we scale up the performance difference becomes significant

```python
import numpy as np
with Timer("Straightforward Way"):
    mat = np.zeros((1000, 1000))
    for i in range(1000):
        for j in range(1000):
            mat[i, j] = i * 1000 + j

with Timer("Optimized Way"):
    mat = np.reshape(np.arange(1000*1000), (1000, 1000))
## Out:
# Straightforward Way: took 0.42455s
# Optimized Way: took 0.00453s
```

we're two orders of magnitude faster if we avoid the loop

### <Your Example Here>

## Contributing

For now, we're just collecting a list of examples. Once we have enough we'll impose some structure on them. Feel free to edit this and add at your leisure, and later we'll add some jump links to the top of the page once the scrolling gets to be too much.

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/Examples.md)