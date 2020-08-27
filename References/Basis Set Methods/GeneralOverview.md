---
---
# Mathematical Overview to Basis Set Methods

With all classic basis set methods, we choose a basis so that our representation is
1. Easy to evaluate
2. Compact (i.e. we don't have to use tons of basis functions)

Often, this corresponds to one where we have a "simple" representation of our system, which is to say when we look at

$$
H_{i, j}=\langle i|\hat{H}|j\rangle
$$

there aren't many values of $i$ and $j$ for which $H_{i, j}$ is non-zero. Equivalently, for _most_ values of $i$ and $j$, $H_{i, j} = 0$.

We also need to choose our basis so that the range of configuration space that's relevant for our problem is also well-described by our basis.
This usually isn't much of a problem, as long as we choose one that covers the same range as our coordinates of interest.

### Ease of Representation in the Hamiltonian

One of our big design principles in picking a basis is that we want one where our matrix elements are easy to evaluate.
What this means is just that we can get analytic forms for any of our matrix elements.

When we look at

$$
\hat{H} = \hat{T} + \hat{V}
$$

we'll look first at the kinetic energy term.
If you're working in Cartesian coordinates, we know

$$
T \propto \frac{d^2}{d x^2}
$$

and so if we can get a representation for $\frac{d^2}{d x^2}$ we can get one for $\hat{T}$ essentially for free.

As we're just discussing the general approach, it's impossible to say whether or not this representation will be easy to evaluate, but we can make use of a nice property of matrix representations when doing so.
First off, we know (assuming sufficient basis completeness) that we can say

$$
\hat{\frac{d}{d x}}|j\rangle = \sum_n c^{(j)}_n |n\rangle
$$

and then we can write

$$
\frac{d^2}{d x^2} = \frac{d}{d x}\frac{d}{d x}
$$

therefore we know that

$$
\frac{d^2}{d x^2}|j\rangle = \frac{d}{d x}\frac{d}{d x}|j\rangle = \frac{d}{d x}\sum_n c^(j)_n |n\rangle
$$

we also know that derivatives are _linear_ operators, therefore we have

$$
\frac{d}{d x}\sum_n c^{(j)}_n |n\rangle = \sum_n c^{(j)}_n \frac{d}{d x} |n\rangle = \sum_n c^{(j)}_n \sum_m c^{(n)}_m |m\rangle
$$

This might not look like a win at the moment, but let's we assume we have a matrix representation of $\frac{d}{d x}$ that I'll call $D$.
I.e. we have

$$
D_{i,j} = \langle i|\frac{d}{d x}|j\rangle
$$

then (feel free to work this through) the previous nested sum is showing that

$$
\langle i|\frac{d^2}{d x^2}|j\rangle = (D D)_{i,j}
$$

which is to say, the second-derivative matrix representation is the same as applying the first-derivative matrix representation to itself.

This means that if the _first_ derivative operator is easy to evaluate, up to the approximateness of our assumption of a complete basis, our second derivative operator is easy to evaluate.

And in fact, there's nothing special about this that restricts us to derivatives.
In general, given some linear operator $\hat{x}$ with matrix representation $X$, we have

$$
\langle i|\hat{x}^n|j\rangle = (\underbrace{X X ... X}_{n \text{times}})_{i,j}
$$

This will be a very powerful tool to let us decrease the amount of work we need to do when making these matrix representations.

### Compactness

When we talk about compactness of a representation, the primary metric we care about is whether or not it's _diagonally dominant_, which just means that given some Hamiltonian representation $H$

$$
\forall_{i} \left|H_ii\right|^2 >= \sum_{j \neq i} \left|H_ij\right|^2
$$

Thinking about what this means in the context of

$$
H_{i,j} = \langle i| \hat{H} |j \rangle = \int_{\pmb{r}\in \mathbb{D}} \phi_i \hat{H} \phi_j d\pmb{r}
$$

the coupling _between_ basis functions is pretty weak.

Of course, _coupling_ is a vague term with no real formal definition beyond $H_{i,j}$ being large, but it commonly appears in the literature so it's worth keeping this definition in mind.

### The Problem with Potentials

This discussion is somewhat different when we start talking about things like _discrete variable representation_, but for the classic basis set approaches, the difficulty in representation generally shows up in the potential.
Most of the bases we like to work with are based on _orthogonal polynomials_,[<sup>1</sup>] which almost always have clean representations for the second derivative operator.
Unfortunately, we have no assurances as to the form of the potential, and so we can't say for sure whether we'll get a simple representation for it.
As we show concrete examples of useful bases, we'll discuss approaches for dealing with this problem. For now, though, simply keep the mantra in mind, _the potential is the problem_.

## Wavefunctions and Energies

Assuming we can get a good matrix representation, the thing we usually want to do is get wavefunction and energies.
This turns out to be straightforward.
First we note that

$$
H \psi_n = E_n \psi_n
$$

is an eigenvalue problem.
Then we recall that we can solve any eigenvalue problem by diagonalization of the relevant matrix representation.
I.e., we get our energies and wavefunctions by diagonlizing the $H_{i,j}$ matrix.

The energies we obtain are straightforward to interpret.

The wavefunctions require a small amount of care.
Since we represented $H_{i,j}$ in a given basis, our wavefunctions will be given by

$$
|\psi_n\rangle = \sum_i C^{n}_{i} |i\rangle
$$

where the $C^{n}_{i}$ coefficients come from the diagonalization.

Usually, we don't try to create an analytic representation of our $\psi_n$ terms, though, and instead mostly work by doing things like representing physical quantities of interest like dipole moments or bond lengths in the same basis.

### Evaluation of Properties

Now that we have our wavefunctions, we can move onto getting physical information from them. The usual way we do this is by defining some property or _observable_, $\hat{O}$, that we care about (usually stuff like dipole moments and structural info like bond distances) and then getting _expectation values_ for a single state or _matrix elements_ between states, where both are given by

$$
\langle O \rangle_{n,m} = \left\langle \psi_n \lvert \hat{O} \rvert \psi_m \right\rangle
$$

and the only difference is that for an expectation value $n=m$. 

It's worth taking a second to talk briefly about _why_ this is a meaningful quantity. 
We can imagine that our $\hat{O}$ is something physically meaningful, like the dipole operator. 
And then "applying" the dipole operator to $ \rvert \psi_m \rangle $ is basically asking the question "how does an interaction with the molecular dipole change our system?"
Finally, the application of $ \langle \psi_n \lvert $ allows us to probe that change by asking "how much does the changed system resemble $\psi_n$?"
For Hermitian operators (i.e. observables), whether we apply $\hat{O}$ to $\rvert \psi_m \rangle$ and then apply $\langle \psi_n \lvert$ or apply $\hat{O}$ to $\rvert \psi_n \rangle$ and then apply $\langle \psi_m \lvert$ we'll get the same value out.

From the algorithmic point of view, to first figure out how the system changes, we expand our $\psi_m$, giving us

$$
\langle O \rangle_{n,m} = \sum_{j} C^{m}_{j} \hat{O} \rvert \phi_j \rangle
$$

then we expand $\psi_n$ giving us

$$
\langle O \rangle_{n,m} = \sum_{i,j} C^{m}_{i}C^{m}_{j} \left\langle \phi_i \lvert \hat{O} \rvert \phi_j \right\rangle
$$

Looking at this, we see we have a component that's just the matrix representation of \hat{O} in the original basis

$$
\textbf{O}_{i,j} = \left\langle \phi_i \lvert \hat{O} \rvert \phi_j \right\rangle
$$

and then project onto the wave function basis by 

$$
\langle O \rangle_{n,m} = C^{m}\textbf{O}C^{n}
$$

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="#fn1">&nbsp;</a> The mathematical literature on these polynomials (which are closely related to the _special functions_) is pretty dense, but interesting. Unfortunately I've never found a good intro for people without an undergrad math background :| If you've got questions about them, ask on the the SO and I'd be delighted to answer.

[<sup>1</sup>]:#fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/GeneralOverview.md)
