## <a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystemConverter.CoordinateSystemConverter">CoordinateSystemConverter</a>
A base class for type converters

### Properties and Methods
<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystemConverter.CoordinateSystemConverter.types" class="docs-object-method">&nbsp;</a>
```python
@property
types(self): 
```
The types property of a converter returns the types the converter converts

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystemConverter.CoordinateSystemConverter.convert_many" class="docs-object-method">&nbsp;</a>
```python
convert_many(self, coords_list, **kwargs): 
```
Converts many coordinates. Used in cases where a CoordinateSet has higher dimension
        than its basis dimension. Should be overridden by a converted to provide efficient conversions
        where necessary.
- `coords_list`: `np.ndarray`
    >many sets of coords
- `kwargs`: `Any`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystemConverter.CoordinateSystemConverter.convert" class="docs-object-method">&nbsp;</a>
```python
convert(self, coords, **kwargs): 
```
The main necessary implementation method for a converter class.
        Provides the actual function that converts the coords set
- `coords`: `np.ndarray`
    >No description...
- `kwargs`: `Any`
    >No description...

<a id="McUtils.Coordinerds.CoordinateSystems.CoordinateSystemConverter.CoordinateSystemConverter.register" class="docs-object-method">&nbsp;</a>
```python
register(self): 
```
Registers the CoordinateSystemConverter
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverter.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverter.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateSystems/CoordinateSystemConverter.py?message=Update%20Docs)