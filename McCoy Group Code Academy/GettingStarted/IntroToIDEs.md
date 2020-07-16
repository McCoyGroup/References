# What is an IDE?

insightful comments.

JetBrains has made a truly great python IDE called [PyCharm](https://www.jetbrains.com/pycharm/).
There's a free community version and also a paid professional version. As someone with a `@uw.edu` email, you can use the pro version for free.

## Why is it useful?

PyCharm is a great tool mainly to make your life easier by catching syntax bugs, auto-completing (code as well as documentation), and providing a really robust debugging suite. Many IDEs do this, but we as a group have converged around PyCharm as convention, mainly because it's relatively easy to set up and use.

## How do I install PyCharm?

**Usage on the group computers**

If you want to use it on the group computers, Argon and Neon currently have the "JetBrains ToolBox" installed on them. Navigate to /opt/jetbrains-toolbox.../ and then run `./jetbrains-toolbox`. This should pop up a graphical interface where you can download PyCharm Community or Professional (As mentioned before, Pro requires a .edu address, The group doesn't use the extra features of Professional all that much). Once this is done downloading and you go through the setup, you _should_ be able to run PyCharm by simply typing `pycharm` on the command line.  If this doesn't work, talk to Ryan as this is relatively new technology in the group.

**Usage on your laptop**

Make sure you download anaconda before proceeding. You can find the installer for PyCharm [here](https://www.jetbrains.com/pycharm/). We will follow the instructions laid out by JetBrains. Use the all the recommended settings, so just keep hitting next until it's finished. Once installed, open it up and follow the configuration instructions, we don't need any of their _featured plugins_.


### Configuring PyCharm after Installation

Once you make your way to the main screen, to get configuration out of the way, start a new project.  You can put the project directory anywhere, as I just want you to get your anaconda installation set up here. It will ask for an interpreter, and go over to `Existing Interpreter`, then click on the `...` box on the side.  Go to `System Interpreter` in the dropdown on the left and you should be able to select your anaconda installation (Conda, symbol looks like a not-yet complete green circle). Press ok through everything and then you should see your project bar on the far left. It will take a few minutes to have your anaconda installation fully make its way into pycharm, so be patient while it's `updating skeletons` or `2 processes running` on the bottom right.

**Git/Github Integration**

_Note: If you are not comfortable with git, github, and/or pycharm it may be good to do this with a senior lab member near you_

PyCharm provides a graphical interface for using git and github.  All version control settings take place in the `VCS` tab up at the top of PyCharm.  Git is already installed on the group computers, so if you are using it there you just need to add a Git repository by going to VCS-->Enable Version Control Integration and select Git (if you are on a laptop it will prompt you to download Git).  Then, you can add a git repository by doing VCS-->Import into version control-->Create git repository.  Then you can use the newly appeared icons on the top right of the pycharm window that have Git next to them to push, pull, and look at code history. You can also share the project on Github using VCS-->Import into version control-->Share Project on Github and then login.  This is an alternative to using command line git procedures.  

_Why bother with Git and Github?? Seems like a pain in the Butt_

One of the most powerful aspects of using Git in PyCharm is the `Show History` (clock icon) option.  It will show you past git commits, as well as what has changed since the last commit.  You can do side-by-side mode to also see what you have changed line-by-line.  This is a great option if you broke your code and are trying to go back to the last known time it worked :).

<span class="text-muted">Next:</span>
 [Your "First" Python Script](FirstPythonScript.md)<br/>
<span class="text-muted">Previous:</span>
 [An Introduction to Python/Anaconda](IntroToPython.md)
 
 Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/IntroToIDEs.md)
