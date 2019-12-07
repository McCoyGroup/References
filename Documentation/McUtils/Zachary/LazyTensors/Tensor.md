## <a id="McUtils.Zachary.LazyTensors.Tensor">Tensor</a>
A semi-symbolic representation of a tensor. Allows for lazy processing of tensor operations.

### Properties and Methods
```python
from_array: method
array: property
dim: property
```
```python
__init__(self, a, shape=None): 
```

```python
get_dim(self): 
```

```python
add(self, other, **kw): 
```

```python
mul(self, other, **kw): 
```

```python
dot(self, other, **kw): 
```

```python
pow(self, other, **kw): 
```

```python
__mul__(self, other): 
```

```python
__rmul__(self, other): 
```

```python
__add__(self, other): 
```

```python
__pow__(self, power, modulo=None): 
```

```python
handle_missing_indices(self, missing, extant): 
```

```python
pull_index(self, *idx): 
```

```python
__getitem__(self, item): 
```

```python
__repr__(self): 
```

### Examples
