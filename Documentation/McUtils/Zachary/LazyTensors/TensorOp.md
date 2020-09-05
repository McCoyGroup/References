## <a id="McUtils.Zachary.LazyTensors.TensorOp">TensorOp</a>
A lazy representation of tensor operations to save memory

### Properties and Methods
<a id="McUtils.Zachary.LazyTensors.TensorOp.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, a, b, axis=None): 
```

<a id="McUtils.Zachary.LazyTensors.TensorOp.op" class="docs-object-method">&nbsp;</a>
```python
op(self, a, b): 
```

<a id="McUtils.Zachary.LazyTensors.TensorOp.get_shape" class="docs-object-method">&nbsp;</a>
```python
get_shape(self, a, b): 
```

<a id="McUtils.Zachary.LazyTensors.TensorOp.shape" class="docs-object-method">&nbsp;</a>
```python
@property
shape(self): 
```

<a id="McUtils.Zachary.LazyTensors.TensorOp.array" class="docs-object-method">&nbsp;</a>
```python
@property
array(self): 
```
Ought to always compile down to a proper ndarray
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Zachary.LazyTensors.TensorOp.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, i): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/LazyTensors/TensorOp.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/LazyTensors/TensorOp.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/LazyTensors/TensorOp.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/LazyTensors/TensorOp.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/LazyTensors.py?message=Update%20Docs)