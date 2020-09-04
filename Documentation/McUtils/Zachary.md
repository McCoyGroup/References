# <a id="McUtils.Zachary">McUtils.Zachary</a>
    
Handles all of the "numerical math" stuff inside Mcutils which made it balloon a little bit

### Members:

  - [FiniteDifferenceFunction](Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceFunction.md)
  - [FiniteDifferenceError](Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceError.md)
  - [finite_difference](Zachary/Taylor/FiniteDifferenceFunction/finite_difference.md)
  - [FiniteDifference1D](Zachary/Taylor/FiniteDifferenceFunction/FiniteDifference1D.md)
  - [RegularGridFiniteDifference](Zachary/Taylor/FiniteDifferenceFunction/RegularGridFiniteDifference.md)
  - [IrregularGridFiniteDifference](Zachary/Taylor/FiniteDifferenceFunction/IrregularGridFiniteDifference.md)
  - [FiniteDifferenceData](Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceData.md)
  - [FiniteDifferenceMatrix](Zachary/Taylor/FiniteDifferenceFunction/FiniteDifferenceMatrix.md)
  - [FunctionExpansion](Zachary/Taylor/FunctionExpansions/FunctionExpansion.md)
  - [FiniteDifferenceDerivative](Zachary/Taylor/Derivatives/FiniteDifferenceDerivative.md)
  - [Mesh](Zachary/Mesh/Mesh.md)
  - [MeshType](Zachary/Mesh/MeshType.md)
  - [Tensor](Zachary/LazyTensors/Tensor.md)
  - [TensorOp](Zachary/LazyTensors/TensorOp.md)
  - [LazyOperatorTensor](Zachary/LazyTensors/LazyOperatorTensor.md)
  - [SparseTensor](Zachary/LazyTensors/SparseTensor.md)
  - [BaseSurface](Zachary/Surfaces/BaseSurface/BaseSurface.md)
  - [TaylorSeriesSurface](Zachary/Surfaces/BaseSurface/TaylorSeriesSurface.md)
  - [LinearExpansionSurface](Zachary/Surfaces/BaseSurface/LinearExpansionSurface.md)
  - [LinearFitSurface](Zachary/Surfaces/BaseSurface/LinearFitSurface.md)
  - [InterpolatedSurface](Zachary/Surfaces/BaseSurface/InterpolatedSurface.md)
  - [Surface](Zachary/Surfaces/Surface/Surface.md)
  - [MultiSurface](Zachary/Surfaces/Surface/MultiSurface.md)
  - [FittableModel](Zachary/FittableModels/FittableModel.md)
  - [LinearFittableModel](Zachary/FittableModels/LinearFittableModel.md)
  - [LinearFitBasis](Zachary/FittableModels/LinearFitBasis.md)
  - [Interpolator](Zachary/Interpolator/Interpolator.md)
  - [Extrapolator](Zachary/Interpolator/Extrapolator.md)

### Examples:


1D finite difference derivative via [finite_difference](Zachary/FiniteDifferenceFunction/finite_difference.md):

```python
from McUtils.Zachary import finite_difference
import numpy as np

sin_grid = np.linspace(0, 2*np.pi, 200)
sin_vals = np.sin(sin_grid)

deriv = finite_difference(sin_grid, sin_vals, 3) # 3rd deriv
```

2D finite difference derivative via [finite_difference](Zachary/FiniteDifferenceFunction/finite_difference.md):

```python
from McUtils.Zachary import finite_difference
import numpy as np

x_grid = np.linspace(0, 2*np.pi, 200)
y_grid = np.linspace(0, 2*np.pi, 100)
sin_x_vals = np.sin(x_grid); sin_y_vals =  np.sin(y_grid)
vals_2D = np.outer(sin_x_vals, sin_y_vals)
grid_2D = np.array(np.meshgrid(x_grid, y_grid)).T

deriv = finite_difference(grid_2D, vals_2D, (1, 3))
```

___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary.md)