# An Introduction to Python

Why learn Python? ...

**A quick aside:** If you start googling around, one of the first things you'll figure out about python is that there are two main versions of it. There's python2, which first came out in 2000, and python3 which came out in 2008.
Migration to python3 has been [incredibly slow](https://stackoverflow.blog/2019/11/14/why-is-the-migration-to-python-3-taking-so-long/), so you'll probably see stuff talking about python2 when you try to look stuff up on the internet.
Despite that, we really want to be using python3. The features are worth it, and python2 is no longer supported.

## What is Anaconda?

Anaconda is a distribution of Python (either 2 or 3) that contains various scientific computing packages (NumPy/SciPy/matplotlib/etc.).  It also provides a package installer/deployer/manager (conda) so that programmers can install python packages, as well as deploy their own in a convient fashion.  As a group, we have moved over to using Anaconda on the group computers. All the supercomputers we use (Mox, NERSC) have anaconda installed or available as well.  The benefit of using Anaconda vs. just downloading pure python is that it is provides a standard across the group and beyond, rather than manually downloading all the packages required yourself.

## How do I download them?
If you already have Anaconda from using jupyter or something of the sort, you are off to a good start.

### Using Preinstalled Anaconda3 on the group computers

If you are using the group computers, they all have anaconda3 installed on them!!+ 

SSH onto a group computer, then:

**Short version (for people who know how to edit files over SSH):**

Add:
`export PATH=/opt/anaconda3/bin:$PATH`
at the end of your ~/.bashrc file and  then restart the terminal.

Now, exit the terminal and start up a new one.  Now, when you type 
`[rjdiri@argon ~]$ which python`
You should get the output
	/opt/anaconda3/bin/python

**Long version (for people who don't know how to edit files over SSH):**

Here are some steps to do it with something called emacs, a text editing software.
Log on, you should see something that looks like:
`[rjdiri@argon ~]$`
Make sure you are in the home directory, which is designated by the ~. If you are not in the home directory, type:
`[rjdiri@argon someFolder]$ cd`
And press enter:
`[rjdiri@argon ~]$ `
Once you have this, you should type 
`[rjdiri@argon ~]$ emacs -nw .bashrc`
And press enter.  You will open up the file at that point.  Use the arrow keys to go to the bottom of the file, and then type
`export PATH=/opt/anaconda3/bin:$PATH`
Once you do this, hit `ctrl+x` and then `ctrl+c` and then type `y`.  This will save the changes you made and exit the emacs software.
Now, exit the terminal (`ctrl+d`) and start up a new one.  Now, when you type 
`[rjdiri@argon ~]$ which python`
You should get the output
	/opt/anaconda3/bin/python


+*If they don't for some reason, consult our shared drive ComputerSOP documentation or a senior member of the group.*

### Installing Anaconda3 on your laptop or desktop at home

Navigate to the [Anaconda downloads page ](https://www.anaconda.com/products/individual) and download the system-specific installer (9 times out of 10 you need the 64-bit installer instead of 32-bit, and download the Graphical Installer one rather than command line). Follow the installer's instructions and recommended installation instructions. You may be asked if you want to download pycharm along the way, which is the group's recommended Integrated Development Environment (IDE) for coding and debugging in Python.

**Windows**
Once you have installed Anaconda, you will be given a suite of tools at your disposal.  The  anaconda powershell is a good one, where you can use linux-style commands (`cd`, `ls`, etc.) and then run your anaconda python installation with `python file.py`, or entering an interactive python session by simply typing `python`.

**Mac**
Need help here, y'all.

**Linux**
If you have a Linux laptop or desktop at home, talk to Ryan about how to install and we will go through it together.


### Installing Python 3 (not recommended)

First we'll go to the [Python Organization downloads page](https://www.python.org/downloads/) and download whichever version they're saying is the latest (as of writing this that's currently 3.8).
That should download an installer and we'll just do what the python.org people tell us to do to get it installed.



<span class="text-muted">Next:</span>
 [What is an IDE?](IntroToIDEs.md)<br/>
<span class="text-muted">Previous:</span>
 [Getting Started](index.md)
 
 Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/IntroToPython.md)
