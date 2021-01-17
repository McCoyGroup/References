---
---
# Multidimensional Bases

When dealing with real-world chemical problems, one usually has to deal with systems that are larger than
one-dimensional. 
So when getting wave functions for such a system, one generally needs to go to some multi-dimensional basis.
In general, this just means, as for any basis, that we have an indexed set of functions, but instead of each
function taking one argument, now it takes multiple arguments, e.g. our basis is something like

$$
\Phi^{(\mathrm{ND})} = \{\phi_n(x_1, x_2, ..., x_N)\}
$$

Everything else we've discussed applies as usual. Representations are still built by "sandwiching" operators
between two basis functions, integrals are the same as usual (but multidimensional as so 
correspondingly more difficult).

Often, though, we don't have a clean set of high dimensional functions with which we can nicely work.
Instead, we commonly work with a _direct product basis_, where one has a starts with a set of $M$ low-dimensional bases

$$
\Phi^{(\mathrm{ND})} = \{\Phi^{(\mathrm{N}_i\mathrm{D})}_i\ : i \in \{1, 2, ..., M\} \}
$$

where

$$
\sum_{i} N_i = N
$$

and basis functions are constructed by taking a product of terms in each of these bases

$$
\phi_{n_1, n_2, ..., n_M}(x_1, x_2, ..., x_N) = \prod_{i} \phi^{(N_i)}_{n_i}
$$

## Normal Modes

To give an examples of this, the zero-order picture we commonly use when studying vibrations is to look at the
normal modes of a system, which comprise a set of vibrations that satisfy the [harmonic oscillator approximation](HarmonicOscillator.md)
when the system is at a stationary point, e.g. its minimum energy structure.
We won't get into how one calculates normal modes here, since that'd just be a distraction, instead we'll note
that the normal modes provide a coordinate system $\{q_i\}$ where we can describe the total vibrational wave function
of the system as a product of 1D harmonic wave functions
$$
\Psi_{n_1, n_2, ..., n_N}(q_1, q_2, ..., q_N) = \prod_{i} \psi_{n_i}(q_i)
$$
This picture also lends itself well to how we often like to talk about vibrations, for instance, in water we might
talk about about a peak in its vibrational spectrum coming from one quantum of excitation in the antisymmetric OH
stretch mode coupled with one quantum of excitation in the HOH bend.
Both of these are allowed normal modes of the system, and so really we're describing the wave function
$$
\Psi_{0, 1, 1}(q_\mathrm{symm}, q_\mathrm{asymm}, q_\mathrm{HOH}) = \psi_{0}(q_\mathrm{symm}) \psi_{1}(q_\mathrm{asymm}) \psi_{1}(q_\mathrm{HOH})
$$

This set of wave functions can then be used as a product basis in methods that go beyond the harmonic approximation.

## The Hydrogen Atom

We don't work with electronic wave functions, so this is purely for example, but we'll recall that the hydrogen atom wave function
can be written as a product of a radial wave function and an angular wave function

$$
\Psi_{n, l, m_l}(r, \theta, \phi) = R_n(r) Y_{l}^{m_l}(\theta, \phi)
$$

Hypothetically, for some electronic problem, one could use these wave functions as a zero-order basis in a perturbation theory treatment.
They are a clean multidimensional product basis, built from 1D and 2D bases themselves.

## Products of Multidimensional Bases

Nothing requires the bases we take a product of to be one dimensional. We've used products of multidimensional bases
in multiple places, e.g. in one of [our treatments of $\mathrm{H}_{5}^{+}$](https://pubs.acs.org/doi/10.1021/acs.jpca.0c02299).
More specific details can be written down if there's interest.

## The Curse of Dimensionality

One of the biggest issues with multidimensional basis set methods is how they scale.
In one dimension, we can use, say, $1000$ basis functions to really nail down the energies and wave functions.
In two dimensions, assuming we take a product of 1D bases, if we wanted the same resolution, 
we'd need $1000$ basis functions in each dimension, giving us $1000^2$ functions.
More generally, in $N$ dimensions, we'd need $1000^N$ basis functions.
From a computational perspective, for the high-ish dimensional problems we work with, this means going beyond
say 4 dimensional with a naive direct product basis requires either an exorbitant amount of computational resources 
or a degradation in the quality of the results obtained.
For reference, getting vibrational wave functions for the water dimer, a system with 6 atoms, is already a 12 
dimensional problem.

To get around this, optimally we use our knowledge and insights from experiment and spectroscopy to reduce
the problem to a low dimensional problem or set of low dimensional problems.
Alternately we can use [pertubative approaches](PerturbationTheory.md) to build off of a good zero-order picture or
we can use [Monte Carlo methods](../Monte%20Carlo%20Methods) to obtain full-dimensional results (although with a 
few caveats).


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/MultidimBasis.md)