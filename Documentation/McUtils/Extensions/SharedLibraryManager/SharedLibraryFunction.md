## <a id="McUtils.Extensions.SharedLibraryManager.SharedLibraryFunction">SharedLibraryFunction</a>
An object that provides a way to call into a shared library function

### Properties and Methods
```python
InDir: type
lib: property
```
<a id="McUtils.Extensions.SharedLibraryManager.SharedLibraryFunction.__init__">&nbsp;</a>
```python
__init__(self, shared_library, function, signature, call_directory=None, docstring=None): 
```

- `shared_library`: `str |`
    >the path to the shared library file you want to use
- `function_name`: `str | callable`
    >the name of the function
- `call_signature`: `ArgumentSignature`
    >the call signature of the function
- `call_directory`: `str`
    >the directory for calling
- `docstring`: `str`
    >the docstring for the function

<a id="McUtils.Extensions.SharedLibraryManager.SharedLibraryFunction.initialize">&nbsp;</a>
```python
initialize(self): 
```

<a id="McUtils.Extensions.SharedLibraryManager.SharedLibraryFunction.call_single">&nbsp;</a>
```python
call_single(self, **kwargs): 
```
Calls the function on a single set of coordinates
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Extensions/SharedLibraryManager/SharedLibraryFunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Extensions/SharedLibraryManager/SharedLibraryFunction.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Extensions/SharedLibraryManager.py?message=Update%20Docs)