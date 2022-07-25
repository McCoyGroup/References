# Fixed-node method

### Theory
Fixed-node method is one way to get the excited state information from the ground state method. In this case, we will focus on the Fixed-node DMC. The idea for the fixed-node method is that if we have some arbitrary potential:
<p align="center">
<img src="../img/fixed_node_potential.png" alt="fixed_node_potential" width="500"/>
</p>
If we know where the node of the excited state function beforehand, we can cover one side of the potential, and the ground state function of the half potential would be the first excited state function of the whole potential. The reason is because if we take a look at the Schrodinger's equation $\frac{H\Psi(x)}{\Psi(x)} = E(x)$. The equation only evolves one position (x) at the time, so it is locally satisfied. So, with DMC, we can get the excited state energy and the excited state wavefunction. We can simulate the half potential with the infinite potential wall for the other half of the potenital. 

###
The only thing we need is the location of the node, the way we get it is by running two adiabatic DMC calculations. On one calculation, we move the potential wall from the right to the left, and on the other calculation, we move the potenital wall from the left to the right. 
<p align="center">
<img src="../img/fixed_node_runs.png" alt="fixed_node_runs" width="800"/>
</p>
We can then use the energy from the calculations to find the node location, since at the correct node position, the energy for the two runs should be the same, we can plot the energy vs the node location for the two runs, fit it, and then find where the fitted lines crossed.
<p align="center">
<img src="../img/fixed_node_energy.png" alt="fixed_node_energy" width="500"/>
</p>
