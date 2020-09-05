## <a id="RynLib.PlzNumbers.Potential.Potential">Potential</a>
A very general wrapper to a potential:
Can take a potential _directory_ and compile that down
Can take a potential source and write the necessary template code around that for use
ides a hook into PotentialCaller once the data has been loaded to directly call the potential like a function

### Properties and Methods
```python
caller: property
mpi_manager: property
args: property
```
<a id="RynLib.PlzNumbers.Potential.Potential.__init__">&nbsp;</a>
```python
__init__(self, name=None, potential_source=None, atom_pattern=None, working_directory=None, wrap_potential=None, function_name=None, raw_array_potential=None, arguments=None, shim_script='', conversion=None, potential_directory=None, static_source=False, extra_functions=(), src_ext='src', description='An extension module', verion='1.0.0', include_dirs=None, linked_libs=None, macros=None, source_files=None, build_script=None, requires_make=False, out_dir=None, cleanup_build=True, python_potential=False, pointer_name=None, fortran_potential=False, bad_walker_file='bad_walkers.txt', mpi_manager=None, vectorized_potential=False, error_value=10000000000.0, transpose_call=None): 
```

- `name`: `Any`
    >No description...
- `potential_source`: `Any`
    >No description...
- `wrap_potential`: `Any`
    >No description...
- `function_name`: `Any`
    >No description...
- `raw_array_potential`: `Any`
    >No description...
- `arguments`: `Any`
    >No description...
- `potential_directory`: `Any`
    >No description...
- `static_source`: `Any`
    >No description...
- `extra_functions`: `Any`
    >No description...
- `src_ext`: `Any`
    >No description...
- `description`: `Any`
    >No description...
- `verion`: `Any`
    >No description...
- `include_dirs`: `Any`
    >No description...
- `linked_libs`: `Any`
    >No description...
- `macros`: `Any`
    >No description...
- `source_files`: `Any`
    >No description...
- `build_script`: `Any`
    >No description...
- `requires_make`: `Any`
    >No description...
- `out_dir`: `Any`
    >No description...
- `cleanup_build`: `Any`
    >No description...
- `python_potential`: `Any`
    >No description...
- `bad_walker_file`: `Any`
    >No description...
- `mpi_manager`: `Any`
    >No description...
- `vectorized_potential`: `Any`
    >No description...
- `error_value`: `Any`
    >No description...

<a id="RynLib.PlzNumbers.Potential.Potential.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

<a id="RynLib.PlzNumbers.Potential.Potential.clean_up">&nbsp;</a>
```python
clean_up(self): 
```

<a id="RynLib.PlzNumbers.Potential.Potential.bind_atoms">&nbsp;</a>
```python
bind_atoms(self, atoms): 
```

<a id="RynLib.PlzNumbers.Potential.Potential.bind_arguments">&nbsp;</a>
```python
bind_arguments(self, args): 
```

<a id="RynLib.PlzNumbers.Potential.Potential.__call__">&nbsp;</a>
```python
__call__(self, coordinates, *extra_args, **extra_kwargs): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/PlzNumbers/Potential/Potential.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/PlzNumbers/Potential/Potential.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/RynLib/edit/master/PlzNumbers/Potential.py?message=Update%20Docs)