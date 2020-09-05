## <a id="RynLib.RynUtils.TemplateWriter.TemplateWriter">TemplateWriter</a>
A general class that can take a directory layout and apply template parameters to it
Very unsophisticated but workable

### Properties and Methods
```python
ignored_files: list
replacements: property
```
<a id="RynLib.RynUtils.TemplateWriter.TemplateWriter.__init__">&nbsp;</a>
```python
__init__(self, template_dir, replacements=None, file_filter=None, **opts): 
```

<a id="RynLib.RynUtils.TemplateWriter.TemplateWriter.apply_replacements">&nbsp;</a>
```python
apply_replacements(self, string): 
```
Applies the defined replacements to the
- `string`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.TemplateWriter.TemplateWriter.write_file">&nbsp;</a>
```python
write_file(self, template_file, out_dir, apply_template=True, template_dir=None): 
```
writes a single _file_ to _dir_ and fills the template from the parameters passed when intializing the class
- `template_file`: `str`
    >the file to load and write into
- `out_dir`: `str`
    >the directory to write the file into
- `apply_template`: `bool`
    >whether to apply the template parameters to the file content or not
- `:returns`: `_`
    >No description...

<a id="RynLib.RynUtils.TemplateWriter.TemplateWriter.iterate_write">&nbsp;</a>
```python
iterate_write(self, out_dir, apply_template=True, src_dir=None, template_dir=None): 
```
Iterates through the files in the template_dir and writes them out to dir
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/RynUtils/TemplateWriter/TemplateWriter.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/RynUtils/TemplateWriter/TemplateWriter.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/RynLib/edit/master/RynUtils/TemplateWriter.py?message=Update%20Docs)