## <a id="McUtils.Zachary.LazyTensors.Tensor">Tensor</a>
A semi-symbolic representation of a tensor. Allows for lazy processing of tensor operations.

### Properties and Methods
```python
from_array: method
```
<a id="McUtils.Zachary.LazyTensors.Tensor.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, a, shape=None): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.array" class="docs-object-method">&nbsp;</a>
```python
@property
array(self): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.get_shape" class="docs-object-method">&nbsp;</a>
```python
get_shape(self, a): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.shape" class="docs-object-method">&nbsp;</a>
```python
@property
shape(self): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.get_dim" class="docs-object-method">&nbsp;</a>
```python
get_dim(self): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.dim" class="docs-object-method">&nbsp;</a>
```python
@property
dim(self): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.add" class="docs-object-method">&nbsp;</a>
```python
add(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.mul" class="docs-object-method">&nbsp;</a>
```python
mul(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.dot" class="docs-object-method">&nbsp;</a>
```python
dot(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.transpose" class="docs-object-method">&nbsp;</a>
```python
transpose(self, axes, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.pow" class="docs-object-method">&nbsp;</a>
```python
pow(self, other, **kw): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__mul__" class="docs-object-method">&nbsp;</a>
```python
__mul__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__rmul__" class="docs-object-method">&nbsp;</a>
```python
__rmul__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__add__" class="docs-object-method">&nbsp;</a>
```python
__add__(self, other): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__pow__" class="docs-object-method">&nbsp;</a>
```python
__pow__(self, power, modulo=None): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.handle_missing_indices" class="docs-object-method">&nbsp;</a>
```python
handle_missing_indices(self, missing, extant): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.pull_index" class="docs-object-method">&nbsp;</a>
```python
pull_index(self, *idx): 
```
Defines custom logic for handling how we pull indices
- `idx`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.LazyTensors.Tensor.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Zachary.LazyTensors.Tensor.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/LazyTensors/Tensor.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/LazyTensors/Tensor.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/LazyTensors.py?message=Update%20Docs)