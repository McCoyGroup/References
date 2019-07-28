# <a id="McUtils.Zachary">McUtils.Zachary</a>
    
A small framework for handling finite differencing of functions and other Taylor series related things

### Members:

  - [FiniteDifferenceFunction](Zachary/FiniteDifferenceFunction/FiniteDifferenceFunction.md)
  - [FiniteDifferenceError](Zachary/FiniteDifferenceFunction/FiniteDifferenceError.md)
  - [finite_difference](Zachary/FiniteDifferenceFunction/finite_difference.md)
  - [FiniteDifferenceDerivative](Zachary/Derivatives/FiniteDifferenceDerivative.md)
  - [Tensor](Zachary/LazyTensors/Tensor.md)
  - [TensorOp](Zachary/LazyTensors/TensorOp.md)
  - [LazyOperatorTensor](Zachary/LazyTensors/LazyOperatorTensor.md)
  - [SparseTensor](Zachary/LazyTensors/SparseTensor.md)
  - [FunctionExpansion](Zachary/FunctionExpansions/FunctionExpansion.md)

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