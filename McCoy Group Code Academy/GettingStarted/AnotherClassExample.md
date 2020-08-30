# Another Example of Classes

We just walked through a pretty simple example of how to get started with object-oriented programming, but that example also might not be the best one for showcasing what classes can do for you.
It's a great place to start, but you might have noted that we only ever have one `UnitConverter` object at once, and none of that really _needed_ to be its own object.

So we're gonna take another go at this, but with a use case that really shows what python classes can do for you.
Our example here will be writing a `Timer` class, that can tell you how fast a chunk of code ran.
This kind of thing is called _profiling_, and is particularly important when you're trying to make your code fast and efficient.

The basic design of our object will be as follows

* A `Timer` wraps a block of code to time
* A `Timer` has meta-info attached to it, like a `name`
* A `Timer` has a method to print out its timing info
* A `Timer` can be reused over multiple iterations

I'm going to put my entire implementation here, for now, but we'll break it down so don't worry if the full block is a bit overwhelming. We'll make it not so.

```python
class Timer:
    """
    Defines a Timer object that can be used with `with` to time a block of code
    """
    def __init__(self, name="Timer", print=True, num_digits=5):
        """
        :param name: name of the timer
        :type name: str
        :param print: whether to print results immediately or not
        :type print: bool
        :param num_digits: the number of digits to round results to
        :type num_digits: int
        """
        self.name = name
        self.print = print
        self.num_digits = num_digits
        self.start_time = None
        self.timing_results = []
    def start(self):
        """
        Starts the timer
        :return:
        :rtype:
        """
        import time
        self.start_time = time.time()
    def end(self):
        """
        Ends the timer
        :return:
        :rtype:
        """
        import time
        self.timing_results.append(time.time()-self.start_time)
        self.start_time = None
    def __enter__(self):
        """
        With `__exit__` one of the two methods we need to provide so that the python `with` statement works
        This sets up the timer to run
        :return:
        :rtype:
        """
        self.start()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        With `__enter__` one of the two methods we need to provide so that the python `with` statement works
        This exits the timing block
        :return:
        :rtype:
        """
        self.end()
        if self.print:
            self.print_latest()
    def print_latest(self):
        """
        Prints the most recent timing
        :return:
        :rtype:
        """
        print("{name}: took {time}s".format(
            name=self.name,
            time=round(self.timing_results[-1], self.num_digits)
        ))
    def print_all(self):
        """
        Prints the total and average times over all of the iterations
        :return:
        :rtype:
        """
        print("{name}: took {total_time}s over {iters} iterations for {avg_time}s/loop".format(
            name=self.name,
            total_time=round(sum(self.timing_results), self.num_digits),
            iters=len(self.timing_results),
            avg_time=round(sum(self.timing_results)/len(self.timing_results), self.num_digits)
        ))
    def __repr__(self):
        """
        If this method is implemented, python changes the way the object prints out
        :return:
        :rtype:
        """
        cls = type(self)
        return "{}(name='{}', print={}, num_results={}, avg_time={}s)".format(
            cls.__name__,
            self.name,
            self.print,
            len(self.timing_results),
            round(sum(self.timing_results)/len(self.timing_results), self.num_digits)
        )
```

The first thing you probably noted was that we have a bunch of methods that look like `__<word>__`. This method naming format, starting and ending with two underscores, is the way we know this is a 'special' method (sometimes called a _magic method_ in the python documentation).
These methods are designed to interact directly with python, allowing us to use the `with` statement with a class or change the way an object displays on the screen.
There are many methods like these, and it's worth having at least a cursory knowledge of what they are and do.

The first one of these worth looking at is the `__init__` method.
This is called by python when we make an instance of our class. We can look at what we did here

