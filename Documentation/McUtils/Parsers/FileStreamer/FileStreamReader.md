## <a id="McUtils.Parsers.FileStreamer.FileStreamReader">FileStreamReader</a>
Represents a file from which we'll stream blocks of data by finding tags and parsing what's between them

### Properties and Methods
<a id="McUtils.Parsers.FileStreamer.FileStreamReader.__init__">&nbsp;</a>
```python
__init__(self, file, mode='r', encoding='utf-8', **kw): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.__enter__">&nbsp;</a>
```python
__enter__(self): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.__exit__">&nbsp;</a>
```python
__exit__(self, exc_type, exc_val, exc_tb): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.__iter__">&nbsp;</a>
```python
__iter__(self): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.__getattr__">&nbsp;</a>
```python
__getattr__(self, item): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.readline">&nbsp;</a>
```python
readline(self): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.read">&nbsp;</a>
```python
read(self, n=1): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.seek">&nbsp;</a>
```python
seek(self, *args, **kwargs): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.tell">&nbsp;</a>
```python
tell(self): 
```

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.find_tag">&nbsp;</a>
```python
find_tag(self, tag, skip_tag=None, seek=None): 
```
Finds a tag in a file
- `header`: `FileStreamerTag`
    >a tag specifying a header to look for + optional follow-up processing/offsets
- `:returns`: `int`
    >position of tag

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.get_tagged_block">&nbsp;</a>
```python
get_tagged_block(self, tag_start, tag_end, block_size=500): 
```
Pulls the string between tag_start and tag_end
- `tag_start`: `FileStreamerTag or None`
    >No description...
- `tag_end`: `FileStreamerTag`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.FileStreamer.FileStreamReader.parse_key_block">&nbsp;</a>
```python
parse_key_block(self, tag_start=None, tag_end=None, mode='Single', parser=None, parse_mode='List', num=None, **ignore): 
```
Parses a block by starting at tag_start and looking for tag_end and parsing what's in between them
- `key`: `str`
    >registered key pattern to pull from a file
- `:returns`: `_`
    >No description...

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/FileStreamer/FileStreamReader.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/FileStreamer/FileStreamReader.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Parsers/FileStreamer.py?message=Update%20Docs)