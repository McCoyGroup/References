## <a id="McUtils.Plots.Styling.ThemeManager">ThemeManager</a>
Simple manager class for plugging into themes in a semi-background agnostic way

### Properties and Methods
```python
extra_themes: dict
add_theme: method
resolve_theme: method
```
<a id="McUtils.Plots.Styling.ThemeManager.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, *theme_names, backend=<Backends.MPL: 'matplotlib'>, **extra_styles): 
```

<a id="McUtils.Plots.Styling.ThemeManager.__enter__" class="docs-object-method">&nbsp;</a>
```python
__enter__(self): 
```

<a id="McUtils.Plots.Styling.ThemeManager.__exit__" class="docs-object-method">&nbsp;</a>
```python
__exit__(self, exc_type, exc_val, exc_tb): 
```

<a id="McUtils.Plots.Styling.ThemeManager.validate_theme" class="docs-object-method">&nbsp;</a>
```python
validate_theme(self, theme_names, theme_styless): 
```

<a id="McUtils.Plots.Styling.ThemeManager.backend_themes" class="docs-object-method">&nbsp;</a>
```python
@property
backend_themes(self): 
```

<a id="McUtils.Plots.Styling.ThemeManager.theme_names" class="docs-object-method">&nbsp;</a>
```python
@property
theme_names(self): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Plots/Styling/ThemeManager.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Plots/Styling/ThemeManager.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Plots/Styling/ThemeManager.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Plots/Styling/ThemeManager.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Plots/Styling.py?message=Update%20Docs)