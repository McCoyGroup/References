## <a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet">CoordinateSet</a>
A subclass of np.ndarray that lives in an explicit coordinate system and can convert between them

### Properties and Methods
```python
multiconfig: property
```
<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.__new__">&nbsp;</a>
```python
__new__(cls, coords, system=CoordinateSystem(Cartesian3D, dimension=(None, 3), matrix=None), converter_options=None): 
```

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.__init__">&nbsp;</a>
```python
__init__(self, coords, system=CoordinateSystem(Cartesian3D, dimension=(None, 3), matrix=None), converter_options=None): 
```

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.__array_finalize__">&nbsp;</a>
```python
__array_finalize__(self, coords): 
```

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.__str__">&nbsp;</a>
```python
__str__(self): 
```

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.__eq__">&nbsp;</a>
```python
__eq__(self, other): 
```

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.transform">&nbsp;</a>
```python
transform(self, tf): 
```
Applies a transformation to the stored coordinates
- `tf`: `Any`
    >the transformation function to apply to the system
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.convert">&nbsp;</a>
```python
convert(self, system, **kw): 
```
Converts across coordinate systems
- `system`: `CoordinateSystem`
    >the target coordinate system
- `:returns`: `CoordinateSet`
    >new_coords

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.derivatives">&nbsp;</a>
```python
derivatives(self, function, order=1, coordinates=None, result_shape=None, **fd_options): 
```
Takes derivatives of `function` with respect to the current geometry
- `function`: `Any`
    >No description...
- `order`: `Any`
    >No description...
- `coordinates`: `Any`
    >No description...
- `fd_options`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSet.CoordinateSet.jacobian">&nbsp;</a>
```python
jacobian(self, system, order=1, coordinates=None, converter_options=None, **fd_options): 
```
Delegates to the jacobian function of the current coordinate system
- `system`: `Any`
    >No description...
- `order`: `Any`
    >No description...
- `mesh_spacing`: `Any`
    >No description...
- `prep`: `Any`
    >No description...
- `coordinates`: `Any`
    >No description...
- `fd_options`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSet/CoordinateSet.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSet/CoordinateSet.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateSystems/CoordinateSet.py?message=Update%20Docs)