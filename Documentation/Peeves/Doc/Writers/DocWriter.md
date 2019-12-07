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
```python
__init__(self, obj, out_file, root=None): 
```

- `obj`: `Any`
    >No description...
- `out_file`: `Any`
    >No description...

```python
write_string(self, txt): 
```

```python
template_params(self): 
```

```python
format(self, template=None): 
```

```python
write(self, template=None): 
```

```python
load_examples(self): 
```

```python
format_item(self, item, item_level=0): 
```

```python
format_link(self, alt, link): 
```

```python
format_obj_link(self, spec): 
```

```python
format_inline_code(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

```python
format_code_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

```python
format_quote_block(self, arg): 
```

- `arg`: `str`
    >No description...
- `:returns`: `_`
    >No description...

```python
parse_doc(self, doc): 
```

- `doc`: `str`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
