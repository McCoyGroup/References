## <a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler">ImportanceSampler</a>
A general-purpose importance sampler that applies acceptance/rejection criteria and computes local energies

### Properties and Methods
<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, trial_wavefunctions, derivs=None, name=None, dx=0.001): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.init_params" class="docs-object-method">&nbsp;</a>
```python
init_params(self, sigmas, time_step, mpi_manager, atoms, *extra_args, atomic_units=False): 
```

- `sigmas`: `Any`
    >No description...
- `time_step`: `Any`
    >No description...
- `mpi_manager`: `None | MPIMangerObject`
    >No description...
- `atoms`: `Iterable[str]`
    >No description...
- `extra_args`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.clean_up" class="docs-object-method">&nbsp;</a>
```python
clean_up(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.mpi_manager" class="docs-object-method">&nbsp;</a>
```python
@property
mpi_manager(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.psi" class="docs-object-method">&nbsp;</a>
```python
@property
psi(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.setup_psi" class="docs-object-method">&nbsp;</a>
```python
setup_psi(self, crds): 
```
Sets up
- `crds`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.accept" class="docs-object-method">&nbsp;</a>
```python
accept(self, coords, disp): 
```
Acceptance/Rejection of a step based on the drift term
- `coords`: `Any`
    >No description...
- `disp`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.accept_step" class="docs-object-method">&nbsp;</a>
```python
accept_step(self, step_no, coords, disp): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.drift" class="docs-object-method">&nbsp;</a>
```python
drift(self, coords, dx=None): 
```
Calcuates the drift term by doing a numerical differentiation
- `coords`: `Any`
    >No description...
- `dx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.psi_calc" class="docs-object-method">&nbsp;</a>
```python
psi_calc(self, coords, dx=None): 
```
Calculates the trial wavefunction over the three displacements that are used in numerical differentiation
- `coords`: `Any`
    >No description...
- `trial_wvfn`: `Any`
    >No description...
- `dx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.metropolis" class="docs-object-method">&nbsp;</a>
```python
metropolis(self, Fqx, Fqy, x, y, psi1, psi2): 
```
Computes the metropolis step
- `Fqx`: `Any`
    >No description...
- `Fqy`: `Any`
    >No description...
- `x`: `Any`
    >No description...
- `y`: `Any`
    >No description...
- `psi1`: `Any`
    >No description...
- `psi2`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.local_kin" class="docs-object-method">&nbsp;</a>
```python
local_kin(self, coords, dx=None): 
```
Calculates the local kinetic energy
- `time_step`: `Any`
    >No description...
- `psi`: `Any`
    >No description...
- `sigmas`: `Any`
    >No description...
- `dx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/DoMyCode/ImportanceSampler/ImportanceSampler.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/DoMyCode/ImportanceSampler/ImportanceSampler.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/RynLib/DoMyCode/ImportanceSampler/ImportanceSampler.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/RynLib/DoMyCode/ImportanceSampler/ImportanceSampler.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/RynLib/edit/master/DoMyCode/ImportanceSampler.py?message=Update%20Docs)