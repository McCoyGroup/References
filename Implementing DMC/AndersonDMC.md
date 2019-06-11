<a id="AndersonDMC" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
# Simple DMC Code

This is walkthrough of a [Python implementation of Discrete Weighting DMC](https://github.com/McCoyGroup/DMC_DescendentWeighting/blob/master/HarmonicOscillatorDW.py) based on Anderson et. al. in  [this paper](https://aip.scitation.org/doi/10.1063/1.432868).

###Introduction
Diffusion Monte Carlo (DMC) is a way to solve the time-dependent Schrodinger equation (TDSE)
 using Monte Carlo sampling of a potential energy surface.  At the end of the simulation we will have a wavefunction 
 and a zero point vibrational energy.  The way we will do this is by representing our 
 wavefunciton ($\Psi$) as an ensemble of localized functions, or "Walkers", each of which represents a configuration 
 of the molecule/system of interest. We are going to represent our wavefunction as an ensemble of localized 
 functions, called "Walkers".  One can think of these as an ensemble of delta functions, taking up one point of 3N 
 configuration space. 
 
 We discretize time into "time steps", and we will displace each walker at every time step, the displacement is based on 
 a normal distribution (Gaussian), which is parametrized by the mass and the step size.  This is intuitive, since 
 a larger mass will move less, and if we are discretizing our timesteps, the larger the step, the more it should move.
 
 We will need to check the energy of each walker after it makes its step to see if it was an energetically favorable
 or not favorable move.  If it was too unfavorable, the walker might be removed from the situation.  If it was very 
 favorable, the walker may be replicated as a reward.  This whole idea of replication and deletion is referred to as 
 discrete weighting.  

###The Implementation
For simplicity of this tutorial, we are going to do a 1-dimensional DMC of the quantum model system, the harmonic oscillator.
Physically, this simulation doesn't really mean much.  This is all done in atomic units.

```python
'''Simulation Parameters!'''
import numpy as np
import math
import matplotlib.pyplot as plt
import copy

numAtoms = 1
initialWalkers = 2000
wvnmbr = 4.55634e-6 #going between atomic units and wavenumbers
omega = 2000.0000*wvnmbr #in atomic units,
dimensions = 1
mass = 1836.35/2
deltaT = 5.0 #simulation parameter - adjustable
alpha = 1.0/(2.0*deltaT) #simulation parameter - adjustable
D = 0.5
sigma = math.sqrt((2*D*deltaT)/mass) #related to the stdev of our displacement of the walkers
```


For ultra simplicity, we are also going to use a list data structure, filled with Walker objects.  This is quite inefficient.  
Talk to somebody in the group about using a numpy array structure to make your implementation more efficient.
However, this makes it ultra clear as to what we are doing.  Each walker has a coordinate and a potential
```python
class Walker:
    def __init__(self):
        self.coords = np.zeros((numAtoms,dimensions)) #1d surface
        self.WalkerV = 0.0
```

###The Overall Algorithm
We can write our algorithm as a loop over n time steps.  At the end of the n time steps, the simulation is over!
For now, ignore the if statement that asks if we're > 950 time steps. We'll get there in a bit.
```python
#Start!
vrefAr = np.zeros(1000)
xc = []
popAr = np.zeros(1000)
Vref = 10000
DW = False
for i in range(1000):
    moveRandomly()
    getPotentialForWalkers()
    if i==0:
        Vref = getVref()
    if i>=950:
        DW = True
        if i==950:
            whoFrom = np.arange(len(myWalkers))
            oneHundo = copy.deepcopy(myWalkers)
    whoFrom = birthOrDeath(Vref,whoFrom,DW)
    getPotentialForWalkers()
    Vref = getVref()
    #Plotting business
    vrefAr[i] = Vref
    popAr[i] = len(myWalkers)

```
As you can see, this is a pretty simple algorithm. The main thing that may be confusion right now is Vref.
We can calculate the average potential of our ensemble, and correct it with the fluctuation in the population to eventually
get our zero point energy.  This is what we refer to as Vref in the simulation.  In my implementation, I set Vref really high 
to start, but we will calculate vref in the first time step so it doesn't really matter.

Algorithmically, we run the simulation for 1000 time steps. During that time, we displace, we evaluate energy, we see 
if walkers should die or replicate, and then we recalculate vref.  

Throughout the simulation, we collect Vref at every time step, the average of which will be our zero point energy.  
We can collect the population so that we can make sure we don't have a massive walker die off, which kills the simulation.


### moveRandomly()

![dmcBirthDead](img/Anderson.png) 	

```python
def dvr_ke(grid, m=1, hb=1):
	'''Computes the kinetic energy for the grid (based on the chosen basis)'''
	import numpy as np
	
	dx=grid[1]-grid[0]
	divs=len(grid)
	ke=np.empty((divs, divs))

	coeff=(hb**2)/(2*m*(dx**2))

	for i in range(divs):
		for j in range(divs):
			if i==j:
				ke[i, j]=(-1**(i-j))*coeff*(math.pi**2)/3
			else:
				ke[i, j]=(-1**(i-j))*coeff*(2)/((i-j)**2)

	return ke
```

### Potential Energy

The potential is simple as is usually the case, so if we have a potential function as a function of the grid point,  ```pot```  we can write this as

```python
def dvr_pe(grid, pot=None):
	'''Computes the potential energy from the gridpoints'''
	import numpy as np
	
	return np.diag([pot(x) for x in grid])
```

### Wavefunctions

This will also operate in the usual way, so we have 

```python
def dvr_wfns(ke, pe):
	'''Computes the wavefunctions'''
	import numpy as np
	
	return np.linalg.eig(ke+pe)
```

<a id="all-together" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

## All Together

```python
'''Colbert and Miller DVR on the [-inf, inf] domain'''

def dvr_grid(domain=(-5, 5), divs=10, **kw):
    '''Calculates the grid'''
    rmin=domain[0]; rmax=domain[1];
    inc=(rmax-rmin)/(divs-1)

    return [rmin+i*inc for i in range(divs)]
    
 def dvr_ke(grid, m=1, hb=1, **kw):
	'''Computes the kinetic energy for the grid (based on the chosen basis)'''
	import numpy as np
	
	dx=grid[1]-grid[0]
	divs=len(grid)
	ke=np.empty((divs, divs))

	coeff=(hb**2)/(2*m*(dx**2))

	for i in range(divs):
		for j in range(divs):
			if i==j:
				ke[i, j]=(-1**(i-j))*coeff*(math.pi**2)/3
			else:
				ke[i, j]=(-1**(i-j))*coeff*(2)/((i-j)**2)

	return ke


def dvr_pe(grid, pot=None, **kw):
	'''Computes the potential energy from the gridpoints'''
	import numpy as np
	
	return np.diag([pot(x) for x in grid])
	
def dvr_wfns(ke, pe, **kw):
	'''Computes the wavefunctions'''
	import numpy as np
	
	return np.linalg.eig(ke+pe)
	
def dvr_run(**params):
	'''Runs the entire DVR'''
	grid = dvr_grid(**params)
	ke = dvr_ke(grid, **params)
	pe = dvr_pe(grid, **params)
	wfns = dvr_wfns(ke, pe, **params)
	
	return wfns
	
	
if __name__=='__main__':
	### parse sys.argv
	
	dvr_run(**ops)
```