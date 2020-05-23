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
