## <a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction">ExpansionWavefunction</a>
Wrapper that takes an expansion alongside its basis

### Properties and Methods
<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, energy, coefficients, analytic_wavefunctions): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.coeffs" class="docs-object-method">&nbsp;</a>
```python
@property
coeffs(self): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.basis" class="docs-object-method">&nbsp;</a>
```python
@property
basis(self): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.evaluate" class="docs-object-method">&nbsp;</a>
```python
evaluate(self, *args, **kwargs): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.expect" class="docs-object-method">&nbsp;</a>
```python
expect(self, operator): 
```

- `operator`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.expectation" class="docs-object-method">&nbsp;</a>
```python
expectation(self, operator, other): 
```
Computes the expectation value of operator op over the wavefunction other and self
- `other`: `Wavefunction`
    >No description...
- `op`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.probability_density" class="docs-object-method">&nbsp;</a>
```python
probability_density(self): 
```
Computes the probability density of the current wavefunction
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Psience/edit/master/BasisReps/Wavefunctions.py?message=Update%20Docs)