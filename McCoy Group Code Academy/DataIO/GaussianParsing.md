# Getting Data out of Gaussian

[As we noted earlier](DataFormats.md), some data formats are better than others.
Gaussian, unfortunately, picks one of the worst possible ones for some of its data, and a workable, if clunky, one for the rest.

Let's start with the workable one. 

#### `.chk` and `.fchk` files
If you recall from the [previous section](GaussianIntro.md), when you made your `.gjf` file you set an option called `%Chk` to indicate where to store the check-pointing data.
This file is in a totally inscrutable binary format, basically a dump of Gaussian's internals as it goes.
On the other hand, bundled with Gaussian is a program called [formcheck](https://gaussian.com/formchk/) that we call like

```lang-none
formchk checkpoint_file.chk formatted_file.fchk
```

and which takes the inscrutable binary data and gives a file that looks something looking like

```lang-none
title                                                                   
Freq      UB2PLYPD3-FC                                                CC-pVTZ             
Number of atoms                            I               15
Info1-9                                    I   N=           9
          66          64        1002           0           0         100
           6           2        6001
Full Title                                 C   N=           1
title       
Route                                      C   N=           5
#p b2plypd3/cc-pvtz integral=...
Nuclear charges                            R   N=          15
  6.00000000E+00  6.00000000E+00  1.00000000E+00  1.00000000E+00  8.00000000E+00
  8.00000000E+00  1.00000000E+00  6.00000000E+00  1.00000000E+00  1.00000000E+00
  1.00000000E+00  6.00000000E+00  1.00000000E+00  1.00000000E+00  1.00000000E+00
Current cartesian coordinates              R   N=          45
  7.04878179E-01  8.24102648E-03  1.33661317E-01  4.64699369E-01 -4.61527005E-01
  2.89747925E+00  ...
Number of symbols in /Mol/                 I                0
Force Field                                I                0
Atom Types                                 C   N=          15
                                                            
                                                            
                                                            
Int Atom Types                             I   N=          15
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0
MM charges                                 R   N=          15
  0.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00
```

where we can see that there are successive named blocks of numbers, some cryptic `I`/`R`/`C` labels, etc.

At the very least, we can write a single class that will parse all of this data, since it's all got a well-defined, regular structure.

This is very helpful, but unfortunately, being a check-point, is only a snapshot of a calculation. 

#### The `.log` File

Usually we need a full potential energy surface, or dipole surface, or the like, which brings us to the much dirtier `.log` file.
As Gaussian runs, it prints all sorts of info out to the `.log` file. Some of it we find very useful, e.g. dipole moments, electronic energies, coordinates, and the like. Some of it, like orbital populations, isn't all that useful.

If there were regularity to the way the data were stored, we could deal. Unfortunately we get stuff out like

```lang-none
Mulliken charges and spin densities with hydrogens summed into heavy atoms:
               1          2
     1  C    0.284937  -0.047805
     2  C   -0.084087   0.975289
     5  O   -0.198441   0.044417
     6  O   -0.009235   0.004233
     8  C    0.009751   0.022752
    12  C   -0.002925   0.001113
 Electronic spatial extent (au):  <R**2>=            586.1312
 Charge=              0.0000 electrons
 Dipole moment (field-independent basis, Debye):
    X=              0.8917    Y=             -0.4708    Z=              1.6277  Tot=              1.9147
 Quadrupole moment (field-independent basis, Debye-Ang):
   XX=            -37.2983   YY=            -36.8835   ZZ=            -38.3391
   XY=              2.0489   XZ=             -3.3046   YZ=             -1.1258
 Traceless Quadrupole moment (field-independent basis, Debye-Ang):
   XX=              0.2087   YY=              0.6235   ZZ=             -0.8321
   XY=              2.0489   XZ=             -3.3046   YZ=             -1.1258
 Octapole moment (field-independent basis, Debye-Ang**2):
  XXX=            -16.5453  YYY=             -5.3136  ZZZ=             -3.4279  XYY=             -5.5706
  XXY=             -6.4237  XXZ=              3.4940  XZZ=             -3.5574  YZZ=              0.7124
  YYZ=              0.6046  XYZ=              1.7525
 Hexadecapole moment (field-independent basis, Debye-Ang**3):
 XXXX=           -335.5914 YYYY=           -215.5172 ZZZZ=           -195.0758 XXXY=             20.4569
 XXXZ=             -9.7915 YYYX=              1.7567 YYYZ=             -1.2146 ZZZX=             -2.3024
 ZZZY=              1.8767 XXYY=            -89.8989 XXZZ=            -95.5782 YYZZ=            -67.4313
 XXYZ=             -0.8395 YYXZ=             -0.0618 ZZXY=              1.2617
 N-N= 2.598308771361D+02 E-N=-1.240434554405D+03  KE= 3.068245376935D+02
  Exact polarizability:  62.069  -0.830  55.437  -2.686  -0.888  55.152
 Approx polarizability:  66.871  -1.448  60.217  -2.414   0.418  61.197
                          Isotropic Fermi Contact Couplings
        Atom                 a.u.       MegaHertz       Gauss      10(-4) cm-1
     1  C(13)             -0.01947     -21.88400      -7.80875      -7.29972
     2  C(13)              0.04515      50.75819      18.11179      16.93111
     3  H(1)              -0.01412     -63.09256     -22.51300     -21.04541
     4  H(1)              -0.01377     -61.55167     -21.96317     -20.53143
     5  O(17)              0.03457     -20.95714      -7.47803      -6.99055
     6  O(17)              0.00489      -2.96727      -1.05880      -0.98978
     7  H(1)              -0.00009      -0.40514      -0.14456      -0.13514
     8  C(13)              0.02456      27.61551       9.85390       9.21154
     9  H(1)               0.00363      16.22441       5.78927       5.41188
    10  H(1)              -0.00047      -2.09733      -0.74838      -0.69960
    11  H(1)               0.00051       2.25983       0.80636       0.75380
    12  C(13)             -0.00035      -0.39272      -0.14013      -0.13100
    13  H(1)              -0.00015      -0.65043      -0.23209      -0.21696
    14  H(1)               0.00070       3.11829       1.11269       1.04015
    15  H(1)              -0.00019      -0.85732      -0.30591      -0.28597
```

which [as we noted before](LoadingDataIn.md#dirty-data) is a pain to parse.

### `McUtils.GaussianInterface`

Over the past ~2 years we've been slowly working on a package to make parsing these things nicer. 
It's part of a larger package of McCoy group utilities called [McUtils](https://github.com/McCoyGroup/McUtils).
We're working on [usage and documentation](../../Documentation/McUtils.GaussianInterface.md), but it allows you to pull dipole moments, energies, coordinates, optimization parameters, etc. from these files (it supports both `.fchk` and `.log` files) and is built so that it can be easily extended.
Let us know if you'd like to check it out and we'll be happy to help.

<span class="text-muted">Previous:</span>
 [Gaussian, an Intro](GaussianIntro.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/GaussianIntro.md)
