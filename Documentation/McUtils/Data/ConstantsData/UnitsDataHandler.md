## <a id="McUtils.Data.ConstantsData.UnitsDataHandler">UnitsDataHandler</a>


### Properties and Methods
```python
prefix_map: OrderedDict
postfix_map: OrderedDict
```
<a id="McUtils.Data.ConstantsData.UnitsDataHandler.__init__">&nbsp;</a>
```python
__init__(self): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.load">&nbsp;</a>
```python
load(self): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.find_conversion">&nbsp;</a>
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

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.add_conversion">&nbsp;</a>
```python
add_conversion(self, unit, target, value): 
```

<a id="McUtils.Data.ConstantsData.UnitsDataHandler.convert">&nbsp;</a>
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
