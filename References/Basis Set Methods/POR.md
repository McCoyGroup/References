---
---
# The Particle on a Ring Basis
The particle on the ring basis is useful for studying rotations and torsions within a molecule. Here we will talk about using this basis with the coefficients of an equation expanded using sin and cos functions. This will enable us to take advantage of the Euler relations. 

### Hamiltonian Forms
The Hamiltonian 

$$
 H = \frac{1}{2}\left[ p_\tau^2B(\tau) +B(\tau) p_\tau^2 +\frac{d^2B(\tau)}{d\tau^2} \right] + V(\tau)
$$

For the purposes of this discussion, $B$ represents an effective rotation constant, and both $B$ and $V$ are expanded in a Fourier series, e.g.
    
$$
B(\tau) = \sum_{m=0}^N b_m\cos\left (m\tau\right )
$$
    
where, based on the Euler relationships
    
$$
\cos\left (m\tau\right ) = \frac{1}{2}\left [\exp\left (im\tau\right) + \exp\left (-im\tau\right)\right ]
$$
    
### Properties of the Basis
The wavefunctions are described as

$$
\Psi_n(\tau) = \sqrt{\frac{1}{2\pi}}\sum_{k=-n_{\rm{bas}}}^{+n_{\rm{bas}}}c_{m}^{(n)}\exp\left (ik\tau\right) 
$$

And so, looking at the matrix elements.. 
If we keep in mind that 

$$
\langle k^\prime|\exp\left (im\tau\right )|k\rangle = \delta_{|k-k^\prime|-m}
$$

In this basis..

$$
\left\langle k^\prime|H|k\right\rangle &=& \left \{b_0\left(k^2\right )+v_0\right \}\delta_{k,k^\prime}\nonumber + \sum_{m=1}  \left\{ \left [\left (k^\prime\right )^2 +k^2-m^2\right ]\frac {b_m}{4}+\frac{v_m}{2}\right \}\delta_{|k-k^\prime|-m,0}
$$

### Sample Applications

...
[EDIT](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/POR.md)
{: .alert .alert-warning}

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Basis%20Set%20Methods/POR.md)
