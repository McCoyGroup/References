## <a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller">PotentialCaller</a>
Takes a pointer to a C++ potential calls this potential on a set of geometries / atoms / whatever

### Properties and Methods
```python
load_lib: method
reload: method
lib: property
PoolPotential: type
mpi_manager: property
```
<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.__init__">&nbsp;</a>
```python
__init__(self, potential, *ignore, bad_walker_file='bad_walkers.txt', mpi_manager=None, raw_array_potential=None, vectorized_potential=False, error_value=10000000000.0, fortran_potential=False): 
```

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.call_single">&nbsp;</a>
```python
call_single(self, walker, atoms, extra_bools=(), extra_ints=(), extra_floats=()): 
```

- `walker`: `np.ndarray`
    >No description...
- `atoms`: `List[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.clean_up">&nbsp;</a>
```python
clean_up(self): 
```

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.call_multiple">&nbsp;</a>
```python
call_multiple(self, walker, atoms, extra_bools=(), extra_ints=(), extra_floats=()): 
```

- `walker`: `np.ndarray`
    >No description...
- `atoms`: `List[str]`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.PlzNumbers.PotentialCaller.PotentialCaller.__call__">&nbsp;</a>
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
