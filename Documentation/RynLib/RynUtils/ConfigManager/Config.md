## <a id="RynLib.RynUtils.ConfigManager.Config">Config</a>


### Properties and Methods
<a id="RynLib.RynUtils.ConfigManager.Config.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, config, root=None, loader=None): 
```
Loads the config from a file
- `loader`: `ModuleLoader | None`
    >No description...
- `config_file`: `str | dict | module`
    >No description...

<a id="RynLib.RynUtils.ConfigManager.Config.name" class="docs-object-method">&nbsp;</a>
```python
@property
name(self): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.conf" class="docs-object-method">&nbsp;</a>
```python
@property
conf(self): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.opt_dict" class="docs-object-method">&nbsp;</a>
```python
@property
opt_dict(self): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.update" class="docs-object-method">&nbsp;</a>
```python
update(self, **kw): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.save" class="docs-object-method">&nbsp;</a>
```python
save(self, file=None, mode=None, attribute='config'): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.load_opts" class="docs-object-method">&nbsp;</a>
```python
load_opts(self): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.get_file" class="docs-object-method">&nbsp;</a>
```python
get_file(self, name, conf_attr='root'): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.get_conf_attr" class="docs-object-method">&nbsp;</a>
```python
get_conf_attr(self, item): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.__getattr__" class="docs-object-method">&nbsp;</a>
```python
__getattr__(self, item): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/RynUtils/ConfigManager/Config.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/RynUtils/ConfigManager/Config.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/RynLib/RynUtils/ConfigManager/Config.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/RynLib/RynUtils/ConfigManager/Config.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/RynLib/edit/master/RynUtils/ConfigManager.py?message=Update%20Docs)