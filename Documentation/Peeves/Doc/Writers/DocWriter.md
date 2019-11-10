## <a id="Peeves.Doc.Writers.DocWriter">DocWriter</a>
A general writer class that writes a file based off a template and filling in object template specs

### Properties and Methods
```python
template: str
outStream: type
out: property
load_template: method
get_identifier: method
identifier: property
param_template: str
```
<a id="Peeves.Doc.Writers.DocWriter.__init__">&nbsp;</a>
```python
__init__(self, obj, out_file, root=None): 
```

- `obj`: `Any`
    >No description...
- `out_file`: `Any`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.write_string">&nbsp;</a>
```python
write_string(self, txt): 
```

<a id="Peeves.Doc.Writers.DocWriter.template_params">&nbsp;</a>
```python
template_params(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.format">&nbsp;</a>
```python
format(self, template=None): 
```

<a id="Peeves.Doc.Writers.DocWriter.write">&nbsp;</a>
```python
write(self, template=None): 
```

<a id="Peeves.Doc.Writers.DocWriter.load_examples">&nbsp;</a>
```python
load_examples(self): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_item">&nbsp;</a>
```python
format_item(self, item, item_level=0): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_link">&nbsp;</a>
```python
format_link(self, alt, link): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_obj_link">&nbsp;</a>
```python
format_obj_link(self, spec): 
```

<a id="Peeves.Doc.Writers.DocWriter.format_inline_code">&nbsp;</a>
```python
format_inline_code(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.format_code_block">&nbsp;</a>
```python
format_code_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.format_quote_block">&nbsp;</a>
```python
format_quote_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Doc.Writers.DocWriter.parse_doc">&nbsp;</a>
```python
parse_doc(self, doc): 
```

- `doc`: `str`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
