## <a id="McUtils.Coordinerds.CoordinateSystems.CommonCoordinateSystems.InternalCoordinateSystem">InternalCoordinateSystem</a>
Represents Internal coordinates generally

### Properties and Methods
```python
name: str
```
<a id="McUtils.Coordinerds.CoordinateSystems.CommonCoordinateSystems.InternalCoordinateSystem.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, dimension=None, coordinate_shape=None, converter_options=None, **opts): 
```

- `converter_options`: `None | dict`
    >options to be passed through to a `CoordinateSystemConverter`
- `coordinate_shape`: `Iterable[None | int]`
    >shape of a single coordinate in this coordiante system
- `dimension`: `Iterable[None | int]`
    >the dimension of the coordinate system
- `opts`: `Any`
    >other options, if `converter_options` is None, these are used as the `converter_options`

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CommonCoordinateSystems/InternalCoordinateSystem.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CommonCoordinateSystems/InternalCoordinateSystem.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CommonCoordinateSystems/InternalCoordinateSystem.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CommonCoordinateSystems/InternalCoordinateSystem.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateSystems/CommonCoordinateSystems.py?message=Update%20Docs)