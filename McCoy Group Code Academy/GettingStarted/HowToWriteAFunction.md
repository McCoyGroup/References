## What are Signs of a Good Function?

A good function has a clear objective while still maintaining _flexibility_. This is really important as you build up a code base. You want to write functions that do a specific task and usually just one or two operations. This relates back to the Hierarchical View of Problem Solving mentioned [here](https://mccoygroup.github.io/References/References/Intro%20To%20Quantum/AHierarchicalViewOfProblemSolving.html). This makes your code easier to debug too because it breaks everything up into smaller chunks. We like functions because they make our code _flexible_ which makes it easy to move between molecules and systems. Previously, in our `wave_to_au.py` script we wrote it so that we could convert one specific value. If we took that script and rewrote it into a function, we could make the function argument the `frequency` variable which would make it much more _flexible_ and we could convert any frequency we want!  

## Let's Try it!

You can start a new script or keep editing `wave_to_au.py`, but you will have to rename the file if you want your function name to be `wave_to_au`. 

### First we will define our function: 

``` python
def wave_to_au(frequency):
  conversion_factor = 219474.6  # cm^-1 = 1 Hartree
  frequency_au = frequency / conversion_factor
  return frequency_au
```

Let's break this down: 
1. Use `def` statement to name function (`wave_to_au`) and set any arguments (`frequency`)
   * There are three main types of arguments: Default, Keyword, and Arbitrary.
   * We currently have an Arbitrary argument where the user has to call this function with some value for frequency defined. If we decided to provide the user with a Default argument, our `def` statement would look like `def wave_to_au(frequency=3600)` where if no input value is provided then the code assumes `frequency = 3600`. Finally if we had multiple arguments, we would want to use Keyword arguments to make sure all the values were defined appropriately.
   * Read more about arguments [here](https://data-flair.training/blogs/python-function-arguments/).
2. Define any variable _local_ to the function
   * In this case, the variable `conversion_factor` is only known to the function `wave_to_au` where as before `conversion_factor` was _global_ and could be called from anywhere in the script. 
   * Now, you can only call the variable `conversion_factor` within the function `wave_to_au`.
   * Read more about this [here](https://www.geeksforgeeks.org/global-local-variables-python/) or play around with this idea by moving your definition of `conversion_factor` in and out of the function
3. Convert the frequency
4. `return` the frequency
   * In this format we `return` the value we compute for `frequency_au` instead of printing it. If we wanted we could add the print statement to our function above the return statement though. 
   * By using `return` instead of `print()` we set an output to the function so we can assign it a variable name. 
   
### Next we will test our function: 

In order to test this function, we need to make a call to it. Make sure you are out of the function definition, then this may look something like:

```python
 value = wave_to_au(3600)
```

but you'll notice that doesn't show us any results. You can try:

```python
  value = wave_to_au(3600)
  print(value)
```

or define a testing variable `test_freq` and bring back our f-string friend for:

```python
  test_freq = 3600
  value = wave_to_au(test_freq)
  print(f"{test_freq} wavenumbers is {value} in Hartree")
```

Another fun thing about f-strings is that they can even evaluate a simple function like this one, so we could modify our call to be:

```python
  test_freq = 3600
  print(f"{test_freq} wavenumbers is {wave_to_au(test_freq)} in Hartree")
```

By now, you will have noticed that the function does the same exact thing our previous script did. But now it is _flexible_. For example, if I wanted to convert the three IR frequencies of a water molecule[<sup>1</sup>], I could by calling to the function three seperate times like so: 

```python
   asym_stretch = 3490
   sym_stretch = 3280
   bend = 1654
   asym_stretch_au = wave_to_au(asym_stretch)
   sym_stretch_au = wave_to_au(sym_stretch)
   bend_au = wave_to_au(bend)
   print(f"The IR frequencies of water are {asym_stretch_au}, {sym_stretch_au}, and {bend_au} in Hartree.")
```

### Now, let's make our script more flexible. 
Orginally we started with a script that converted one frequency to atomic units. Now, our function can convert any frequency we give it. But what if we combined two scripts such as `wave_to_au.py` and `ang_to_bohr.py` to make a more generic `converter.py` script. In order to do this, first you will need to write a function that converts from angstroms to bohr.  We want the function to work in this way so that both of our functions are going from some unit into atomic units, mainly so we don't get confused later.  

This new function will probably look something like:

``` python
def ang_to_bohr(distance):
  conversion_factor = 0.529177  # angstrom = 1 Bohr
  distance_au = distance / conversion_factor 
  return distance_au
```
Test this function by running: 
```python
   ang_to_bohr(0.96)  # the average bond length of an OH in water. 
```

Notice how we used the same variable name `conversion_factor`? That's because we defined them _locally_ so they don't know about each other and won't interfere with one another! Try printing the variable from various places in the code if you don't believe me. 

### Finally, let's test this script. 

Now we can ask our functions to return some statement like:

```python
  "The average frequency of an OH bend in water is 0.01640 Hartree and it has an average bond length of 1.81414 Bohr."
```

Try it yourself! Does your run call and print statement look something like:

```python
testFreq = 3600
testAng = 0.96
print(f"The average frequency of an OH bend in water is {wave_to_au(testFreq):.5f} Hartree and it has an average bond length of {ang_to_bohr(testAng):.5f} Bohr.")
```

### What else can we do with this?
Now that we took our script and organized it into functions, is there another layer of organization we can add? Yep! The next step from here is writing code into object-orientated structures called *Classes*. Spend some time playing with functions and when you are ready move on to [From Functions to Classes](FunctionsToClasses.md)

---
1. <a id="fn1"></a> Frequencies from [NIST Webbook](https://webbook.nist.gov/cgi/inchi/InChI%3D1S/H2O/h1H2). 

[<sup>1</sup>]: #fn1

<span class="text-muted">Next:</span>
 [From Functions to Classes](FunctionsToClasses.md)<br/>
<span class="text-muted">Previous:</span>
 [Your "First" Python Script](FirstPythonScript.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/HowToWriteAFunction.md)
