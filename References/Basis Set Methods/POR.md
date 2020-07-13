---
---
# The Particle on a Ring Basis

The particle on the ring (POR) basis is useful for studying internal rotations and torsions within a molecule.
It gives the solutions to the Schrödinger equation for the Hamiltonian

$$
H = -\frac{1}{2 I} \frac{d^2}{d \tau^2}
$$

where $I = m R^2$ is the moment of inertia for a particle of mass $m$ on a ring of radius $R$ and $\tau$ is the rotation angle.

To be valid wavefunctions, the POR basis must be _periodic_ and hence is relevant for periodic problems on the domain $[0, 2 \pi]$

### Properties of the Basis

The wavefunctions are given by

$$
\phi_k(\tau) = \sqrt{\frac{1}{2\pi}} e^{(i k \tau)}
$$

where $k$ is any integer.

This leads to a few key properties[<sup>1</sup>]. Assuming that $n<m$

$$
|m\rangle|n\rangle = |n+m\rangle \\
\langle n|\frac{d^2}{d x^2}|m\rangle = -k^2 \delta_{n,m} \\
\langle n|\cos(k \tau)|m\rangle = \begin{cases}
  1 &  k=m+n \\
  1 & -k=m+n \\
  0 &  \text{else}
\end{cases} \\
\langle n|\sin(k \tau)|m\rangle = \begin{cases}
  1 &  k=n+m \\
 -1 & -k=n+m \\
  0 &  \text{else}
\end{cases}
$$

### Hamiltonian Forms

Any function that can be fit to a form like

$$
F(\tau) = \sum_{k} c_k cos(k \tau) + s_k sin(k \tau)
$$

will have a simple representation in this basis. The technical name for this form is a _Fourier series_, so in the applications that follow we'll talk about using a Fourier expansion for our operators.

A common form of Hamiltonian that this is good for is something like

$$
\hat{H} = -\frac{1}{2 I} \frac{d^2}{d \tau^2} + \sum_{k} c_k cos(k \tau)
$$

which is just a particle on a ring with an added potential term.

For things like torsions, the effective moment of inertia is generally a function of $\tau$. If that's the case, a kinetic energy like

$$
 \hat{T} = \frac{1}{2}\left( p_\tau^2B(\tau) +B(\tau) p_\tau^2 +\frac{d^2}{d\tau^2}B(\tau) \right)
$$

is more appropriate.

For the purposes of this discussion, $B$ represents an effective rotation constant. We also treat $B$ through a Fourier expansion as

$$
B(\tau) = \sum_k b_k \cos(k \tau)
$$


### Sample Applications

You can find an exercise to implement the Particle on a Ring Basis [here](). 
In this exercise, you will work through how to set up and solve for eigenvalues and eigenfunctions of the above described Hamiltonian granted that you have coefficents of $B$ and $V$ as they are expanded in a Fourier series. 

If you have already solved the Hamiltion and are interested in the wavefunctions and plotting them, you can find an exercise for that [here]().

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="#fn1">&nbsp;</a> Try to show these yourself, keeping [Euler's relation](https://en.wikipedia.org/wiki/Euler%27s_identity) in mind

[<sup>1</sup>]: #fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/POR.md)
