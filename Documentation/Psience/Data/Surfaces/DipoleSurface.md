## <a id="Psience.Data.Surfaces.DipoleSurface">DipoleSurface</a>
Provides a unified interface to working with dipole surfaces.
Currently basically no fancier than a regular surface (although with convenient loading functions), but dipole-specific
stuff could come

### Properties and Methods
```python
from_log_file: method
from_fchk_file: method
```
<a id="Psience.Data.Surfaces.DipoleSurface.__init__">&nbsp;</a>
```python
__init__(self, mu_x, mu_y, mu_z): 
```

- `mu_x`: `Surface`
    >X-component of dipole moment
- `mu_y`: `Surface`
    >Y-component of dipole moment
- `mu_z`: `Surface`
    >Z-component of dipole moment

<a id="Psience.Data.Surfaces.DipoleSurface.get_log_values">&nbsp;</a>
```python
get_log_values(log_file, keys=('StandardCartesianCoordinates', 'DipoleMoments')): 
```

<a id="Psience.Data.Surfaces.DipoleSurface.get_fchk_values">&nbsp;</a>
```python
get_fchk_values(fchk_file): 
```

<a id="Psience.Data.Surfaces.DipoleSurface.__call__">&nbsp;</a>
```python
__call__(self, gridpoints, **opts): 
```
Explicitly overrides the Surface-level evaluation because we know the Taylor surface needs us to flatten our gridpoints
- `gridpoints`: `Any`
    >No description...
- `opts`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/Data/Surfaces/DipoleSurface.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/Data/Surfaces/DipoleSurface.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/Data/Surfaces.py?message=Update%20Docs)