# Python and its Place in the World

Python, as a programming language, isn't fast compared to petal-to-the metal languages like C, C++, and Fortran. Briefly, Python is an "interpreted" language, as opposed to a "compiled" language, which means that Python requires a lot more (under the hood) machine code to run when compared to the compiled machine code that C/C++/Fortran output in their executables.  A lot of the time, this is not an issue, and many of us choose to use Python over compiled languages as our go-to language because there are a lot of programming perks that come along with Python, making it not only suitable for large-scale software development but also easy to code for beginners.

# Numpy

Most of what programmers want to do doesn't have to be blazingly fast.  If one only has to compute a few thousand operations, pure Python will perform more than fast enough.  Unfortunately, we usually need to do more than a few thousand operations in research.  Additionally, working with multidimensional arrays (matrices/tensors) requires care and attention, such as making sure one is using the correct indices for your summations, and writing code so that it is concise and comprehensible.

Since people still love Python for all its perks, back in the Dark Ages (i.e. 2005) people saw the writing on the wall and started writing [NumPy](https://numpy.org/), a Python package devoted entirely to numerical programming and handling high-dimensional arrays. There are tons of NumPy tutorials out there, like [this](https://numpy.org/devdocs/user/quickstart.html), [this](https://www.tutorialspoint.com/numpy/index.htm), [this](https://cs231n.github.io/python-numpy-tutorial/), [this](https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54), etc.
New ones come out every day and we've got no real desire to write our own when the resources already exist.
That said, the tutorials can be dense, and they may not go over the relevant information that we use in the McCoy group every day. So, we're going to work through the basics and some examples that are relevant to the research we do.

Here's the road map:
* [Numpy 101](numpy101.md)
* [List of Helpful NumPy Functions](numpyFunctions.md)
* [Usage Examples](Examples.md)

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/NumPy/index.md)
