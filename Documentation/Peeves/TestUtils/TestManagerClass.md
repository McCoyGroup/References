## <a id="Peeves.TestUtils.TestManagerClass">TestManagerClass</a>
Just manages where things load from

### Properties and Methods
```python
log_file: str
log_results: bool
quiet_mode: bool
debug_tests: bool
validation_tests: bool
timing_tests: bool
test_files: str
test_root: property
base_dir: property
test_pkg: property
test_dir: property
test_data_dir: property
```
```python
__init__(self, test_root=None, test_dir=None, test_data=None, base_dir=None, test_pkg='Tests', test_data_ext='TestData'): 
```

```python
test_data(self, filename): 
```

```python
run(self, exit=True): 
```

### Examples
