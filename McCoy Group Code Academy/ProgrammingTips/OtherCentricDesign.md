# Writing for Someone Else

One of the cornerstones of good code is writing for other people.
What does this mean? In essence, always write as if someone else will use, and probably read, your code.
It doesn't matter if you're 100% sure no one else will use what you're doing (and that is probably a bad bet). Still, write as if someone will.
Even better, write as if someone who knows _less_ than you will use it.
That alone will encourage good practices, even if you don't know what good practices are.
Most of "good practice" comes naturally to people, as long as they're willing to do it.

## Guiding Principles

But it's probably good to codify what we think good practice is with respect to making sure that other people can use your code.
So here are some basic guiding principles and we'll show some concrete examples in a bit.

1. It should be clear to your user what can be used
2. No single thing should do too much
3. When possible, an object-oriented style should be used
4. Names should indicate function
5. The user shouldn't need to know about the details of the implementation


These aren't complete and keep in mind [all](https://engineering.intenthq.com/2015/03/what-is-good-code-a-scientific-definition/) [sorts](https://www.toptal.com/software/six-commandments-of-good-code) [of](https://developerzen.com/how-do-you-define-good-code-c8a383c207a4) [people](https://medium.com/better-programming/good-code-vs-bad-code-35624b4e91bc) [have](https://www.freecodecamp.org/news/the-junior-developers-guide-to-writing-super-clean-and-readable-code-cd2568e08aae/) [ideas](https://blog.pragmaticengineer.com/readable-code/) [about](https://jasonmccreary.me/articles/practices-write-readable-code-less-complex/) [good](https://gist.github.com/peterhurford/3ad9f48071bd2665a8af) [code](https://medium.com/swlh/writing-highly-readable-code-94da94d5d636).
Reading the literature is a great way to learn.

There are also other _practices_ we want to encourage like zealous commenting and usage of docstrings, but we think those are best picked up by looking at examples.


### Examples

_It should be clear to your user what can be used_: python provides a nice mechanism for this through the `__all__` variable. Any time you write a module or package, you can include this.

Here's an example, where I have a bunch of helper classes, but only want my users to use a single convenience function

```python
__all__ = ["my_function"]

# Objects:
class A:
    """A helper class for doing a thing"""
    ...
class B(A):
    """A secondary helper class for doing the thing"""
    ...
    
# Functions:

def my_function():
    """
    Does a super cool thing
    """
    a = A() # create an A object that we'll use to do an operation
    b = B() # I guess also create a B object?
    ...
```

Through this, I'm letting them know that I've only made 100% sure that `my_function` does what it should. There might be corner cases to `A` and `B` and their interactions that I haven't worked out yet.


_No single thing should do too much_ + _When possible, an object-oriented style should be used_: these two go hand-in-hand. By composing our primary use cases out of many smaller pieces, we're able to make sure that no one piece is trying to do too much.

Here's an example where we build a `House` object

```python
class Hinge:
    """A hinge object, e.g. for a door"""
    ...
class Lock:
    """A lock object, e.g. for a door"""
    ...
class Handle:
    """A handle object, e.g. for a door or faucet"""
    ...
    def __init__(self, lock=None):
        ...
class Material:
    """A material of some kind, e.g. wood"""
    ...
class Door:
    """A door object that can be used all over our house"""
    def __init__(self, handle, hinge, material):
        """
        :type handle: Handle
        :type hinge: Hinge
        :type material: Material
        """
        ...
class Floor:
    ...
...
class Story:
    ...
class House:
    """Our main house object. Only needs to have a set of Story objects, which are assumed to play well together"""
    def __init__(self, *stories):
        ...
```

By delegating the work, our `House` doesn't need to know how to open a door. Only a `Door` needs to know how to open a door. Our `House` doesn't even need to know what its "front door" is. It just needs to know what its ground story is, so that when a user asks it for the front door, it can pass the question on to its ground story.

This object-oriented style also makes things easier for your users. They can think about houses and doors. They understand the relationships between these things.
By being able to talk directly to objects, they can leverage this existing implicit understanding of how the world works.

_Names should mirror function_: hopefully this doesn't need an example. If it's a door, call it a `Door`; don't call it a `Spatula` and probably don't call it an `OpenCloseConstruct`.

_The user shouldn't need to know about details of implementation_: This is possibly the hardest one to pull off.

When writing code, it's really easy to accidentally require that your user knows how you did a thing.
Let's say you're generating an interpolating function and you're using an interpolation algorithm that only works if you've got evenly spaced points.
Your user likely won't know this _a priori_, and so if you don't check that their grid really is evenly spaced, it's entirely plausible that they'll naively give you unevenly spaced data and you'll give them total junk back in return.
Rather than forcing yourself to check everything over-and-over, a clean thing to do is to _only expose the functions you've bulletproofed_.
In this way, our first principle can help you need to do less work.
And if you are going to give a function to someone else, make sure you're doing things like [writing unit tests](https://docs.python-guide.org/writing/tests/) for it.

<span class="text-muted">Next:</span>
 [Writing for the Future](FutureCentricDesign.md)<br/>
<span class="text-muted">Previous:</span>
 [Why Write Good Code?](WhyWriteGoodCode.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/ProgrammingTips/OtherCentricDesign.md)
