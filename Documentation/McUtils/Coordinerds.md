# <a id="McUtils.Coordinerds">McUtils.Coordinerds</a>
    
The Coordinerds package implements stuff for dealing with coordinates and generalized coordinate systems

It provides a semi-symbolic way to represent a CoordinateSystem and a CoordinateSet that provides coordinates within a
coordinate system. An extensible system for converting between coordinate systems and is provided.

The basic design of the package is set up so that one creates a `CoordinateSet` object, which in turn tracks its `CoordinateSystem`.
A `CoordinateSet` is a subclass of `np.ndarray`, and so any operation that works for a `np.ndarray` will work in turn for `CoordinateSet`.
This provides a large amount flexibility.

The `CoordinateSystem` object handles much of the heavy lifting for a `CoordinateSet`.
Conversions between different systems are implemented by a `CoordinateSystemConverter`.
Chained conversions are not _currently_ supported, but might well become supported in the future.

### Members:

  - [CoordinateSet](Coordinerds/CoordinateSystems/CoordinateSet/CoordinateSet.md)
  - [CartesianCoordinateSystem](Coordinerds/CoordinateSystems/CommonCoordinateSystems/CartesianCoordinateSystem.md)
  - [InternalCoordinateSystem](Coordinerds/CoordinateSystems/CommonCoordinateSystems/InternalCoordinateSystem.md)
  - [CartesianCoordinateSystem3D](Coordinerds/CoordinateSystems/CommonCoordinateSystems/CartesianCoordinateSystem3D.md)
  - [CartesianCoordinates3D](Coordinerds/CoordinateSystems/CommonCoordinateSystems/CartesianCoordinates3D.md)
  - [SphericalCoordinateSystem](Coordinerds/CoordinateSystems/CommonCoordinateSystems/SphericalCoordinateSystem.md)
  - [SphericalCoordinates](Coordinerds/CoordinateSystems/CommonCoordinateSystems/SphericalCoordinates.md)
  - [ZMatrixCoordinateSystem](Coordinerds/CoordinateSystems/CommonCoordinateSystems/ZMatrixCoordinateSystem.md)
  - [ZMatrixCoordinates](Coordinerds/CoordinateSystems/CommonCoordinateSystems/ZMatrixCoordinates.md)
  - [CoordinateSystem](Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystem.md)
  - [BaseCoordinateSystem](Coordinerds/CoordinateSystems/CoordinateSystem/BaseCoordinateSystem.md)
  - [CoordinateSystemError](Coordinerds/CoordinateSystems/CoordinateSystem/CoordinateSystemError.md)
  - [CoordinateSystemConverters](Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverters.md)
  - [CoordinateSystemConverter](Coordinerds/CoordinateSystems/CoordinateSystemConverter/CoordinateSystemConverter.md)
  - [CoordinateTransform](Coordinerds/CoordinateTransformations/CoordinateTransform/CoordinateTransform.md)
  - [TransformationFunction](Coordinerds/CoordinateTransformations/TransformationFunction/TransformationFunction.md)
  - [AffineTransform](Coordinerds/CoordinateTransformations/AffineTransform/AffineTransform.md)
  - [TranslationTransform](Coordinerds/CoordinateTransformations/TranslationTransform/TranslationTransform.md)
  - [RotationTransform](Coordinerds/CoordinateTransformations/RotationTransform/RotationTransform.md)

### Examples:



___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Coordinerds.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Coordinerds.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Coordinerds.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Coordinerds.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Coordinerds/__init__.py?message=Update%20Docs)