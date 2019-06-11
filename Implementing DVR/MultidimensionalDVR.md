<a id="multidimensionaldvr" class="Section" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

# Multidimensional DVR

Assuming one has a separable kinetic energy, DVR in n dimensions is a simple tensor extension of a 1D DVR. We'll reuse the Colbert and Miller kinetic energy and build the potential as usual.

<a id="grid" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

###Grid

We discretize as before, but use NumPy functions for do this more efficiently

<a id="kineticenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

###Kinetic Energy

The kinetic energy is constant along bands, so we can use this property to fill out our matrix more quickly.

<a id="potentialenergy" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

###Potential Energy

Here, we'll assume  `pot` has been written in order to take advantage of NumPy's vectorized operations and hence should be called with our entire grid fed in.

<a id="wavefunctions" class="Subsubsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

###Wavefunctions

This already used NumPy so we won't change anything here.

<a id="alltogether" class="Subsection" style="width:0;height:0;margin:0;padding:0;">&zwnj;</a>

## All Together