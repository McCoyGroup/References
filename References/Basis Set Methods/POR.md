---
---
# The Particle on a Ring Basis

The particle on the ring (POR) basis is useful for studying internal rotations and torsions within a molecule.
It gives the solutions to the Schrödinger equation for the Hamiltonian

$$
H = -\frac{\hbar^2}{2 I} \frac{d^2}{d \tau^2} = \frac{p_\tau^2}{2 I}
$$

where $I = m R^2$ is the moment of inertia for a particle of mass $m$ on a ring of radius $R$ and $\tau$ is the rotation angle. For simplicity, moving forward from here we will assume that $\hbar$ = 1.

To be valid wavefunctions, the POR basis must be _periodic_ and hence is relevant for periodic problems on the domain $[0, 2 \pi]$

### Properties of the Basis

The wavefunctions are given by

$$
\phi_m(\tau) = \sqrt{\frac{1}{2\pi}} e^{i m \tau}
$$

where $m$ is any integer.

This leads to a few key properties[<sup>1</sup>].

$$
\begin{align} 
e^{i m \tau}|n\rangle &= |m+n\rangle\\
\langle n|\frac{d^2}{d x^2}|m\rangle &= -m^2 \delta_{n,m}\\
\langle n|\cos(k \tau)|m\rangle &= \frac{1}{2}(\delta_{n, m+k} + \delta_{n, m-k})\\
\langle n|\sin(k \tau)|m\rangle &= \frac{1}{2i}(\delta_{n, m+k} - \delta_{n, m-k}) 
\end{align}
$$

where $n$ and $m$ represent the Particle on a Ring basis states. This means that the range of $n$ and $m$ varies with the number of basis functions you choose to use or the _Basis Size_. Ultimately, the range spans from - _Basis Size_ to _Basis Size_ including 0. 
One last thing to note at this point, the Basis Size at it's smallest would be equal to the expansion order or $k_{max}$, but in order to get _stable_ solutions to the Hamiltionian (not changing numerically by increasing the basis size), the basis size will become larger than the value of $k_{max}$, but these properties greatly simplify increasing the size of the basis. Do you see why?

### Hamiltonian Forms

Any function that can be fit to a form like

$$
F(\tau) = \sum_{k}^{k_max} c_k cos(k \tau) + s_k^{k_max} sin(k \tau)
$$

will have a simple representation in this basis. The technical name for this form is a _Fourier series_, so in the applications that follow we'll talk about using a Fourier expansion for our operators.

A common form of Hamiltonian that this is good for is something like

$$
\hat{H} = \frac{p_\tau^2}{2 I} + \sum_{k}^{k_max} v_k cos(k \tau)
$$

which is just a particle on a ring with an added potential term, also expanded as a Fourier series.

For things like torsions, the effective moment of inertia is generally a function of $\tau$. If that's the case, a kinetic energy like

$$
 \hat{T} = \frac{1}{2}\left( p_\tau^2B(\tau) +B(\tau) p_\tau^2 +\frac{d^2}{d\tau^2}B(\tau) \right)
$$

is more appropriate.

For the purposes of this discussion, $B$ represents an effective rotation constant. We also treat $B$ through a Fourier expansion as

$$
B(\tau) = \sum_k b_k \cos(k \tau)
$$

So in the frame of this discussion we are looking at a total Hamiltonian of the form

$$
H = \frac{1}{2}\left [p_\tau^2B(\tau) +B(\tau) p_\tau^2 +\frac{d^2B(\tau)}{d\tau^2}\right ] + \sum_{k} v_k cos(k \tau)
$$

We will solve for the matrix elements of this Hamiltonian by looking at it in three pieces. 
First, as if $B(\tau)$ and $V(\tau)$ are just intergers, i.e. $b_0$ and $v_0$

$$
\begin{align}
\left\langle n|b_0|m\right\rangle &= b_0\left(m^2\right )\delta_{m,n}\nonumber \\
\left\langle n|v_0|m\right\rangle &= v_0\delta_{m,n}\nonumber 
\end{align}
$$

Second, by looking at the rest of the series of $V(\tau)$

$$
\left\langle n\left|\sum_{k=1}v_k cos(k \tau)\right|m\right\rangle = \frac{v_k}{2}\delta_{|m-n|-k,0}
$$

And finally by looking at the rest of the kinetic energy operator. This is where the fun math trick comes into play. So, looking at what is left

$$
\left\langle n \left| \frac{1}{2} \sum_{k=1} \left(b_k cos(k \tau)p_\tau^2 + p_\tau^2cos(k \tau) + \frac{d^2B(\tau)}{d\tau^2}cos(k \tau)\right)\right| m\right\rangle
$$

We operate the first term to the left, the second to the right, and evaluate the third. What falls out is

$$
\sum_{k=1} \frac {b_k}{4} \left\[ n^2 +m^2-k^2\right \] \delta_{\left|m-n\right|-k,0}
$$

Pretty neat huh? Okay well, maybe not. Make sure you take a few minutes with all of this and make sure you undrestand where these results came from. We just applied the properties of the basis listed above, but prove that to yourself. Putting the three pieces together we get matrix elements of the form

$$
        \left\langle n|H|m\right\rangle = \left \{b_0\left(m^2\right )+v_0\right \}\delta_{m,n}\nonumber + \sum_{k=1}  \left\{ \left [n^2 +m^2-k^2\right ]\frac {b_k}{4}+\frac{v_k}{2}\right \}\delta_{|m-n|-k,0}
$$

A final note, circling back to the properties of the basis, we know that once $m - n > k_{max}$ or $m - n < -k_{max}$ the matrix element is 0. Keep this in mind as you are thinking of ways to write and _optimize_ your python implementation of the Particle on a Ring Basis Set Representation.

### Sample Applications

Within the McCode Academy exercises found [here](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/Exercises/), you will find three related to this topic.
1. How to expand a function as a Fourier Series.
2. How to set up and solve for eigenvalues and eigenvectors of the above described Hamiltonian starting with coefficents of $B$ and $V$ as they are expanded in a Fourier series.
3. How to use the eigenvalues and eigevectors of this representation to evaluate and plot the Particle on a Ring wavefunctions.

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="#fn1">&nbsp;</a> Try to show these yourself, keeping [Euler's relation](https://en.wikipedia.org/wiki/Euler%27s_identity) in mind

[<sup>1</sup>]: #fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/POR.md)
