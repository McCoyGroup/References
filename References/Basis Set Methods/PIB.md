---
---
# The Particle in a Box Basis

The particle in a box (PIB) basis comes from probably the simplest possible Hamiltonian imagineable

$$
H = -\frac{1}{2 m} \frac{d^2}{d x^2}
$$

where $m$ is the mass of the system.
To give proper wavefunctions, this form needs to have an associated "box length", $L$, i.e. the domain has to be $[a, b]$ where  $L = b-a$.

When studying vibrations, we often don't use the PIB basis directly, preferring things like the HO basis.
On the other hand, it's a very important building block for a commonly used type of discrete variable representation, so we'd be remiss not to discuss it.

### Properties of the Basis

The PIB basis functions are

$$
\phi_n(x) = N_n \sin\left(\frac{n \pi}{L}x\right)
$$

Ufortunately this form doesn't many have nice properties.
At some level, this comes from the fact that there aren't all that many nice relationships between $\sin$ functions.
For instance, we can know that

$$
\sin\left(\frac{n \pi}{L} x\right) = \sin\left(\frac{(n-k) \pi}{L} x\right)\cos\left(\frac{k \pi}{L} x\right) + \sin\left(\frac{k \pi}{L} x\right)\cos\left(\frac{(n-k) \pi}{L} x\right)
$$

but the $\cos$ terms prevent this from being all that useful.

On the other hand, we _do_ have that

$$
\langle n|\frac{d^2}{d x^2}|m\rangle = -k^2 \delta_{n,m}
$$

If you want something more, we can also use a symbolic algebra program like Mathematica to show that

$$
\langle n|\hat{x}|m\rangle = \frac{4 \left(-1+(-1)^{m+n}\right) L m n}{\left(m^2-n^2\right)^2 \pi^2}
$$

This allows us to express operators like $\hat{x}^2$ if we would like to, but as we'll see, there are simpler approaches to be had.

### Hamiltonian Forms

As noted before, this basis on its own is only really good for the problem it arises from.
But we want to know about it later for its application to DVR.

If we've got a restricted domain, we _can_ use it for things like

$$
\hat{H} = -\frac{1}{2 m} \frac{d^2}{d x^2} + \sum_{k} c_k x^k
$$

but I'd argue we should look elsewhere instead.

## Sample Applications

...

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/PIB.md)