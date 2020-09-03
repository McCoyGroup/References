# An Introduction to Python

Python is a _programming language_, which is to say, it's a way to write down instructions for computers to do things so we don't have to.
There are tons of programming languages out there and as you get more and more comfortable with programming, you'll undoubtedly find yourself working with more than one of them.
The fact that there are so many languages out there also means that we should probably justify why we opt to use python over any of the other choices, and there are a few big reasons:
1. Python is nice: It works hard to hide unnecessary details about how computers work (people often say it's a _high-level language_)
2. Python is flexible: It's not the fastest language, but it can do just about anything. As scientists, we generally need flexibility more than speed.
3. Python is popular: As opposed to something like [Mathematica](https://www.wolfram.com/language/elementary-introduction/2nd-ed/01-starting-out-elementary-arithmetic.html), another nice, flexible language, Python has a huge user base. This means most Python questions can be resolved just with a bit of googling.

**Note:** If you start googling around, one of the first things you'll figure out about python is that there are two main versions of it. There's Python 2, which first came out in 2000, and python3 which came out in 2008.
Migration to Python 3 has been [incredibly slow](https://stackoverflow.blog/2019/11/14/why-is-the-migration-to-python-3-taking-so-long/), so you'll probably see stuff talking about Python 2 when you try to look stuff up on the internet.
Despite that, we really want to be using Python 3. The features are worth it, and Python 2 is no longer formally supported.
{: .alert .alert-danger}

## What is Anaconda?

Unlike a regular application, e.g. Slack, lots of different organizations have their own _distributions_ of Python which all have slightly different use cases.
For the most part, we're agnostic as to what distribution you use, but if you're just getting started, we'll recommend [Anaconda](https://www.anaconda.com/products/individual).

Anaconda is a distribution of Python that comes with various scientific computing packages ([NumPy](https://numpy.org/) / [SciPy](https://www.scipy.org/) / [matplotlib](https://matplotlib.org/)/etc.) ) preinstalled.
It also provides extra tools, like its own installer/package manager ([`conda`](https://docs.conda.io/en/latest/)).
As a group, we have moved over to using Anaconda on the group computers. All the supercomputers we use ([Hyak/Mox](https://wiki.cac.washington.edu/display/hyakusers/Hyak+mox+Overview) & [NeRSC](https://www.nersc.gov/)) have Anaconda installed or available as well.

### Using Anaconda on the Group Computers

If you are working on one of the group computers, they all already have anaconda3 installed on them.
The first time you use Anaconda on one of the computers, you'll need to do a bit of set up work.
Every other time it should "just work".

To start, you'll need to [`ssh`](https://stackoverflow.com/c/mccoygroup/questions/11) onto one of the group computers.
Once you've got that working, run

```console
$ conda -V
```

if Anaconda has been set up, you should get something like

```console
$ conda -V
conda 4.8.3
```

if not we'll need to set things up.

<div class="accordion mb-2">
<div class="card">
 <div class="card card-header" markdown="1">
 **Short version**: _(for people who know how to edit files via the command line)_
 <a class="float-right" data-toggle="collapse" href="#anaconda-short-version"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="card card-body collapse" id="anaconda-short-version" markdown="1">
Add the following to your `~/.bashrc` file

```lang-none
export PATH=/opt/anaconda3/bin:$PATH
````

Now, exit and log in again.
 </div>
</div>

<div class="card">
 <div class="card card-header" markdown="1">
**Long version**: _(for people who don't know how to edit files via the command line)_
 <a class="float-right" data-toggle="collapse" href="#anaconda-long-version"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="card card-body collapse show" id="anaconda-long-version" markdown="1">

Here are some steps to do the same with a text editing software called [`emacs`](https://www.gnu.org/software/emacs/).

Log on to one of the group computers. If you don't know how, [this](https://stackoverflow.com/c/mccoygroup/questions/11) will help you out.

When you do, you should see something that looks like

```console
[yourusername@thecomputer ~]$
```

Once you have this, we'll use `emacs` to edit the `.bashrc` file in our home directory, by doing

```console
[yourusername@thecomputer some_folder] emacs -nw ~/.bashrc$
```

You will open up the file at that point.
Use the arrow keys to go to the bottom of the file, and add the line

```lang-none
export PATH=/opt/anaconda3/bin:$PATH
````

Once you do this, hit `Ctrl+x` and then `Ctrl+c` and then type `y`.
This will save the changes you made and exit the emacs software.
When you log off and log back in, Anaconda should be ready to go.

*If this doesn't work for some reason, consult our shared drive ComputerSOP documentation or a senior member of the group.*
 </div>
</div>
</div>

### Installing Anaconda3 on your laptop or desktop at home

Go to the [Anaconda downloads page](https://www.anaconda.com/products/individual#Downloads) and download the appropriate installer. Almost certainly, you'll want the **64-bit Graphical Installer**.
Follow the installer's instructions and recommended installation instructions.
You may be asked if you want to download `PyCharm` along the way, which is the group's recommended Integrated Development Environment (IDE) for coding and debugging in Python.

If you have a Mac, you can add 

```shell
export PATH=/opt/anaconda3/bin:$PATH
```

to your `~/.bashrc` as shown above to use anaconda on the command line when you type `python`.

If you have a PC, you can use the `Anaconda Powershell` to access anaconda on the command line, or you can download [Windows Susbsystem for Linux](https://lifehacker.com/how-to-get-started-with-the-windows-subsystem-for-linux-1828952698) and do the Mac-like installation of it in your subsystem.



### Installing Python 3

If for some reason you prefer to use the standard distribution Python over the Anaconda one (this is discouraged), that works too.
To do this, go to the [Python Organization downloads page](https://www.python.org/downloads/) and download whichever version they're saying is the latest (as of writing this that's currently 3.8).
That should download an installer and we'll just do what the python.org people tell us to do to get it installed.


<span class="text-muted">Next:</span>
 [What is an IDE?](IntroToIDEs.md)<br/>
<span class="text-muted">Previous:</span>
 [Getting Started](index.md)
 
 Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/IntroToPython.md)
