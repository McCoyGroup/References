---
---
# General Overview to Basis Set Methods

With all classic basis set methods, we choose a basis to give a "simple" representation of our system.

$$
H_{i, j}=\langle i|\hat{H}|j\rangle
$$

there aren't many values of $i$ and $j$ for which $H_{i, j}$ is non-zero.

We also want to choose our basis so that the range of configuration space that's relevant for our problem is also well-described by our basis.
I.e. we choose one that covers the same range as our coordinates of interest.

### Representation "Simplicity"

For a complete basis, i.e. an indexed set of functions we'll call $\|n\rangle$, we know _a priori_ that given an operator $\hat{O}$ there's a set of coefficients $$ \{ c_n \} $$ such that

$$
\hat{O}|j\rangle = \sum_n c_n |n\rangle
$$

and for an orthonormal basis, then, we know

$$
\langle i|\hat{O}|j\rangle = \langle i|\sum_n c_n |n\rangle = \sum_n c_n  \langle i|n\rangle = c_i
$$

therefore the key to determining whether a representation of $\hat{O}$ is simple or not is determining how many of the $$ \{ c_n \} $$ are non-zero.
The more of these coefficient that are zero, the simpler the representation.

### Simplicity in the Hamiltonian

Returning to an actual physical system, we know we have

$$
H_{i, j}=\langle i|\hat{T} + \hat{V}|j\rangle = \langle i|\hat{T}|j\rangle + \langle i|\hat{V}|j\rangle
$$

So when we're looking at simplicity in this representation, we're really asking about the simplicity of the representations of $\hat{T}$ and $\hat{V}$.

The kinetic energy term is often somewhat easier to deal with, so we'll start there.
In general, we have

$$
T \propto \frac{d^2}{d x^2}
$$

and so if we can get a representation for $\frac{d^2}{d x^2}$ we can get one for $\hat{T}$ essentially for free.

As we're just discussing the general approach, it's impossible to say whether or not this representation will be simple, but we can make use of a nice property of matrix representations when computing it.
We know that we can say

$$
\hat{\frac{d}{d x}}|j\rangle = \sum_n c^{(j)}_n |n\rangle
$$

and we can write

$$
\frac{d^2}{d x^2} = \frac{d}{d x}\frac{d}{d x}
$$

therefore we can note that

$$
\frac{d^2}{d x^2}|j\rangle = \frac{d}{d x}\frac{d}{d x}|j\rangle = \frac{d}{d x}\sum_n c^(j)_n |n\rangle
$$

we also know that derivatives are _linear_ operators, therefore we have

$$
\frac{d}{d x}\sum_n c^{(j)}_n |n\rangle = \sum_n c^{(j)}_n \frac{d}{d x} |n\rangle = \sum_n c^{(j)}_n \sum_m c^{(n)}_m |m\rangle
$$

This might not look like a win at the moment, but if we assume we have a matrix representation of $\frac{d}{d x}$ that I'll call $D$, i.e. we have

$$
D_{i,j} = \langle i|\frac{d}{d x}|j\rangle
$$

then (feel free to work this through) the previous nested sum is showing that

$$
\langle i|\frac{d^2}{d x^2}|j\rangle = (D D)_{i,j}
$$

which is to say, the second-derivative matrix representation is the same as applying the first-derivative matrix representation to itself.

And in fact, there was nothing special about this that restricts us to derivatives. In general, given some linear operator $\hat{x}$ with matrix representation $X$, we have

$$
\langle i|\hat{x}^n|j\rangle = (\underbrace{X X ... X}_{n \text{times}})_{i,j}
$$

This will be a very powerful tool to let us decrease the amount of work we need to do when making these matrix representations.

### The Problem with Potentials

This discussion will be somewhat different when we start talking about things like _discrete variable representation_, but for the classic basis set approaches, the difficulty in representation generally shows up in the potential.
Most of the bases we like to work with are based on _orthogonal polynomials_,[<sup>1</sup>] which almost always have simple representations for the second derivative operator.
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
Once we have that, we can do some matrix multiplications and get the quantities that we care about without much extra effort.
That discussion, however, is for another day.

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
<a id="#fn1">&nbsp;</a> The mathematical literature on these polynomials (which are closely related to the _special functions_) is pretty dense, but interesting. Unfortunately I've never found a good intro for people without an undergrad math background :| If you've got questions about them, ask on the the SO and I'd be delighted to answer.

[<sup>1</sup>]:#fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/GeneralOverview.md)