# Writing for the Future

The second of the ideas that we want to highlight with this is the need to write with the future in mind.
In programming speaks, this means your code needs to be [maintainable](https://softwareengineering.stackexchange.com/questions/134855/what-characteristics-or-features-make-code-maintainable) and [extensible](http://whats-in-a-game.com/coding-for-the-future-readability-and-extensibility/).
Incidentally, both of these actually heavily play into our previous argument that you should write as if other people will read your code.

## Maintainability

But, honestly, bother of these concepts are a bit subjective, so what do we mean when we say "code should be maintainable"?
We are not professional computer scientists, so we have no good, formal prescription for what will make your code easier to debug in the future.
On the other hand, here are the three things we think are most important
1. Code should be self-documenting and complemented with minimal, but complete documentation
2. The behavior of a function should not change based on subtleties of internal details
3. For high-level or complex functionality, usage examples & expected results must be provided

You won't always be able to do all of these. You might not even _often_ be able to, but we think you should still strive to.
Why are these important? 
Well, first off, the best documentation is the documentation you don't need to write.
If the behavior of a function can be explain by pointing someone to a simple tutorial on say, [finite difference derivatives](https://en.wikipedia.org/wiki/Finite_difference#Relation_with_derivatives), then you should do that. 
So give things names that will help people find those tutorials.
Let other people do the heavy lifting for you, so you can spend more time doing research.
Secondly, if your function returns different results when passed the array `[1, 1, 1]` instead of `[1., 1., 1.]`, this is going to cause you all sorts of grief.
Of course, there are times (often due to design decisions of other people...) where you won't be able to hide all of the internal details. 
We'll cover what you should try to do in those cases later on.
Finally, an example is worth 1000 words of documentation. Why explain what your class does when you can demonstrate it instead? 
And once you're already writing examples, why not turn them into [tests](https://realpython.com/python-testing/) so that if you change things in the future, you know your code hasn't broken?

Of course, that's all still very general, so let's dig in to a few more concrete cases.

#### Self-Documenting Code & Minimal, Complete Documentation

There are [many](https://stackoverflow.com/questions/209015/what-is-self-documenting-code-and-can-it-replace-well-documented-code), [many](https://stackoverflow.com/questions/23680467/self-documenting-python-code), [many](https://itnext.io/tips-for-writing-self-documenting-code-e54a15e9de2), [many](https://multi-programming.com/blog/self-documenting-code), [many](https://hackbrightacademy.com/blog/writing-self-documenting-code/) pieces on self-documenting code on the internet. There are [just](https://medium.com/it-dead-inside/self-documenting-code-is-mostly-nonsense-1de5f593810f) [as](https://medium.com/eloquent-coding/do-developers-dream-of-self-documenting-code-ca64d472197a) [many](https://www.ericholscher.com/blog/2017/jan/27/code-is-self-documenting/) arguing that self-documenting code isn't sufficient.
Both are true, but we're aiming at scientists, not software engineers, here, and so we're guessing that most people haven't even heard the term "self-documenting code".

So what's the crux of the argument, here? 
Well, mainly that someone should be able to use your code, optimally, without having to read documentation or source code. 
Given that good documentation is just as difficult to write as code itself, and that you often need ten lines of documentation to explain five lines of code, getting away without documentation seems like a bargain.
For most real-world stuff, this won't be sufficient, and of course documentation explains the objective of the code, not just its operation, but if you can write less documentation because you wrote better code, we'd call that good.

What are the characteristics of self-documenting code? We're going to claim there are four big ones
* All functionality is written in functions and classes
* Individual functions are kept small
* Names indicate intent and operation
* There are no magic parameters

We'll walk through these one-by-one

> *All functionality is written in functions and classes*

Most blog posts you'll read will probably omit this first one, but we're dealing with scientists here, and so we felt it should be made explicit.
All we're trying to say is that instead of having a python module that does this

```python
ws = np.zeros(500)
for x in range(10000):
    ws += np.random.rand(500)
    e = 1/2*200*(ws)**2
    vr = np.average(e)
print(ws, vr)
```

you write that module like

```python

def run_simulation(n_steps):
    ws = np.zeros(500)
    for x in range(n_steps):
        ws += np.random.rand(500)
        e = 1/2*200*(ws)**2
        vr = np.average(e)
    return ws, vr

if __name__ == "__main__":
    print(run_simulation(10000))
```

Currently, that's not much more readable, but at least we're making it clear that we intend for that block to be a simulation that we're running. 
We're also making it so that we can reuse `run_simulation` elsewhere without having to modify the source code later, which is always error-prone.

> *Individual functions are kept small*
> *Names indicate intent and operation*

This is only a five line program, but we can make it even cleaner by splitting the pieces up. We'll move toward more evocative names

```python
def get_initial_walkers():
    return np.zeros(500)
def get_displacements():
    return np.random.rand(500)
def get_energy(walkers):
    return 1/2*200*(walkers)**2
def get_vref(energy):
    return np.average(energy)
def propagate(walkers):
    walkers += get_displacements()
    energies = get_energy(walkers)
    reference_energy = get_vref(energies)
    return walkers, reference_energy
def run_simulation(n_steps):
    walkers = get_initial_walkers()
    for x in range(n_steps):
       walkers, reference_energy = propagate(walkers)
    return walkers, reference_energy

if __name__ == "__main__":
    print(run_simulation(10000))
```

The big benefit of this is that now the intent of every step is clear. 
Our `run_simulation` just initializes a pool of walkers and does `n_steps` of propagation. 
Our propagation just displaces and calculates the average energy.
(It's also clear from this that this is not a useful simulation, by making the structure of the problem clearer that's easier to see_).

> *There are no magic parameters*

This is one of the things that scientists do that most cramps the maintainability of their code.
You'll note in this code that we have all sorts of numbers floating around, hard coded in, without any explanation.
People need to really read the code to understand what they mean, and what if they want to simulate with a different set of parameters?
Better is to give these parameters names and simultaneously make them passable to the `run_simulation`.
Python supports default values, so make use of that.

Our final pass, which is not to say that this code is good, necessarily, might look like

```python
def get_initial_walkers(num_walkers):
    return np.zeros(num_walkers)
def get_displacements(num_walkers):
    return np.random.rand(num_walkers)
def get_harmonic_energy(walkers, mass=1/2, frequency=20):
    return 1/2*(mass*frequency**2)*(walkers)**2
def get_vref(energy):
    return np.average(energy)
def propagate(walkers, potential):
    walkers += get_displacements(len(walkers))
    energies = potential(walkers)
    reference_energy = get_vref(energies)
    return walkers, reference_energy
def run_simulation(n_steps, num_walkers=500, potential=get_harmonic_energy):
    walkers = get_initial_walkers(num_walkers)
    for x in range(n_steps):
       walkers, reference_energy = propagate(walkers, potential)
    return walkers, reference_energy

if __name__ == "__main__":
    print(run_simulation(10000))
```

The actual process of calling `run_simulation` hasn't changed at all. But now everything has a name. 
The numbers in `get_energy`? Turns out they were just parameters for a harmonic potential.
And now if someone wants to call `run_simulation` with a different set of parameters, they just have to pass them.
The number of lines of code is maybe ~2X what it originally was, but the code now tells the reader what it's trying to do & 
gives the user the flexibility to try new things without having to mess with the source.

Now we're going to want to add some minimal, but complete documentation to this. If this were a diffusion Monte Carlo simulation, we could mostly just [point people to a reference](../../References/Monte%20Carlo%20Methods/DMC.md).
Unfortunately it's not, so we need to add a [docstring](https://www.programiz.com/python-programming/docstrings) to this module.
That might look like

```python
"""
my_simple_simulation computes the average energy of a set of harmonic oscillators as they randomly.
`run_simulation` runs a simulation out for a specified number of time steps and gives back the oscillator positions and average energy.
This can be extended by changing up the potential function.
"""

def get_initial_walkers(num_walkers):
    return np.zeros(num_walkers)
def get_displacements(num_walkers):
    return np.random.rand(num_walkers)
def get_harmonic_energy(walkers, mass=1/2, frequency=20):
    return 1/2*(mass*frequency**2)*(walkers)**2
def get_vref(energy):
    return np.average(energy)
def propagate(walkers, potential):
    walkers += get_displacements(len(walkers))
    energies = potential(walkers)
    reference_energy = get_vref(energies)
    return walkers, reference_energy
def run_simulation(n_steps, num_walkers=500, potential=get_harmonic_energy):
    walkers = get_initial_walkers(num_walkers)
    for x in range(n_steps):
       walkers, reference_energy = propagate(walkers, potential)
    return walkers, reference_energy

if __name__ == "__main__":
    print(run_simulation(10000))
```

#### The behavior of a function should not change based on subtleties of internal details

This one is a bit hard to get concrete examples of, but we can give some more general examples of what often happens.
Let's say you've been developing a new method call `Floopation`, or maybe just implementing it in a new context. 
Let's further say that the function you wrote to do it is called `floopate_wavefunctions`.
We'll assume your first implementation of it was designed to take in 1D systems. This is a common, good starting place.
Then you had to go deal with other projects and someone else comes on later to use your code.
Hopefully you'll agree this is a plausible scenario.

Now we need to make the calling of `floopate_wavefunctions` a bit more concrete. Maybe the call signature looks like

```python
def floopate_wavefunctions(base_array, ...):
    """floopate_wavefunctions performs Floopation(doi:66600/s12.at34a.n) on base_array"""
    # your amazing function here
    ...
```

We'll assume that the future person knows that `base_array` has to be 1D. Unfortunately 1D could mean a [row vector or a column vector](https://en.wikipedia.org/wiki/Row_and_column_vectors) and nothing in this indicates which shape `base_array` should have.
Perhaps you knew that it had to be a column vector, but the person taking over after you doesn't.
And NumPy, in its desire to be helpful, will likely not throw an error if it's passed as a row vector, but might well return a drastically different result in return.
In this case, it's crucial to both document what form these things should take as well as put safety checks in place.

You can't code for every use case. That is an unfortunate truth. You _can_ however throw errors for everything that looks like it might be wrong.
Errors are your friends. Make use of them.
Conversely, don't try to be too kind to your users. 
It's good to take a broad range of inputs, if you know how to convert them to the form your code expects.
On the other hand it's worse to mis-handle an input out of a desire to cover all use cases than to throw and error if you're not totally sure what to do.

And as long as the error message is reasonable, this will definitely help the people who have to maintain this code after you.

#### Usage examples & expected results must be provided



<span class="text-muted">Next:</span>
 [Code Style](DevelopingCodeStyle.md)<br/>
<span class="text-muted">Previous:</span>
 [Writing for Someone Else](OtherCentricDesign.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/ProgrammingTips/FutureCentricDesign.md)