## <a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature">ArgumentSignature</a>
Defines an argument signature for a C-level caller

### Properties and Methods
<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *args, return_type=None): 
```

- `args`: `Iterable[tuple]`
    >the set of argument types to be passed into the caller

<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.build_argument" class="docs-object-method">&nbsp;</a>
```python
build_argument(self, argtup, which=None): 
```
Converts an argument tuple into an Argument object
- `argtup`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.args" class="docs-object-method">&nbsp;</a>
```python
@property
args(self): 
```

<a id="McUtils.Extensions.SharedLibraryManager.ArgumentSignature.return_type" class="docs-object-method">&nbsp;</a>
```python
@property
return_type(self): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Extensions/SharedLibraryManager/ArgumentSignature.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Extensions/SharedLibraryManager.py?message=Update%20Docs)