## <a id="McUtils.Parsers.FileStreamer.FileStreamReader">FileStreamReader</a>
Represents a file from which we'll stream blocks of data by finding tags and parsing what's between them

### Properties and Methods
```python
__init__(self, file, mode='r', encoding='utf-8', **kw): 
```

```python
__enter__(self): 
```

```python
__exit__(self, exc_type, exc_val, exc_tb): 
```

```python
__iter__(self): 
```

```python
__getattr__(self, item): 
```

```python
readline(self): 
```

```python
read(self, n=1): 
```

```python
seek(self, *args, **kwargs): 
```

```python
tell(self): 
```

```python
find_tag(self, tag, skip_tag=None, seek=None): 
```
Finds a tag in a file
- `header`: `FileStreamerTag`
    >a tag specifying a header to look for + optional follow-up processing/offsets
- `:returns`: `int`
    >position of tag

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

```python
parse_key_block(self, tag_start=None, tag_end=None, mode='Single', parser=None, parse_mode='List', num=None, **ignore): 
```
Parses a block by starting at tag_start and looking for tag_end and parsing what's in between them
- `key`: `str`
    >registered key pattern to pull from a file
- `:returns`: `_`
    >No description...

### Examples
