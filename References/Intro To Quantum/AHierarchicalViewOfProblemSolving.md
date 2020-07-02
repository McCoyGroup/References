# A Hierarchical View of Problem Solving

What's nice about the kinds of problems we solve as quantum chemists is that they're _straightforward_. 
We don't deal with massively complex systems. 
We don't deal with lots of subsytems that are talking to each other. 
And probably most importantly, we don't have to deal with humans. 
The straightforwardness of our problems means we can also take a pretty straightforward approach to solving them, where we basically create a conceptual hierarchy and solve each bit independently.
This kind of approach also often works other places, but I'd be wary of treating it this reductionist view an always-viable approach.

## Breaking Down a Problem

So what's the main idea behind this approach? Basically, it's asking yourself _what do I want to know_ and separating that from _what do I need to do to find that out_.

Here are some examples of the first bit.
> I want to know...
* what's physically going on in an experimental spectrum
* what distribution of bond lengths I can expect in a cluster of molecules
* where the energy of an absorbed photon goes in my system

And here are some example so the second (based on the first).
> To figure this out, I need to...
* figure out what transition energies are possible in my system and how likely transitions are
* determine the most probable structures of my cluster and calculate bond lengths from them
* find out what parts of my system will best absorb photons and what kinds of internal conversions are possible after that

Then we can focus our energy in on each bit of the stuff we "need to do" and break this down into its components, e.g. we can now say "I want to figure out transition energies are possible in my system" and then we can break this down into steps, like

> I want to _transition energies are possible in my system_, so I need to _figure out what kinds of transitions are possible in my system_.

then we'd do it for this step

> I want to _figure out what kinds of transitions are possible in my system_, so I need to _figure out what the allowed states of my system are_.

and again

> I want to _figure out what the allowed states of my system are_, so I need to _calculate the possible wavefunctions for my system_

and once we've reached the step where we're _calculating_, now we get to make decisions about how to do the calculation.
Even though actually doing the calculation might be the hardest step in the process pain, we want to keep the focus on the stuff we actually _want to know_.
Calculation techniques are useful and important to know, but they're not why we're doing the science.

You might notice that our original statement of what we needed to do had two branches, i.e. we said

> I want to know _what's physically going on in my experimental spectrum_, so I need to figure out _what transition energies are possible in my system_ and _how likely are the possible transitions in my system_.

and so for each of those branches we'll want to build out our hierarchy of what we need to do, something like

> I want to know what's physically going on in my experimental spectrum

* So I need to figure what transition energies are possible in my system
  * So I need to figure out what kinds of transitions are possible in my system
    * So I need to figure out what the allowed states of my system are
      * So I need to _calculate_ the possible wavefunctions for my system
    * Once I have states, a transition is just going from a lower-energy state to a higher-energy one
  * Once I have transitions, I need to figure out what their energies are
    * So I need to figure out the difference in energy between the lower- and higher-energy state in the transition
      * So I need to _calculate_ to energies of the states
