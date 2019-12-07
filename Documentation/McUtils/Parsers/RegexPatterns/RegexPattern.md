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
join_function: property
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
```python
__init__(self, pat, name=None, children=None, parents=None, dtype=None, repetitions=None, key=None, joiner='', join_function=None, wrapper_function=None, suffix=None, prefix=None, parser=None, handler=None, capturing=None, allow_inner_captures=False): 
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

```python
get_capturing_groups(self, allow_inners=None): 
```
We walk down the tree to find the children with capturing groups in them and
        then find the outermost RegexPattern for those unless allow_inners is on in which case we pull them all

```python
combine(self, other, *args, **kwargs): 
```
Combines self and other
- `other`: `RegexPattern | str`
    >No description...
- `:returns`: `str | callable`
    >No description...

```python
wrap(self, *args, **kwargs): 
```

```python
build(self, joiner=None, prefix=None, suffix=None, recompile=True, no_captures=False, verbose=False): 
```

```python
add_parent(self, parent): 
```

```python
remove_parent(self, parent): 
```

```python
add_child(self, child): 
```

```python
add_children(self, children): 
```

```python
remove_child(self, child): 
```

```python
insert_child(self, index, child): 
```

```python
invalidate_cache(self): 
```

```python
__copy__(self): 
```

```python
__add__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

```python
__radd__(self, other): 
```
Combines self and other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

```python
__call__(self, other, *args, name=None, dtype=None, repetitions=None, key=None, joiner=None, join_function=None, wrap_function=None, suffix=None, prefix=None, multiline=None, parser=None, handler=None, capturing=None, allow_inner_captures=None, **kwargs): 
```
Wraps self around other
- `other`: `RegexPattern`
    >No description...
- `:returns`: `_`
    >No description...

```python
__repr__(self): 
```

```python
__str__(self): 
```

```python
__getitem__(self, item): 
```

```python
match(self, txt): 
```

```python
search(self, txt): 
```

```python
findall(self, txt): 
```

```python
finditer(self, txt): 
```

### Examples
