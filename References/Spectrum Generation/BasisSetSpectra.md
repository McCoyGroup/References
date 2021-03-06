# Basis Set Spectra

We'll assume we've already done a basis-set calculation to get a set of energies $\{E_n\}$ and wavefunctions $\{\psi_n\}$.

The key relationship we want to model is 

$$
I_{n,m} \propto \nu_{n,m} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2}
$$

From what we already have, $\nu_{n,m} = E_m - E_n$ is easy to calculate, so we'll give most of our attention to to the transition moment.

Recalling our discussion on [evaluating properties with a basis set approach](../Basis%20Set%20Methods/GeneralOverview.html#evaluation-of-properties), we know that to do this we first need to build a representation for the dipole moment in our original basis, ${\phi_i}$.
This is the hard part, and we'll look at the special case of a harmonic oscillator basis in a bit.

Assuming, however, that we have the representation

$$
\textbf{M}_{i,j} = \left\langle \phi_i \lvert \mu \rvert \phi_j \right\rangle
$$

we then know that we can get

$$
\left\langle \psi_n | \mu | \psi_m \right\rangle = C^{n} \textbf{M} C^{m}
$$

## The Dipole Moment Vector

There's one subtlety to this, which we've been sweeping under the rug until now, which is that the dipole moment is a three-dimensional vector.
I.e. for every set of molecular coordinates $\textbf{r}$ we have a component of the dipole moment that points along the _x_-axis, one that points along the _y_-axis, and one that points along the _z_-axis.[<sup>1</sup>]

That means when we evaluate 

$$
\textbf{M}_{i,j} = \left\langle \phi_i \lvert \mu \rvert \phi_j \right\rangle
$$

we really need to calculate, e.g.

$$
\begin{align}
\textbf{M}^{x}_{i,j} &= \left\langle \phi_i \lvert \mu^{x} \rvert \phi_j \right\rangle \\
\textbf{M}^{y}_{i,j} &= \left\langle \phi_i \lvert \mu^{y} \rvert \phi_j \right\rangle \\
\textbf{M}^{z}_{i,j} &= \left\langle \phi_i \lvert \mu^{z} \rvert \phi_j \right\rangle
\end{align}
$$

and then our squared-transition moment is actually the norm of the transition moment squared, i.e.

$$
{\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2} =
  {\left\lvert \left\langle \psi_n | \mu^{x} | \psi_m \right\rangle \right\rvert}^{2} +
  {\left\lvert \left\langle \psi_n | \mu^{y} | \psi_m \right\rangle \right\rvert}^{2} +
  {\left\lvert \left\langle \psi_n | \mu^{z} | \psi_m \right\rangle \right\rvert}^{2}
$$

## The 1D Harmonic Oscillator

To help build intuition, we'll return to the simplest basis for studying vibrations, the 1D harmonic oscillator eigenfunctions.
We won't go over their properties again, since [we've already done that](../Basis%20Set%20Methods/HarmonicOscillator.html). 
Instead we'll just remember one thing. For the coordinate operator, $\hat{r}$, we have

$$
\langle i \lvert \hat{r} \rvert j \rangle =
    \begin{cases}
     \sqrt{\frac{i+1}{2}} & j=i+1 \\
     \sqrt{\frac{i}{2}} & j=i-1 \\
     0 & \text{else}
    \end{cases}
$$

Why is this relevant? Well we can write out a Taylor expansion of our dipole function about our equilibrium structure like

$$
\mu(r) = \sum_k \frac{1}{k!} \frac{d^k \mu}{d r^k}(r_e) \Delta r^k 
$$

and in general it's not a bad approximation to truncate this at first order. We often call this the _linear dipole approximation_.

Again, you may be thinking, "okay...why do I care?", well we'll first say that $r_e = 0$, since the origin is arbitrary in the first place, and then our truncated expression becomes

$$
\mu(r)^{(1)} = \mu_0 + \mu_0^{\prime} r
$$

now when we build our representation of the dipole like

$$
\textbf{M}_{i,j} = \left\langle \phi_i \lvert \mu(r)^{(1)} \rvert \phi_j \right\rangle
$$

we get

$$
\langle i \lvert \mu(r)^{(1)} \rvert j \rangle =
    \begin{cases}
     \mu_0 & j=i \\
     \sqrt{\frac{i+1}{2}} \mu_0^{\prime} & j=i+1 \\
     \sqrt{\frac{i}{2}} \mu_0^{\prime} & j=i-1 \\
     0 & \text{else}
    \end{cases}
$$

and so for a harmonic oscillator under the linear dipole approximation, _transitions are allowed only for states that differ by one quantum_, i.e. only when $j = i+1$ or $j=i-1$ is the transition moment non-zero.
For many systems, this is actually a very good approximation. For what we tend to be interested in, it is not. 

One thing we often want to account for is the non-linearity in the dipole moment.
That means truncating our Taylor expansion at some higher order, say at second order

$$
\mu(r)^{(2)} = \mu_0 + \mu_0^{\prime} r + \frac{\mu_0^{\prime\prime}}{2} r^2
$$

then when we evaluate matrix elements, writing $r^2 = rr$, we get (try showing this for yourself)

$$
\langle i \lvert \mu(r)^{(2)} \rvert j \rangle =
    \begin{cases}
     \mu_0 + \frac{(2i + 1)}{2} \frac{\mu_0^{\prime\prime}}{2} & j=i \\
     \sqrt{\frac{i+1}{2}} \mu_0^{\prime} & j=i+1 \\
     \sqrt{\frac{i}{2}} \mu_0^{\prime} & j=i-1 \\
     \sqrt{\frac{i+1}{2}}\sqrt{\frac{i+2}{2}} \frac{\mu_0^{\prime\prime}}{2} & j=i+2 \\
     \sqrt{\frac{i-1}{2}}\sqrt{\frac{i}{2}} \frac{\mu_0^{\prime\prime}}{2} & j=i-2 \\
     0 & \text{else}
    \end{cases}
$$

What is noteworthy about this is that _transitions are allowed for states that differ by one or two quanta_. In general, we find that if we want to use harmonic oscillators to see transition with up to $n$ quanta of excitation, we need to expand our dipole moment out the the $n^{th}$ order. 

Obviously, real systems are not perfectly harmonic and real dipoles aren't perfectly linear. 
To investigate real world systems like that, we'll often move to something like a [discrete variable representation](DVRSpectra.md) approach.

## From Transition Moment to Intensity

It is importnant to note that these methods outline how to get a _dipole moment vector_ and not a proper intesity. Not to worry though, the dipole moment vector is the tricky part.  
First, recall the intensity formula

$$ I_{n,m} \propto \nu_{n,m} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2} $$

we have half of this, but to get a proper intensity we need to multiply by $\nu_{n,m}$ and of course, make sure you are tracking your units. (Wavenumbers is probably a good place to start.) If you choose to stick with this, you will probably want to convert it to a _relative intensity_ where your transistions are normalized so that either the sum is 1 or one of the fundamental transitions is 1. 

Second, if don't want a _relative intensity_, you can implement one of the unit conversions described [here](https://mccoygroup.github.io/References/References/Spectrum%20Generation/StickSpectra.html#a-note-on-units). 

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="fn1"></a> In a principle axis frame, we'd probably instead opt to use use _a_, _b_, and _c_

[<sup>1</sup>]: #fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Spectrum%20Generation/BasisSetSpectra.md)
