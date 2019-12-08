## <a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian">PerturbationTheoryHamiltonian</a>
Represents the main handler used in the perturbation theory calculation
- `coords`: `Any`
    >The current coordinates of the system (used for computing the Jacobians)
- `pot_derivs`: `Any`
    >The first, second, third, and fourth derivatives of the potential
- `modes`: `CoordinateSystem`
    >The cartesian coordinate normal modes
- `internals`: `Any`
    >The internal coordinate normal modes

### Properties and Methods
<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.__init__">&nbsp;</a>
```python
__init__(self, coords, pot_derivs, modes, internals): 
```

<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.pmatrix_ho">&nbsp;</a>
```python
pmatrix_ho(self, n): 
```

- `n`: `Any`
    >No description...
- `:returns`: `sp.csr_matrix`
    >No description...

<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.qmatrix_ho">&nbsp;</a>
```python
qmatrix_ho(self, n): 
```

- `n`: `Any`
    >No description...
- `:returns`: `sp.csr_matrix`
    >No description...

<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.product_operator_tensor">&nbsp;</a>
```python
product_operator_tensor(self, funcs, dims): 
```
Generates the tensor created from the product of funcs over the dimensions dims
- `funcs`: `Any`
    >No description...
- `dims`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.QQQ">&nbsp;</a>
```python
QQQ(self, coefficients, dimensions, qmatrix=None): 
```

<a id="PyVPT.PerturbationTheory.PerturbationTheoryHamiltonian.pQp">&nbsp;</a>
```python
pQp(self, coefficients, dimensions, pmatrix=None, qmatrix=None): 
```

### Examples
