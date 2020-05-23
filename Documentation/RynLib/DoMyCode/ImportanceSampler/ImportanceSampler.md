## <a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler">ImportanceSampler</a>
A general-purpose importance sampler that applies acceptance/rejection criteria and computes local energies

### Properties and Methods
```python
psi: property
```
<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.__init__">&nbsp;</a>
```python
__init__(self, trial_wavefunctions, derivs=None, name=None): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.init_params">&nbsp;</a>
```python
init_params(self, sigmas, time_step, mpi_manager, atoms, *extra_args): 
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

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.clean_up">&nbsp;</a>
```python
clean_up(self): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.setup_psi">&nbsp;</a>
```python
setup_psi(self, crds): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.accept">&nbsp;</a>
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

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.accept_step">&nbsp;</a>
```python
accept_step(self, step_no, coords, disp): 
```

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.drift">&nbsp;</a>
```python
drift(self, coords, dx=0.001): 
```
Calcuates the drift term by doing a numerical differentiation
- `coords`: `Any`
    >No description...
- `dx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.psi_calc">&nbsp;</a>
```python
psi_calc(self, coords, dx=0.001): 
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

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.metropolis">&nbsp;</a>
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

<a id="RynLib.DoMyCode.ImportanceSampler.ImportanceSampler.local_kin">&nbsp;</a>
```python
local_kin(self, coords, dx=0.001): 
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
