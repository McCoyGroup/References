# <a id="McUtils.Numputils.AnalyticDerivs.rot_deriv">rot_deriv</a>

```python
rot_deriv(angle, axis, dAngle, dAxis): 
```
Gives a rotational derivative w/r/t some unspecified coordinate
    (you have to supply the chain rule terms)
- `angle`: `float`
    >angle for rotation
- `axis`: `np.ndarray`
    >axis for rotation
- `dAngle`: `float`
    >chain rule angle deriv.
- `dAxis`: `np.ndarray`
    >chain rule axis deriv.
- `:returns`: `np.ndarray`
    >derivatives of the rotation matrices with respect to both the angle and the axis

Examples: 


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Numputils/AnalyticDerivs/rot_deriv.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Numputils/AnalyticDerivs/rot_deriv.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Numputils/AnalyticDerivs.py?message=Update%20Docs)