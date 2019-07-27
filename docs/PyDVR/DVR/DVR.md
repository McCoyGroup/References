## <a id=PyDVR.DVR.DVR>DVR</a>
This is a manager class for working with DVRs

It uses files from which it loads the spec data and methods
Currently all defaults are for 1D but the ND extension shouldn't be bad

```python
loaded_DVRs: dict
dvr_dir: str
dvr_file: method
load_dvr: method
```
<a id=PyDVR.DVR.DVR.__init__>&nbsp;</a>
```python
__init__(self, dvr_file='ColbertMiller1D', **kwargs): 
```

<a id=PyDVR.DVR.DVR.domain>&nbsp;</a>
```python
domain(self): 
```

<a id=PyDVR.DVR.DVR.divs>&nbsp;</a>
```python
divs(self): 
```

<a id=PyDVR.DVR.DVR.grid>&nbsp;</a>
```python
grid(self): 
```

<a id=PyDVR.DVR.DVR.kinetic_energy>&nbsp;</a>
```python
kinetic_energy(self): 
```

<a id=PyDVR.DVR.DVR.potential_energy>&nbsp;</a>
```python
potential_energy(self): 
```

<a id=PyDVR.DVR.DVR.hamiltonian>&nbsp;</a>
```python
hamiltonian(self): 
```

<a id=PyDVR.DVR.DVR.wavefunctions>&nbsp;</a>
```python
wavefunctions(self): 
```

<a id=PyDVR.DVR.DVR.run>&nbsp;</a>
```python
run(self, **runpars): 
```
