---
---
# The Harmonic Oscillator Basis

The harmonic oscillator (HO) basis is, in some sense,
_the_ fundamental basis for studying vibrations.
Unsurprisingly, for a vibration that's perfectly harmonic, the HO basis gives the simplest possible representation.

For _nearly harmonic_ vibrations, the HO basis is often still good.

### Properties of the Basis

The appropriate coordinate range is $[-\infty, \infty]$.

The HO basis has two important operators for which it gives simple representations.

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
 k_{i+1} & j=i+n \\
 -k_{i} & j=i-n \\
 0 & \text{else}
\end{cases}
$$

where the $c_i$ and $k_i$ are simple coefficients that only depend on the value of $i$.

For completeness, these are

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

...


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/HarmonicOscillator.md)