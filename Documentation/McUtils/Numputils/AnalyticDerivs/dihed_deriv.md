# <a id="McUtils.Numputils.AnalyticDerivs.dihed_deriv">dihed_deriv</a>

```python
dihed_deriv(coords, i, j, k, l): 
```
Gives the derivative of the dihedral between i, j, k, and l with respect to the Cartesians
    Currently gives what are sometimes called the `psi` angles.
    Will be extended to also support more traditional `phi` angles
- `coords`: `np.ndarray`
    >No description...
- `i`: `int | Iterable[int]`
    >No description...
- `j`: `int | Iterable[int]`
    >No description...
- `k`: `int | Iterable[int]`
    >No description...
- `l`: `int | Iterable[int]`
    >No description...
- `:returns`: `np.ndarray`
    >derivatives of the dihedral with respect to atoms i, j, k, and l 

### Examples: 


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Numputils/AnalyticDerivs/dihed_deriv.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Numputils/AnalyticDerivs/dihed_deriv.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Numputils/AnalyticDerivs/dihed_deriv.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Numputils/AnalyticDerivs/dihed_deriv.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Numputils/AnalyticDerivs.py?message=Update%20Docs)