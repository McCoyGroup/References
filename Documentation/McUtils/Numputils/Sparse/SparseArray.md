## <a id="McUtils.Numputils.Sparse.SparseArray">SparseArray</a>
Array class that generalize the regular `scipy.sparse`
Basically acts like a high-dimensional wrapper that manages the _shape_ of a standard `scipy.sparse_matrix`, since that is rigidly 2D.

### Properties and Methods
```python
from_diag: method
data: property
fmt: property
shape: property
ndim: property
block_data: property
```
<a id="McUtils.Numputils.Sparse.SparseArray.__init__">&nbsp;</a>
```python
__init__(self, a, shape=None, layout=<class 'scipy.sparse.csc.csc_matrix'>, initialize=True): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.toarray">&nbsp;</a>
```python
toarray(self): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.todense">&nbsp;</a>
```python
todense(self): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.transpose">&nbsp;</a>
```python
transpose(self, transp): 
```
Transposes the array and returns a new one. Not necessarily a cheap operation.
- `transp`: `Iterable[int]`
    >the transposition to do
- `:returns`: `_`
    >No description...

<a id="McUtils.Numputils.Sparse.SparseArray.reshape">&nbsp;</a>
```python
reshape(self, shp): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.squeeze">&nbsp;</a>
```python
squeeze(self): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__matmul__">&nbsp;</a>
```python
__matmul__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.dot">&nbsp;</a>
```python
dot(self, b, reverse=False): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.tensordot">&nbsp;</a>
```python
tensordot(self, b, axes=2, reverse=False): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__add__">&nbsp;</a>
```python
__add__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.plus">&nbsp;</a>
```python
plus(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.floopy_flop">&nbsp;</a>
```python
floopy_flop(self): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__truediv__">&nbsp;</a>
```python
__truediv__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__rtruediv__">&nbsp;</a>
```python
__rtruediv__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__rmul__">&nbsp;</a>
```python
__rmul__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__mul__">&nbsp;</a>
```python
__mul__(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.multiply">&nbsp;</a>
```python
multiply(self, other): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Numputils.Sparse.SparseArray.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Numputils/Sparse/SparseArray.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Numputils/Sparse/SparseArray.md)