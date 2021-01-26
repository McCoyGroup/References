# The G-Matrix

The "G-matrix", as we use it, is a pretty straightforward object to work with, but actually has an interesting meaning
and history.
In other branches of math or physics, it would usually be called the [metric tensor](https://en.wikipedia.org/wiki/Metric_tensor#Metric_in_coordinates).
As with much mathematical stuff, the formal definition requires a decent bit of background to understand.
But for our purposes we'll understand as an object that maps arc lengths in internal coordinates to distances in Cartesian coordinates.
We won't use this definition in practice (we will actually do very little with the G-matrix in practice), but that understanding
helps motivate why and where we _do_ use it.
We will always call this matrix $G$, because the entirety of the mathematical literature calls it $G$.

The kinetic energy of a system of atoms is given, in Cartesian coordinates, by

$$
T = - \sum_{i} \frac{1}{2 m_i} \frac{\partial^2}{\partial x_i^2}
$$

we then mass-weight our coordinates

$$
y_i = \sqrt{m_i} x_i
$$

to get 

$$
T = - \frac{1}{2} \sum_{i} \frac{\partial^2}{\partial y_i^2}
$$

The derivation of what follows is any number of places in the literature[<sup>1</sup>], so we won't go into it, but with this
coordinate system in hand, we finally define our G-matrix as

$$
G = (\nabla_Y R)^{\intercal}(\nabla_Y R)
$$

and through a few applications of the multidimensional chain-rule we can write

$$
T = - \frac{1}{2} pGp + V^{\prime}
$$

We'll talk about $V\prime$ [later](Psuedopotential.md), but it's a product of performing a change of variables from
Cartesian coordinates to internal coordinates and then coercing kinetic energy into $pGp$ form.

---
1. <a id="fn1"></a> Pickett has a nice discussion of all transformations of the rotation/vibration kinetic energy [here](https://aip-scitation-org.offcampus.lib.washington.edu/doi/pdf/10.1063/1.1677430), which in turn makes use of [this work](https://aip.scitation.org/doi/pdf/10.1063/1.1670272) by Meyer

[<sup>1</sup>]: #fn1

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Hamiltonian%20Components/GMatrix.md)