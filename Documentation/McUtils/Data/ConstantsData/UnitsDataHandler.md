## <a id="McUtils.Data.ConstantsData.UnitsDataHandler">UnitsDataHandler</a>
A DataHandler that's built for use with the units data we've collected.
Usually used through the `UnitsData` object.

### Properties and Methods
```python
prefix_map: OrderedDict
postfix_map: OrderedDict
```
<a id="McUtils.Data.ConstantsData.UnitsDataHandler.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.load" class="docs-object-method">&nbsp;</a>
```python
load(self): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.find_conversion" class="docs-object-method">&nbsp;</a>
```python
find_conversion(self, unit, target): 
```
Attempts to find a conversion between two sets of units. Currently only implemented for "plain" units.
- `unit`: `Any`
    >No description...
- `target`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.add_conversion" class="docs-object-method">&nbsp;</a>
```python
add_conversion(self, unit, target, value): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.convert" class="docs-object-method">&nbsp;</a>
```python
convert(self, unit, target): 
```
Converts base unit into target using the scraped NIST data
- `unit`: `Any`
    >No description...
- `target`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Data/ConstantsData/UnitsDataHandler.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Data/ConstantsData/UnitsDataHandler.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Data/ConstantsData/UnitsDataHandler.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Data/ConstantsData/UnitsDataHandler.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Data/ConstantsData.py?message=Update%20Docs)