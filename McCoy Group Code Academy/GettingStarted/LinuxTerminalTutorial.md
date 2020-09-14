# An Introduction to the Linux Terminal

Whether using a Linux or MacOS machine, you have access to the Bash command line (Historical Name: "Bourne-Again Shell", which is based on the original Shell command line).  This is different than a Windows command prompt, which has its own suite of commands.  If you have a windows machine you will be using for research, it is recommended to download Windows Subsystem for Linux, or you may get away with using Windows Powershell and PyCharm for most of your development needs in the group.

The command line allows you to navigate around your filesystem, execute and edit code, and much more without using a graphical user interface (GUI). 

There are a ton of online resources and [youtube tutorials](https://youtu.be/YHFzr-akOas?t=204) that will get you familiar with the command line.

When you begin in the group, you have to talk to Anne or a senior graduate student about getting an account on the lab computers.  Once you get an account, you will have a directory that is your own in the filesystem on each computer.

# SSH and SFTP
To access the filsystem, you will need a way to SSH (Secure shell) onto the lab computers (or any other Linux Machine). There is a [McCoy Group stackoverflow question detailing this](https://stackoverflow.com/c/mccoygroup/a/12/2).  You can also transfer files across Linux/MacOS machines using [SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server) (Secure File Transfer Protocol).

## Windows
On Windows, you may not directly SSH or SFTP using the commmand prompt :(. This is not entirely true, as, recently, you can now SSH using the Windows PowerShell terminal, but it is not the same as using a Linux Terminal.  So, we recommend to download software to do both.  To SSH onto a Linux machine, we recommend using [MobaXTerm] (https://mobaxterm.mobatek.net/), which has a lot of convenient tools built-in to it. To transfer files from Windows machines to Linux and back, we recommend using [WinSCP](https://winscp.net/eng/index.php).  It provides a nice GUI for transfering files back and forth.  

There are plenty of alternative clients for these tasks, including PuTTY for SSH and FileZilla for SCP/SFTP, but we found these two do be a great combination.

As a note, you may also download Windows Subsystem for Linux, and then, after downloading and installing a Linux OS like Ubuntu, you can SSH to the group computers using the WSL command line.

## MacOS/Linux
If you choose to do so, you can SSH and SFTP onto remote computers purely using the command line.  If you want a graphical interface to transfer files, you can download [CyberDuck](https://cyberduck.io/)!

# A Brief Note on Permissions
On the group computers, you will have read-only access to other group mates' filesystems (and the system files), and you will have autonomy over your own filesystem.  You will not have super-user or root access on the group computers unless specifically given the responsibility.  The keeper of the root passwords is designated in the group, but for security purposes we are not putting whot that is here.  Ask Anne if you need root access or if you need someone to do something root-accessible.

# A Brief Note on Text Editors
There are a ton of terminal text editors out there. The two main ones are emacs and vim (or vi, vim is the generic name for vi).  Both of these are installed on each group computer.  We will not recommend one over the other, Anne uses vim and so it may be a good idea to learn that, but some would say that there is a steeper learning curve in vim than emacs.  Emacs automatically opens up a GUI, to allow it to run in terminal provide the command `emacs -nw`, which means "no window". 

# Useful commands not covered thus far
There are [plenty of internet resources](https://www.educative.io/blog/bash-shell-command-cheat-sheet) that will show you helpful command line commands, but here are some that we use in the group all the time that we wanted to highlight:

* [at](https://linuxize.com/post/at-command-in-linux/): The at command allows you to execute an arbitrary command at a specified time.  Here is a [stackoverflow example](https://stackoverflow.com/c/mccoygroup/a/98/2) of how to run a Gaussian job on one of the group computers using the at command
* grep: Allows you to search for text in a file, it will automatically output the line where it is found (and the surrounding lines if specified with -A and -B) to the command line. 
* eog: The photo client for our computers, eog <filename>.png will open up a graphics windows with the picture.
* who: Shows who is logged on to a computer.
* top: Show all current processes running on the computer.
* pwd: Show current working directory
* du -h: Get the size (MB/GB) of the data in the current directory
* cd ~/...: cd to your home directory, and then onwards
* cd <blankspace>: Bring you to your home directory
* cd ..: Bring you out of the current directory, one 'upwards'
* cd /: Go to the root filesystem (a no-no on the group computers)


Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/LinuxTerminalTutorial.md)
