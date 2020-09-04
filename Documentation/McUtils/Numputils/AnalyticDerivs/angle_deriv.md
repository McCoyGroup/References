<a id="McUtils.Numputils.AnalyticDerivs.angle_deriv">&nbsp;</a>
```python
angle_deriv(coords, i, j, k): 
```
Gives the derivative of the angle between i, j, and k with respect to the Cartesians
- `coords`: `np.ndarray`
    >No description...
- `i`: `int | Iterable[int]`
    >index of the central atom
- `j`: `int | Iterable[int]`
    >index of one of the outside atoms
- `k`: `int | Iterable[int]`
    >index of the other outside atom
- `:returns`: `np.ndarray`
    >derivatives of the angle with respect to atoms i, j, and k

