## <a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem">CoordinateSystem</a>
A representation of a coordinate system. It doesn't do much on its own but it *does* provide a way
to unify internal, cartesian, derived type coordinates

### Properties and Methods
<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, name=None, basis=None, matrix=None, inverse=None, dimension=None, origin=None, coordinate_shape=None, jacobian_prep=None, converter_options=None): 
```
Sets up the CoordinateSystem object
- `name`: `str`
    >a name to give to the coordinate system
- `basis`: `Any`
    >a basis for the coordinate system
- `matrix`: `np.ndarray | None`
    >an expansion coefficient matrix for the set of coordinates in its basis
- `dimension`: `Iterable[None | int]`
    >the dimension of a single configuration in the coordinate system (for validation)
- `jacobian_prep`: `function | None`
    >a function for preparing coordinates to be used in computing the Jacobian
- `coordinate_shape`: `iterable[int]`
    >the actual shape of a single coordinate in the coordinate system

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.basis" class="docs-object-method">&nbsp;</a>
```python
@property
basis(self): 
```
The basis for the representation of `matrix`
- `:returns`: `CoordinateSystem`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.origin" class="docs-object-method">&nbsp;</a>
```python
@property
origin(self): 
```
The origin for the expansion defined by `matrix`
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.matrix" class="docs-object-method">&nbsp;</a>
```python
@property
matrix(self): 
```
The matrix representation in the CoordinateSystem.basis
        None is shorthand for the identity matrix
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.inverse" class="docs-object-method">&nbsp;</a>
```python
@property
inverse(self): 
```
The inverse of the representation in the `basis`
        None is shorthand for the inverse or pseudoinverse of `matrix`
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.dimension" class="docs-object-method">&nbsp;</a>
```python
@property
dimension(self): 
```
The dimension of the coordinate system
        None means unspecified dimension
- `:returns`: `int or None`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.converter" class="docs-object-method">&nbsp;</a>
```python
converter(self, system): 
```
Gets the converter from the current system to a new system
- `system`: `CoordinateSystem`
    >the target CoordinateSystem
- `:returns`: `CoordinateSystemConverter`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.convert_coords" class="docs-object-method">&nbsp;</a>
```python
convert_coords(self, coords, system, **kw): 
```
Converts coordiantes from the current coordinate system to _system_
- `coords`: `CoordinateSet`
    >No description...
- `system`: `CoordinateSystem`
    >No description...
- `kw`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.displacement" class="docs-object-method">&nbsp;</a>
```python
displacement(self, amts): 
```
Generates a displacement or matrix of displacements based on the vector or matrix amts
- `amts`: `np.ndarray`
    >No description...
- `:returns`: `np.ndarray`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.derivatives" class="docs-object-method">&nbsp;</a>
```python
derivatives(self, coords, function, order=1, coordinates=None, result_shape=None, **finite_difference_options): 
```
Computes derivatives for an arbitrary function with respect to this coordinate system
- `function`: `Any`
    >No description...
- `order`: `Any`
    >No description...
- `coordinates`: `Any`
    >No description...
- `finite_difference_options`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.jacobian" class="docs-object-method">&nbsp;</a>
```python
jacobian(self, coords, system, order=1, coordinates=None, converter_options=None, all_numerical=False, **finite_difference_options): 
```
Computes the Jacobian between the current coordinate system and a target coordinate system
- `system`: `CoordinateSystem`
    >the target CoordinateSystem
- `order`: `int | Iterable[int]`
    >the order of the Jacobian to compute, 1 for a standard, 2 for the Hessian, etc.
- `coordinates`: `None | iterable[iterable[int] | None`
    >a spec of which coordinates to generate derivatives for (None means all)
- `mesh_spacing`: `float | np.ndarray`
    >the spacing to use when displacing
- `prep`: `None | function`
    >a function for pre-validating the generated coordinate values and grids
- `fd_options`: `Any`
    >options to be passed straight through to FiniteDifferenceFunction
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystem.CoordinateSystem.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystem.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystem.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystem.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystem.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateSystems/CoordinateSystem.py?message=Update%20Docs)