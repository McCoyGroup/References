## <a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction">ExpansionWavefunction</a>
Wrapper that takes an expansion alongside its basis

### Properties and Methods
```python
coeffs: property
basis: property
```
<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.__init__">&nbsp;</a>
```python
__init__(self, energy, coefficients, analytic_wavefunctions): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.evaluate">&nbsp;</a>
```python
evaluate(self, *args, **kwargs): 
```

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.expect">&nbsp;</a>
```python
expect(self, operator): 
```

- `operator`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.expectation">&nbsp;</a>
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

<a id="Psience.BasisReps.Wavefunctions.ExpansionWavefunction.probability_density">&nbsp;</a>
```python
probability_density(self): 
```
Computes the probability density of the current wavefunction
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Wavefunctions/ExpansionWavefunction.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/BasisReps/Wavefunctions.py?message=Update%20Docs)