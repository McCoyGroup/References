## <a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian">PerturbationTheoryHamiltonian</a>
Represents the main Ha,o; used in the perturbation theory calculation
- `molecule`: `Molecule`
>The molecule we're doing the perturbation theory on
_quanta`: `int | np.ndarray | Iterable[int]`
>The numbers of quanta of excitation to use for every mode
asis`: `RepresentationBasis | None`
>The basis used for representing, e.g., pQp and QQQ

### Properties and Methods
```python
from_fchk: method
```
<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, molecule=None, n_quanta=3, basis=None): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.H0" class="docs-object-method">&nbsp;</a>
```python
@property
H0(self): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.H1" class="docs-object-method">&nbsp;</a>
```python
@property
H1(self): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.H2" class="docs-object-method">&nbsp;</a>
```python
@property
H2(self): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_state_indices" class="docs-object-method">&nbsp;</a>
```python
get_state_indices(self, states): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_state_quantum_numbers" class="docs-object-method">&nbsp;</a>
```python
get_state_quantum_numbers(self, states): 
```

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_corrections" class="docs-object-method">&nbsp;</a>
```python
get_corrections(self, states=15, coupled_states=None, coeff_threshold=None, energy_threshold=None): 
```

- `states`: `Any`
    >No description...
- `coeff_threshold`: `float | Iterable[float]`
    >a hack for ditching near degeneracies
- `:returns`: `_`
    >No description...

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.get_wavefunctions" class="docs-object-method">&nbsp;</a>
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

<a id="Psience.VPT2.PerturbationTheory.PerturbationTheoryHamiltonian.martin_test" class="docs-object-method">&nbsp;</a>
```python
martin_test(self, states=15, coupled_states=None): 
```
Applies the Martin Test to all of the specified states and returns the resulting correlation matrix
- `states`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/VPT2/PerturbationTheory/PerturbationTheoryHamiltonian.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/VPT2/PerturbationTheory/PerturbationTheoryHamiltonian.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/VPT2/PerturbationTheory.py?message=Update%20Docs)