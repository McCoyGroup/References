## <a id="McUtils.Parsers.RegexPatterns.RegexPattern">RegexPattern</a>
Represents a combinator structure for building more complex regexes

    It might be worth working with this combinator structure in a _lazy_ fashion so that we can drill down
    into the expression structure... that way we can define a sort-of Regex calculus that we can use to build up higher
    order regexes but still be able to recursively inspect subparts?

### Properties and Methods
```python
pat: property
children: property
child_count: property
child_map: property
parents: property
joiner: property
suffix: property
prefix: property
dtype: property
is_repeating: property
capturing: property
captures: property
capturing_groups: property
named_groups: property
compiled: property
```
<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__init__">&nbsp;</a>
```python
__init__(self, pat, name=None, children=None, parents=None, dtype=None, repetitions=None, key=None, joiner='', wrapper_function=None, suffix=None, prefix=None, parser=None, handler=None, capturing=None, allow_inner_captures=False): 
```

- `pat`: `str | callable`
    >No description...
- `name`: `str`
    >No description...
- `dtype`: `Any`
    >No description...
- `repeated`: `Any`
    >No description...
- `key`: `Any`
    >No description...
- `joiner`: `Any`
    >No description...
- `children`: `Any`
    >No description...
- `parents`: `Any`
    >No description...
- `wrapper_function`: `Any`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.get_capturing_groups">&nbsp;</a>
```python
get_capturing_groups(self, allow_inners=None): 
```
We walk down the tree to find the children with capturing groups in them and
        then find the outermost RegexPattern for those unless allow_inners is on in which case we pull them all

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.combine">&nbsp;</a>
```python
combine(self, other, *args, **kwargs): 
```
Combines self and other
- `other`: `RegexPattern | str`
    >No description...
- `:returns`: `str | callable`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.wrap">&nbsp;</a>
```python
wrap(self, *args, **kwargs): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.build">&nbsp;</a>
```python
build(self, joiner=None, prefix=None, suffix=None, recompile=True, no_captures=False): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_parent">&nbsp;</a>
```python
add_parent(self, parent): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.remove_parent">&nbsp;</a>
```python
remove_parent(self, parent): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_child">&nbsp;</a>
```python
add_child(self, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_children">&nbsp;</a>
```python
add_children(self, children): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.remove_child">&nbsp;</a>
```python
remove_child(self, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.insert_child">&nbsp;</a>
```python
insert_child(self, index, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.invalidate_cache">&nbsp;</a>
```python
invalidate_cache(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__copy__">&nbsp;</a>
```python
__copy__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__add__">&nbsp;</a>
```python
__add__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__radd__">&nbsp;</a>
```python
__radd__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__call__">&nbsp;</a>
```python
__call__(self, other, *args, name=None, dtype=None, repetitions=None, key=None, joiner=None, wrap_function=None, suffix=None, prefix=None, multiline=None, parser=None, handler=None, capturing=None, allow_inner_captures=None, **kwargs): 
```
Wraps self around other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__repr__">&nbsp;</a>
```python
__repr__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__str__">&nbsp;</a>
```python
__str__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__getitem__">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.match">&nbsp;</a>
```python
match(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.search">&nbsp;</a>
```python
search(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.findall">&nbsp;</a>
```python
findall(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.finditer">&nbsp;</a>
```python
finditer(self, txt): 
```

### Examples
