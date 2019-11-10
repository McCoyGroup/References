## <a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction">FiniteDifferenceFunction</a>
The FiniteDifferenceFunction encapsulates a bunch of functionality extracted from Fornberger's
    Calculation of Wieghts in Finite Difference Formulas (https://epubs.siam.org/doi/pdf/10.1137/S0036144596322507)

### Properties and Methods
```python
REGULAR_GRID: str
IRREGULAR_GRID: str
coefficients: property
gridtype: property
widths: property
order: property
function: property
RegularGridFunction: method
IrregularGridFunction: method
from_grid: method
```
<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.__init__">&nbsp;</a>
```python
__init__(self, coefficients, widths=None, order=None, gridtype=None, regularize_results=False, mesh_spacings=None, shape=None, only_core=False, only_center=False, axis=0): 
```

<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.__call__">&nbsp;</a>
```python
__call__(self, *args, **kwargs): 
```

<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.get_mesh_spacings">&nbsp;</a>
```python
get_mesh_spacings(gp): 
```
Computes the mesh spacings of gp
- `gp`: `np.ndarray`
    >No description...
- `:returns`: `np.ndarray`
    >mesh_spacings

<a id="McUtils.Zachary.FiniteDifferenceFunction.FiniteDifferenceFunction.get_FDF">&nbsp;</a>
```python
get_FDF(self, *args, **kwargs): 
```

### Examples
