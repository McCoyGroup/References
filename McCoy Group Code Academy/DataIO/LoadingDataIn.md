# Getting Data in to Your Code

We've already talked a bit about the power of good data formatting. It makes everyone's life better.
We think it'd be good to get a bit more concrete about what that means for us, though. 
We also know that you're not always going to have clean data to work with, and being able to deal with the mess is a useful skill.

But let's start with the first one.

## Clean Data

[If you can use the built in NumPy formats, do so.](NumpyFiles.md)

Otherwise, we argued that you should "just use JSON" when working with your data.
Let's take a look at what that kind of thing can mean.
[JSON](https://en.wikipedia.org/wiki/JSON) is a nice format. It's designed to transmit data on the web.
And it looks almost exactly like a python dictionary. Here's how we could store results from a simulation

```json
{
  "simulation_name": "My Simulation",
  "simulator_version": "0.0.1",
  "timings": {
    "seconds_elapsed": 1000,
    "time_step": 0.1,
    "total_steps": 10000000
    },
  "energies":  [0.0, 1.2, -1.2, 1.2, 0.5, 2.8, ...]
}
```

The python [`json` module](https://docs.python.org/3/library/json.html) can load this in easily. You can extend it to add units, coordinates, etc. 
It's not the world's most efficient format, but we also don't work with all that much data. If we need a speed boost, there's a hybrid JSON/data table format that we'll talk about in the next section.

The one thing we'll want to make sure of is that when we load in our data we convert that `"energies"` array to a proper NumPy array so we can work with it more easily.

## Dirty Data

Unfortunately, not all data is clean. Many people started writing code in 1980, when [Fortran's 80 character line length](https://softwareengineering.stackexchange.com/a/148729) was hip & cool. 
Many people also got with the times and adapted to improvements in computation that make everyone's lives better.
Many scientists did not.
And particularly Gaussian, the electronic structure software makers, did not.

So unfortunately we're still stuck with many, many situations where our data looks like

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

and in fact, we're likely to have this type of block repeated many times over a file.

So what do we do with data like this? Well one option is to use copy everything out by hand. 
If you've got thousands of calculations, I'm gonna say that's a no go.

Instead, unfortunately, we're gonna be stuck doing what's called [_parsing_](https://en.wikipedia.org/wiki/Parsing) 
(etym.: from the French _parser_ or _"to weep tears of frustration").
Parsing is a very, very broad topic and there are tons of ways to do it.
We're gonna briefly hit on two of the big ones in python
1. File searching
2. String splitting

The first of these isn't so terrible, although this will get a little bit technical. 
(Don't worry if you don't follow totally, _most_ of the parsers you'll need have already been written and you just need to know how to extend them)
We'll assume that block (and many others like it) is inside a file called `my_amazing_calc.log`. 
Let's also say we want to get that the line with dipole moment from it.
If we could take the subsection of the string between the line

```lang-none
 Dipole moment (field-independent basis, Debye):
```

and 

```lang-none
 Quadrupole moment (field-independent basis, Debye-Ang):
```

we'd be most of the way there. So how would we do it?
Well first we need to know how to search a file in python. 
We're going to work off the assumption that the file is very big and we don't want to make python read it all at once.
And so the way we do this is by using the `.find` method on a python [memory-mapped file](https://docs.python.org/3/library/mmap.html). 
(I told you this would get technical)
Basically this allows us to pretend a file is a string.
Once we've found the our opening block, we track where in the file that was (using `.tell`), and then look for the closing tag.
Once we've got both of those, we can read what was between them.

We'll wrap this up in a little `class` to make it easier to manage

```python
import mmap
class FileSearcher:
    """
    Represents a file from which we'll stream blocks of data by finding tags and parsing what's between them
    """
    def __init__(self, file, encoding="utf-8"):
        self.file = file
        self.encoding = encoding # files all have encodings, usually the data is utf-8 or ASCII (the two are intercompatible)
    def __enter__(self): # allows us to use the `with` keyword
        self.fstream = open(self.file, mode='rb')
        self.stream = mmap.mmap(self.fstream.fileno(), 0)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # allows us to use the `with` keyword
        self.stream.close()
        self.fstream.close()
    def read_block(self, opening, closing):
        """reads the block between `opening` and `closing`"""
        open_tag = opening.encode(self.encoding) # we need to encode our tag the same way we 
        open_pos = self.stream.find(open_tag)
        new_pos = open_pos + len(open_tag)
        self.stream.seek(new_pos) # move to the end of the tag and search from there
        close_tag = closing.encode(self.encoding)
        close_pos = self.stream.find(close_tag)
        # read between the positions, then move to the end of the tag
        block = self.stream.read(new_pos - close_pos)
        new_pos = close_pos + len(close_tag)
        self.stream.seek(new_pos)
        return block.decode(self.encoding)
```

which we can then use like

```python
with FileSearcher('my_amazing_calc.log') as file:
    block = file.read_block(
        "Dipole moment (field-independent basis, Debye):",
        "Quadrupole moment (field-independent basis, Debye-Ang):"
        )
```

which will give us the string

```python
"""
    X=              0.8917    Y=             -0.4708    Z=              1.6277  Tot=              1.9147
 """
```

If we want to be safe about things, e.g. if the strings we're looking for _aren't_ in the file, we'll need to add a number of safety checks.
If you want to see what that looks like, we have an example [here](https://github.com/McCoyGroup/McUtils/blob/11d4605afd21f64241d638e21a8e760e8b58939d/Parsers/FileStreamer.py#L33).

Our block reader is also set up so that we can get multiple strings out just by using the same `read_block` multiple times withing the same `with` block.

At this point, we get to do some nice string manipulation to get the actual dipole moment out. 
The way we'll do this is by splitting the string every time we see `=`. Python strings are very kind and support a `.split` method to make this easy.

So we'd do

```python
dip_block = """
    X=              0.8917    Y=             -0.4708    Z=              1.6277  Tot=              1.9147
 """
dip_chunks = dip_block.split("=")
```

now `dip_chunks` will look like

```python
["""
    X""", "              0.8917    Y", "             -0.4708    Z", "              1.6277  Tot", """              1.9147
 """]
```

and we'll note first that we only want the middle three of these and second that for each of these we can then split on the whitespace and pick the _second_ component. So to get out the real dipole components we'd do

```python
real_dip_chunks = [chunk.split("=")[1] for chunk in dip_chunks[1:-2]]
```

and finally to get our dipole moment we use the python `float` function to convert these to python numbers like

```python
dip_mom = [float(num) for num in real_dip_chunks]
```

Now imagine you want a different property from that log file. You get to figure this process out all over again for that one. And for the next. And the next.

Hopefully this makes it clear why we've got such a preference for _clean_ data formats. 

Just remember, _if you can't use NumPy, just use JSON_. 

### A Note on Regular Expressions

Python has support for [regular expressions](https://docs.python.org/3/library/re.html) (or regex). These are incredibly powerful and basically are a pattern language for strings. We wrote up a little regular expression builder so that if you the string from above 

```python
"""
    X=              0.8917    Y=             -0.4708    Z=              1.6277  Tot=              1.9147
 """
```

you can write out it out as a regular expression like

```python
RegexPattern((
    "X=", Whitespace, Capturing(Number), Whitespace,
    "Y=", Whitespace, Capturing(Number), Whitespace,
    "Z=", Whitespace, Capturing(Number)
))
```

which will convert to the rather less-readable regular expression

```python
"X=\\s+(\\d+)\\s+Y=\\s+(\\d+)\\s+Z=\\s+(\\d+)"
```

and allow you to get the three numbers out. If you'd like to learn more, we're happy to share.

<span class="text-muted">Next:</span>
 [Getting Data out of your Program](ExportingDataOut.md)<br/>
<span class="text-muted">Previous:</span>
 [Data Formats](DataFormats.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/LoadingDataIn.md)