# Spectrum Generation

One of the fundamental ways (maybe _the_ fundamental way) we theorists make sure that the physics we model actually maps on to reality is through the generation of spectra. Our experimental <s>servants</s> colleagues go to great lengths in the lab to hit stuff with light and see what comes back. At that point, we/they can compare the collected signal to theoretical predictions to understand what kind of physics is going on.

Of course, this means that we need to be able to theoretically model the kinds of light-matter interactions that are going on in the experiments. That modelling process is what we're calling _spectrum generation_. There are many approaches to this, but the ones we use center on the relationship

$$
I_{n,m} \propto \nu_{n,m} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2}
$$

where $I_{n,m}$ is the _intensity_ of the transition from state $\psi_n$ to state $\psi_m$. This is akin to the probability that a given photon of energy $\nu_{n,m}$ will interact with a molecule in state $\psi_n$ (assuming there is one). We see two contributions to this relationship

* $\nu_{n,m}$: the _transition frequency_, given by $E_m - E_n$
* $  \left\langle \psi_n \lvert \mu \rvert \psi_m \right\rangle$: the _transition moment_, where $\mu$ is the dipole moment function for the system

We can understand this from a phenomenological point of view. First, a photon is composed of an oscillating electric and magnetic field. Therefore, for a photon to interact with matter, it has to interact via an electrostatic or magnetic interaction. 
From the molecular perspective, the dominant contributor to these kinds of interactions is the molecular dipole moment, and from the quantum mechanical perspective, we need the average dipole for the transition, or the _transition moment_. 
Finally, the electric field on the photon is constantly oscillating, and the faster it oscillates, the more often the electric field will be aligned with the molecular dipole, hence the higher the _frequency_ of the oscillation the more likely an interaction is to occur. Recalling that, quantum mechanically, a transition from $\psi_n$ to $\psi_m$ can only happen when the energy of the incident photon is exactly $E_m - E_n$, this means that our will be linearly dependent on that energy difference, or the _transition frequency_.

In the McCoy group, we're mostly interested in modeling how molecular vibrations interact with light. This means our frequencies will usually correspond to those of infrared radiation and our $\psi_n$ and $\psi_m$ will always be vibrational wave functions.
Beyond that, everything we've said here is entirely applicable to rotational or electronic spectroscopy as well.

Here's a road map for the methods we use:

* [An Introduction to Stick Spectra](StickSpectra.md)
* [Basis Set Spectra](BasisSetSpectra.md)
* [Discrete Variable Representation Spectra](DVRSpectra.md)
* [The Difficulty with DMC](DMCSpectraDifficulties.md)
* [Fixed-Node DMC Spectra](FixedNodeSpectra.md)
* [Ground-State Approximation DMC Spectra](GSASpectra.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Spectrum%20Generation/index.md)