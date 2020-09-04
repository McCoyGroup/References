## <a id="Psience.BasisReps.Terms.TermComputer">TermComputer</a>
A TermComputer provides a simple interface to compute only some elements of high-dimensional tensors.
It takes a tensor shape and a function to compute tensor elements.
The `compute` function should be able to take a block of indices and return all the matrix elements.

### Properties and Methods
```python
diag: property
```
<a id="Psience.BasisReps.Terms.TermComputer.__init__">&nbsp;</a>
```python
__init__(self, compute, n_quanta): 
```

<a id="Psience.BasisReps.Terms.TermComputer.get_element">&nbsp;</a>
```python
get_element(self, n, m): 
```
Computes term elements.
        Determines first whether it needs to pull single elements or blocks of them.
- `n`: `Any`
    >No description...
- `m`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Terms.TermComputer.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Terms/TermComputer.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Terms/TermComputer.md)