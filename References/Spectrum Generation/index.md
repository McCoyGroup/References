# Spectrum Generation

One of the fundamental ways (maybe _the_ fundamental way) we theorists make sure that the physics we model actually maps on to reality is through the generation of spectra. Our experimental colleagues go to great lengths in the lab to hit stuff with light and see what comes back. At that point, we/they can compare the collected signal to theoretical predictions to understand what kind of physics is going on.

Of course, this means that we need to be able to theoretically model the kinds of light-matter interactions that are going on in the experiments. That modelling process is what we're calling _spectrum generation_. There are many approaches to this, but the ones we use center on the relationship

$$
I_{n,m} \propto \nu_{n,m} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2}
$$

where $I_{n,m}$ is the _intensity_ of the transition from state $\psi_n$ to state $\psi_m$. This is akin to the probability that a given photon of energy $\nu_{n,m}$ will interact with a molecule in state $\psi_n$ (assuming there is one). We see two contributions to this relationship

* $\nu_{n,m}$: the _transition frequency_, given by $E_m - E_n$
* $  \left\langle \psi_n \lvert \mu \rvert \psi_m \right\rangle$: the _transition moment_, where $\mu$ is the dipole moment function for the system

Beyond a very rough phenomenological perspective of light interacting with the dipole of the molecule, there's nothing really to be gained from going through a derivation of this.
There are many details, but little insight.
If you're interested, [Schatz and Ratner](https://books.google.com/books/about/Quantum_Mechanics_in_Chemistry.html?id=T9KBlS-bj0sC) have a discussion of this in their textbook, but it's not clear to us that there's a benefit to buying a textbook just for this (or for that matter, for much else). [This LibreTexts](https://phys.libretexts.org/Bookshelves/Astronomy__Cosmology/Book%3A_Stellar_Atmospheres_(Tatum)/09%3A_Oscillator_Strengths_and_Related_Topics/9.02%3A_Oscillator_Strength._(die_Oszillatorenst%C3%A4rke)) description probably gives just as much insight as you'd get from a book.

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
