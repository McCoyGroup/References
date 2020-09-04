## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.IrregularGridFiniteDifference">IrregularGridFiniteDifference</a>
Defines a finite difference over an irregular grid

### Properties and Methods
```python
finite_difference_data: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.IrregularGridFiniteDifference.__init__">&nbsp;</a>
```python
__init__(self, grid, order, stencil=None, accuracy=2, end_point_accuracy=2, **kw): 
```

- `grid`: `np.ndarray`
    >the grid to get the weights from
- `order`: `int`
    >the order of the derivative to take
- `stencil`: `int | None`
    >the number of stencil points to add
- `accuracy`: `int | None`
    >the approximate accuracy to target with the method
- `end_point_accuracy`: `int | None`
    >the extra number of stencil points to add to the end points
- `kw`: `Any`
    >options passed through to the `FiniteDifferenceMatrix`

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.IrregularGridFiniteDifference.get_grid_slices">&nbsp;</a>
```python
get_grid_slices(grid, stencil): 
```

- `grid`: `Any`
    >No description...
- `stencil`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.IrregularGridFiniteDifference.get_weights">&nbsp;</a>
```python
get_weights(m, z, x): 
```
Extracts the grid weights for an unevenly spaced grid based off of the algorithm outlined by
        Fronberger in https://pdfs.semanticscholar.org/8bf5/912bde884f6bd4cfb4991ba3d077cace94c0.pdf
- `m`: `Any`
    >highest derivative order
- `z`: `Any`
    >center of the derivatives
- `X`: `Any`
    >grid of points

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/IrregularGridFiniteDifference.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/IrregularGridFiniteDifference.md)