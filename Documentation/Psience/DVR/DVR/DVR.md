## <a id="Psience.DVR.DVR.DVR">DVR</a>
This is a manager class for working with DVRs

It uses files from which it loads the spec data and methods
Currently all defaults are for 1D but the ND extension shouldn't be bad

### Properties and Methods
```python
loaded_DVRs: dict
dvr_dir: str
dvr_file: method
load_dvr: method
Results: type
```
<a id="Psience.DVR.DVR.DVR.__init__">&nbsp;</a>
```python
__init__(self, dvr_file='ColbertMiller1D', **kwargs): 
```

<a id="Psience.DVR.DVR.DVR.domain">&nbsp;</a>
```python
domain(self): 
```
Computes the domain for the DVR

<a id="Psience.DVR.DVR.DVR.divs">&nbsp;</a>
```python
divs(self): 
```
Computes the divisions for the DVR

<a id="Psience.DVR.DVR.DVR.grid">&nbsp;</a>
```python
grid(self): 
```
Computes the grid for the DVR

<a id="Psience.DVR.DVR.DVR.kinetic_energy">&nbsp;</a>
```python
kinetic_energy(self): 
```
Computes the kinetic_energy for the DVR

<a id="Psience.DVR.DVR.DVR.potential_energy">&nbsp;</a>
```python
potential_energy(self): 
```
Computes the potential_energy for the DVR

<a id="Psience.DVR.DVR.DVR.hamiltonian">&nbsp;</a>
```python
hamiltonian(self): 
```
Computes the hamiltonian for the DVR

<a id="Psience.DVR.DVR.DVR.wavefunctions">&nbsp;</a>
```python
wavefunctions(self): 
```
Computes the wavefunctions for the DVR

<a id="Psience.DVR.DVR.DVR.run">&nbsp;</a>
```python
run(self, **runpars): 
```
Runs the DVR. Resets state after the run

### Examples
