# Your First Python Script

The biggest hurdle to overcome when starting out isn't the kind of abstract thinking coding requires, nor is it needing to understand the syntax of the language, and it's definitely not needing to know how computers do what they do--very few programmers actually know that.
Instead, it's literally just getting everything installed and playing nicely together.
So we're gonna walk through the basics of what'll be needed to get through this tutorial.

## Set Up

You can either work with Python interactively in the command window, or with an IDE like PyCharm. 

### Interactive Python

Python provides us with something called a _read-evaluate-print loop_ (REPL) which is just a way to interactively play around with the language.
We can fire this up by opening up the _command prompt_ which is just a way that we can interact with our computer directly via commands, rather than by clicking on icons and stuff.
On Mac this is a program called Terminal, on Windows it's called Command Prompt.
If you're using Linux, there's a decent chance you're already familiar with the command prompt, which is good because I don't know how to open it on Linux.

In any case, no matter which you use you should see a blank, bare bones window in which to type stuff. Mine looks like

![my terminal](img/blank_terminal.png){: width="500px"}

on that blank line, assuming everything installed nicely, we can just type

```console
$ python3
```

and then when we press enter we should get a response like this

```console
$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

That `>>>` tells us that python is ready to read what we write, evaluate it, and print out a result.
I'm not sure how much we want to belabor python syntax or anything like that, seeing as there are tutorials out there that teach the syntax very well, e.g. the proper [Code Academy](https://www.codecademy.com/learn/learn-python-3) ones or, just because I got my start programming with them, the [MIT OCW lectures](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/index.htm).
That said, we'll quickly run through how we can use this to explore.

Let's try a series of inputs

```
>>> 1 # just a number for python to spit out
1
>>> 1+1 # we can add
2
>>> 1+1+1 # we can do lots of adding
3
>>> 1*5 # we can multiply
5
>>> 'my cat' # python supports word-like stuff (always called strings in the programming world)
'my cat'
>>> 'my cat'*5 # you can multiply strings by integers to repeat them
'my catmy catmy catmy catmy cat'
>>> ['my cat]*5 # if your syntax is wrong python will whine at your
  File "<stdin>", line 1
    ['my cat]*5
              ^
SyntaxError: EOL while scanning string literal
>>> ['my cat']*5 # you can repeat stuff in lists by multiplying by an integer (a list is just python's name for a sequence of stuff)
['my cat', 'my cat', 'my cat', 'my cat', 'my cat']
>>> ';_;'.join(['my cat']*5) # if you've got a bunch of strings in a list, you can join them
'my cat;_;my cat;_;my cat;_;my cat;_;my cat'
```

I'm not gonna run through all the possible options, since the only way to learn is to play around with it.
Something that gets lost in discussions of how to learn to program is that it should be _fun_.
It's a way to explore ideas and build tools that you can share with other people, so have fun with it.
Do silly things, make mistakes, hack into the NSA's servers, sell state secrets to the highest bidder, get arrested, etc.
This is a great time to explore, and the moment you turn 18 all of that gets expunged from your permanent record.

## Writing and Running a Script

If you haven't already installed PyCharm, now might be a good time to. Actually, just do it. Here are the [instructions](IntroToIDEs.md). PyCharm is basically a Spell Check of sorts for Python Code, so if you are gonna start writing scripts, why wouldn't you want Spell Check?

Ok, now we're ready to start writing a script that'll do something super cool.
What this super cool thing is...well that's still TBD. (and to be determined by you!)
For now we're just gonna write a script that converts frequencies from wavenumbers (cm^-1) to their atomic units (Hartree).
To do so we'll make a file called `wave_to_au.py`.

In it, to start, we'll put this content:

```python
  frequency = 3600  # the frequency of an OH strech in water 
  conversion_factor = 219474.6  # cm^-1 = 1 Hartree
  print()
```
Now, let's break this down a little bit:

# What else can we do with this?
...

Now, we'll move onto discussing some tips for making it easier to write code that does interesting stuff.
Don't feel like you need to plow straight on, though.
Play around for a while and go on when you're ready.

<span class="text-muted">Next:</span>
 [To Functions and Beyond](FunctionsAndBeyond.md)<br/>
<span class="text-muted">Previous:</span>
 [Introduction](intro.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/CommonIssues.md)
