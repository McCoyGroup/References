## <a id="Psience.Molecools.Vibrations.MolecularNormalModes">MolecularNormalModes</a>
A Coordinerds CoordinateSystem object that manages all of the data needed to
work with normal mode coordinates + some convenience functions for generating and whatnot

### Properties and Methods
```python
name: str
from_force_constants: method
```
<a id="Psience.Molecools.Vibrations.MolecularNormalModes.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, molecule, coeffs, name=None, freqs=None, internal=False, origin=None, basis=None, inverse=None): 
```

<a id="Psience.Molecools.Vibrations.MolecularNormalModes.to_internals" class="docs-object-method">&nbsp;</a>
```python
to_internals(self, intcrds=None, dYdR=None, dRdY=None): 
```

<a id="Psience.Molecools.Vibrations.MolecularNormalModes.origin" class="docs-object-method">&nbsp;</a>
```python
@property
origin(self): 
```

<a id="Psience.Molecools.Vibrations.MolecularNormalModes.embed" class="docs-object-method">&nbsp;</a>
```python
embed(self, frame): 
```

- `frame`: `MolecularTransformation`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/Molecools/Vibrations/MolecularNormalModes.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/Molecools/Vibrations/MolecularNormalModes.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Psience/Molecools/Vibrations/MolecularNormalModes.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Psience/Molecools/Vibrations/MolecularNormalModes.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Psience/edit/master/Molecools/Vibrations.py?message=Update%20Docs)