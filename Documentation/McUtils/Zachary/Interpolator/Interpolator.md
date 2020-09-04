## <a id="McUtils.Zachary.Interpolator.Interpolator">Interpolator</a>
A general purpose that takes your data and just interpolates it without whining or making you do a pile of extra work

### Properties and Methods
```python
get_interpolator: method
get_extrapolator: method
morse_interpolator: method
```
<a id="McUtils.Zachary.Interpolator.Interpolator.__init__">&nbsp;</a>
```python
__init__(self, grid, vals, interpolation_function=None, interpolation_order=None, extrapolator=None, extrapolation_order=1, **interpolation_opts): 
```

- `grid`: `np.ndarray`
    >an unstructured grid of points **or** a structured grid of points **or** a 1D array
- `vals`: `np.ndarray`
    >the values at the grid points
- `interpolation_function`: `None | function`
    >the basic function to be used to handle the raw interpolation
- `interpolation_order`: `int | str | None`
    >the order of extrapolation to use (when applicable)
- `extrapolator`: `Extrapolator | None | str | function`
    >the extrapolator to use for data points not on the grid
- `extrapolation_order`: `int | str | None`
    >the order of extrapolation to use by default
- `interpolation_opts`: `Any`
    >the options to be fed into the interpolating_function

<a id="McUtils.Zachary.Interpolator.Interpolator.apply">&nbsp;</a>
```python
apply(self, grid_points, **opts): 
```
Interpolates then extrapolates the function at the grid_points
- `grid_points`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Zachary.Interpolator.Interpolator.__call__">&nbsp;</a>
```python
__call__(self, *args, **kwargs): 
```

<a id="McUtils.Zachary.Interpolator.Interpolator.regularize_mesh">&nbsp;</a>
```python
regularize_mesh(self, interp_kind='cubic', interpolator=None, **kwargs): 
```
Interpolates along the different slices in the grid, building a RegularMesh overall
- `grid`: `np.ndarray (x, y)`
    >a semistructured grid of points.
- `vals`: `np.ndarray (z)`
    >the values at the grid points.
- `interp_kind`: `str`
    >type of interpolation to do ('cubic' | 'linear' | 'nearest' | ...)
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >square_grid: a structured grid of points (np.ndarray) (x, y)

<a id="McUtils.Zachary.Interpolator.Interpolator.regular_grid">&nbsp;</a>
```python
regular_grid(self, interp_kind='cubic', fillvalues=False, plot=False, **kwargs): 
```
TODO: extend to also check y coordinates... maybe add param to do x, y, or both?
        creates a regular grid from a set of semistructured points. Only has 2D capabilities.
        :param grid: a semistructured grid of points.
        :type grid: np.ndarray (x, y)
        :param vals: the values at the grid points.
        :type vals: np.ndarray (z)
        :param interp_kind: type of interpolation to do ('cubic' | 'linear' | 'nearest' | ...)
        :type interp_kind: str
        :param fillvalues: if true, outer edges are filled with last data point extending out.
         Otherwise extrapolates according to interp_kind (default)
- `fillvalues`: `bool`
    >No description...
- `plot`: `bool`
    >if true, plots the extrapolated cuts for visualization purposes.
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >square_grid: a structured grid of points (np.ndarray) (x, y)

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Interpolator/Interpolator.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Interpolator/Interpolator.md)