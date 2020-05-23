## <a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian">PerturbationTheoryHamiltonian</a>
Represents the main handler used in the perturbation theory calculation
    I probably want it to rely on a Molecule object...
- `coords`: `np.ndarray | CoordinateSet`
    >The current coordinates of the system (used for computing the Jacobians)
- `masses`: `Any`
    >The masses of the coordinate system (used for computing the G-matrix and friends)
- `pot_derivs`: `Any`
    >The Cartesian derivatives of the potential
- `modes`: `NormalModeCoordinates`
    >The Cartesian coordinate normal modes and the corresponding inverse
- `internals`: `CoordinateSystem`
    >The internal coordinate normal modes
- `numbers_of_quanta`: `np.ndarray | Iterable[int]`
    >The numbers of quanta of excitation to use for every mode

### Properties and Methods
```python
from_fchk: method
ExpansionTerms: type
PotentialTerms: type
KineticTerms: type
SubHamiltonian: type
H0: property
H1: property
H2: property
ProductOperator: type
```
<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.__init__">&nbsp;</a>
```python
__init__(self, *ignore, coords=None, masses=None, pot_derivs=None, modes=None, internals=None, n_quanta=3, undimensionalize=True): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.undimensionalize">&nbsp;</a>
```python
undimensionalize(self, masses, modes): 
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
Computes perturbation expansion of the wavefunctions and energies
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
