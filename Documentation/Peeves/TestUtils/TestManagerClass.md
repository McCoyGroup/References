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
data_gen_tests: bool
test_files: str
test_name: str
test_root: property
base_dir: property
test_pkg: property
test_dir: property
test_data_dir: property
```
<a id="Peeves.TestUtils.TestManagerClass.__init__">&nbsp;</a>
```python
__init__(self, test_root=None, test_dir=None, test_data=None, base_dir=None, test_pkg=None, test_data_ext='TestData'): 
```

- `test_root`: `Any`
    >the root package
- `test_dir`: `Any`
    >the directory to load tests from (usually test_root/test_pkg)
- `test_data`: `Any`
    >the directory to load test data from (usually test_dir/test_data_ext)
- `base_dir`: `Any`
    >the overall base directory to start test discovery from
- `test_pkg`: `Any`
    >the name of the python package that holds all the tests
- `test_data_ext`: `Any`
    >the extension from test_dir to look for data in (usually TestData)

<a id="Peeves.TestUtils.TestManagerClass.test_data">&nbsp;</a>
```python
test_data(self, filename): 
```

<a id="Peeves.TestUtils.TestManagerClass.run">&nbsp;</a>
```python
run(self, exit=True): 
```

### Examples


___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Peeves/TestUtils/TestManagerClass.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Peeves/TestUtils/TestManagerClass.md)