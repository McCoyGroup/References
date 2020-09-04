## <a id="McUtils.Extensions.SharedLibraryManager.Argument">Argument</a>
Defines a single Argument for a C-level caller to support default values, etc.

### Properties and Methods
```python
type_map: dict
inverse_type_map: dict
infer_type: method
infer_array_type: method
inferred_type_string: method
```
<a id="McUtils.Extensions.SharedLibraryManager.Argument.__init__">&nbsp;</a>
```python
__init__(self, name, dtype, default=None, pointer_type=None, array_type=None): 
```

- `name`: `str`
    >the name of the argument
- `dtype`: `Any`
    >the type of the argument
- `default`: `Any`
    >the default value for the argument

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Extensions/SharedLibraryManager/Argument.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Extensions/SharedLibraryManager/Argument.md)