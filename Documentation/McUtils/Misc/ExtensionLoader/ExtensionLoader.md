## <a id="McUtils.Misc.ExtensionLoader.ExtensionLoader">ExtensionLoader</a>
An ExtensionLoader creates a Loader object that can load a python module from a file path

### Properties and Methods
```python
__init__(self, rootdir='', rootpkg=None): 
```

- `rootdir`: `str`
    >root directory to look for files off of
- `rootpkg`: `str or None`
    >root package to look for files off of

```python
get_data(self, file): 
```

```python
get_filename(self, fullname): 
```

```python
get_spec(self, file, pkg=None): 
```

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
