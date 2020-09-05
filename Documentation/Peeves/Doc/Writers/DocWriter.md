## <a id="Peeves.Doc.Writers.DocWriter">DocWriter</a>
A general writer class that writes a file based off a template and filling in object template specs

### Properties and Methods
```python
template: str
template_root: str
template_name: str
default_template_dir: str
example_root: str
outStream: type
load_template: method
get_identifier: method
param_template: str
```
<a id="Peeves.Doc.Writers.DocWriter.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, obj, out_file, obj_name=None, parent_obj=None, template=None, root=None, ignore_paths=None): 
```

- `obj`: `Any`
    >No description...
- `out_file`: `Any`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.get_name" class="docs-object-method">&nbsp;</a>
```python
get_name(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.out" class="docs-object-method">&nbsp;</a>
```python
@property
out(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.write_string" class="docs-object-method">&nbsp;</a>
```python
write_string(self, txt): 
```

<a id="Peeves.Doc.Writers.DocWriter.template_params" class="docs-object-method">&nbsp;</a>
```python
template_params(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.format" class="docs-object-method">&nbsp;</a>
```python
format(self, template=None): 
```

<a id="Peeves.Doc.Writers.DocWriter.write" class="docs-object-method">&nbsp;</a>
```python
write(self, template=None): 
```

<a id="Peeves.Doc.Writers.DocWriter.get_package_and_url" class="docs-object-method">&nbsp;</a>
```python
get_package_and_url(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.package_path" class="docs-object-method">&nbsp;</a>
```python
@property
package_path(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.identifier" class="docs-object-method">&nbsp;</a>
```python
@property
identifier(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.load_examples" class="docs-object-method">&nbsp;</a>
```python
load_examples(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_item" class="docs-object-method">&nbsp;</a>
```python
format_item(self, item, item_level=0): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_link" class="docs-object-method">&nbsp;</a>
```python
format_link(self, alt, link): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_obj_link" class="docs-object-method">&nbsp;</a>
```python
format_obj_link(self, spec): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_inline_code" class="docs-object-method">&nbsp;</a>
```python
format_inline_code(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.format_code_block" class="docs-object-method">&nbsp;</a>
```python
format_code_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.format_quote_block" class="docs-object-method">&nbsp;</a>
```python
format_quote_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.parse_doc" class="docs-object-method">&nbsp;</a>
```python
parse_doc(self, doc): 
```

- `doc`: `str`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Peeves/Doc/Writers/DocWriter.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Peeves/Doc/Writers/DocWriter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Peeves/Doc/Writers/DocWriter.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Peeves/Doc/Writers/DocWriter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Doc/Writers.py?message=Update%20Docs)