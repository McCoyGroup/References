## <a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction">AnalyticWavefunction</a>
Little extension to RepresentationBasis so that we can use p and x and stuff
to evaluate out matrix elements and stuff

### Properties and Methods
<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.__init__">&nbsp;</a>
```python
__init__(self, energy, data, **opts): 
```

<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.evaluate">&nbsp;</a>
```python
evaluate(self, *args, **kwargs): 
```

<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.plot">&nbsp;</a>
```python
plot(self, figure=None, plot_class=None, domain=(-5, 5), **opts): 
```
Uses McUtils to plot the wavefunction on the passed figure (makes a new one if none)
- `figure`: `Graphics | Graphics3D`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.expect">&nbsp;</a>
```python
expect(self, operator): 
```
Provides expectation values of operators, but the operators have to be Operator objects...
          basically all the logic is inside the operator, but this is worth it for use in ExpansionWavefunction
        We can also potentially add support for ExpansionOperators or SymbolicOperators in the future that are
          able to very cleanly reuse stuff like the `p` matrix that a RepresentationBasis defines
- `operator`: `Operator`
    >the operator to take the expectation of

<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.expectation">&nbsp;</a>
```python
expectation(self, op, other): 
```
Computes the expectation value of operator op over the wavefunction other and self
- `other`: `AnalyticWavefunction`
    >the other wavefunction
- `op`: `Operator`
    >the operator to take the matrix element of
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Wavefunctions.AnalyticWavefunction.probability_density">&nbsp;</a>
```python
probability_density(self): 
```
Computes the probability density of the current wavefunction
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Wavefunctions/AnalyticWavefunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Wavefunctions/AnalyticWavefunction.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/BasisReps/Wavefunctions.py?message=Update%20Docs)