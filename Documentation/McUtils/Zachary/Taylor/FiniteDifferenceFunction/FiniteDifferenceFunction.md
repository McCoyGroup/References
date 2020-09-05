## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction">FiniteDifferenceFunction</a>
The FiniteDifferenceFunction encapsulates a bunch of functionality extracted from Fornberger's
Calculation of Wieghts in Finite Difference Formulas (https://epubs.siam.org/doi/pdf/10.1137/S0036144596322507)

Only applies to direct product grids, but each subgrid can be regular or irregular

### Properties and Methods
```python
order: property
weights: property
widths: property
regular_difference: method
from_grid: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__init__">&nbsp;</a>
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

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.apply">&nbsp;</a>
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

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifferenceFunction.__call__">&nbsp;</a>
```python
__call__(self, vals, axes=None, mesh_spacing=None): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)