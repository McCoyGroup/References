## <a id="McUtils.Zachary.LazyTensors.Tensor">Tensor</a>
A semi-symbolic representation of a tensor. Allows for lazy processing of tensor operations.

### Properties and Methods
```python
from_array: method
array: property
shape: property
dim: property
```
<a id="McUtils.Zachary.LazyTensors.Tensor.__init__">&nbsp;</a>
```python
__init__(self, a, shape=None): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.get_shape">&nbsp;</a>
```python
get_shape(self, a): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.get_dim">&nbsp;</a>
```python
get_dim(self): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.add">&nbsp;</a>
```python
add(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.mul">&nbsp;</a>
```python
mul(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.dot">&nbsp;</a>
```python
dot(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.transpose">&nbsp;</a>
```python
transpose(self, axes, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.pow">&nbsp;</a>
```python
pow(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__mul__">&nbsp;</a>
```python
__mul__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__rmul__">&nbsp;</a>
```python
__rmul__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__add__">&nbsp;</a>
```python
__add__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__pow__">&nbsp;</a>
```python
__pow__(self, power, modulo=None): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.handle_missing_indices">&nbsp;</a>
```python
handle_missing_indices(self, missing, extant): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.pull_index">&nbsp;</a>
```python
pull_index(self, *idx): 
```
Defines custom logic for handling how we pull indices
- `idx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.LazyTensors.Tensor.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/LazyTensors/Tensor.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/LazyTensors/Tensor.md)