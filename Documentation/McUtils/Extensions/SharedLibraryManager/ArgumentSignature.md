## <a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature">ArgumentSignature</a>
Defines an argument signature for a C-level caller

### Properties and Methods
```python
args: property
return_type: property
```
<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.__init__">&nbsp;</a>
```python
__init__(self, *args, return_type=None): 
```

- `args`: `Iterable[tuple]`
    >the set of argument types to be passed into the caller

<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.build_argument">&nbsp;</a>
```python
build_argument(self, argtup, which=None): 
```
Converts an argument tuple into an Argument object
- `argtup`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Extensions/SharedLibraryManager.py?message=Update%20Docs)