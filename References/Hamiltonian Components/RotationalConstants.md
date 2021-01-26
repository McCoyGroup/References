# Rotational Constants and Moments of Inertia

Rotational constants, as we use them, show up most frequently when adding a rotational band profile to a vibrational spectrum.
We won't worry about the specifics of that, since it's described [all](https://doi.org/10.1016/0022-2852(91)90393-O) [over](http://pgopher.chm.bris.ac.uk/Help/asymham.htm) [the](http://www.chem.helsinki.fi/~sundholm/winterschool/lecture_notes_2013/Gauss_Helsinki_winterschool_2013.pdf) [place](http://vallance.chem.ox.ac.uk/pdfs/MolecularEnergyLevelsNotes.pdf), but
instead we'll just note that these constants are defined (in atomic units) as

$$
\Xi = \frac{1}{2 I_{\xi}}
$$

where $\Xi \in \{\text{A}, \text{B}, \text{C}\}$ and $\xi \in \{\text{a}, \text{b}, \text{c}\}$ and $I_{\xi}$ is the 
[moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia#Point_mass) along the $\xi$ axis.

Being able to describe what $\text{a}$, $\text{b}$, and $\text{c}$ are here is directly tied to how a moment of inertia is calculated,
so we'll take a four second aside to describe that.

Given a set of atoms, we'll represent this a set of pairs $(m_i, r_i)$ where $r_i$ is the vector pointing from the center of mass of the
set of atoms (we always rotate about the center of mass).
If we have some rotation axis $\hat{R}$ given as a unit vector, we calculate the moment of inertia for rotation about that axis as

$$
I_{R} = \sum_{i} m_i {\lvert r_i - (r_i \cdot R)\hat{R} \rvert}^{2}
$$

i.e. we take a weighted sum of the _distances to the axis_ squared.
This lines up with the classic definition.

Given some axis system $(x, y, z)$ we might also want a single matrix/set of equations that allows us to calculate moments of inertia
about any axis of interest. We'll call this the _inertia tensor_. In the interest of brevity/not doing useless things, we're not going to 
derive how we get to this, but the two-line derivation is given [here](https://en.wikipedia.org/wiki/Moment_of_inertia#Derivation_of_the_tensor_components).

This tensor is constructed in basically the same way as our simple moment of inertia by

$$
\textbf{I} = \sum_{i} m_i ({\lvert r_i \rvert}^{2} E_3 - r_i \otimes r_i)
$$

where $r_i \otimes r_i$ is the outer-product of the elements of $r_i$ and $E_3$ is the 3x3 identity matrix.

If we then want, say, the moment of inertia along the axis $R$ from before, we can just write

$$
I_{R} = R^T \textbf{I} R
$$

Dope.

With that, we're ready to talk about the $\text{a}$, $\text{b}$, and $\text{c}$ from before. 
When we constructed $\textbf{I}$, we had an implict axis system, since each $r_i$ is going to be a vector like $(x_i, y_i, z_i)$.
From this, $\text{a}$, $\text{b}$, and $\text{c}$ are the "best" axes for describing rotations, i.e. the ones for which the moment of inertia
tensor is diagonal
i.e. $\text{a}$, $\text{b}$, and $\text{c}$ are the eigenvectors of $\textbf{I}$ and $I_{\xi}$ is the corresponding eigenvector.

### Derivatives of the Inertia Tensor

For certain applications, e.g. calculating the [pseudopotential](Pseudopotential.md), we might need derivatives of the inertia tensor.
This might seem nasty, but it ends up being pretty straight-forward.
The trick we'll use is to only ever take derivatives with respect to the atomic positions $r_i$.
When we need internal coordinate derivatives, we will get these through the chain rule.

With that in hand, to get the derivative tensor with respect to say, $r_n$, we have

$$
\begin{align}
\frac{\partial }{\partial r_n} \textbf{I} 
  &= \frac{\partial }{\partial r_n}\sum_{i} m_i ({\lvert r_i \rvert}^{2} E_3 - r_i \otimes r_i) \\
  &= \sum_{i} m_i \frac{\partial }{\partial r_n} ({\lvert r_i \rvert}^{2} E_3 - r_i \otimes r_i) \\
  &= m_n \left(\frac{\partial }{\partial r_n} {\lvert r_n \rvert}^{2} E_3 - \frac{\partial }{\partial r_n} r_n \otimes r_n \right) \\
  &= m_n \left(\frac{\partial }{\partial r_n} {\lvert r_n \rvert}^{2} E_3 - \left(\frac{\partial r_n }{\partial r_n} \otimes r_n + r_n \otimes \frac{\partial r_n }{\partial r_n} \right) \right) \\
  &= m_n \left(
    2  r_i (E_3 \otimes E_3)- 
    \left(E_3 \otimes r_n + r_n \otimes E_3 \right) \right)
\end{align}
$$

where here we're using $\otimes$ to be a generalized outer product that maps over tensor dimensions, i.e. for $F$ an NxM tensor and $G$ an AxLxM, $F \otimes G$ is an AxNxLxMxM, or more concretely,
$E_3 \otimes E_3$ is a 3x3x3x3 so that $r_i (E_3 \otimes E_3)$ is a 3x3x3 tensor and $r_n \otimes E_3$ is basically the vector of outer-products $(r_n \otimes e_i)$.
It's annoying and a lot to keep track of, I know. So just write code that will do it for you.


---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Hamiltonian%20Components/RotationalConstants.md)