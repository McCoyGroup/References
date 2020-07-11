# Basis Set Methods

One of the oldest approaches to solving the Schrödinger equation, _basis set methods_ (sometimes called _matrix methods_) are based in linear algebra.
If you're unfamiliar with linear algebra, this can sound a little bit scary.
As you build up your familiarity, though, you'll come to find that there's no branch of "advanced" math that's kinder to us.[<sup>1</sup>]

The basic idea is to build a _matrix representation_ of the Hamiltonian in a given _basis_, which is just a compact way to say a set of functions that can be indexed (i.e. we can assign a number from $0...\infty$ to them) and are distinct from one another.[<sup>2</sup>]
We'll do the traditional thing and call our basis $\{\phi_i\}$, which just means a set of functions, where each is called $\phi$, indexed by the variable $i$.

We don't really need to understand how to derive this[<sup>3</sup>], but the heart of our matrix representation is to say

$$
H_{i\, j}=\langle i|\hat{H}|j\rangle =\int _{\pmb{r}\in \mathbb{D}}\phi _i(\pmb{r})\hat{H}\left(\phi _j(\pmb{r})\right)d\, \pmb{r}
$$

This (rightfully) looks nasty. There is nothing harder in mathematics than doing integrals.
On the other hand ___we never need to do these integrals by hand___.
Instead, by picking $\{\phi_i\}$ appropriately we can let other people do the grunt work and reuse their results.
All we need to do is a bunch of summations, and even there as long as we use the language of linear algebra, we don't even need to do that!

I'm not going to go through the specific cases here, but we've written up some references to help introduce you to the most useful basis sets to use.
These are intended to be read in no particular order, but roughly go from simpler to more complicated.

* [The Particle in a Box Basis](PIB.md)
* [The Harmonic Oscillator Basis](HarmonicOscillator.md)
* [The Particle on a Ring Basis](POR.md)
* [Discrete Variable Representation](BasicDVR.md)

We've also got a set of more advanced references for tackling multidimensional systems that will be easiest to understand after you understand the preliminaries.

* [Multidimensional Bases](MultidimBasis.md)
* [Multidimensional DVR](MultidimDVR.md)
* [Adiabatic Separations](AdiabaticSeparations.md)
* [Second-Order Vibrational Perturbation Theory](VPT2.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
1. <a id="fn1"></a> I'm not lying when I say this. Linear algebra is basically taking regular `y = m*x + b`-type algebra and making it work when we have more variables than just `x`. This means that 90% of what you need to learn is rooted in stuff you probably learned in Middle school.
2. <a id="fn2"></a> Formally, this is _linear independence_
3. <a id="fn3"></a> If you'd like more detail on this, I've written up the intuitive explanation [here](https://stackoverflow.com/c/mccoygroup/questions/74).

[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2
[<sup>3</sup>]: #fn3

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/index.md)
