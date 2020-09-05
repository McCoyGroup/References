## <a id="McUtils.Coordinerds.CoordinateTransformations.TransformationFunction.TransformationFunction">TransformationFunction</a>
The TransformationFunction class is an abstract class
It provides the scaffolding for representing a single transformation operation

### Properties and Methods
<a id="McUtils.Coordinerds.CoordinateTransformations.TransformationFunction.TransformationFunction.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self): 
```
Initializes a transformation function based on the transfdata
- `transfdata`: `Any`
    >No description...

<a id="McUtils.Coordinerds.CoordinateTransformations.TransformationFunction.TransformationFunction.merge" class="docs-object-method">&nbsp;</a>
```python
merge(self, other): 
```
Tries to merge with another TransformationFunction
- `other`: `TransformationFunction`
    >a TransformationFunction to try to merge with
- `:returns`: `TransformationFunction`
    >tfunc

<a id="McUtils.Coordinerds.CoordinateTransformations.TransformationFunction.TransformationFunction.operate" class="docs-object-method">&nbsp;</a>
```python
operate(self, coords): 
```
Operates on the coords. *Must* be able to deal with a list of coordinates, optimally in an efficient manner
- `coords`: `np.ndarry`
    >the list of coordinates to apply the transformation to

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/TransformationFunction/TransformationFunction.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds/CoordinateTransformations/TransformationFunction/TransformationFunction.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/CoordinateTransformations/TransformationFunction.py?message=Update%20Docs)