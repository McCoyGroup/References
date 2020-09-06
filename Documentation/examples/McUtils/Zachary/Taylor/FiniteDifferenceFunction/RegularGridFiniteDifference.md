## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.RegularGridFiniteDifference">RegularGridFiniteDifference</a>
Defines a 1D finite difference over a regular grid

### Properties and Methods
```python
finite_difference_data: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.RegularGridFiniteDifference.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, order, stencil=None, accuracy=4, end_point_accuracy=2, **kw): 
```

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

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.RegularGridFiniteDifference.get_weights" class="docs-object-method">&nbsp;</a>
```python
get_weights(m, s, n): 
```
Extracts the weights for an evenly spaced grid
- `m`: `Any`
    >No description...
- `s`: `Any`
    >No description...
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/RegularGridFiniteDifference.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/RegularGridFiniteDifference.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/RegularGridFiniteDifference.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/RegularGridFiniteDifference.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)