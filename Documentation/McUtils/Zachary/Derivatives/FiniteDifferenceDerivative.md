## <a id="McUtils.Zachary.Derivatives.FiniteDifferenceDerivative">FiniteDifferenceDerivative</a>
Provides derivatives for a function (scalar or vector valued)
    Can be indexed into or the entire tensor of derivatives may be requested

### Properties and Methods
```python
differencer: type
array: property
```
```python
__init__(self, f, order=1, function_shape=(0, 0), **fd_opts): 
```

- `f`: `callable`
    >the function we would like to take derivatives of
- `order`: `int | list[int]`
    >the order of the derivative we would like to take
- `function_shape`: `int | iterable[iterable[int] | int]`
    >The input and output shapes of f. None means a scalar function.
- `fd_opts`: `Any`
    >the options to pass to the finite difference function

```python
derivatives(self, center=0, order=None, coordinates=None, displacement_function=None, mesh_spacing=0.01, prep=None, **fd_opts): 
```
Generates a differencer object that can be used to get derivs however your little heart desires
- `center`: `Any`
    >No description...
- `order`: `Any`
    >No description...
- `coordinates`: `Any`
    >No description...
- `displacement_function`: `Any`
    >No description...
- `mesh_spacing`: `Any`
    >No description...
- `prep`: `Any`
    >No description...
- `fd_opts`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
