## <a id="RynLib.RynUtils.ConfigManager.Config">Config</a>


### Properties and Methods
```python
name: property
conf: property
opt_dict: property
```
<a id="RynLib.RynUtils.ConfigManager.Config.__init__">&nbsp;</a>
```python
__init__(self, config, root=None, loader=None): 
```
Loads the config from a file
- `loader`: `ModuleLoader | None`
    >No description...
- `config_file`: `str | dict | module`
    >No description...

<a id="RynLib.RynUtils.ConfigManager.Config.update">&nbsp;</a>
```python
update(self, **kw): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.save">&nbsp;</a>
```python
save(self, file=None, mode=None, attribute='config'): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.load_opts">&nbsp;</a>
```python
load_opts(self): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.get_file">&nbsp;</a>
```python
get_file(self, name, conf_attr='root'): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.get_conf_attr">&nbsp;</a>
```python
get_conf_attr(self, item): 
```

<a id="RynLib.RynUtils.ConfigManager.Config.__getattr__">&nbsp;</a>
```python
__getattr__(self, item): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/RynUtils/ConfigManager/Config.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/RynUtils/ConfigManager/Config.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/RynLib/edit/master/RynUtils/ConfigManager.py?message=Update%20Docs)