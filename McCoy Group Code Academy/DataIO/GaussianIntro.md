# Gaussian, an Intro

[Gaussian](https://gaussian.com/) is a software package for doing electronic structure calculations. 
There are [many electronic structure packages](https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software) out there, many of them free & open source, but we tend to use Gaussian.
Whether that's the best set up is unclear, but Gaussian has a few benefits. 
It's relatively fast, maybe faster than other stuff like [Psi4](http://www.psicode.org/) probably not faster than [NWChem](https://nwchemgit.github.io/) (we'll never know because [Gaussian bans people](https://www.nature.com/articles/429231a#:~:text=Thousands%20of%20site%20licences%20for,replicates%20parts%20of%20Gaussian's%20functionality.) [who do timing tests](http://www.chemistry-blog.com/2012/05/09/gaussians-banhammer/)). 
It's widely used, and so there's a lot of experience in the community on how to use it.
_Most importantly for us, though, we've already got it installed and the group has been using it for years._

### Using Gaussian

What does actually using it look like? Well the first thing we need to do is make a [Gaussian job file (`.gjf`)](http://gaussian.com/input/).
This is a file with a structure like (`!` indicates a comment in a `.gjf`)

```lang-none
! Memory / Storage Settings
%Chk=... ! This specifies the location for checkpointing data. You should always include this so you can use the data later.
%Mem=... ! This specified how much memory Gaussian can use. Give it the maximum you can, since that'll speed things up.
...
! Job Settings
#P
#Opt=(Z-Matrix)
#Density=Current
#MP2/aug-cc-pVTZ
...

! Brief job description
This is my optimization calculation for something (it's good to include this so your future self knows what went on)

! Molecule specification (http://gaussian.com/molspec/) we suggest using the Z-matrix format
...
```

The full list of memory/storage settings is [here](https://gaussian.com/link0/), the different job types are [here](https://gaussian.com/capabilities/) & settings approrpriate for those are listed (e.g. here are the ones for [Opt jobs](https://gaussian.com/opt/)). Gaussian explains its Z-matrix layout [here](http://gaussian.com/zmat/).

Gaussian also has some info on [running jobs](http://gaussian.com/running/), which goes into this in more detail.

**Note**: Whenever you set up a Gaussian job, make sure to both include the command `#P`, which makes it so all relevant info (crucially dipoles) are printed & use the setting `#Density=Current`, which causes Gaussian to do things like dipole calculations with the same level of accuracy as it does the energy calculations
{: .alert .alert-danger}

### Running Gaussian

Running Gaussian on the group computers and hyak is something that we've discussed briefly [on the group StackOverflow](https://stackoverflow.com/c/mccoygroup/questions/21), so give that a look and let us know if you've got lingering questions.

<span class="text-muted">Next:</span>
 [Getting Data out of Gaussian](GaussianParsing.md)<br/>
<span class="text-muted">Previous:</span>
 [NumPy Data Files](NumpyFiles.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/GaussianIntro.md)
