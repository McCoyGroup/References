# Monte Carlo Methods

Diffusion Monte Carlo (DMC) is a way to solve the time-independent Schrödinger equation (TISE)
 using Monte Carlo sampling of a potential energy surface. The implementation that we use in the group is
 based on Anderson et. al. in [this paper](https://aip.scitation.org/doi/10.1063/1.432868). At the end of the simulation we will have a wavefunction
 and a zero point vibrational energy.  The way we will do this is by representing our
 wavefunciton as an ensemble of localized functions, or "Walkers", each of which represents a configuration
 of the molecule/system of interest. One can think of these as an ensemble of localized functions, where a function has amplitude in one geometry and zero elsewhere:

$$
\Psi (x, \tau) = \sum_j w_j g(x - x_j(\tau))
$$

 We discretize time into "time steps", and we will displace each of the coordinates of each walker at every time step, the displacement is based on a normal distribution (Gaussian), which is parametrized inversely proportionally to the mass and proportional to the step size. We can think about it in terms of moving an object. The bigger the object, the harder it is to move and the less time we have to move object, the shorter the distance we can move it will be.

 We will need to check the energy of each walker after it makes its step to see if it was an energetically favorable
 or unfavorable move.  If it was too unfavorable, the walker might be removed from the simulation.  If it was very
 favorable, the walker may be replicated.
 
 I'm not going to go through the specific cases here, but we've written up some references to help introduce you to the basics of DMC.
 They are written in an order of simple to more complicated.

* [Basic Diffusion Monte Carlo](DMC.md)
* [Descendant-Weighting and Wavefunction Analysis](DWandWfns.md)
* [Importance Sampling](ImpSamp.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Monte%20Carlo%20Methods/index.md)

