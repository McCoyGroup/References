# There Are Too Many Tools

One of the first issues you might run into when trying to plot your data is that you can't figure out what you should use to plot it.
Like, you could coerce your data into an Excel spreadsheet and do some manual work to plot it there.
If you're command-line oriented, you can use a tool like [gnuplot](http://www.gnuplot.info/) to do all sorts of stuff.
Or if you've got the familiarity, software like Mathematica has all sorts of [plotting features](https://reference.wolfram.com/language/guide/DataVisualization.html).

We're gonna put our hat in the ring in favor of [matplotlib](), not necessarily because we think it's better than any of the others (it is probably emphatically [_worse_](https://ryxcommar.com/2020/04/11/why-you-hate-matplotlib/) than most of them), but because it's the _de facto_ standard in the Python world.
There are two other major python plotting interfaces, [plotly](https://plotly.com/python-api-reference/) and [seaborn](https://seaborn.pydata.org/), but neither of those is a perfect solution and for flexibility it's often good to aim for the common standard.
On the other hand, if you've got experience with them or other software and you can make it do what you need, that's totally cool by us. Our suggestions on [good data presentation](TheGoodPlot.md) will still hold.

As with NumPy, there are a [bajillion](https://matplotlib.org/3.2.2/tutorials/introductory/lifecycle.html#getting-started) [matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html) [references](https://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut2.html) [out](https://matplotlib.org/tutorials/introductory/customizing.html) [there](https://www.tutorialspoint.com/matplotlib/matplotlib_object_oriented_interface.htm).
We're not gonna try to write our own.
We _are_ however, going to try to steer you away from some of the many, many pitfalls `matplotlib` exposes.

<span class="text-muted">Next:</span>
 [Getting Started with Matplotlib](OOPMatplotlib.md)<br/>

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/Plotting/TooManyTools.md)