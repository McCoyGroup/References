# Pseudopotential

In a previous section on the [G-matrix](GMatrix.md) we mentioned that in arbitrary coordinates the kinetic energy operator can be written
as

$$
T = \frac{1}{2} pGp + V^{\prime}
$$

the development of this form really starts with [Podolsky](https://journals.aps.org/pr/abstract/10.1103/PhysRev.32.812) who showed that the entire
kinetic energy can be written as

$$
T = \sum_{r} \sum_{s} g^{-1/2} \frac{\partial}{\partial u_r} 
    (g^{1/2} g^{r s} \frac{\partial}{\partial u_s})
$$

[Wilson and Howard](https://aip.scitation.org/doi/10.1063/1.1749833) then transformed this to a more standard form which we will not type out because it is never seen again.
Finally, [Meyer](https://aip.scitation.org/doi/10.1063/1.1670272) did a large-scale refactoring of the Wilson result, 
and [Pickett](https://aip.scitation.org/doi/10.1063/1.1677430) transformed this into what we actually use

$$
T = pGp + V'(Q)
$$

That $V'(Q)$ is a the pseudopotential, called such because it's a scalar function of the coordinates with no derivative dependence, just like the potential.
We can take Pickett's expression (see Eq. 20) and write it in matrix-algebraic form like

$$
V'(Q) = 
 \frac{1}{8} \left( 
   \text{Tr}(\nabla_{q} G \nabla_{q} \ln g) 
   + G \odot \nabla_{q^2} \ln g
   + \frac{1}{4} (\nabla_{q} \ln g G \nabla_{q} \ln g)
   \right)
$$

where we've followed Pickett in defining

$$
g = \frac{\lvert I \rvert}{\lvert G \rvert}
$$

All of these derivatives can be done numerically of course, but it is actually possible to define everything here through coordinate transformations
and the chain rule by making use of [Jacobi's Formula](https://en.wikipedia.org/wiki/Jacobi%27s_formula)

$$
\frac{\partial }{\partial q_i}|G| = \text{Tr}\left(G^{-1} |G| \frac{\partial G}{\partial q_i}\right)
$$

and then for the second derivatives, we take something out of the [Matrix Cookbook](https://www.ics.uci.edu/~welling/teaching/KernelsICS273B/MatrixCookBook.pdf)

$$
\frac{\partial }{\partial y_n} G^{-1} = - (G^{-1}) \frac{\partial G}{\partial y_n} (G^{-1})
$$

which means that if we can take derivatives of $G$ (which we often need to), by using our inertia tensor derivatives from earlier we
can evaluate this term as analytically as possible.

Whether that's worth it or not is left to the reader, 
but a sample implementation is [here](https://github.com/McCoyGroup/Psience/blob/3bd778480196636e9b1fb0d4e262c046ee549c92/Psience/VPT2/Terms.py#L1199).

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Hamiltonian%20Components/Pseudopotential.md)