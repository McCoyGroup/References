# Data Formats

Data, like grad students, comes in all different shapes and sizes. And like grad students, some data formats are [organized and effective](https://github.com/rjdirisio), some are [disorganized and effective](https://github.com/vgl2), and some are [me](../img/trash.png).

We're gonna try to stick to using the organized and effective ones. Figuring out what's organized is actually a bit subtle, though. 
Let's imagine we're using the results of someone else's simulation and they give us a results file like this:

```lang-none
Parameters:
----------
parameter: Seattle, WA
parameter: Distance 2.5 miles
parameter: Name dog_count Value 4 dogs Description how many dogs I expect to see on my walk

Log Steps:
 Step-1: nope
 Step-2: no
 Step-3: still no
 Step-4: Yes!
 Step-5: no...

Results:
-------
One dog was seen today
```

This certainly _looks_ organized and as a human I can make sense of it. But if you try to work with this in your code, you're bound for frustration, because there's no consistency in the data. Let's count just a small number of the ways this will be a pain

1. The `Parameters:` and `Results:` blocks header are delimited by a line of `-`, the `Log Steps:` block has no delimiter
2. The `Results:` block and `Parameters:` blocks are delimited by different numbers of `-`, but the `Log Steps` lines _also_ use `-`
3. Numerical values (e.g. `2.5`, `4`) and string values (e.g. `how many dogs I expect to see on my walk`) are mixed freely
4. The parameters in the `Parameters` blocks don't follow a standard format
5. `no` is mixed with `nope` and `still no` and other variants, even though they all mean the same thing
6. `One` is used instead of `1`

This is obviously a somewhat contrived example, but this kind of thing, using natural human language in outputs, is incredibly common in science. 
A very common example in our work is the `.log` file that comes out of the Gaussian electronic structure program. 
A lot of very important data is in that file. 
Unfortunately it's written out in such a way as to make ingesting it in code a huge pain, since they focused on making it human readable, at the expense of computational convenience.

## Focus on Machine Readable

Humans have incredibly flexible, powerful brains. Computers do not. Therefore, when we give data to our collaborators or share it within the group, we always want to focus on making it easy for the _computer_ to read. The humans can figure it out.

As an example, let's look at the simplest file format we tend to work with, the [`.xyz` molecule format](https://en.wikipedia.org/wiki/XYZ_file_format). Here's how you might input the structure of pyridine

```lang-none
11
pyridine molecular structure
C       -0.180226841      0.360945118     -1.120304970
C       -0.180226841      1.559292118     -0.407860970
C       -0.180226841      1.503191118      0.986935030
N       -0.180226841      0.360945118      1.29018350
C       -0.180226841     -0.781300882      0.986935030
C       -0.180226841     -0.837401882     -0.407860970
H       -0.180226841      0.360945118     -2.206546970
H       -0.180226841      2.517950118     -0.917077970
H       -0.180226841      2.421289118      1.572099030
H       -0.180226841     -1.699398882      1.572099030
H       -0.180226841     -1.796059882     -0.917077970
```

That first line tells you how many atoms you have. The second is a general-purpose comment line. The rest is the list of atoms and their coordinates. We can make sense of it as humans. 
Computers can read this very easily. And given that if we're looking at molecular structures, we probably want to [visualize them](https://en.wikipedia.org/wiki/List_of_molecular_graphics_systems), it matters more that the computer can easily read it than we can, since that means the computer can plot it for us.

Find an exercise in reading and writing your own `.xyz` files [here](https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/Exercises/) 

### Binary vs. Text Formats

We can go even further with this, though. Computers, since they work in binary (`1`/`0`), don't store their data in words. 
Instead, they store it as long strings of numbers. 
That means if we want to maximize computer readability, we can just have our program dump out its internal representation of our data to a file. 
Then if we want to get that data back into a new program at a later time, the computer can just load it directly in without us having to tell it anything about the file format.
This is super powerful and super convenient (and NumPy supports this through [`.npy` and `.npz` files](NumpyFiles.md)).
People call this kind of format a _binary format_ and you should use them when you can. Unfortunately there is no universal binary format, so if you go between programming languages you'll need to transfer your data in a _text format_, i.e. a format that humans can read, even if it's hard to make sense of.

## Standard File Formats / JSON

There are a bajillion chemical file formats out there, e.g. `.xyz`, `.mol`, `.mol2`, `.sdf`, `.cif`, `.pdb`, etc. 
We'd like to say that they all have different use cases they're designed for, but the fact is that most of them just exist because people like to invent their own format for their project.
If you can't use a `.npz` file, we're going to advise you _not_ to do that and instead either use a standard chemical format _or_ (better) just use JSON.

JSON allows you to store any set of strings, numbers, etc. and is compact, easy for computers to read, and most importantly is supported naturally by pretty much every programming in existence today.
It's easy. Python can export it. Anyone can use it. Do we need to say anything more?

### A Note on HDF5

In the high-performance computing world, the [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) format has gained widespread popularity. Just like JSON it allows you to store pretty much any type of data with any set of keys, and even better it's a binary format. 

The only reason we don't recommend it over JSON is that at the time of writing this it has a smaller footprint and is less-well integrated into the modern programming languages. 
If you want to use it, we're all for that, just keep in mind that the people you're sharing with will need to install the libraries to use it, too.

## The Benefits of Standardization

We're all for standards. They make programming easier, allow better reuse of code, better extension of code, and are generally helpful when you're a grad student and strapped for time.
Unfortunately, most scientific programming is done by people who aren't particular experienced programmers, and so they have yet to come around to this truth.
We can't fix that. 
We can't fix the fact that potential energy surfaces have absolutely no standardization in their interfaces. 
We can't fix the fact that there is no standard way to do distributed linear algebra on HPCs.
We _can_ however fix the fact that inside the group we don't share our data in a standardized way. 

This is particularly relevant in three places:
1. Naming and storage of simulation parameters
2. Naming and storage of wave functions
3. Naming and storage of molecular structure data

At this point in time, we don't have a perfect solution for this, so if you, dear reader, would like to suggest some standards, we'd be happy to hear them.
We'd also encourage you to reach out and see what other people do before you make a new standard on your own.

<span class="text-muted">Next:</span>
 [Getting Data into your Program](LoadingDataIn.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/DataFormats.md)
