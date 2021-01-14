# Discrete Variable Representation Spectra

As [we have noted](../Basis%20Set%20Methods/BasicDVR.md), discrete variable representation, or DVR, is just a very special, very convenient case of a standard basis set approach.

When it comes to obtaining frequencies and intensities, this means the same principles as for a [basis set approach](BasisSetSpectra.md) apply. In particular, the biggest hurdle to obtaining intensities is the evaluation of the transition dipole moment. 
On the other hand, recalling our prior discussion on [evaluating properties with a DVR](../Basis%20Set%20Methods/BasicDVR.md#evaluation-of-properties), for a multiplicative operator like the dipole moment, this is actually also pretty simple!

We'll start by assuming that we have the dipole moment as a function of our coordinates, $\mu(r)$. This could be from a Taylor series approximation (e.g. a linear dipole) or we can evaluate it using an interpolation or something in that vein.

With that, we'll then assume that we've run a DVR calculation, which means we have a set of DVR points, ${r_i}$, and a set of wavefunction values at those grid points ${\psi_n(r_i)}$, then to get the transition moment we simply do

$$
\left\langle \psi_n \lvert \mu \rvert \psi_m \right\rangle = \sum_i \mu(r_i) \psi_n(r_i)\psi_m(r_i)
$$

_Note: one very important thing to keep in mind with this is that you must evaluate $\mu(r_i)$ at your DVR points, you can't do the reverse and evaluate your DVR wavefunctions at the points where you already have the dipole moment. If you were to evaluate the DVR wavefunction at different gridpoints, it will cause your DVR wavefunctions to no longer be normalized._

As we noted in the general basis set spectrum section, the dipole moment actually has an _x_, _y_, and _z_ component to it and we've got to take that into account when we calculate intensities.

## From Transition Moment to Intensity

Once you feel good about the Transition Moment, you are two steps away from having an Intensity! 
First, recall the intensity formula

$$ I_{n,m} \propto \nu_{n,m} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2} $$

we have half of this, but to get a proper intensity we need to multiply by $\nu_{n,m}$ and of course, make sure you are tracking your units. (Wavenumbers is probably a good place to start.) If you choose to stick with this, you will probably want to convert it to a _relative intensity_ where your transistion are normalized so that either the sum is 1 or one of the fundamental transitions is 1. 

Second, if don't want a _relative intensity_, you can implement one of the unit conversions described [here](https://mccoygroup.github.io/References/References/Spectrum%20Generation/StickSpectra.html#a-note-on-units). 

### Applications and Exercises

We've provided an exercise to give you practice with this on the [McCode Academy Exercises](../../McCoy%20Group%20Code%20Academy/Exercises) page. Check it out, play around with it, and develop some intuition.

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Spectrum%20Generation/DVRSpectra.md)
