## <a id="McUtils.Plots.Styling.ThemeManager">ThemeManager</a>
Simple manager class for plugging into themes in a semi-background agnostic way

### Properties and Methods
```python
extra_themes: dict
add_theme: method
resolve_theme: method
backend_themes: property
theme_names: property
```
<a id="McUtils.Plots.Styling.ThemeManager.__init__">&nbsp;</a>
```python
__init__(self, *theme_names, backend=<Backends.MPL: 'matplotlib'>, **extra_styles): 
```

<a id="McUtils.Plots.Styling.ThemeManager.__enter__">&nbsp;</a>
```python
__enter__(self): 
```

<a id="McUtils.Plots.Styling.ThemeManager.__exit__">&nbsp;</a>
```python
__exit__(self, exc_type, exc_val, exc_tb): 
```

<a id="McUtils.Plots.Styling.ThemeManager.validate_theme">&nbsp;</a>
```python
validate_theme(self, theme_names, theme_styless): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Styling/ThemeManager.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Styling/ThemeManager.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Styling.py?message=Update%20Docs)