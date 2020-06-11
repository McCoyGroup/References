# Practical Quantum Mechanics

There are thousands of primers on quantum mechanics out there, so like why am I writing my own?
Well, if you ask me, those thousands of primers focus on the stuff that doesn't matter (even if it can be fun).
What does matter? I'd say impact.

There's no reason to do a bunch of work and calculate a bunch of things just because it's hard (sorry JFK). Instead, we'll want to work on things that have some kind of impact.
Obviously, claiming anything has direct or indirect impact or that your results specifically matter for something is impossible in any scientific field. 
Science at its best is a bunch of drunks stumbling home from the bar, and occasionally one finds a polio vaccine and fundamentally changes the world.
But even so, we still need to _try_ to do stuff that matters, and one big thing that matters is understanding stuff like chemical reactivity.

How will our quantum mechanics come into this? Well reactions occur along the _allowed vibrations_ of a system[<sup>1</sup>].
And so to gain insight on the reactivity of our system, we can look at its vibrations. 
And to do that, because the world is unfortunately fundamentally quantum mechanical, we need to solve an equation that looks like

$$
H\psi(x) = E\psi(x)
$$

Technically, this is called the time-independent Schrödinger equation. I prefer to think of it more mechanistically. 
That $H$ term there is a function[<sup>2</sup>] that represents the energy in our system--a super vague term which could be a molecule, or maybe a bunch of interacting molecules, or maybe just a single atom, basically whatever we're interested in.
We can always write this like

$$
H = T + V
$$

where $T$ is the total _kinetic_ energy and $V$ is the total _potential_ energy. 

Next, the $\psi(x)$ represents our system's _wave function_, which is just the way the quantum mechanics represents our system.[<sup>3</sup>]

So what is this telling us?
Well in general we know how to write $T$ and $V$ (which is to say, someone else worked it out and we make use of this), so it's telling us that if we want to know about our system & like how reactive it is or whatever, we need to find a $\psi(x)$ that satisfies the equation.
That is, we need to find a $\psi(x)$ so that when we ask $\psi(x)$ what its total energy is, it 
* doesn't change and 
* just gives us a number ($E$) back

once we've found this $\psi(x)$ we now know what our system will look like and what its energy will be! 

And that's...pretty much all we need do? Once we have that we can use other functions _like_ $H$ to ask about properties like reactivity instead of energy.

There are lots of ways to find or approximate $\psi(x)$ and I don't have the time, energy, or expertise to enumerate them all.
Hopefully over the course of this brief intro, though, you'll become convinced that no matter what the method, with a bit of grit and a good dollop of time, you could find $\psi(x)$ too.


Next: [A Hierarchical View Of Problem Solving](AHierarchicalViewOfProblemSolving.md)
---

1. <a id="fn1"></a> It's a little bit tricky to explain _what_ an allowed vibration really is (and it's a little circular), but it's very, very closely related to the potential energy surface of a system (here's what Wikipedia has to say: https://en.wikipedia.org/wiki/Transition_state_theory#Potential_energy_surfaces).
2. <a id="fn2"></a> Technically it's an "operator" which is just something that takes a function and returns a function, rather than a something that takes a coordinate and returns a value.
3. <a id="fn3"></a> If you're interested, a wave function is really strongly closely related to a _probability distribution_. There's a good chance you've seen a "bell curve" or "normal distribution", maybe in relation to like test scores? A wave function is just like that, but rather than describing the probability that someone gets a given test score, it's related to the probability that our system "looks" a a certain way.

[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2
[<sup>3</sup>]: #fn3