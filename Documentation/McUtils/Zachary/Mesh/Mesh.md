## <a id="McUtils.Zachary.Mesh.Mesh">Mesh</a>
A general Mesh class representing data points in n-dimensions in either a structured or unstructured manner

### Properties and Methods
```python
mesh_spacings: property
subgrids: property
dimension: property
npoints: property
gridpoints: property
get_npoints: method
get_gridpoints: method
get_mesh_subgrids: method
get_mesh_spacings: method
get_mesh_type: method
RegularMesh: method
```
<a id="McUtils.Zachary.Mesh.Mesh.__new__">&nbsp;</a>
```python
__new__(cls, data, mesh_type=None): 
```

- `griddata`: `np.ndarray`
    >the raw grid-point data the mesh uses
- `mesh_type`: `None | str`
    >the type of mesh we have
- `opts`: `Any`
    >No description...

<a id="McUtils.Zachary.Mesh.Mesh.__init__">&nbsp;</a>
```python
__init__(self, *args, **kwargs): 
```

<a id="McUtils.Zachary.Mesh.Mesh.__array_finalize__">&nbsp;</a>
```python
__array_finalize__(self, mesh): 
```

<a id="McUtils.Zachary.Mesh.Mesh.get_slice_iter">&nbsp;</a>
```python
get_slice_iter(self, axis=-1): 
```
Returns an iterator over the slices of the mesh along the specified axis
- `axis`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Mesh/Mesh.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Mesh/Mesh.md)