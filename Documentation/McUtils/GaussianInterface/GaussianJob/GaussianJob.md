## <a id="McUtils.GaussianInterface.GaussianJob.GaussianJob">GaussianJob</a>
A class that writes Gaussian .gjf files given a system and config/template options

### Properties and Methods
```python
job_template_dir: str
Job: type
Config: type
System: type
```
<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, name, *args, description=None, system=None, job=None, config=None, template='Template.gjf', file=None): 
```

<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.format" class="docs-object-method">&nbsp;</a>
```python
format(self): 
```

<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.write" class="docs-object-method">&nbsp;</a>
```python
write(self, file=None): 
```

<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.start" class="docs-object-method">&nbsp;</a>
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

<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.run" class="docs-object-method">&nbsp;</a>
```python
run(self, *args, **kwargs): 
```

<a id="McUtils.GaussianInterface.GaussianJob.GaussianJob.__str__" class="docs-object-method">&nbsp;</a>
```python
__str__(self): 
```

### Examples
```python
from McUtils.GaussianInterface import GaussianJob 

job = GaussianJob(
        "water scan",
        description="Simple water scan",
        config= GaussianJob.Config(
            NProc = 4,
            Mem = '1000MB'
        ),
        job= GaussianJob.Job(
            'Scan'
        ),
        system = GaussianJob.System(
            charge=0,
            molecule=[
                ["O", "H", "H"],
                [
                    [0, 0, 0],
                    [.987, 0, 0],
                    [0, .987, 0]
                ]
            ],
            vars=[
                GaussianJob.System.Variable("y1", 0., 10., .1),
                GaussianJob.System.Constant("x1", 10)
            ]
    
        )
    )
# print(job.write(), file=sys.stderr)
self.assertIsInstance(job.format(), str)
```

___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/GaussianInterface/GaussianJob/GaussianJob.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/GaussianInterface/GaussianJob/GaussianJob.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/GaussianInterface/GaussianJob.py?message=Update%20Docs)