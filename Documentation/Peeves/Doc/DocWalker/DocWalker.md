## <a id="Peeves.Doc.DocWalker.DocWalker">DocWalker</a>
A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
and a Markdown index file.

Takes a set of objects & writers and walks through the objects, generating files on the way

### Properties and Methods
<a id="Peeves.Doc.DocWalker.DocWalker.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, objects, out=None, module_writer=None, class_writer=None, function_writer=None, object_writer=None, ignore_paths=None): 
```

- `objects`: `Iterable[Any]`
    >the objects to write out
- `out`: `None | str`
    >the directory in which to write the files (`None` means `sys.stdout`)
- `module_writer`: `type`
    >the class to used to write module Markdown (`None` means `ModuleWriter`)
- `class_writer`: `type`
    >the class to used to write class Markdown(`None` means `ClassWriter`)
- `function_writer`: `type`
    >the class to used to write function Markdown (`None` means `FunctionWriter`)
- `object_writer`: `type`
    >the class to used to write object Markdown (`None` means `ObjectWriter`)
- `ignore_paths`: `None | Iterable[str]`
    >a set of paths not to write (passed to the objects)

<a id="Peeves.Doc.DocWalker.DocWalker.write_object" class="docs-object-method">&nbsp;</a>
```python
write_object(self, o, written=None): 
```
Writes a single object to file
- `o`: `Any`
    >the object we want to write
- `written`: `None | dict`
    >a caching dict of objects to break cyclic reference loops
- `:returns`: `None | str`
    >the written file

<a id="Peeves.Doc.DocWalker.DocWalker.write_docs" class="docs-object-method">&nbsp;</a>
```python
write_docs(self): 
```
Walks through the objects supplied and writes them & their children to file
- `:returns`: `list[str]`
    >written files

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Peeves/Doc/DocWalker/DocWalker.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Peeves/Doc/DocWalker/DocWalker.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Peeves/Doc/DocWalker/DocWalker.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Peeves/Doc/DocWalker/DocWalker.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Doc/DocWalker.py?message=Update%20Docs)