## <a id="McUtils.Parsers.StructuredType.StructuredTypeArray">StructuredTypeArray</a>
Represents an array of objects defined by the StructuredType spec provided
mostly useful as it dispatches to NumPy where things are simple enough to do so

It has a system to dispatch intelligently based on the type of array provided
The kinds of structures supported are: OrderedDict, list, and np.ndarray

A _simple_ StructuredTypeArray is one that can just be represented as a single np.ndarray
A _compound_ StructuredTypeArray requires either a list or OrderedDict of StructuredTypeArray subarrays

### Properties and Methods
<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, stype, num_elements=50, padding_mode='fill', padding_value=None): 
```

- `stype`: `StructuredType`
    >No description...
- `num_elements`: `int`
    >number of default elements in dynamically sized arrays

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.is_simple" class="docs-object-method">&nbsp;</a>
```python
@property
is_simple(self): 
```
Just returns wheter the core datatype is simple
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.dict_like" class="docs-object-method">&nbsp;</a>
```python
@property
dict_like(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.extension_axis" class="docs-object-method">&nbsp;</a>
```python
@property
extension_axis(self): 
```
Determines which axis to extend when adding more memory to the array
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.shape" class="docs-object-method">&nbsp;</a>
```python
@property
shape(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.block_size" class="docs-object-method">&nbsp;</a>
```python
@property
block_size(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.append_depth" class="docs-object-method">&nbsp;</a>
```python
@property
append_depth(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.dtype" class="docs-object-method">&nbsp;</a>
```python
@property
dtype(self): 
```
Returns the core data type held by the StructuredType that represents the array
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.stype" class="docs-object-method">&nbsp;</a>
```python
@property
stype(self): 
```
Returns the StructuredType that the array holds data for
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.array" class="docs-object-method">&nbsp;</a>
```python
@property
array(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.axis_shape_indeterminate" class="docs-object-method">&nbsp;</a>
```python
axis_shape_indeterminate(self, axis): 
```
Tries to determine if an axis has had any data placed into it or otherwise been given a determined shape
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.has_indeterminate_shape" class="docs-object-method">&nbsp;</a>
```python
@property
has_indeterminate_shape(self): 
```
Tries to determine if the entire array has a determined shape
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.filled_to" class="docs-object-method">&nbsp;</a>
```python
@property
filled_to(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.set_filling" class="docs-object-method">&nbsp;</a>
```python
set_filling(self, amt, axis=0): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.increment_filling" class="docs-object-method">&nbsp;</a>
```python
increment_filling(self, inc=1, axis=0): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__len__" class="docs-object-method">&nbsp;</a>
```python
__len__(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.empty_array" class="docs-object-method">&nbsp;</a>
```python
empty_array(self, shape=None, num_elements=None): 
```
Creates empty arrays with (potentially) default elements

        The shape handling rules operate like this:
            if shape is None, we assume we'll initialize this as an array with a single element to be filled out
            if shape is (None,) or (n,) we'll initialize this as an array with multiple elments to be filled out
            otherwise we'll just take the specified shape
- `num_elements`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.extend_array" class="docs-object-method">&nbsp;</a>
```python
extend_array(self, axis=None): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__setitem__" class="docs-object-method">&nbsp;</a>
```python
__setitem__(self, key, value): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.set_part" class="docs-object-method">&nbsp;</a>
```python
set_part(self, key, value): 
```
Recursively sets parts of an array if not simple, otherwise just delegates to NumPy
- `key`: `Any`
    >No description...
- `value`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.get_part" class="docs-object-method">&nbsp;</a>
```python
get_part(self, item, use_full_array=True): 
```
If simple, delegates to NumPy, otherwise tries to recursively get parts...?
        Unclear how slicing is best handled here.
- `item`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.add_axis" class="docs-object-method">&nbsp;</a>
```python
add_axis(self, which=0, num_elements=None, change_shape=True): 
```
Adds an axis to the array, generally used for expanding from singular or 1D data to higher dimensional
        This happens with parse_all and repeated things like that
- `which`: `Any`
    >No description...
- `num_elements`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.can_cast" class="docs-object-method">&nbsp;</a>
```python
can_cast(self, val): 
```
Determines whether val can probably be cast to the right return type and shape without further processing or if that's definitely not possible
- `val`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.append" class="docs-object-method">&nbsp;</a>
```python
append(self, val, axis=0): 
```
Puts val in the first empty slot in the array
- `val`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.extend" class="docs-object-method">&nbsp;</a>
```python
extend(self, val, single=True, prepend=False, axis=None): 
```
Adds the sequence val to the array
- `val`: `Any`
    >No description...
- `single`: `bool`
    >a flag that indicates whether val can be treated as a single object or if it needs to be reshapen when handling in non-simple case
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.fill" class="docs-object-method">&nbsp;</a>
```python
fill(self, array): 
```
Sets the result array to be the passed array
- `array`: `str | np.ndarray`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.cast_to_array" class="docs-object-method">&nbsp;</a>
```python
cast_to_array(self, txt): 
```
Casts a string of things with a given data type to an array of that type and does some optional
        shape coercion
- `txt`: `str | iterable[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/StructuredType/StructuredTypeArray.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/StructuredType/StructuredTypeArray.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Parsers/StructuredType/StructuredTypeArray.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Parsers/StructuredType/StructuredTypeArray.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Parsers/StructuredType.py?message=Update%20Docs)