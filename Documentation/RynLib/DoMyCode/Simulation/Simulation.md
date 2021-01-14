## <a id="RynLib.DoMyCode.Simulation.Simulation">Simulation</a>
A DMC simulation class. Uses a number of subclasses to manage its methods

### Properties and Methods
```python
load_lib: method
reload_lib: method
```
<a id="RynLib.DoMyCode.Simulation.Simulation.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, params): 
```
Initializes the simulation from the simulation parameters
- `params`: `SimulationParameters`
    >the parameters for the simulation

<a id="RynLib.DoMyCode.Simulation.Simulation.configure_simulation" class="docs-object-method">&nbsp;</a>
```python
configure_simulation(self, name='dmc', description='a dmc simulation', walker_set=None, time_step=0, alpha=None, potential=None, atomic_units=False, steps_per_propagation=None, mpi_manager=True, importance_sampler=None, num_wavefunctions=0, ignore_errors=False, branching_threshold=1.0, energy_error_value=1000000000.0, max_weight_threshold=None, min_potential_threshold=None, branch_on_steps=False, parallelize_diffusion=True, branch_on_cores=False, random_seed=None, pre_run_script=None, post_run_script=None): 
```

- `name`: `str`
    >No description...
- `description`: `str`
    >No description...
- `walker_set`: `WalkerSet`
    >No description...
- `time_step`: `int`
    >No description...
- `alpha`: `float`
    >No description...
- `potential`: `str | Potential`
    >No description...
- `mpi_manager`: `MPIManagerObject`
    >No description...
- `steps_per_propagation`: `int`
    >No description...
- `importance_sampler`: `ImportanceSampler`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.config_string" class="docs-object-method">&nbsp;</a>
```python
@property
config_string(self): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.checkpoint" class="docs-object-method">&nbsp;</a>
```python
checkpoint(self, test=True): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.garbage_collect" class="docs-object-method">&nbsp;</a>
```python
garbage_collect(self, test=True): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.reload" class="docs-object-method">&nbsp;</a>
```python
reload(self, energies_file='energies.npy', walkers_file='walkers_{n}.npz', full_weights_file='full_weights.npy', full_energies_file='full_energies.npy'): 
```
Reloads the core data in a Simulation object from a checkpoint file
- `core_dir`: `Any`
    >No description...
- `params_file`: `Any`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.log_print" class="docs-object-method">&nbsp;</a>
```python
log_print(self, *arg, allow_dummy=False, **kwargs): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.run" class="docs-object-method">&nbsp;</a>
```python
run(self): 
```
Runs the DMC until we've gone through the requested number of time steps, checkpoint-ing if there's a crash
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.lib" class="docs-object-method">&nbsp;</a>
```python
@property
lib(self): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.apply_branching" class="docs-object-method">&nbsp;</a>
```python
apply_branching(self, energies): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.evaluate_potential_and_branch" class="docs-object-method">&nbsp;</a>
```python
evaluate_potential_and_branch(self, nsteps): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.propagate" class="docs-object-method">&nbsp;</a>
```python
propagate(self, nsteps=None): 
```
Propagates the system forward n steps
- `nsteps`: `Any`
    >number of steps to propagate for; None means automatic
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.update_weights" class="docs-object-method">&nbsp;</a>
```python
update_weights(self, energies, weights): 
```
Iteratively updates the weights over a set of vectors of energies
- `energies`: `np.ndarray`
    >No description...
- `weights`: `np.ndarray`
    >No description...
- `:returns`: `np.ndarray`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.chop_weights" class="docs-object-method">&nbsp;</a>
```python
chop_weights(eliminated_walkers, weights, parents, walkers, energies): 
```

<a id="RynLib.DoMyCode.Simulation.Simulation.branch" class="docs-object-method">&nbsp;</a>
```python
branch(self, energies): 
```
Handles branching in the system.
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.Simulation.Simulation.descendent_weight" class="docs-object-method">&nbsp;</a>
```python
descendent_weight(self): 
```
Calls into the walker descendent weighting if the timing is right
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/DoMyCode/Simulation/Simulation.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/DoMyCode/Simulation/Simulation.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/RynLib/DoMyCode/Simulation/Simulation.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/RynLib/DoMyCode/Simulation/Simulation.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/RynLib/edit/master/DoMyCode/Simulation.py?message=Update%20Docs)