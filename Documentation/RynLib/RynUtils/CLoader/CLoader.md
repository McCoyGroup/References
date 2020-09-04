## <a id="RynLib.RynUtils.CLoader.CLoader">CLoader</a>
A general loader for C++ extensions to python, based off of the kind of thing that I have had to do multiple times

### Properties and Methods
```python
src_dir: property
lib_lib_dir: property
```
<a id="RynLib.RynUtils.CLoader.CLoader.__init__">&nbsp;</a>
```python
__init__(self, lib_name, lib_dir, load_path=None, src_ext='src', description='An extension module', version='1.0.0', include_dirs=None, runtime_dirs=None, linked_libs=None, macros=None, extra_link_args=None, extra_compile_args=None, extra_objects=None, source_files=None, build_script=None, requires_make=False, out_dir=None, cleanup_build=True): 
```

<a id="RynLib.RynUtils.CLoader.CLoader.load">&nbsp;</a>
```python
load(self): 
```

<a id="RynLib.RynUtils.CLoader.CLoader.find_extension">&nbsp;</a>
```python
find_extension(self): 
```
Tries to find the extension in the top-level directory
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.compile_extension">&nbsp;</a>
```python
compile_extension(self): 
```
Compiles and loads a C++ extension
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.get_extension">&nbsp;</a>
```python
get_extension(self): 
```
Gets the Extension module to be compiled
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.custom_make">&nbsp;</a>
```python
custom_make(self, make_file, make_dir): 
```
A way to call a custom make file either for building the helper lib or for building the proper lib
- `make_file`: `Any`
    >No description...
- `make_dir`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.make_required_libs">&nbsp;</a>
```python
make_required_libs(self): 
```
Makes any libs required by the current one
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.build_lib">&nbsp;</a>
```python
build_lib(self): 
```

<a id="RynLib.RynUtils.CLoader.CLoader.locate_lib">&nbsp;</a>
```python
locate_lib(self, root=None): 
```
Tries to locate the build library file (if it exists)
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.CLoader.CLoader.cleanup">&nbsp;</a>
```python
cleanup(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/RynUtils/CLoader/CLoader.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/RynUtils/CLoader/CLoader.md)