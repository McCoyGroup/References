## <a id="McUtils.Parsers.StringParser.StringParser">StringParser</a>
A convenience class that makes it easy to pull blocks out of strings and whatnot

### Properties and Methods
```python
MatchIterator: type
get_regex_block_handlers: method
get_regex_dtypes: method
handler_method: method
to_array: method
array_handler: method
```
<a id="McUtils.Parsers.StringParser.StringParser.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, regex): 
```

<a id="McUtils.Parsers.StringParser.StringParser.parse" class="docs-object-method">&nbsp;</a>
```python
parse(self, txt, regex=None, block_handlers=None, dtypes=None, out=None): 
```
Finds a single match for the and applies parsers for the specified regex in txt
- `txt`: `str`
    >a chunk of text to be matched
- `regex`: `RegexPattern`
    >the regex to match in _txt_
- `block_handlers`: `iterable[callable] | OrderedDict[str: callable]`
    >handlers for the matched blocks in _regex_ -- usually comes from _regex_
- `dtypes`: `iterable[type | StructuredType] | OrderedDict[str: type | StructuredType]`
    >the types of the data that we expect to match -- usually comes from _regex_
- `out`: `None | StructuredTypeArray | iterable[StructuredTypeArray] | OrderedDict[str: StructuredTypeArray]`
    >where to place the parsed out data -- usually comes from _regex_
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.StringParser.StringParser.parse_all" class="docs-object-method">&nbsp;</a>
```python
parse_all(self, txt, regex=None, num_results=None, block_handlers=None, dtypes=None, out=None): 
```

<a id="McUtils.Parsers.StringParser.StringParser.parse_iter" class="docs-object-method">&nbsp;</a>
```python
parse_iter(self, txt, regex=None, num_results=None, block_handlers=None, dtypes=None): 
```

<a id="McUtils.Parsers.StringParser.StringParser.load_array" class="docs-object-method">&nbsp;</a>
```python
load_array(data, dtype='float'): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/StringParser/StringParser.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/StringParser/StringParser.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Parsers/StringParser.py?message=Update%20Docs)