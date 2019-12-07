## <a id="McUtils.GaussianInterface.GaussianJob.GaussianJob">GaussianJob</a>
A class that writes Gaussian .gjf files given a system and config/template options

### Properties and Methods
```python
job_template_dir: str
Job: type
Config: type
System: type
```
```python
__init__(self, name, *args, description=None, system=None, job=None, config=None, template='Template.gjf', file=None): 
```

```python
format(self): 
```

```python
write(self, file=None): 
```

```python
start(self, *cmd, binary='g09', **kwargs): 
```
Starts a Gaussian job
- `cmd`: `Any`
    >No description...
- `binary`: `Any`
    >No description...
- `kwargs`: `Any`
    >No description...
- `:returns`: `_`
    >started process

```python
run(self, *args, **kwargs): 
```

```python
__str__(self): 
```

### Examples
