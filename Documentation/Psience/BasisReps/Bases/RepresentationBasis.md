## <a id="Psience.BasisReps.Bases.RepresentationBasis">RepresentationBasis</a>
Metaclass for representations.
Requires concrete implementations of the position and momentum operators.

### Properties and Methods
```python
name: str
```
<a id="Psience.BasisReps.Bases.RepresentationBasis.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, function_generator, n_quanta): 
```

- `function_generator`: `Any`
    >No description...
- `n_quanta`: `int`
    >numbers of quanta

<a id="Psience.BasisReps.Bases.RepresentationBasis.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="Psience.BasisReps.Bases.RepresentationBasis.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

<a id="Psience.BasisReps.Bases.RepresentationBasis.p" class="docs-object-method">&nbsp;</a>
```python
p(self, n): 
```
Generates the momentum matrix up to n-quanta

        There's one big subtlety to what we're doing here, which is that
          for efficiency reasons we return an entirely real matrix
        The reason for that is we assumed people would mostly use it in the context
          of stuff like pp, pQp, or pQQp, in which case the imaginary part pulls out
          and becomes a negative sign
        We actually use this assumption across _all_ of our representations
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Bases.RepresentationBasis.x" class="docs-object-method">&nbsp;</a>
```python
x(self, n): 
```
Generates the coordinate matrix up to n-quanta
- `n`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.BasisReps.Bases.RepresentationBasis.operator_mapping" class="docs-object-method">&nbsp;</a>
```python
@property
operator_mapping(self): 
```

<a id="Psience.BasisReps.Bases.RepresentationBasis.operator" class="docs-object-method">&nbsp;</a>
```python
operator(self, *terms): 
```

<a id="Psience.BasisReps.Bases.RepresentationBasis.representation" class="docs-object-method">&nbsp;</a>
```python
representation(self, *terms): 
```
Provides a representation of a product operator specified by 'terms'
- `terms`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/BasisReps/Bases/RepresentationBasis.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/BasisReps/Bases/RepresentationBasis.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/Psience/edit/master/BasisReps/Bases.py?message=Update%20Docs)