# <a id="McUtils.Numputils.AnalyticDerivs.angle_deriv">angle_deriv</a>

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

### Examples: 


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Numputils/AnalyticDerivs/angle_deriv.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Numputils/AnalyticDerivs/angle_deriv.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Numputils/AnalyticDerivs.py?message=Update%20Docs)