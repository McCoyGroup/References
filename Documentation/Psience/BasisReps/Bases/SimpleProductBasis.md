## <a id="Psience.BasisReps.Bases.SimpleProductBasis">SimpleProductBasis</a>
Defines a direct product basis from a simpler basis.
Mixed product bases aren't currently supported

### Properties and Methods
<a id="Psience.BasisReps.Bases.SimpleProductBasis.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, basis_type, n_quanta): 
```

- `basis_type`: `type`
    >the type of basis to do a product over
- `n_quanta`: `Iterable[int]`
    >the number of quanta for the representations

<a id="Psience.BasisReps.Bases.SimpleProductBasis.quanta" class="docs-object-method">&nbsp;</a>
```python
@property
quanta(self): 
```

<a id="Psience.BasisReps.Bases.SimpleProductBasis.get_function" class="docs-object-method">&nbsp;</a>
```python
get_function(self, idx): 
```

<a id="Psience.BasisReps.Bases.SimpleProductBasis.operator" class="docs-object-method">&nbsp;</a>
```python
operator(self, *terms): 
```

<a id="Psience.BasisReps.Bases.SimpleProductBasis.representation" class="docs-object-method">&nbsp;</a>
```python
representation(self, *terms): 
```
Provides a representation of a product operator specified by 'terms'
- `terms`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Bases.SimpleProductBasis.x" class="docs-object-method">&nbsp;</a>
```python
x(self, n): 
```
Returns the representation of x in the multi-dimensional basis with every term evaluated up to n quanta
        Whether this is what we want or not is still TBD
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Bases.SimpleProductBasis.p" class="docs-object-method">&nbsp;</a>
```python
p(self, n): 
```
Returns the representation of p in the multi-dimensional basis with every term evaluated up to n quanta
        Whether this is what we want or not is still TBD
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Bases/SimpleProductBasis.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Bases/SimpleProductBasis.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/BasisReps/Bases.py?message=Update%20Docs)