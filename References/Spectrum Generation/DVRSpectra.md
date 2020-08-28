# Discrete Variable Representation Spectra

As [we have noted](../Basis%20Set%20Methods/BasicDVR.md), discrete variable representation, or DVR, is just a very special, very convenient case of a standard basis set approach.

When it comes to obtaining frequencies and intensities, this means the same principles as for a [basis set approach](BasisSetSpectra.md) apply. In particular, the biggest hurdle to obtaining intensities is the evaluation of the transition dipole moment. 
On the other hand, recalling our prior discussion on [evaluating properties with a DVR](../Basis%20Set%20Methods/BasicDVR.md#evaluation-of-properties), for a multiplicative operator like the dipole moment, this is actually also pretty simple!

We'll start by assuming that we have the dipole moment as a function of our coordinates, $\mu(r)$. This could be from a Taylor series approximation (e.g. a linear dipole) or we can evaluate it using an interpolation or something in that vein.

With that, we'll then assume that we've run a DVR calculation, which means we have a set of DVR points, ${r_i}$, and a set of wavefunction values at those grid points ${\psi_n(r_i)}$, then to get the transition moment we simply do

$$
\left\langle \psi_n \lvert \mu \rvert \psi_m \right\rangle = \sum_i \mu(r_i) \psi_n(r_i)\psi_m(r_i)
$$

_Note: one very important thing to keep in mind with this is that you must evaluate $\mu(r_i)$ at your DVR points, you can't do the reverse and evaluate your DVR wavefunctions at the points where you already have the dipole moment_

As we noted in the general basis set spectrum section, the dipole moment actually has an _x_, _y_, and _z_ component to it and we've got to take that into account when we calculate intensities.

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Spectrum%20Generation/DVRSpectra.md)