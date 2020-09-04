## <a id="McUtils.Zachary.FittableModels.LinearFittableModel">LinearFittableModel</a>
Defines a class of models that can be expressed as linear expansions of basis functions.
    We _could_ define an alternate fit function by explicitly building & fitting a design matrix, but I think we're good on that for now

### Properties and Methods
<a id="McUtils.Zachary.FittableModels.LinearFittableModel.__init__">&nbsp;</a>
```python
__init__(self, basis, initial_params=None, pre_fit=False, covariance=None): 
```

<a id="McUtils.Zachary.FittableModels.LinearFittableModel.evaluate">&nbsp;</a>
```python
evaluate(self, xdata): 
```

### Examples
