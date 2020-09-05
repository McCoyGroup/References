## <a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller">PotentialCaller</a>
Takes a pointer to a C++ potential calls this potential on a set of geometries / atoms / whatever

### Properties and Methods
```python
load_lib: method
reload: method
PoolPotential: type
```
<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, potential, *ignore, bad_walker_file='bad_walkers.txt', mpi_manager=None, raw_array_potential=None, vectorized_potential=False, error_value=10000000000.0, fortran_potential=False, transpose_call=None): 
```

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.lib" class="docs-object-method">&nbsp;</a>
```python
@property
lib(self): 
```

- `:returns`: `module`
    >No description...

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.call_single" class="docs-object-method">&nbsp;</a>
```python
call_single(self, walker, atoms, extra_bools=(), extra_ints=(), extra_floats=()): 
```

- `walker`: `np.ndarray`
    >No description...
- `atoms`: `List[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.mpi_manager" class="docs-object-method">&nbsp;</a>
```python
@property
mpi_manager(self): 
```

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.clean_up" class="docs-object-method">&nbsp;</a>
```python
clean_up(self): 
```

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.call_multiple" class="docs-object-method">&nbsp;</a>
```python
call_multiple(self, walker, atoms, extra_bools=(), extra_ints=(), extra_floats=()): 
```

- `walker`: `np.ndarray`
    >No description...
- `atoms`: `List[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, walkers, atoms, *extra_args): 
```

- `walker`: `np.ndarray`
    >No description...
- `atoms`: `List[str]`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/PlzNumbers/PotentialCaller/PotentialCaller.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/PlzNumbers/PotentialCaller/PotentialCaller.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/RynLib/edit/master/PlzNumbers/PotentialCaller.py?message=Update%20Docs)