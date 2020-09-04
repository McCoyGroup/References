## <a id="Psience.Molecools.Molecule.Molecule">Molecule</a>
General purpose 'Molecule' class where the 'Molecule' need not be a molecule at all

### Properties and Methods
```python
from_zmat: method
num_atoms: property
atoms: property
masses: property
bonds: property
coords: property
sys: property
formula: property
multiconfig: property
name: property
force_constants: property
potential_derivatives: property
potential_surface: property
dipole_surface: property
center_of_mass: property
inertial_axes: property
internal_coordinates: property
normal_modes: property
shape: property
from_pybel: method
from_file: method
```
<a id="Psience.Molecools.Molecule.Molecule.__init__">&nbsp;</a>
```python
__init__(self, atoms, coords, bonds=None, obmol=None, charge=None, name=None, zmatrix=None, dipole_surface=None, potential_surface=None, potential_derivatives=None, source_file=None, guess_bonds=True, **kw): 
```

- `atoms`: `Iterable[str]`
    >atoms specified by name, either full name or short
- `coords`: `np.ndarray`
    >coordinates for the molecule, assumed to be in Bohr by default
- `bonds`: `Iterable[Iterable[int]] | None`
    >bond specification for the molecule
- `obmol`: `Any`
    >OpenBabel molecule for doing conversions
- `charge`: `int | None`
    >Net charge on the molecule
- `name`: `str | None`
    >Name for the molecule
- `dipole_surface`: `DipoleSurface | None`
    >The dipole surface for the system
- `potential_surface`: `PotentialSurface | None`
    >The potential surface for the system
- `potential_derivatives`: `Iterable[np.ndarray] | None`
    >Derivatives of the potential surface
- `guess_bonds`: `bool`
    >Whether or not to guess the bonding arrangement when that would be used
- `source_file`: `str`
    >The data file the molecule was loaded from
- `kw`: `Any`
    >Other bound parameters that might be useful

<a id="Psience.Molecools.Molecule.Molecule.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.take_submolecule">&nbsp;</a>
```python
take_submolecule(self, spec): 
```
Takes a 'slice' of a molecule if working with Cartesian coords.
        If not, need to do some corner case handling for that.
- `spec`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.__len__">&nbsp;</a>
```python
__len__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.__iter__">&nbsp;</a>
```python
__iter__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="Psience.Molecools.Molecule.Molecule.copy">&nbsp;</a>
```python
copy(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.prop">&nbsp;</a>
```python
prop(self, name, *args, **kwargs): 
```

<a id="Psience.Molecools.Molecule.Molecule.load_force_constants">&nbsp;</a>
```python
load_force_constants(self, file=None): 
```
Loads force constants from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_potential_derivatives">&nbsp;</a>
```python
load_potential_derivatives(self, file=None): 
```
Loads potential derivatives from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_normal_modes">&nbsp;</a>
```python
load_normal_modes(self, file=None): 
```
Loads potential derivatives from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_potential_surface">&nbsp;</a>
```python
load_potential_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.load_dipole_surface">&nbsp;</a>
```python
load_dipole_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.principle_axis_frame">&nbsp;</a>
```python
principle_axis_frame(self, sel=None, inverse=False): 
```
Gets the principle axis frame(s) for the molecule
- `mol`: `Any`
    >No description...
- `sel`: `Any`
    >selection of atoms to use when getting the Eckart frame
- `inverse`: `bool`
    >whether to return the inverse of the rotations or not
- `:returns`: `MolecularTransformation | List[MolecularTransformation]`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.eckart_frame">&nbsp;</a>
```python
eckart_frame(self, mol, sel=None, inverse=False): 
```
Gets the Eckart frame(s) for the molecule
- `mol`: `Any`
    >No description...
- `sel`: `Any`
    >selection of atoms to use when getting the Eckart frame
- `inverse`: `bool`
    >whether to return the inverse of the rotations or not
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.get_embedded_molecule">&nbsp;</a>
```python
get_embedded_molecule(self, ref=None): 
```
Returns a Molecule embedded in an Eckart frame if ref is not None, otherwise returns
        a principle-axis embedded Molecule
- `:returns`: `Molecule`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.plot">&nbsp;</a>
```python
plot(self, *geometries, figure=None, bond_radius=0.1, atom_radius_scaling=0.25, atom_style=None, bond_style=None, mode='fast', objects=False, **plot_ops): 
```

<a id="Psience.Molecools.Molecule.Molecule.get_normal_modes">&nbsp;</a>
```python
get_normal_modes(self, **kwargs): 
```

### Examples
