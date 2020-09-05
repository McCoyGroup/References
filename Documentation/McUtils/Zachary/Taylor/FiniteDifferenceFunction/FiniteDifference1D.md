## <a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D">FiniteDifference1D</a>


### Properties and Methods
```python
order: property
weights: property
widths: property
get_stencil: method
```
<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.__init__">&nbsp;</a>
```python
__init__(self, finite_difference_data, matrix): 
```

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.apply">&nbsp;</a>
```python
apply(self, vals, val_dim=None, axis=0, mesh_spacing=None): 
```
Applies the held FiniteDifferenceMatrix to the array of values
- `vals`: `np.ndarray | sparse.csr_matrix`
    >values to do the difference over
- `val_dim`: `int`
    >dimensions of the vals
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Taylor.FiniteDifferenceFunction.FiniteDifference1D.sparse_tensordot">&nbsp;</a>
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

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Taylor/FiniteDifferenceFunction.py?message=Update%20Docs)