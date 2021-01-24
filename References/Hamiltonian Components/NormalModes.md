# Normal Modes

Far and away the most common form we start from when solving vibrational problems is the harmonic approximation,
which assumes a Hamiltonian of the form

$$
H = \sum_{i} \frac{p_i^2}{2 m} + \sum_{i} m \omega_i^2 q_i^2
$$

i.e. a perfectly separable sum of 1D kinetic and potential energies, where each potential term is simply a parabola.
This approximation is in general insufficient for what we study, but it's a good starting point.

To find the best set of coordinates ${q_i}$ and corresponding moments ${p_i}$ to satisfy this, we start with a potential
energy surface coming from electronic structure, $V$. 
Given a geometry of our system that minimizes this potential, ${\textbf{r}_e}$, we know that the _gradient_ of the potential,
or in other words, the vector first derivatives of the potential with respect to all of the configurational coordiantes in our
system (e.g. the Cartesian coordinates describing the position of each of the atoms in the system) is zero.
Or in compact notation, we have

$$
\nabla_{R} V(\textbf{r}_e) = 0
$$

This means we can approximate our potential expandeded around this minimum-energy geometry as

$$
V(\textbf{r}) = V(\textbf{r}_e) + (\textbf{r}-\textbf{r}_e) \nabla_{R^2} V(\textbf{r}_e) (\textbf{r}-\textbf{r}_e) 
$$

and by performing a constant shift by $V(\textbf{r}_e)$ term we can have a potential that only depends on the 
matrix of second derivatives of the potential, called the Hessian.

For notational consistency with standard literature and stuff, we'll write 

$$
F = \nabla_{R^2} V(\textbf{r}_e)
$$

Next, we want to get a set of coordinates so that only the _diagonal_ potential terms matter.
We also want to do this subject to the constraint that only the diagonal kinetic energy terms matter.

We'll do this by first constructing the [G-matrix](GMatrix.md) for our system and solve 
the [generalized eigenvalue problem](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Generalized_eigenvalue_problem)

$$
GFL = L\Omega
$$

This is straightforwardly done with modern linear algebra libraries, e.g. it's in [scipy.linalg.eigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html).

This matrix $L$ (again, name chosen for consistency with standard literature) defines a transformation from our configurational coordinates, $R$, 
to a set of normal coordinates, or normal modes, which satisfy the Hamiltonian we set out to get.
By construction, since we include a mass-weighting in our $G$ matrix, the associated masses are $1$, and

$$
\Omega_{i,i} = \omega_i^2
$$


---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Hamiltonian%20Components/NormalModes.md)