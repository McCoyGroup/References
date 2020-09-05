## <a id="McUtils.Parsers.RegexPatterns.RegexPattern">RegexPattern</a>
Represents a combinator structure for building more complex regexes

    It might be worth working with this combinator structure in a _lazy_ fashion so that we can drill down
    into the expression structure... that way we can define a sort-of Regex calculus that we can use to build up higher
    order regexes but still be able to recursively inspect subparts?

### Properties and Methods
<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, pat, name=None, children=None, parents=None, dtype=None, repetitions=None, key=None, joiner='', join_function=None, wrapper_function=None, suffix=None, prefix=None, parser=None, handler=None, default_value=None, capturing=None, allow_inner_captures=False): 
```

- `pat`: `str | callable`
    >No description...
- `name`: `str`
    >No description...
- `dtype`: `Any`
    >No description...
- `repetitions`: `Any`
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
- `suffix`: `Any`
    >No description...
- `prefix`: `Any`
    >No description...
- `parser`: `Any`
    >No description...
- `handler`: `Any`
    >No description...
- `capturing`: `Any`
    >No description...
- `allow_inner_captures`: `Any`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.pat" class="docs-object-method">&nbsp;</a>
```python
@property
pat(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.children" class="docs-object-method">&nbsp;</a>
```python
@property
children(self): 
```

- `:returns`: `tuple[RegexPattern]`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.child_count" class="docs-object-method">&nbsp;</a>
```python
@property
child_count(self): 
```

- `:returns`: `int`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.child_map" class="docs-object-method">&nbsp;</a>
```python
@property
child_map(self): 
```
Returns the map to subregexes for named regex components
- `:returns`: `Dict[str, RegexPattern]`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.parents" class="docs-object-method">&nbsp;</a>
```python
@property
parents(self): 
```

- `:returns`: `tuple[RegexPattern]`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.joiner" class="docs-object-method">&nbsp;</a>
```python
@property
joiner(self): 
```

- `:returns`: `str`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.join_function" class="docs-object-method">&nbsp;</a>
```python
@property
join_function(self): 
```

- `:returns`: `function`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.suffix" class="docs-object-method">&nbsp;</a>
```python
@property
suffix(self): 
```

- `:returns`: `str | RegexPattern`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.prefix" class="docs-object-method">&nbsp;</a>
```python
@property
prefix(self): 
```

- `:returns`: `str | RegexPattern`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.dtype" class="docs-object-method">&nbsp;</a>
```python
@property
dtype(self): 
```
Returns the StructuredType for the matched object

        The basic thing we do is build the type from the contained child dtypes
        The process effectively works like this:
            If there's a single object, we use its dtype no matter what
            Otherwise, we add together our type objects one by one, allowing the StructuredType to handle the calculus

        After we've built our raw types, we compute the shape on top of these, using the assigned repetitions object
        One thing I realize now I failed to do is to include the effects of sub-repetitions... only a single one will
        ever get called.
- `:returns`: `None | StructuredType`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.is_repeating" class="docs-object-method">&nbsp;</a>
```python
@property
is_repeating(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.capturing" class="docs-object-method">&nbsp;</a>
```python
@property
capturing(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.get_capturing_groups" class="docs-object-method">&nbsp;</a>
```python
get_capturing_groups(self, allow_inners=None): 
```
We walk down the tree to find the children with capturing groups in them and
        then find the outermost RegexPattern for those unless allow_inners is on in which case we pull them all

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.captures" class="docs-object-method">&nbsp;</a>
```python
@property
captures(self): 
```
Subtly different from capturing n that it will tell us if we need to use the group in post-processing, essentially
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.capturing_groups" class="docs-object-method">&nbsp;</a>
```python
@property
capturing_groups(self): 
```
Returns the capturing children for the pattern
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.named_groups" class="docs-object-method">&nbsp;</a>
```python
@property
named_groups(self): 
```
Returns the named children for the pattern
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.combine" class="docs-object-method">&nbsp;</a>
```python
combine(self, other, *args, **kwargs): 
```
Combines self and other
- `other`: `RegexPattern | str`
    >No description...
- `:returns`: `str | callable`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.wrap" class="docs-object-method">&nbsp;</a>
```python
wrap(self, *args, **kwargs): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.build" class="docs-object-method">&nbsp;</a>
```python
build(self, joiner=None, prefix=None, suffix=None, recompile=True, no_captures=False, verbose=False): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.compiled" class="docs-object-method">&nbsp;</a>
```python
@property
compiled(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_parent" class="docs-object-method">&nbsp;</a>
```python
add_parent(self, parent): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.remove_parent" class="docs-object-method">&nbsp;</a>
```python
remove_parent(self, parent): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_child" class="docs-object-method">&nbsp;</a>
```python
add_child(self, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.add_children" class="docs-object-method">&nbsp;</a>
```python
add_children(self, children): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.remove_child" class="docs-object-method">&nbsp;</a>
```python
remove_child(self, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.insert_child" class="docs-object-method">&nbsp;</a>
```python
insert_child(self, index, child): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.invalidate_cache" class="docs-object-method">&nbsp;</a>
```python
invalidate_cache(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__copy__" class="docs-object-method">&nbsp;</a>
```python
__copy__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__add__" class="docs-object-method">&nbsp;</a>
```python
__add__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__radd__" class="docs-object-method">&nbsp;</a>
```python
__radd__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__call__" class="docs-object-method">&nbsp;</a>
```python
__call__(self, other, *args, name=None, dtype=None, repetitions=None, key=None, joiner=None, join_function=None, wrap_function=None, suffix=None, prefix=None, multiline=None, parser=None, handler=None, capturing=None, default=None, allow_inner_captures=None, **kwargs): 
```
Wraps self around other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__str__" class="docs-object-method">&nbsp;</a>
```python
__str__(self): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.match" class="docs-object-method">&nbsp;</a>
```python
match(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.search" class="docs-object-method">&nbsp;</a>
```python
search(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.findall" class="docs-object-method">&nbsp;</a>
```python
findall(self, txt): 
```

<a id="McUtils.Parsers.RegexPatterns.RegexPattern.finditer" class="docs-object-method">&nbsp;</a>
```python
finditer(self, txt): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Parsers/RegexPatterns/RegexPattern.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Parsers/RegexPatterns/RegexPattern.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/Parsers/RegexPatterns.py?message=Update%20Docs)