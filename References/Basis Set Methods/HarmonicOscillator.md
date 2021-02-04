---
---
# The Harmonic Oscillator Basis

The harmonic oscillator (HO) basis is, in some sense,
_the_ fundamental basis for studying vibrations.
It gives the solution to the Schrödinger equation for the Hamiltonian

$$
H = -\frac{1}{2 m} \frac{d^2}{d x^2} + m \omega^2 x^2
$$

where $m$ is the mass of the system and $\omega$ is the frequency of the vibration. For this, $x$ should range from $[-\infty, \infty]$.
Unsurprisingly, for a vibration that's perfectly harmonic, the HO basis gives the simplest possible representation.

For _nearly harmonic_ vibrations, the HO basis is often still good.

### Properties of the Basis

The HO wavefunctions are

$$
\phi_n(x) = N_n H_n(x) e^{-(x^2/2)}
$$

where $N_n$ is a normalization factor and $H_n$ is the $n^{th}$ _Hermite polynomial_.

This basis has two important operators for which it gives simple representations.

We have the coordinate operator

$$
\langle i|\hat{x}|j\rangle =
\begin{cases}
 c_{i+1} & j=i+1 \\
 c_{i} & j=i-1 \\
 0 & \text{else}
\end{cases}
$$

and the derivative operator

$$
\langle i|\frac{d}{d x}|j\rangle =
\begin{cases}
 k_{i+1} & j=i+1 \\
 -k_{i} & j=i-1 \\
 0 & \text{else}
\end{cases}
$$

where the $c_i$ and $k_i$ are simple coefficients that only depend on the value of $i$.

It's worth noting that these representations are _simple_, because for most values of $i$ and $j$, these matrix elements will be zero.
Specifically, only when $i = j \pm 1$ will this be non-zero, which means our matrix representation will have zeroes everywhere _except_ for the first upper and lower sub-diagonals.

For completeness, the coefficients are

$$
\begin{align}
c_i = \frac{a}{\sqrt{2}}\sqrt{i} \\
k_i = \frac{1}{a \sqrt{2}}\sqrt{i}
\end{align}
$$

where $a$ takes care of the units and is $1$ if we've put our coordinate in dimensionless units.

### Hamiltonian Forms

Taken together, this means our harmonic oscillator basis is good for problems where we have a Cartesian-like (i.e. non-curvilinear) coordinate and a potential that can be described by

$$
V(x)=\sum_{n=0} v_n x^n
$$

I haven't justified why this last property is true, recalling from the [General Overview](GeneralOverview.md) that

$$
X^n_{i,j} = (X X ... X)_{i, j}
$$

and we already know how to get the representation of $\hat{x}$.

Therefore, given a Hamiltonian like

$$
H = \frac{1}{2 m} \frac{d^2}{d x^2} + \sum_{n=0} v_n x^n
$$

we know how to get its matrix representation.

## Sample Applications

On our [McCode Academy Exercises Page](../../McCoy%20Group%20Code%20Academy/Exercises), you will find an exercise to help you implement this Basis Set representation.
Check it out


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/HarmonicOscillator.md)
