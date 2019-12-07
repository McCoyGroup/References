## <a id="RynDMC.AbstractDMC.AbstractDMC">AbstractDMC</a>
A completely abstract implementation of DMC

### Properties and Methods
```python
zpe: property
equilibrated: property
```
```python
__init__(self, name, description, walker_set=None, D=None, time_step=None, steps_per_propagation=None, num_time_steps=None, equilibration=None, potential=None, descendent_weighting_delay=None, log_file=None): 
```

```python
get_zpe(self, n=30): 
```

```python
get_potential(self, coords=None, atoms=None): 
```
Handles potential calls
- `:returns`: `_`
    >list of potentials

```python
branch(self): 
```
Handles branching in DMC. Returns the new energy array after the branching occurs.
- `:returns`: `_`
    >No description...

```python
update_weights(self, energies, weights): 
```
Handles weights in DMC

```python
weight_descendants(self): 
```
Applies descendant weighting

```python
propagate(self, nsteps=None): 
```
Propagates the system forward n steps
- `nsteps`: `Any`
    >number of steps to propagate for; None means automatic
- `:returns`: `_`
    >No description...

```python
snapshot(self, file=None): 
```
Saves a snapshot of the simulation to file
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
