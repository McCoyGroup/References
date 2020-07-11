---
---
# The Harmonic Oscillator Basis

With all basis set methods, we choose a basis to give a "simple" representation of our system.
What that means is that when we compute

$$
H_{i\, j}=\langle i|\hat{H}|j\rangle
$$

there aren't many values of $i$ and $j$ for which $H_{i\, j}$ is non-zero.

We also want to choose our basis so that the range of configuration space that's relevant for our problem is also well-described by our basis.
For the harmonic oscillator, this range is $[-\infty, \infty]$.

### Properties of the Basis

The harmonic oscillator basis, with respect to these, has the nice property that

$$
\langle i|x|j\rangle =
\begin{cases}
 c_{i+1} & j=i+1 \\
 c_{i} & j=i-1 \\
 0 & \text{else}
\end{cases}
$$

and

$$
\langle i|\frac{d}{d x}|j\rangle =
\begin{cases}
 k_{i+1} & j=i+n \\
 -k_{i} & j=i-n \\
 0 & \text{else}
\end{cases}
$$

where the $c_i$ and $k_i$ are simple coefficients that only depend on the value of $i$.

For completeness, these are

$$
c_i = \frac{a}{\sqrt{2}}\sqrt{i}
k_i = \frac{1}{a \sqrt{2}}\sqrt{i}
$$

where $a$ takes care of the units and is $1$ if we've put our coordinate in dimensionless units.

Now, obviously you should ask yourself why that matters.

First off, this means that when we build representations of the $x$ or $\frac{d}{d x}$ operators we'll get matrices where only the first super- and sub-diagonals are non-zero. I.e. the representations of these operators are "simple".

Secondly, let's recall that

$$
H = T + V
$$

and in Cartesian coordinates

$$
T \propto \frac{d^2}{d x^2}
$$

so up to a unit conversion, we have

$$
\langle i| T |j\rangle \propto \langle i|\frac{d^2}{d x^2}|j\rangle = \langle i|\frac{d}{d x}\frac{d}{d x}|j\rangle
$$

then we'll invoke a nice property of linear operators, which is that if we can get a matrix representation of the first derivative as

$$
D_{i,j} = \langle i|\frac{d}{d x}|j\rangle
$$

we can get the second derivative through a simple matrix multiplication as

$$
D^2_{i,j} = (D D)_{i, j}
$$

### Hamiltonian Forms

Taken together, this means our harmonic oscillator basis is good for problems where we have a Cartesian-like (i.e. non-curvilinear) coordinate and a potential that can be described by

$$
V(x)=\sum_{n=0} v_n x^n
$$

I haven't justified why this last property is true, but using the same matrix multiplication property we used when getting the second derivative, we have

$$
X^n_{i,j} = (X X ... X)_{i, j}
$$

and we already know how to get the representation of $X$.

Therefore, given a Hamiltonian like

$$
H = \frac{1}{2 m} \frac{d^2}{d x^2} + \sum_{n=0} v_n x^n
$$

we know how to get a matrix representation of it.

## Wavefunctions and Energies

With this matrix representation in hand, the thing we usually want to do is get wavefunction and energies, by noting that

$$
H \psi_n = E_n \psi_n
$$

and solving this eigenvalue problem by diagonalization of the $H_{i,j}$ matrix.

The energies we obtain are straightforward to interpret.

The wavefunctions require a small amount of care.
Since we represented $H_{i,j}$ in the harmonic oscillator basis, our wavefunctions will be given by

$$
\psi_n(x) = \sum_{i=1} C^{n}_{i} \phi_i(x)
$$

where the $C^{n}_{i}$ coefficients come from the diagonalization.

Usually, we don't try to create an analytic representation of our our $\psi_n$ terms, though, and instead mostly work by doing things like representing physical quantities of interest like dipole moments or bond lengths in the same basis.
Once we have that, we can do some matrix multiplications and get the quantities that we care about without much extra effort.


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/HarmonicOscillator.md)