# Fixed-node method

### Theory and Overview
Fixed-node method is one way to get the excited state information from the ground state method. In this case, we will focus on the Fixed-node DMC. The idea for the fixed-node method is that if we have some arbitrary potential:
<p align="center">
<img src="../img/fixed_node_potential.png" alt="fixed_node_potential" width="500"/>
</p>
if we know exactly where the node is for the excited state, we can make the two half-potentials by putting the infinite potential wall on the other side of the node. Note that the combinations of the ground state solutions of the half-potentials would be the same as the first excited state solution of the whole potential since all of the solutions need to satisfy the same Schrödinger's equation. Therefore, we can use the ground state method, like DMC, to find the first excited state energy and wavefunction from the two half potentials.

### Finding node position
The only thing we need is the location of the node, the way we get it is by running two adiabatic DMC calculations. On one calculation, we move the potential wall from the right to the left, and on the other calculation, we move the potenital wall from the left to the right. 
<p align="center">
<img src="../img/fixed_node_runs.png" alt="fixed_node_runs" width="800"/>
</p>
We can then use the energy from the calculations to find the node location, since at the correct node position, the energy for the two runs should be the same, we can plot the energy vs the node location for the two runs, fit it, and then find where the fitted lines crossed.
<p align="center">
<img src="../img/fixed_node_energy.png" alt="fixed_node_energy" width="500"/>
</p>

### Recrossing
One last problem on fixed-node DMC is that in DMC, we work with discrete time step, and so there is a chance that in one time step, the walker crosses the node and recrosses back. If we were to have a perfect simulation where the time step is infinitesimal, we would have killed that walker. The way we deal with this problem is that the probability of the recrossing can be calculated according to [Anderson et. al.](https://aip.scitation.org/doi/10.1063/1.432868) to be $\exp(-\frac{2x'x''m}{\Delta\tau})$ where $x'$ and $x''$ are the initial and final position, $\Delta\tau$ is the time step interval, and $m$ is the mass associated with our system. So, we kill each walker with that probability to simulate the recrossing situation.

### Working with PyVibDMC
In most situation, you will be working with PyVibDMC to run a fixed-node DMC, and PyVibDMC already has a function for running fixed-node DMC. Here is what you need to add to the ground state PyVibDMC calculation:
- a function for distance calculation
- a function or a number for g matrix element (1/mass of the system)
- a line in DMC_Sim with the following
`fixed_node = {"function":xxx,"g_matrix":yyy}` Replace the `xxx` and `yyy` with your distance and g matrix function.


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Spectrum%20Generation/FixedNodeSpectra.md)
