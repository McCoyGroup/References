## <a id="Psience.BasisReps.Operators.Operator">Operator</a>
Provides a (usually) _lazy_ representation of an operator, which allows things like
QQQ and pQp to be calculated block-by-block

### Properties and Methods
```python
ndim: property
shape: property
tensor: property
```
<a id="Psience.BasisReps.Operators.Operator.__init__">&nbsp;</a>
```python
__init__(self, funcs, quanta): 
```

- `funcs`: `callable | Iterable[callable]`
    >The functions use to calculate representation
- `quanta`: `int | Iterable[int]`
    >The number of quanta to do the deepest-level calculations up to

<a id="Psience.BasisReps.Operators.Operator.get_inner_indices">&nbsp;</a>
```python
get_inner_indices(self): 
```
Gets the n-dimensional array of ijkl (e.g.) indices that functions will map over
        Basically returns the indices of the inner-most tensor
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Operators.Operator.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="Psience.BasisReps.Operators.Operator.get_individual_elements">&nbsp;</a>
```python
get_individual_elements(self, idx): 
```
TBH I can't remember what this function is supposed to do ?_?
- `idx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Operators.Operator.get_elements">&nbsp;</a>
```python
get_elements(self, idx): 
```

<a id="Psience.BasisReps.Operators.Operator.product_operator_tensor">&nbsp;</a>
```python
product_operator_tensor(self): 
```
Generates the tensor created from the product of funcs over the dimensions dims,
        Note that this isn't a totally legit tensor since it's ragged
- `funcs`: `Any`
    >No description...
- `dims`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Operators/Operator.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Operators/Operator.md)