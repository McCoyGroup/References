## <a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian">PerturbationTheoryHamiltonian</a>
Represents the main Ha,o; used in the perturbation theory calculation
- `molecule`: `Molecule`
    >The molecule we're doing the perturbation theory on
- `n_quanta`: `int | np.ndarray | Iterable[int]`
    >The numbers of quanta of excitation to use for every mode
- `basis`: `RepresentationBasis | None`
    >The basis used for representing, e.g., pQp and QQQ

### Properties and Methods
```python
from_fchk: method
H0: property
H1: property
H2: property
```
<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.__init__">&nbsp;</a>
```python
__init__(self, molecule=None, n_quanta=3, basis=None): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_state_indices">&nbsp;</a>
```python
get_state_indices(self, states): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_state_quantum_numbers">&nbsp;</a>
```python
get_state_quantum_numbers(self, states): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_corrections">&nbsp;</a>
```python
get_corrections(self, states=15, coupled_states=None, coeff_threshold=None, energy_threshold=None): 
```

- `states`: `Any`
    >No description...
- `coeff_threshold`: `float | Iterable[float]`
    >a hack for ditching near degeneracies
- `:returns`: `_`
    >No description...

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_wavefunctions">&nbsp;</a>
```python
get_wavefunctions(self, states=15, coupled_states=None, coeff_threshold=None, energy_threshold=None): 
```
Computes perturbation expansion of the wavefunctions and energies.
            We're pushing all higher-level stuff into the wavefunctions, so this is
              usually the function we want
- `states`: `int | iterable[int] | None`
    >the states to target
- `:returns`: `np.ndarray`
    >coeffs

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.martin_test">&nbsp;</a>
```python
martin_test(self, states=15, coupled_states=None): 
```
Applies the Martin Test to all of the specified states and returns the resulting correlation matrix
- `states`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
