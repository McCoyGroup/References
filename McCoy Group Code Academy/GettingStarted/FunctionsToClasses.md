# What is a Class?

Previously, we looked at writing functions. As we remember, they're mainly a way for us to make the logic of our code more obvious and less dependent on details of how we implement things (usually we call this _abstraction_).
We can use a higher-level object than a function, though, called a `class`.
The idea with a class is to allow us to write code in an even more abstract way that makes the logic of our program even clearer, by replacing things like looping through lists and manipulating arrays with relationships between different conceptual objects.
That's why this is usually called _object-oriented programming_.

This is the 1000 foot view, of course, and maybe somewhat conceptually difficult to wrap one's head around, so we'll take a concrete example that'll extend what we did before and also be useful as we move forward, by writing a class that this time we're calling `UnitConverter`.
Our `UnitConverter` will do one thing and one thing only: it'll convert units.
But in contrast to what we did before, we're gonna set it up so that it can handle any unit set, as long as we add the appropriate conversion factor.

What will this look like? Well we'll write up the actual implementation later, but this idea is we want something that we can use like

```python
converter = UnitConverter() # we need to make an "instance" of our class before we can use it; this is more useful when we have multiple instances that need to be distinct from each other
data = ...
new_data = converter.convert(data, "angstroms", "bohr")
```

### Why Do I Care?

Before we get into this, we should make it clear why this is useful.
If you're like me, you're probably thinking _"I can convert units via a function already, why would I want to change that"_.
My counter-point is twofold:

1. our prior attempts were restricted in what they could do
2. our new version can easily be used inside _other_ classes

We'll get to `1.` in a moment, but just to give a 5 second idea of what we'll can think about doing with `2.`. Let's imagine we have a `Molecule` class that stores atoms and their positions.
Maybe we need the positions to always be in `"bohr"`, we can then imagine doing something like the following. Don't worry if the syntax is a bit cryptic, we'll get to that later and I'll emphasize what matters here.

```python
class Molecule:
  converter = UnitConverter()
  def __init__(self, atoms, coords, coord_units="angstroms"):
    self.coords = self.converter(coords, coord_units, "bohr")
    ...
```

The key, here, is that we've got an instance of our `UnitConverter` attached to our `Molecule` class and no matter what units our `coords` start in, our `converter` can convert them. Moreover, if we find we need to add a new unit, we can add it directly to the `converter`, rather than having to change up our unit conversion function.
This becomes even more useful when we start turning more things into objects and writing our code as interactions between them.

### Let's Try it!

Having hopefully convinced you that it's at least worth trying to write object-oriented code, let's see what this looks like when we implement it.
The syntax for defining a class of objects looks similar to the way we define a function, except for where we put the arguments.
On the other hand, there're two key differences:
1. classes can hold data, too
2. classes can have more than one function

For instance, our `UnitConverter` class might look like

```python
class UnitConverter:
  """
  An object that allows for conversions of quantities from one unit to another
  """
  conversion_factors = {...}
  def get_conversion(self, from_unit, to_unit):
    """
    Gets the conversion factor between `from_unit` and `to_unit` or raises an error if that's not possible
    :type from_unit: str
    :type to_unit: str
    """
    ...
  def convert(self, quantity, from_unit, to_unit):
    """
    Converts `quantity` from `from_unit` to `to_unit` or raises an error if that's not possible
    :type from_unit: str
    :type to_unit: str
    """
    ...
```

You'll notice that we have a `dict` called `conversion_factors` which is where we'll stick our conversions.
You'll also notice that we put a number of `def` statements in this class, which looks a lot like a regular function definition, except each has a `self` argument. We call these _methods_, and this `self` argument is the only reason they're different from regular functions.
On the other hand, this `self` is really why this is "object-oriented".
When we make an instance of our class and call one of its methods, the instance itself is passed as that `self` argument, which means it can refer to its own stored data.

To see why this is powerful, let's look at how we'd implement `get_conversion` and `convert`.
For now, we'll just set up one conversion factor between angstroms and Bohr radii, giving us

```python
class UnitConverter:
  """
  An object that allows for conversions of quantities from one unit to another
  """
  conversion_factors = {("bohr", "angstroms"):.529} # look up a more precise number if you're gonna reuse this
```

so with this in mind, we can think about how we'd implement the `get_conversion` function, which might look like

```python
  def get_conversion(self, from_unit, to_unit):
    """
    Gets the conversion factor between `from_unit` and `to_unit` or raises an error if that's not possible
    :type from_unit: str
    :type to_unit: str
    """
    # first we try to pull out a conversion in the forward direction
    key = (from_unit, to_unit)
    forward_direction = False
    # if we can't find a conversion factor in the forward direction,
    # we try to go the reverse direction
    if key not in self.conversion_factors:
      key = (to_unit, from_unit)
      forward_direction = True
    # if we can't find a conversion factor at all, we raise an error
    if key not in self.conversion_factors:
      raise KeyError(
        "No conversion factor from '{}' to '{}' known".format(
          from_unit, to_unit
      ))
    # otherwise we pull the conversion factor, and if the factor
    # is for the reverse direction, we invert it
    conv = self.conversion_factors[key]
    if not forward_direction:
      conv = 1 / conv
    return conv
```

and then with this in hand, we can pretty easily do the `convert` method

```python
  def convert(self, quantity, from_unit, to_unit):
    """
    Converts `quantity` from `from_unit` to `to_unit` or raises an error if that's not possible
    :type from_unit: str
    :type to_unit: str
    """
    conv = self.get_conversion(from_unit, to_unit)
    return conv * quantity
```

<span class="text-muted">Next:</span>
 [Another Example of Classes](AnotherClassExample.md)<br/>
<span class="text-muted">Previous:</span>
 [How to Write a Function](HowToWriteAFunction.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/FunctionsToClasses.md)