```python
    def __init__(self, name="Timer", print=True, num_digits=5):
        """
        :param name: name of the timer
        :type name: str
        :param print: whether to print results immediately or not
        :type print: bool
        :param num_digits: the number of digits to round results to
        :type num_digits: int
        """
        self.name = name
        self.print = print
        self.num_digits = num_digits
        self.start_time = None
        self.timing_results = []
```

in this method we take three arguments (`name`, `print,` and `num_digits`) and we attach them to our instance.
We also initialize a property called `start_time` and a list of `timing_results`.
All of these will be used by the object when we ask it to do things.

It's this method that allows us to do stuff like

```python
timer_instance = Timer("My Block")
```

and give our `Timer` instance a `name` at the same time as we make it.

### `__enter__` and `__exit__`

This pair of functions is another one that python looks for to enable special behavior.
Formally, these define a [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers), which just means we can use them with the `with` statement.
I.e. this allows us to do stuff like

```python
import time
with Timer("My Block"):
    time.sleep(1)
## Out:
# My Block: took 1.00296s
```

If we look at our implementation of `__enter__`, we'll see it's actually pretty simple

```python
    def __enter__(self):
        """
        With `__exit__` one of the two methods we need to provide so that the python `with` statement works
        This sets up the timer to run
        :return:
        :rtype:
        """
        self.start()
        return self
```

Most of this is just documentation string, and we see we actually only have two lines of code. First we call `self.start()`, then we `return self`.

The first step just executes what we need to do before running the block we're timing. The second one allows us to do stuff like

```python
import time
with Timer("My Block") as my_timer:
    time.sleep(1)
print(my_timer)
## Out:
# Timer(name='My Block', print=True, num_results=1, avg_time=1.00296s)
```

whatever we `return` from `__enter__` can be bound to the variable coming after `as`.

Our `__exit__` method is also pretty spare. If we ignore the docstring, we have

```python
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
        if self.print:
            self.print_latest()
```

the `end` function here records the actual timing, and the `if self.print` block prints the latest timing, assuming we didn't pass `print=False` to our `Timer`.

### `__repr__`

In the last example, you might also have noticed that the output from that looks like `Timer(...)`, rather than the default `<__main__.Timer object at 0x10b24eeb8>`.
That's because we set up a `__repr__` method. This should return a string that python uses as the display form for our object.
It's also what would be returned by the `repr` function, if you were to call that.

We followed the "standard" `repr` format, inasmuch as there is one, and it's probably worth going over the function in a little detail.

```python
    def __repr__(self):
        cls = type(self)
        return "{}(name='{}', print={}, num_results={}, avg_time={}s)".format(
            cls.__name__,
            self.name,
            self.print,
            len(self.timing_results),
            round(sum(self.timing_results)/len(self.timing_results), self.num_digits)
        )
```

### `start`, `end`, `print_latest`, and `print_all`

These four methods are the ones that actually make our timer a timer.
They implement the starting, stopping, and reporting of our results.
They're also, I'd wager, more straightforward to understand than the `__<...>__` methods. So here's an exercise left to the reader: work through how these four methods do what they do.

## Benefits of Object Orientation

As with most things, you could emulate this `Timer` without object-oriented programming or classes. But, first off, you'd lose access to stuff like `with`, and secondly it'd be less natural.

In particular, with this class setup we get the ability to nest timers with 0 extra work, e.g. we can do

```python
import time
with Timer("Main Block"):
    time.sleep(3)
    subtimer = Timer("Sub Block", print=False)
    for i in range(20):
        with subtimer:
            time.sleep(.05)
    subtimer.print_all()
## Out:
# Sub Block: took 1.04951s over 20 iterations for 0.05248s/loop
# Main Block: took 4.05038s
```

if we were managing all of the arrays and data ourselves, we'd have a harder timer making these things 100% nestable/bug free.


<span class="text-muted">Next:</span>
 [What Now?](WhatNow.md)<br/>
<span class="text-muted">Previous:</span>
 [From Functions to Classes](FunctionsToClasses.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/AnotherClassExample.md)