## <a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform">AffineTransform</a>
A simple AffineTranform implementation of the TransformationFunction abstract base class

### Properties and Methods
<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, tmat, shift=None): 
```
tmat must be a transformation matrix to work properly
- `shift`: `np.ndarray | None`
    >the shift for the transformation
- `tmat`: `np.ndarray`
    >the matrix for the linear transformation

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.transform" class="docs-object-method">&nbsp;</a>
```python
@property
transform(self): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.shift" class="docs-object-method">&nbsp;</a>
```python
@property
shift(self): 
```

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.merge" class="docs-object-method">&nbsp;</a>
```python
merge(self, other): 
```

- `other`: `np.ndarray or AffineTransform`
    >No description...

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.reverse" class="docs-object-method">&nbsp;</a>
```python
reverse(self): 
```
Inverts the matrix
- `:returns`: `_`
    >No description...

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.operate" class="docs-object-method">&nbsp;</a>
```python
operate(self, coords): 
```

- `coords`: `np.ndarry`
    >the array of coordinates passed in

<a id="McUtils.Coordinerds.CoordinateTransformations.AffineTransform.AffineTransform.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/AffineTransform/AffineTransform.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/AffineTransform/AffineTransform.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Coordinerds/CoordinateTransformations/AffineTransform/AffineTransform.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Coordinerds/CoordinateTransformations/AffineTransform/AffineTransform.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateTransformations/AffineTransform.py?message=Update%20Docs)