# Python and NumPy

Python, as a programming language, isn't blazingly fast. It provides us with a huge amount of flexibility, but that comes at a performance premium.
Compared to code written in more rigid languages like C++, Fortran, and Java, Python code will generally be at least a few orders of magnitude slower.
Usually, however, this isn't a problem.
Most of what programmers do _doesn't_ have to be blazingly fast, and there are many, many perks to being able to use a language like Python that's both suitable for beginners writing their first scripts, individual scientists prototyping new methods, and groups of developers writing industrial-scale software.

One place, however, where this speed difference does become an issue, is when dealing with big blocks of numbers. 
Our rule of thumb is that if you need to do a few thousand operations, Python will be fast enough. If you have to do tens of thousands, you're going to start to run into issues.
When dealing with vectors, matrices, and tensors, we very quickly start to push into the realm of millions of operations.
And as computational chemists, vectors, matrices, and tensors are core staples of our research.

Back in the Dark Ages (i.e. 2005) people saw the writing on the wall and started writing what would become [NumPy](https://numpy.org/), a Python package devoted entirely to numerical programming and handling arrays.
We use NumPy every day. We even use it in contexts where we could have used pure Python, since its design allows us to write less code, and therefore write fewer bugs.
There are tons of NumPy tutorials out there, like [this](https://numpy.org/devdocs/user/quickstart.html), [this](https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54), [this](https://cs231n.github.io/python-numpy-tutorial/), etc.
New ones come out every day and we've got no real desire to write our own when the resources already exist.
That said, these tutorials can be dense, and they may not go over the key operations that we use in the McCoy group every day. 
So, we're going to work through the basics and some examples that are relevant to the research we do.

Here's the road map:
* [Numpy 101](numpy101.md)
* [List of Helpful NumPy Functions](numpyFunctions.md)

After you're acclimated and have had some time to play around with NumPy, we recommend going back to those tutorials.
For key operations & a better understanding of how arrays work, we recommend [this one](https://github.com/bonn0062/GSoD/blob/master/absolute_beginners.rst).
For an overview of the NumPy ecosystem, we recommend [this one](https://numpy.org/devdocs/user/quickstart.html).
And if you'd like an intro into high-dimensional array (tensor) operations in NumPy, [this one](https://machinelearningmastery.com/introduction-to-tensors-for-machine-learning/) isn't a bad place to start.

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/index.md)
