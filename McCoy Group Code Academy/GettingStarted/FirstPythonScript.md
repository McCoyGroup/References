# Your "First" Python Script

Whether or not you have a background in coding, this could very well be your first dive into coding for Quantum Chemistry. While it won't be super sophisticated to start, this probably is your _first_ python script in this context. This page along with other tutorials you will read through will set up what we have deemed _fundamental_ to writing code to solve more scientifically heavy problems. We hope that you remember these steps and processes as you start confronting your own research problems.  

## Writing and Running a Script

If you haven't already installed PyCharm, now might be a good time to. Actually, just do it. Here are the [instructions](IntroToIDEs.md). PyCharm is basically a Spell Check of sorts for Python Code, so if you are gonna start writing scripts, why wouldn't you want Spell Check?

Ok, now we're ready to start writing a script that'll do something super cool.
What this super cool thing is...well that's still TBD. (and to be determined by you!)
For now we're just gonna write a script that converts frequencies from wavenumbers ($cm{^-1}$) to their atomic unit (Hartree).
To do so we'll make a file called `wave_to_au.py`.

In it, to start, we'll put this content:

```python
  frequency = 3600  # the frequency of an OH strech in water 
  conversion_factor = 219474.6  # cm^-1 = 1 Hartree
  frequency_au = frequency / conversion_factor
  print(f"{frequency} wavenumbers is {frequency_au} in Hartree")
```
Now, let's break this down a little bit:
1. Define variables, `frequency` and `conversion_factor`.
2. Convert the frequency. 
3. Print a _Format String_ showing the input frequency and the converted frequency. 

A _Format String_ you ask? This is one of your best friends for getting data quick, checking values, and debugging. You define a format string by placing a lowercase `f` in front of your string quotes like so, `f" "`. with this in place, you can type and insert variables directly by enclosing them in curly brackets `{}`. Then when the `print()` function prints your string to the command window, it fills in the blanks with the values of the variables you provided.  

### What else can we do with this?
You're probably thinking "That's great and all but..." and that's good. What if you tried a script like `rad_to_degree.py` or maybe even `ang_to_bohr.py`? Or if you are thinking "Well what if I want to convert a different frequency? or a lot of frequencies?" you might want to try: [How to Write A Function](HowToWriteAFunction.md). Or play around for a while and go on when you're ready.


<span class="text-muted">Next:</span>
 [How to Write a Function](HowToWriteAFunction.md)<br/>
<span class="text-muted">Previous:</span>
 [What is an IDE?](IntroToIDEs.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/GettingStarted/CommonIssues.md)
