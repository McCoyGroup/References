## <a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction">FiniteDifferenceFunction</a>
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
<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.__init__">&nbsp;</a>
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

<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.apply">&nbsp;</a>
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

<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.__call__">&nbsp;</a>
```python
__call__(self, vals, axes=None, mesh_spacing=None): 
```

### Examples
