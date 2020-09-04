## <a id="McUtils.Parsers.StructuredType.StructuredTypeArray">StructuredTypeArray</a>
Represents an array of objects defined by the StructuredType spec provided
mostly useful as it dispatches to NumPy where things are simple enough to do so

It has a system to dispatch intelligently based on the type of array provided
The kinds of structures supported are: OrderedDict, list, and np.ndarray

A _simple_ StructuredTypeArray is one that can just be represented as a single np.ndarray
A _compound_ StructuredTypeArray requires either a list or OrderedDict of StructuredTypeArray subarrays

### Properties and Methods
```python
is_simple: property
dict_like: property
extension_axis: property
shape: property
block_size: property
append_depth: property
dtype: property
stype: property
array: property
has_indeterminate_shape: property
filled_to: property
```
<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__init__">&nbsp;</a>
```python
__init__(self, stype, num_elements=50, padding_mode='fill', padding_value=None): 
```

- `stype`: `StructuredType`
    >No description...
- `num_elements`: `int`
    >number of default elements in dynamically sized arrays

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.axis_shape_indeterminate">&nbsp;</a>
```python
axis_shape_indeterminate(self, axis): 
```
Tries to determine if an axis has had any data placed into it or otherwise been given a determined shape
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.set_filling">&nbsp;</a>
```python
set_filling(self, amt, axis=0): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.increment_filling">&nbsp;</a>
```python
increment_filling(self, inc=1, axis=0): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__len__">&nbsp;</a>
```python
__len__(self): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.empty_array">&nbsp;</a>
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

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.extend_array">&nbsp;</a>
```python
extend_array(self, axis=None): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__setitem__">&nbsp;</a>
```python
__setitem__(self, key, value): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.set_part">&nbsp;</a>
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

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.get_part">&nbsp;</a>
```python
get_part(self, item, use_full_array=True): 
```
If simple, delegates to NumPy, otherwise tries to recursively get parts...?
        Unclear how slicing is best handled here.
- `item`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.add_axis">&nbsp;</a>
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

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.can_cast">&nbsp;</a>
```python
can_cast(self, val): 
```
Determines whether val can probably be cast to the right return type and shape without further processing or if that's definitely not possible
- `val`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.append">&nbsp;</a>
```python
append(self, val, axis=0): 
```
Puts val in the first empty slot in the array
- `val`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.extend">&nbsp;</a>
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

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.fill">&nbsp;</a>
```python
fill(self, array): 
```
Sets the result array to be the passed array
- `array`: `str | np.ndarray`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.cast_to_array">&nbsp;</a>
```python
cast_to_array(self, txt): 
```
Casts a string of things with a given data type to an array of that type and does some optional
        shape coercion
- `txt`: `str | iterable[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StructuredType.StructuredTypeArray.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/StructuredType/StructuredTypeArray.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/StructuredType/StructuredTypeArray.md)