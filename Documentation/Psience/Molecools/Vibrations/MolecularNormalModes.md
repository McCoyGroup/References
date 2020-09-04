## <a id="Psience.Molecools.Vibrations.MolecularNormalModes">MolecularNormalModes</a>
A Coordinerds CoordinateSystem object that manages all of the data needed to
     work with normal mode coordinates + some convenience functions for generating and whatnot

### Properties and Methods
```python
name: str
origin: property
from_force_constants: method
```
<a id="Psience.Molecools.Vibrations.MolecularNormalModes.__init__">&nbsp;</a>
```python
__init__(self, molecule, coeffs, name=None, freqs=None, internal=False, origin=None, basis=None, inverse=None): 
```

<a id="Psience.Molecools.Vibrations.MolecularNormalModes.to_internals">&nbsp;</a>
```python
to_internals(self, intcrds=None, dYdR=None, dRdY=None): 
```

<a id="Psience.Molecools.Vibrations.MolecularNormalModes.embed">&nbsp;</a>
```python
embed(self, frame): 
```

- `frame`: `MolecularTransformation`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
