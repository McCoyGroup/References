## <a id="McUtils.Zachary.Derivatives.FiniteDifferenceDerivative">FiniteDifferenceDerivative</a>
Provides derivatives for a function (scalar or vector valued)
    Can be indexed into or the entire tensor of derivatives may be requested

### Properties and Methods
<a id="McUtils.Zachary.Derivatives.FiniteDifferenceDerivative.__init__">&nbsp;</a>
```python
__init__(self, f, function_shape=(0, 0), **fd_opts): 
```

- `f`: `FunctionSpec | callable`
    >the function we would like to take derivatives of
- `function_shape`: `Iterable[Iterable[int] | int] | None`
    >the shape of the function we'd like to take the derivatives of
- `fd_opts`: `Any`
    >the options to pass to the finite difference function

<a id="McUtils.Zachary.Derivatives.FiniteDifferenceDerivative.__call__">&nbsp;</a>
```python
__call__(self, *args, **opts): 
```

<a id="McUtils.Zachary.Derivatives.FiniteDifferenceDerivative.derivatives">&nbsp;</a>
```python
derivatives(self, center, displacement_function=None, prep=None, lazy=None, mesh_spacing=None, **fd_opts): 
```
Generates a differencer object that can be used to get derivs however your little heart desires
- `center`: `np.ndarray`
    >the center point around which to generate differences
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
