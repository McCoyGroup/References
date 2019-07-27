Extract values of constants:

```python
from McUtils.Data import UnitsData

UnitsData.data[("Hartrees", "InverseMeters")]["Value"]
```

Convert between units:

```python
from McUtils.Data import UnitsData

UnitsData.data[("Hartrees", "Wavenumbers")]
```