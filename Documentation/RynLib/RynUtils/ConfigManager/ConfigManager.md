## <a id="RynLib.RynUtils.ConfigManager.ConfigManager">ConfigManager</a>
Manages configurations inside a single directory

### Properties and Methods
<a id="RynLib.RynUtils.ConfigManager.ConfigManager.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, conf_dir, conf_file='config.py', config_package='Configs'): 
```

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.list_configs" class="docs-object-method">&nbsp;</a>
```python
list_configs(self): 
```
Lists the configurations known by the ConfigManager
- `:returns`: `List[str]`
    >the names of the configs stored in the config directory

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.config_loc" class="docs-object-method">&nbsp;</a>
```python
config_loc(self, name): 
```

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.load_config" class="docs-object-method">&nbsp;</a>
```python
load_config(self, name, conf_file=None): 
```
Loads a Config by name from the directory
- `name`: `str`
    >the name of the config file
- `conf_file`: `str | None`
    >the config file to load from -- defaults to `'config.py'`
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.check_config" class="docs-object-method">&nbsp;</a>
```python
check_config(self, config_tag): 
```

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.add_config" class="docs-object-method">&nbsp;</a>
```python
add_config(self, config_tag, config_file=None, **opts): 
```
Adds a config to the known list. Requires a name. Takes either a config file or a bunch of options.
- `name`: `Any`
    >No description...
- `conf_file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.remove_config" class="docs-object-method">&nbsp;</a>
```python
remove_config(self, name): 
```
Removes a config from the known list. Requires a name.
- `name`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.ConfigManager.ConfigManager.edit_config" class="docs-object-method">&nbsp;</a>
```python
edit_config(self, config_tag, **opts): 
```
Updates a config from the known list. Requires a name.
- `name`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/RynUtils/ConfigManager/ConfigManager.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/RynUtils/ConfigManager/ConfigManager.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/RynLib/RynUtils/ConfigManager/ConfigManager.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/RynLib/RynUtils/ConfigManager/ConfigManager.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/RynLib/edit/master/RynUtils/ConfigManager.py?message=Update%20Docs)