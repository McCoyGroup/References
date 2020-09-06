## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D">FiniteDifference1D</a>
A one-dimensional finite difference derivative object.
Higher-dimensional derivatives are built by chaining these.

### Properties and Methods
```python
get_stencil: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, finite_difference_data, matrix): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.widths" class="docs-object-method">&nbsp;</a>
```python
@property
widths(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.apply" class="docs-object-method">&nbsp;</a>
```python
apply(self, vals, val_dim=None, axis=0, mesh_spacing=None): 
```
Applies the held `FiniteDifferenceMatrix` to the array of values
- `vals`: `np.ndarray | sparse.csr_matrix`
    >values to do the difference over
- `val_dim`: `int`
    >dimensions of the vals
- `axis`: `int | tuple[int]`
    >the axis to apply along
- `mesh_spacing`: `float`
    >the mesh spacing for the weights
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.sparse_tensordot" class="docs-object-method">&nbsp;</a>
```python
sparse_tensordot(sparse, mat, axis): 
```
Not sure how fast this will be, but does a very simple contraction of `mat` along `axis` by the final axis of `sparse`

        Heavily de-generalized from here: https://github.com/pydata/sparse/blob/9dc40e15a04eda8d8efff35dfc08950b4c07a810/sparse/_coo/common.py
- `sparse`: `sparse.sparsemat`
    >No description...
- `mat`: `np.ndarray`
    >No description...
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D">FiniteDifference1D</a>
A one-dimensional finite difference derivative object.
Higher-dimensional derivatives are built by chaining these.

### Properties and Methods
```python
get_stencil: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, finite_difference_data, matrix): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.order" class="docs-object-method">&nbsp;</a>
```python
@property
order(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.weights" class="docs-object-method">&nbsp;</a>
```python
@property
weights(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.widths" class="docs-object-method">&nbsp;</a>
```python
@property
widths(self): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.apply" class="docs-object-method">&nbsp;</a>
```python
apply(self, vals, val_dim=None, axis=0, mesh_spacing=None): 
```
Applies the held `FiniteDifferenceMatrix` to the array of values
- `vals`: `np.ndarray | sparse.csr_matrix`
    >values to do the difference over
- `val_dim`: `int`
    >dimensions of the vals
- `axis`: `int | tuple[int]`
    >the axis to apply along
- `mesh_spacing`: `float`
    >the mesh spacing for the weights
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.sparse_tensordot" class="docs-object-method">&nbsp;</a>
```python
sparse_tensordot(sparse, mat, axis): 
```
Not sure how fast this will be, but does a very simple contraction of `mat` along `axis` by the final axis of `sparse`

        Heavily de-generalized from here: https://github.com/pydata/sparse/blob/9dc40e15a04eda8d8efff35dfc08950b4c07a810/sparse/_coo/common.py
- `sparse`: `sparse.sparsemat`
    >No description...
- `mat`: `np.ndarray`
    >No description...
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)

___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)