* And I need how likely the possible transitions in my system are
  * So I need to figure out what kinds of transitions are possible in my system
    * So I need to figure out what the allowed states of my system are
      * So I need to _calculate_ the possible wavefunctions for my system
    * Once I have states, a transition is just going from a lower-energy state to a higher-energy one
  * Once I have transitions, I need to figure out how likely they are
    * So I need to figure out how likely a photon is cause the system to go from the lower- to higher-energy state
      * So I need to _calculate_ a transition moment (we won't get into _why_ for this step, yet)
 
### Hiding Complexity

We can see in this that we actually have a pretty large shared chunk between the branches:

* So I need to figure out what kinds of transitions are possible in my system
  * So I need to figure out what the allowed states of my system are
    * So I need to _calculate_ the possible wavefunctions for my system
  * Once I have states, a transition is just going from a lower-energy state to a higher-energy one

and it's super common that we end up in a situation like this, so it can be useful to give this chunk a name (say like `Get Transitions`), so now our overall flow might be

* So I need to figure what transition energies are possible in my system
  * Get Transitions
  * Once I have transitions, I need to figure out what their energies are
    * So I need to figure out the difference in energy between the lower- and higher-energy state in the transition
      * So I need to _calculate_ to energies of the states
* And I need how likely the possible transitions in my system are
  * Get Transitions
  * Once I have transitions, I need to figure out how likely they are
    * So I need to figure out how likely a photon is cause the system to go from the lower- to higher-energy state
      * So I need to _calculate_ a transition moment (we won't get into _why_ for this step, yet)

and by hiding that complexity under a shared name, we've managed to make our problem look way more manageable! All glibness, aside, hiding complexity like this is going to be the key to what makes our problems so nice to work with. 
It's hard to keep tons of things in mind at once, and so by replacing some of them with big black boxes where we just need to know what goes in and what comes out, we can tackle much harder problems with less mental strain.

## Problem Solving as Travel Directions

As an analogy, I like to think about solving this type of problem as being akin to traveling a long distance. 
Say we want to go from Seattle to Ürümqi. This is the overarching thing we want to do. 
So what do we need to do? Well we could design tons of routes, but they'll probably all look like this

1. Get to Xinjiang
2. Get to Ürümqi[<sup>1</sup>]

and the first step is kinda big, so maybe we want to break it down like

* To get to Xinjiang
  * First, get to Eastern China
  * Then, get to Xinjiang

and at this stage we might say "Great! There are tons of flights to Beijing or Shanghai, so much of that complexity is hidden!". 
We don't need to know the details of how the flight will get us to China; we just need to know that it _can_ get us to China. And we can _plausibly assume_ that once we get to Xinjiang, we can get to Ürümqi. Then we can fill in then details on that as we write out our plan. 

As a super manufactured hypothetical though, what if aviation fuel has become crazy expensive and there are no flights longer than ~6 hours?[<sup>2</sup>]
In that case, we'll need to put more thought into our route, maybe now we say

* To get to Xinjiang
  * First, get to far Eastern Russia
  * Then, get to Eastern China
  * Then, get to Xinjiang

or alternately, we could say that getting to far Eastern Russia is too complex or maybe getting to China from far Eastern Russia is hard, so maybe we want to change step 1 altogether and instead we say

* To get to Xinjiang
  * First, get to Western Europe
  * Then, get to Kazakhstan
  * Then, get to Xinjiang
  
and we can definitely do Step 1, because we know we can get across the _Atlantic_ in ~6 hours. Step 2 we can _plausibly assume_ is easy, given that we know rail travel in Europe is good, and so even though this seems like a longer path than going through Eastern Russia, it's quite possible it's _conceptually_ simpler.

Why am I talking about travel directions? Well the parallels are actually pretty direct with what we were doing before. We have something we _want to do_ (get from Seattle to Ürümqi) and to do that we need to do two big things (get to Xinjiang then get to Ürümqi). 
Then to do each of those things, we need to do some smaller things. They might be simple (get to Eastern China) or more difficult (get to Eastern Russian and then to Eastern China), but in either case, we're able to hide the actual complexity of the task and focus just on the higher level structure.

With our problem of interest before, we're able to do the same thing. There's one main goal

> I want to know what's physically going on in my experimental spectrum

to do that we need to do two things

1. Get transition energies
2. Get transition probabilities

and then we fill in the details of each of those steps as we need to.

When doing this, it's easy to focus on the details, which in our analogy would be like the airline you fly on, or the number of stop, or the best/cheapest times to fly, not to mention the specifics of how a plane acutally works, and those details _are_ relevant, but they're not what's important. 
Undoubtedly as you do quantum chemistry you'll need to wrangle with details, but don't let that cause you to lose sight of the bigger picture.

Finally, there will be times where something that's more conceptually difficult _feels_ easier than something that's conceptually easier, e.g. writing a piece of code from scratch vs. taking some code written by someone else that does _most_ of what you want but you'd need to adapt it to get it the last mile.
When that happens, you need to make a realistic assessment of whether or not it really _is_ easier. 
It's very easy to underestimate the number of details you need to handle to do it from scratch and it's _also_ very easy to overestimate the complexity of the problem.
I have no hard-and-fast guidance on this, and unfortunately the only way to really learn this balance is to get it wrong a bunch of times.

## Problem Solving via Code 

This approach to problem solving, alongside being (hopefully) rather intuitive and decreasing the amount of stuff we need to remember, has the added benefit of translating really nicely into _code_. 
I'm not going to do any high-level coding, so there's no need to immediately run out and start to read up on how code works, but that _will_ be super relevant moving forward so if you haven't seen any code before, it'll be useful to at least read a primer or two on the basics.

All I'm going to care about right now, though, are _functions_. What is a function? Well it's just a chunk of code with two nice properties

1. It takes some inputs and returns an output
2. It has a name

In other words, we to start we can treat it like a black box with a label on it.

And if those two properties are tickling your memory, it might be because we saw something like this earlier. 
When we were talking about hiding complexity, we had the example of this bit of logic

* So I need to figure out what kinds of transitions are possible in my system
  * So I need to figure out what the allowed states of my system are
    * So I need to _calculate_ the possible wavefunctions for my system
  * Once I have states, a transition is just going from a lower-energy state to a higher-energy one
  
and we just replaced it with one step called `Get Transitions`.

That's all a "function" is. It's a way to take a bit of logic and give it a name.

And by chaining functions together, we can represent the overall structure of our problem. Before I jump into an example of this, let's get some notation in place. 
I'm going to represent functions the way the Python programming language does, so each one will look like this

```python
def function_name(function, args, are, separated, by, commas):
  """This is the description of what my function does"""
  ... # the ellipsis is a placeholder for when I actually fill in the details of how my function works
  return what_my_function_returns 
```

So our `Get Transitions` logic can be written like

```python
def get_transitions(system):
  """Gets the possible transitions available to the system"""
  states = get_states(system)
  pairs = get_pairs_of_states(states)
  return pairs
```

which broken down says that our `get_transitions` function takes some representation of our `system`[<sup>3</sup>] as input, it gives that to the function that gets the states of our system, then it takes those to get pairs of lower- and higher-energy states.

The subfunctions, `get_states` and `get_pairs_of_states` will have their own subfunctions and details to work with.

Then this `get_transitions` function can be worked into the overall logic of our problem. Let's recall what that looked like
 
* So I need to figure what transition energies are possible in my system
  * Get Transitions
  * Once I have transitions, I need to figure out what their energies are
    * So I need to figure out the difference in energy between the lower- and higher-energy state in the transition
      * So I need to _calculate_ to energies of the states
* And I need how likely the possible transitions in my system are
  * Get Transitions
  * Once I have transitions, I need to figure out how likely they are
    * So I need to figure out how likely a photon is cause the system to go from the lower- to higher-energy state
      * So I need to _calculate_ a transition moment (we won't get into _why_ for this step, yet)
      
and so we can turn this into functions like

```python
def get_spectrum(system):
  """Gets the energies and transition probabilities for the system"""
  transitions = get_transitions(system)
  energies = get_energies(system, transitions)
  probabilities = get_probabilities(system, transitions)
  return [energies, probabilities]

def get_energies(system, transitions):
  """Gets the energy difference between the states in the transitions for each transition"""
  energies = [ get_states_energy_difference(system, transition) for transition in transitions ]
  return energies

def get_probabilities(system, transitions):
  """Gets the transition moment for each transition"""
  probabilities = [ get_transition_moment(system, transition) for transition in transitions ]
  return probabilities
```

most python code you see _won't_ look like this, simply for reasons of convenience, as writing out hundreds of little functions can be tedious.
On the other hand, all programs _have this structure_, even if the person writing it didn't realize it. 
By hiding complexity beneath lots of little functions, though, you make your logic clearer, make it less taxing to write, and make it easier to reuse.

<span class="text-muted">Previous:</span>
 [Reading A Function](ReadingAFunction.md)<br/>
<span class="text-muted">Previous:</span>
 [Practical Quantum Mechanics](PracticalQuantumMechanics.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="fn1"></a> The capitol of the Xinjiang Uyghur Autonomous Region in the Western edge of China
2. <a id="fn2"></a> For our kind of problems, maybe the standard approaches are just simply too _computationally_ expensive
3. <a id="fn2"></a> What _specifically_ this looks like will vary system-to-system and person-to-person; it's mostly a matter of personal preference. 

[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2
[<sup>3</sup>]: #fn3


[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Intro%20To%20Quantum/AHierarchicalViewOfProblemSolving.md)