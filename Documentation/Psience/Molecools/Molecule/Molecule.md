## <a id="Psience.Molecools.Molecule.Molecule">Molecule</a>
General purpose 'Molecule' class where the 'Molecule' need not be a molecule at all

### Properties and Methods
```python
PYBEL_SUPPORTED: NoneType
OC_SUPPORTED: NoneType
atoms: property
bonds: property
coords: property
from_zmat: method
from_pybel: method
from_file: method
normal_modes: property
```
<a id="Psience.Molecools.Molecule.Molecule.__init__">&nbsp;</a>
```python
__init__(self, atoms, coords, bonds=None, mol=None, **kw): 
```

<a id="Psience.Molecools.Molecule.Molecule.prop">&nbsp;</a>
```python
prop(self, name): 
```

<a id="Psience.Molecools.Molecule.Molecule.guess_bonds">&nbsp;</a>
```python
guess_bonds(self, tol=1.05, guess_type=True): 
```
Guesses the bonds for the molecule by finding the ones that are less than some percentage of a single bond for that
        pair of elements
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.plot">&nbsp;</a>
```python
plot(self, *geometries, figure=None, bond_radius=0.1, atom_radius_scaling=0.25, atom_style=None, bond_style=None, mode='fast', objects=False, **plot_ops): 
```

<a id="Psience.Molecools.Molecule.Molecule.get_normal_modes">&nbsp;</a>
```python
get_normal_modes(self, **kwargs): 
```

<a id="Psience.Molecools.Molecule.Molecule.__getattr__">&nbsp;</a>
```python
__getattr__(self, item): 
```

### Examples
