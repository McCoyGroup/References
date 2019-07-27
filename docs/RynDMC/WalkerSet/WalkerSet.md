## <a id="RynDMC.WalkerSet.WalkerSet">WalkerSet</a>


<a id="RynDMC.WalkerSet.WalkerSet.__init__">&nbsp;</a>
```python
__init__(self, atoms, coords, *miscargs, initial_walkers=5000, masses=None, sigmas=None, weights=None, _initialize=True): 
```

<a id="RynDMC.WalkerSet.WalkerSet.initialize">&nbsp;</a>
```python
initialize(self, time_step, D): 
```
Sets up necessary parameters for use in calculating displacements and stuff
- `deltaT`: `Any`
    >No description...
- `D`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynDMC.WalkerSet.WalkerSet.get_displacements">&nbsp;</a>
```python
get_displacements(self, n=1, sigmas=None): 
```
Computes n random Gaussian displacements from the sigmas and the timestep
- `n`: `Any`
    >No description...
- `sigmas`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynDMC.WalkerSet.WalkerSet.get_displaced_coords">&nbsp;</a>
```python
get_displaced_coords(self, n=1): 
```
Computes n new displaced coordinates based on the original ones from the sigmas
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynDMC.WalkerSet.WalkerSet.displace">&nbsp;</a>
```python
displace(self, n=1): 
```
Generates multiple displacements and binds the last one
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

