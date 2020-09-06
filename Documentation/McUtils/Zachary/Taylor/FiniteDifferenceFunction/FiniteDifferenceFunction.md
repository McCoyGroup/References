## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction">FiniteDifferenceFunction</a>
The FiniteDifferenceFunction encapsulates a bunch of functionality extracted from Fornberger's
Calculation of Wieghts in Finite Difference Formulas (https://epubs.siam.org/doi/pdf/10.1137/S0036144596322507)

Only applies to direct product grids, but each subgrid can be regular or irregular

### Properties and Methods
```python
regular_difference: method
from_grid: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *diffs, axes=0, contract=False): 
```
Constructs an object to take finite differences derivatives of grids of data
- `diffs`: `FiniteDifference1D`
    >A set of differences to take along successive axes in the data
- `axes`: `int | Iterable[int]`
    >The axes to take the specified differences along
- `contract`: `bool`
    >Whether to reduce the shape of the returned tensor if applicable after application

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.apply" class="docs-object-method">&nbsp;</a>
```python
apply(self, vals, axes=None, mesh_spacing=None, contract=None): 
```
Iteratively applies the stored finite difference objects to the vals
- `vals`: `np.ndarray`
    >The tensor of values to take the difference on
- `axes`: `int | Iterable[int]`
    >The axis or axes to take the differences along (defaults to `self.axes`)
- `:returns`: `np.ndarray`
    >The tensor of derivatives

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, vals, axes=None, mesh_spacing=None): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

- `:returns`: `tuple[int]`
    >the order of the derivative requested

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

- `:returns`: `tuple[np.array[float]]`
    >the weights for the specified stencil

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.widths" class="docs-object-method">&nbsp;</a>
```python
@property
widths(self): 
```

- `:returns`: `tuple[(int, int)]`
    >the number of points in each dimension, left and right, for the specified stencil

### Examples
## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction">FiniteDifferenceFunction</a>
The FiniteDifferenceFunction encapsulates a bunch of functionality extracted from Fornberger's
Calculation of Wieghts in Finite Difference Formulas (https://epubs.siam.org/doi/pdf/10.1137/S0036144596322507)

Only applies to direct product grids, but each subgrid can be regular or irregular

### Properties and Methods
```python
regular_difference: method
from_grid: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *diffs, axes=0, contract=False): 
```
Constructs an object to take finite differences derivatives of grids of data
- `diffs`: `FiniteDifference1D`
    >A set of differences to take along successive axes in the data
- `axes`: `int | Iterable[int]`
    >The axes to take the specified differences along
- `contract`: `bool`
    >Whether to reduce the shape of the returned tensor if applicable after application

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.apply" class="docs-object-method">&nbsp;</a>
```python
apply(self, vals, axes=None, mesh_spacing=None, contract=None): 
```
Iteratively applies the stored finite difference objects to the vals
- `vals`: `np.ndarray`
    >The tensor of values to take the difference on
- `axes`: `int | Iterable[int]`
    >The axis or axes to take the differences along (defaults to `self.axes`)
- `:returns`: `np.ndarray`
    >The tensor of derivatives

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, vals, axes=None, mesh_spacing=None): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

- `:returns`: `tuple[int]`
    >the order of the derivative requested

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

- `:returns`: `tuple[np.array[float]]`
    >the weights for the specified stencil

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.widths" class="docs-object-method">&nbsp;</a>
```python
@property
widths(self): 
```

- `:returns`: `tuple[(int, int)]`
    >the number of points in each dimension, left and right, for the specified stencil

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)

___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)