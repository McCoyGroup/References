## <a id="McUtils.Parsers.StructuredType.StructuredType">StructuredType</a>
Represents a structured type with a defined calculus to simplify the construction of combined types when writing
    parsers that take multi-typed data

    Supports a compound StructuredType where the types are keyed

### Properties and Methods
```python
is_simple: property
```
```python
__init__(self, base_type, shape=None, is_alternative=False, is_optional=False, default_value=None): 
```

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

```python
__add__(self, other): 
```

```python
compound_types(self, other): 
```
Creates a structured type where rather than merging types they simply compound onto one another
- `other`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

```python
__call__(self, other): 
```

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

```python
drop_axis(self, axis=0): 
```
Returns a new version of the type, but with the appropriate shape for dropping an axis
- `axis`: `int`
    >No description...
- `:returns`: `_`
    >No description...

```python
extend_shape(self, base_shape): 
```
Extends the shape of the type such that base_shape precedes the existing shape
- `base_shape`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

```python
__repr__(self): 
```

### Examples
