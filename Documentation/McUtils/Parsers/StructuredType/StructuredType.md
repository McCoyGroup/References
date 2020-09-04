## <a id="McUtils.Parsers.StructuredType.StructuredType">StructuredType</a>
Represents a structured type with a defined calculus to simplify the construction of combined types when writing
parsers that take multi-typed data

Supports a compound StructuredType where the types are keyed

### Properties and Methods
```python
is_simple: property
```
<a id="McUtils.Parsers.StructuredType.StructuredType.__init__">&nbsp;</a>
```python
__init__(self, base_type, shape=None, is_alternative=False, is_optional=False, default_value=None): 
```

<a id="McUtils.Parsers.StructuredType.StructuredType.add_types">&nbsp;</a>
```python
add_types(self, other): 
```
Constructs a new type by treating the two objects as siblings, that is if they can be merged due to type and
        shape similarity they will be, otherwise a non-nesting structure will be constructed from them

        We'll also want a nesting version of this I'm guessing, which probably we hook into __call__
- `other`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredType.__add__">&nbsp;</a>
```python
__add__(self, other): 
```

<a id="McUtils.Parsers.StructuredType.StructuredType.compound_types">&nbsp;</a>
```python
compound_types(self, other): 
```
Creates a structured type where rather than merging types they simply compound onto one another
- `other`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredType.__call__">&nbsp;</a>
```python
__call__(self, other): 
```

<a id="McUtils.Parsers.StructuredType.StructuredType.repeat">&nbsp;</a>
```python
repeat(self, n=None, m=None): 
```
Returns a new version of the type, but with the appropriate shape for being repeated n-to-m times
- `n`: `Any`
    >No description...
- `m`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredType.drop_axis">&nbsp;</a>
```python
drop_axis(self, axis=0): 
```
Returns a new version of the type, but with the appropriate shape for dropping an axis
- `axis`: `int`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredType.extend_shape">&nbsp;</a>
```python
extend_shape(self, base_shape): 
```
Extends the shape of the type such that base_shape precedes the existing shape
- `base_shape`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredType.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/StructuredType/StructuredType.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/StructuredType/StructuredType.md)