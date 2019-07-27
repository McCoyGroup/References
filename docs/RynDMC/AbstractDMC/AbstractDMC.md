## <a id=RynDMC.AbstractDMC.AbstractDMC>AbstractDMC</a>
A completely abstract implementation of DMC

```python
zpe: property
equilibrated: property
```
<a id=RynDMC.AbstractDMC.AbstractDMC.__init__>&nbsp;</a>
```python
__init__(self, name, description, walker_set=None, D=None, time_step=None, steps_per_propagation=None, num_time_steps=None, equilibration=None, potential=None, descendent_weighting_delay=None, log_file=None): 
```

<a id=RynDMC.AbstractDMC.AbstractDMC.get_zpe>&nbsp;</a>
```python
get_zpe(self, n=30): 
```

<a id=RynDMC.AbstractDMC.AbstractDMC.get_potential>&nbsp;</a>
```python
get_potential(self, coords=None, atoms=None): 
```
Handles potential calls
- `:returns`: `_`
    >list of potentials

<a id=RynDMC.AbstractDMC.AbstractDMC.branch>&nbsp;</a>
```python
branch(self): 
```
Handles branching in DMC. Returns the new energy array after the branching occurs.
- `:returns`: `_`
    >No description...

<a id=RynDMC.AbstractDMC.AbstractDMC.update_weights>&nbsp;</a>
```python
update_weights(self, energies, weights): 
```

<a id=RynDMC.AbstractDMC.AbstractDMC.weight_descendants>&nbsp;</a>
```python
weight_descendants(self): 
```

<a id=RynDMC.AbstractDMC.AbstractDMC.propagate>&nbsp;</a>
```python
propagate(self, nsteps=None): 
```
Propagates the system forward n steps
- `nsteps`: `Any`
    >number of steps to propagate for; None means automatic
- `:returns`: `_`
    >No description...

<a id=RynDMC.AbstractDMC.AbstractDMC.snapshot>&nbsp;</a>
```python
snapshot(self, file=None): 
```
Saves a snapshot of the simulation to file
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

