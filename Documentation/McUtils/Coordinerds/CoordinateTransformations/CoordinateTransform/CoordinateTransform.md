## <a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform">CoordinateTransform</a>
The CoordinateTransform class provides a simple, general way to represent a
compound coordinate transformation.
In general, it's basically just a wrapper chaining together a number of TransformationFunctions.

### Properties and Methods
```python
transformation_function: property
transforms: property
```
<a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform.__init__">&nbsp;</a>
```python
__init__(self, *transforms): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform.apply">&nbsp;</a>
```python
apply(self, coords): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform.__call__">&nbsp;</a>
```python
__call__(self, coords): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform.condense_transforms">&nbsp;</a>
```python
condense_transforms(self): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.CoordinateTransform.CoordinateTransform.parse_transform">&nbsp;</a>
```python
parse_transform(tf): 
```
Provides a way to "tag" a transformation
- `tf`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/CoordinateTransform/CoordinateTransform.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/CoordinateTransform/CoordinateTransform.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateTransformations/CoordinateTransform.py?message=Update%20Docs)