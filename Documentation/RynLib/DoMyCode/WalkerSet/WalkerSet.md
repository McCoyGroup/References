## <a id="RynLib.DoMyCode.WalkerSet.WalkerSet">WalkerSet</a>


### Properties and Methods
```python
from_file: method
load: method
```
<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.__init__">&nbsp;</a>
```python
__init__(self, atoms=None, masses=None, initial_walker=None, initial_weights=1.0, num_walkers=None, mpi_manager=None, walkers_per_core=None): 
```

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.initialize">&nbsp;</a>
```python
initialize(self, deltaT, D=0.5): 
```
Sets up necessary parameters for use in calculating displacements and stuff
- `deltaT`: `Any`
    >No description...
- `D`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.get_displacements">&nbsp;</a>
```python
get_displacements(self, steps=1, coords=None, atomic_units=False): 
```

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.get_displaced_coords">&nbsp;</a>
```python
get_displaced_coords(self, n=1, coords=None, importance_sampler=None, atomic_units=False): 
```

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.displace">&nbsp;</a>
```python
displace(self, n=1, importance_sampler=None, atomic_units=False): 
```

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.descendent_weight">&nbsp;</a>
```python
descendent_weight(self): 
```
Handles the descendent weighting in the system
- `:returns`: `_`
    >tuple of parent coordinates, descendend weights, and original weights

<a id="RynLib.DoMyCode.WalkerSet.WalkerSet.snapshot">&nbsp;</a>
```python
snapshot(self, file): 
```
Snapshots the current walker set to file

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/DoMyCode/WalkerSet/WalkerSet.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/DoMyCode/WalkerSet/WalkerSet.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/RynLib/edit/master/DoMyCode/WalkerSet.py?message=Update%20Docs)