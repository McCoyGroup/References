# Descendant Weighting and Wave Function Analysis

### What is Descendant Weighting
So, we've gone over how to run a basic DMC simulation but now what should we do with these walkers?
Well, you might be interested in obtaining projections of this system's probability amplitude onto coordinates
of interest. If that's the case we will be using a technique called descendant weighting in order to
obtain the probability amplitude. This technique has been described by
 [Suhm and Watts](https://doi.org/10.1016/0370-1573(91)90136-A) and boils down to keeping track of the descendants
of each walker over a certain time. To be more specific, say we have a snapshot of our walkers at time $\tau$, then we 
want to track the descendants of those walkers until some time $\tau$'. So, for example lets say we have the following
set of walkers.

![initial_walkers](Implementing%20DMC/img/Initial_walkers.PNG){:width="500px"}

These walkers will simulate our set of walkers at time $\tau$. Then we will track the descendants of these walkers over
a set amount of time. For example, the following figure shows how the walkers propogate over 5 time steps.

![descendants](Implementing%20DMC/img/descendants.PNG){:width="500px"}

We see that the orange walker dies after 2 time steps and the green walker gives birth. Then after four time steps the 
purple walker dies and a red one gives birth. For discrete weighting you would just count up the number of walkers that
each walker produced at the end. For example, the green walker would have a descendant weight of 2, while the purple walker
would have a descendant weight of 0. For continuous weighting, you would add up the weight of each walker's descendants.
For example, let's say that the two green walkers at the end had weights of 1.2 and 0.9, then the descendant weight of the
green walker would be 2.1.

### Using Descendant Weights

Now that we have these descendant weights, we can obtain a projection of the probability amplitude onto coordinates of interest
through a histogram using the coordinate associated with each walker and the descendant weights of those walker. For example,
if we were interested in a projection of the probability amplitude onto a specific bond length, we would calculate that bond
length for each walker and then create a histogram using those bond lengths and the descendant weights of the walkers.

If we wanted an expectation value of a specific operator then all we have to do is use the following equation:

$$
<A> = \frac{\sum_j d_j A}{\sum_j d_j}
$$

Where A is the operator of interest and d$_j$ is the descendant weight of the $j$th walker.

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Monte%20Carlo%20Methods/DMC.md)