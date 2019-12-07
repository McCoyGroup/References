## <a id="PyDVR.DVR.DVR">DVR</a>
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
```python
__init__(self, dvr_file='ColbertMiller1D', **kwargs): 
```

```python
domain(self): 
```
Computes the domain for the DVR

```python
divs(self): 
```
Computes the divisions for the DVR

```python
grid(self): 
```
Computes the grid for the DVR

```python
kinetic_energy(self): 
```
Computes the kinetic_energy for the DVR

```python
potential_energy(self): 
```
Computes the potential_energy for the DVR

```python
hamiltonian(self): 
```
Computes the hamiltonian for the DVR

```python
wavefunctions(self): 
```
Computes the wavefunctions for the DVR

```python
run(self, **runpars): 
```
Runs the DVR. Resets state after the run

### Examples
