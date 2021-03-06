## <a id="Psience.DVR.DVR.DVR">DVR</a>
This is a manager class for working with DVRs.
It uses files from which it loads the spec data and methods, which are placed in the `Classes` subfolder.

### Properties and Methods
```python
loaded_DVRs: dict
dvr_dir: str
dvr_file: method
load_dvr: method
Results: type
```
<a id="Psience.DVR.DVR.DVR.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, dvr_file='ColbertMiller1D', **kwargs): 
```

<a id="Psience.DVR.DVR.DVR.domain" class="docs-object-method">&nbsp;</a>
```python
domain(self): 
```

- `:returns`: `_`
    >the domain for the DVR

<a id="Psience.DVR.DVR.DVR.divs" class="docs-object-method">&nbsp;</a>
```python
divs(self): 
```

- `:returns`: `tuple(int)`
    >the number of DVR points

<a id="Psience.DVR.DVR.DVR.grid" class="docs-object-method">&nbsp;</a>
```python
grid(self): 
```

- `:returns`: `np.ndarray`
    >the grid for the DVR

<a id="Psience.DVR.DVR.DVR.kinetic_energy" class="docs-object-method">&nbsp;</a>
```python
kinetic_energy(self): 
```

- `:returns`: `np.ndarray`
    >the kinetic energy matrix

<a id="Psience.DVR.DVR.DVR.potential_energy" class="docs-object-method">&nbsp;</a>
```python
potential_energy(self): 
```

- `:returns`: `np.ndarray`
    >the potential energy matrix

<a id="Psience.DVR.DVR.DVR.hamiltonian" class="docs-object-method">&nbsp;</a>
```python
hamiltonian(self): 
```

- `:returns`: `np.ndarray`
    >the total Hamiltonian matrix

<a id="Psience.DVR.DVR.DVR.wavefunctions" class="docs-object-method">&nbsp;</a>
```python
wavefunctions(self): 
```

- `:returns`: `(np.ndarray, np.ndarray)`
    >the DVR wavefunctions

<a id="Psience.DVR.DVR.DVR.run" class="docs-object-method">&nbsp;</a>
```python
run(self, **runpars): 
```
Runs the DVR with the passed parameters, delegating most calls to the loaded class
- `runpars`: `Any`
    >No description...
- `:returns`: `DVR.Results`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/DVR/DVR/DVR.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/DVR/DVR/DVR.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Psience/DVR/DVR/DVR.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Psience/DVR/DVR/DVR.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Psience/edit/master/DVR/DVR.py?message=Update%20Docs)