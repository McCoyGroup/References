## <a id="Psience.Molecools.Vibrations.MolecularVibrations">MolecularVibrations</a>


### Properties and Methods
```python
basis: property
molecule: property
coords: property
```
<a id="Psience.Molecools.Vibrations.MolecularVibrations.__init__">&nbsp;</a>
```python
__init__(self, molecule, basis, freqs=None, init=None): 
```
Sets up a vibration for a Molecule object over the CoordinateSystem basis
- `molecule`: `Molecule`
    >No description...
- `init`: `None | CoordinateSet`
    >No description...
- `basis`: `MolecularNormalModes`
    >No description...

<a id="Psience.Molecools.Vibrations.MolecularVibrations.__len__">&nbsp;</a>
```python
__len__(self): 
```

<a id="Psience.Molecools.Vibrations.MolecularVibrations.displace">&nbsp;</a>
```python
displace(self, displacements=None, amt=0.1, n=1, which=0): 
```

<a id="Psience.Molecools.Vibrations.MolecularVibrations.visualize">&nbsp;</a>
```python
visualize(self, step_size=0.1, steps=(5, 5), which=0, anim_opts=None, mode='fast', **plot_args): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/Molecools/Vibrations/MolecularVibrations.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/Molecools/Vibrations/MolecularVibrations.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/Molecools/Vibrations.py?message=Update%20Docs)