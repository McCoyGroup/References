<a id=McUtils.Zachary.FiniteDifferenceFunction.finite_difference>&nbsp;</a>
```python
finite_difference(grid, values, order, accuracy=4, stencil=None, end_point_precision=4, axis=None, gridtype='regular', **kw): 
```
Computes a finite difference derivative for the values on the grid
- `grid`: `np.ndarray`
    >the grid of points for which the vlaues lie on
- `values`: `np.ndarray`
    >the values on the grid
- `order`: `int | list[int]`
    >order of the derivative to compute
- `stencil`: `int | list[int]`
    >number of points to use in the stencil
- `accuracy`: `Any`
    >No description...
- `end_point_precision`: `Any`
    >No description...
- `gridtype`: `str`
    >'regular' or 'irregular' specifying grid type
- `:returns`: `_`
    >No description...

