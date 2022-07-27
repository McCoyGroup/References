# The Difficulties of Generating Spectra with Diffusion Monte Carlo

There are two key pieces that are needed in order to obtain each peak in a spectrum: the frequency and intensity of the transition. For the frequency, we need the difference in energy between the state we are exciting to and the state we are exciting from (usually the ground-state). For the intensity we need all the pieces of the following equation,

$$
I \propto \nu_{nm} {\left\lvert \left\langle \psi_n | \mu | \psi_m \right\rangle \right\rvert}^{2}
$$

The problem with using DMC to obtain these is that DMC is a _ground-state_ method. It only allows us to obtain the _ground-state_ energy and _ground-state_ wave function and that means that we are missing some key pieces if we want to generate a spectrum. There are tricks that we can use in order to extend this method so that we can obtain some of these pieces however. 

If we are just interested in the frequency of a specific transition then all we need is the excited-state energy of the vibration that is associated with that peak. There are a couple ways we can obtain this. The first is through a method called Fixed-Node DMC which is presented in depth [here](https://mccoygroup.github.io/References/References/Spectrum%20Generation/FixedNodeSpectra.html). We could also use an excited-state guiding function and use guided DMC as presented [here](https://mccoygroup.github.io/References/References/Monte%20Carlo%20Methods/ImpSamp.html). The only addition that is needed is that you kill walkers where the sign of the guiding function for that position has changed. (This is already implemented in PyVibDMC - ask for help if you want to try!).

There is a third method that can obtain frequencies and also the intensities of transitions. This method uses the ground state probability amplitudes (GSPA) to approximate the excited-states. This was most recently done in [this paper](https://pubs.acs.org/doi/10.1021/acs.jpca.1c05025). It requires the user to develop a full set of internal coordinates that describe the system, which can not only be time-consuming but if done incorrectly will affect the results.

Other than that, since DMC is a _ground-state_ method, it's best uses aren't typically for recreating spectra, but more for analyzing properties based on the _ground-state_.



Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Monte%20Carlo%20Methods/DMCSpectraDifficulties.md)

