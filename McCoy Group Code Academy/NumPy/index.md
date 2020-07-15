# NumPy

Python, as a programming language, isn't particularly fast (well honestly it's really slow).
95% of the time, that's not an issue.
Most of what programmers want to do doesn't have to be blazingly fast and it's really easy to tie oneself into a knot trying to make something fast when it doesn't need to be.
If you've only got to do a few thousand operations, python will do it more than fast enough.
Unfortunately, a place where you need to do tons of little operations is in numerical programming.

Back in the Dark Ages (i.e. 2005) people saw the writing on the wall and started writing what has become [NumPy](https://numpy.org/), a python package devoted entirely to numerical programming and handling high-dimensional arrays.
There are tons of NumPy tutorials out there, like [this](https://numpy.org/devdocs/user/quickstart.html), [this](https://www.tutorialspoint.com/numpy/index.htm), [this](https://cs231n.github.io/python-numpy-tutorial/), [this](https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54), etc.
New ones come out every day and we've got no real desire to write our own when the resources already exist.
On the other hand, we don't really use most of the NumPy features that the tutorial writers care about and also want to make sure that everyone has a similar base level of knowledge, so long story short we're gonna write a rather limited one that hits the highlights of what we think everyone really ought to know.

Here's the road map:
* [Numpy 101](Numpy101.md)
* [List of Helpful NumPy Functions](NumpyFunctions.md)
* [Usage Examples](Examples.md)

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/index.md)