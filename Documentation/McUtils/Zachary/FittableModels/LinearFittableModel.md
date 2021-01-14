## <a id="McUtils.Zachary.FittableModels.LinearFittableModel">LinearFittableModel</a>
Defines a class of models that can be expressed as linear expansions of basis functions.
We _could_ define an alternate fit function by explicitly building & fitting a design matrix, but I think we're good on that for now

### Properties and Methods
<a id="McUtils.Zachary.FittableModels.LinearFittableModel.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, basis, initial_params=None, pre_fit=False, covariance=None): 
```

<a id="McUtils.Zachary.FittableModels.LinearFittableModel.evaluate" class="docs-object-method">&nbsp;</a>
```python
evaluate(self, xdata): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/FittableModels/LinearFittableModel.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/FittableModels/LinearFittableModel.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/FittableModels/LinearFittableModel.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/FittableModels/LinearFittableModel.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/FittableModels.py?message=Update%20Docs)