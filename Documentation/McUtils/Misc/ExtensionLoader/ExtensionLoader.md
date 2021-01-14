## <a id="McUtils.Misc.ExtensionLoader.ExtensionLoader">ExtensionLoader</a>
An ExtensionLoader creates a Loader object that can load a python module from a file path

### Properties and Methods
<a id="McUtils.Misc.ExtensionLoader.ExtensionLoader.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, rootdir='', rootpkg=None): 
```

- `rootdir`: `str`
    >root directory to look for files off of
- `rootpkg`: `str or None`
    >root package to look for files off of

<a id="McUtils.Misc.ExtensionLoader.ExtensionLoader.get_data" class="docs-object-method">&nbsp;</a>
```python
get_data(self, file): 
```

<a id="McUtils.Misc.ExtensionLoader.ExtensionLoader.get_filename" class="docs-object-method">&nbsp;</a>
```python
get_filename(self, fullname): 
```

<a id="McUtils.Misc.ExtensionLoader.ExtensionLoader.get_spec" class="docs-object-method">&nbsp;</a>
```python
get_spec(self, file, pkg=None): 
```

<a id="McUtils.Misc.ExtensionLoader.ExtensionLoader.load" class="docs-object-method">&nbsp;</a>
```python
load(self, file, pkg=None): 
```
loads a file as a module with optional package name
- `file`: `str`
    >No description...
- `pkg`: `str or None`
    >No description...
- `:returns`: `module`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Misc/ExtensionLoader/ExtensionLoader.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Misc/ExtensionLoader/ExtensionLoader.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Misc/ExtensionLoader/ExtensionLoader.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Misc/ExtensionLoader/ExtensionLoader.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Misc/ExtensionLoader.py?message=Update%20Docs)