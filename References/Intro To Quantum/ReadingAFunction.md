# Reading a Function

As I noted in the previous section, not all code is written as clean series of transformations of data through small functions.
Honestly, most of the code you'll see is garbage (and sadly no one is immune to writing garbage code).
That being said, even good code can be hard to read, since it represents the logic someone else was using to solve a problem.
On the other hand, the best way to get better at writing code is to _read_ code. Seeing how other people tackled a problem will give you ideas and you'll probably learn useful tricks along the way, so 

But it's hard at first, so here are some tips and tricks for how to break down code. 
Keep in mind that we're gonna be working with random code I pulled off the internet, so having a basic knowledge of python stuff like [`classes`](https://docs.python.org/3/tutorial/classes.html), [`while` and `for` loops](https://docs.python.org/3/tutorial/controlflow.html), and [basic data-types](https://docs.python.org/3/library/stdtypes.html) like `int`, `lists`, and `dicts` will likely be helpful.

Here' the flow I recommend 

1. Look at the function name and argument _names_ and, if available, the docstring
  * If the docstring is there, read it carefully. It'll hopefully have some insight into what the function is doing
  * If you can, see if you can figure out what the arguments are supposed to represent conceptually
  * After that, see if you can have a reasonable guess at what the argument types are
2. Look for comments
  * Comments document the logical flow in natural language, so can be very, very helpful even in fragmentary form
3. Look at the return value _name_
  * See if you can figure out what this conceptually represents
4. Look for functions that use this function
  * These functions may not be in the same file the function is defined
  * If you find a function that uses this function, try to understand what its goal is before moving on
5. Break the function into three chunks
  * Variable allocations/constants
  * Transformations of data
  * Prepping to return
6. Give each transformation a name, assuming it's more than just a function call
7. Piece together the "story" the function is telling

## Examples

We'll run through these steps for some chunks of code I found on the internet.

### DVR1D/getKinetic

First off, here's a function from one of our group repos: [McCoyGroup/GroundStateApproximation/DVR1D.py](https://github.com/McCoyGroup/GroundStateApproximation/blob/e62a422e731ba47e544cf5f4ef0bc39294e62a08/DVR1D.py#L47)

```python
def getKinetic(dim):
    ke = np.zeros((dim,dim))
    d=tcoef * (np.pi * np.pi / 3.)
    np.fill_diagonal(ke, d)
    for i in range(1,dim):
        for j in range(i):
            ke[i,j]=tcoef*\
                    (-1.)**(i-j)*\
                    (2./((i-j)**2))
    dg = np.diagonal(ke)
    s=ke+ke.T-np.diag(dg)
    return s
```

**Step 1**: function and arg names + docstring

We first see the function name, it's called `getKinetic` which suggests it's related to getting some kind of kinetic energy.
Next, looking at the arguments, there's one argument called `dim`...so maybe it's related to a some kind of dimension? Not sure at this point.
No docstring so...nothing to do

**Step 2**: look for comments

No comments. Usually only people with a lot of experience or who are developing big libraries of functions write many comments.
Everyone knows they _should_, but people get lazy and figure "eh, no one else is ever gonna read this"

**Step 3**: look at the return value _name_ 

It's called `s` so...yeah I got nothing. Often single letter variables correspond to a `type`, like `l` for `list`, or `i` for `int`, or `s` for `str`, but I don't think the kinetic energy is gonna be a string.

**Step 4**: look for functions that use this function

I found this function used towards the bottom of the file in this just of stuff that's not in a function (short scripts often aren't in functions and so this seems to be a script)[<sup>1</sup>]

```python
scanPotential(config,modeN,refScanGeom)
V = getPotential("eng_dip_"+config+'_Mode_'+modeN)
npts = len(np.diag(V))
dx=0.01*np.loadtxt("tn/tnorm_"+config+"Mode_"+modeN)
tcoef = hbar ** 2 / (2 * mass * dx * dx)
T = getKinetic(len(V))
E,Wf=diagonalizeH(T+V)
Ecm= E*au2wn
print(Ecm)
print('Delta E 0-->1',Ecm[1]-Ecm[0])
np.savetxt("DeltaE/DeltaE01"+refScanGeom+"_"+config+"_"+modeN,np.array([Ecm[1]-Ecm[0]]))
```

and seeing all of that uncommented stuff definitely does elicit a bit of a [боже мой!](https://youtu.be/gXlfXirQF3A?t=70) reaction, but at least I see that it's used here

```python
T = getKinetic(len(V))
E,Wf=diagonalizeH(T+V)
```

and we see two big things straight away 

1. the return value is called `T`, which is usually used for the kinetic energy matrix representation[<sup>2</sup>]
2. the input value is `len(V)` which means our `dim` from before is an `int` (and the length of whatever `V` is, to be specific)

so then we look at the next line and see two more things

1. this `T` is used in `diagonalizeH(T+V)` and that's super reminiscent of $H=T+V$, which is something we've seen before
2. that function returns two values, `E` and `Wf`, which then looks reminiscent of $H\psi(x)=E\psi(x)$

and that means we can be pretty sure that `getKinetic` is a function that takes a number of elements to use in the matrix representation (determined by how big `V` is) and returns the matrix representation of the kinetic energy.

Great! Now we have inputs, intent, and return values. 
At this stage we don't necessarily even need to figure how the function does what it does, but given that this is an educational example, let's move onto the next steps.

**Step 5**: Break the function into chunks

First off, we'll figure out what parts are basically the _initialization_. 
Looking through it we see that the first line is just creating an empty matrix to fill in

```python
    ke = np.zeros((dim,dim))
```

the next ones seem to be doing stuff with that matrix

```python
    d=tcoef * (np.pi * np.pi / 3.)
    np.fill_diagonal(ke, d)
    for i in range(1,dim):
        for j in range(i):
            ke[i,j]=tcoef*\
                    (-1.)**(i-j)*\
                    (2./((i-j)**2))
    dg = np.diagonal(ke)
    s=ke+ke.T-np.diag(dg)
```

and then there doesn't seem to be anything needed to prep the data for return, so the return line is just

```python
    return s
```

obviously there is no _unique_ way to break this up, so it's totally up to personal preference how one chooses to do this, but this partition seems reasonable to me.

**Step 6**: Give transformations a name

This is and Step 5 are probably the toughest steps, since they require working through what's actually going on. 
When possible, try to _avoid_ getting this far down the checklist. 
It's usually much more useful to just know what goes in and what on a conceptual level.

But sometimes it's educational or necessary to know exactly how the other person wrote their function, so for cases like that we'll work through how to do this.
First, we look at the fact that the variable `d` is only used in these two lines 
```python
    d=tcoef * (np.pi * np.pi / 3.)
    np.fill_diagonal(ke, d)
```

So we might call this function something like

```python
def assign_diagonal(ke, tcoef):
    d=tcoef * (np.pi * np.pi / 3.)
    np.fill_diagonal(ke, d)
```

the next section is a nested for loop which goes over the upper triangle of a matrix, so maybe we'd call this

```python
def fill_upper_triangle(ke, tcoef):
    for i in range(1,len(ke)):
        for j in range(i):
            ke[i,j]=tcoef*\
                    (-1.)**(i-j)*\
                    (2./((i-j)**2))
```

and these last two lines seem to be involved in symmetrizing the matrix, so for that we'd have

```python
def make_matrix_symmetric(ke):
    dg = np.diagonal(ke)
    s=ke+ke.T-np.diag(dg)
    return s
```

and with all these bits, we can now write our overall function as 

```python
def getKinetic(dim):
    ke = np.zeros((dim,dim))
    assign_diagonal(ke, tcoef)
    fill_upper_triangle(ke, tcoef)
    s = make_matrix_symmetric(ke)
    return s
```

which looks a lot simpler.

**Step 7**: tell the "story" of the function

Code is precise and clean and all that, but nothing sticks in the head like a narrative. 
So how would we describe what this function does?

Well I might say

> This function generates a matrix that represents the kinetic energy in a wavefunction calculation.
> First, it asks for how big a matrix we want to generate.
> Once it has that, it fills the diagonal with one value derived from `tcoef` and it fills the upper triangle with a different one, which again depends of `tcoef`, but which also depends on where in the matrix it is.
> After filling the upper triangle in, it makes this matrix symmetric.

now _physically_ this is meaningless and making the physical connection to the code is really important when possible, but given that I pulled this code out of the aether, we'd need way more info to fully make sense of it.

At the very least, though, we now have a better sense for what the function does, how we call it, and what we get out of it, and 90% of the time all we need are the last two. Complexity hiding is your friend.

### tensordot

The next example is a super useful numpy function called [`tensordot`](https://github.com/numpy/numpy/blob/74c111f0c40978ad064daabfe17658a308721a2d/numpy/core/numeric.py#L917)

```python
def tensordot(a, b, axes=2):
    """
    Compute tensor dot product along specified axes.
    Given two tensors, `a` and `b`, and an array_like object containing
    two array_like objects, ``(a_axes, b_axes)``, sum the products of
    `a`'s and `b`'s elements (components) over the axes specified by
    ``a_axes`` and ``b_axes``. The third argument can be a single non-negative
    integer_like scalar, ``N``; if it is such, then the last ``N`` dimensions
    of `a` and the first ``N`` dimensions of `b` are summed over.
    Parameters
    ----------
    a, b : array_like
        Tensors to "dot".
    axes : int or (2,) array_like
        * integer_like
          If an int N, sum over the last N axes of `a` and the first N axes
          of `b` in order. The sizes of the corresponding axes must match.
        * (2,) array_like
          Or, a list of axes to be summed over, first sequence applying to `a`,
          second to `b`. Both elements array_like must be of the same length.
    Returns
    -------
    output : ndarray
        The tensor dot product of the input.
    See Also
    --------
    dot, einsum
    Notes
    -----
    Three common use cases are:
        * ``axes = 0`` : tensor product :math:`a\\otimes b`
        * ``axes = 1`` : tensor dot product :math:`a\\cdot b`
        * ``axes = 2`` : (default) tensor double contraction :math:`a:b`
    When `axes` is integer_like, the sequence for evaluation will be: first
    the -Nth axis in `a` and 0th axis in `b`, and the -1th axis in `a` and
    Nth axis in `b` last.
    When there is more than one axis to sum over - and they are not the last
    (first) axes of `a` (`b`) - the argument `axes` should consist of
    two sequences of the same length, with the first axis to sum over given
    first in both sequences, the second axis second, and so forth.
    The shape of the result consists of the non-contracted axes of the
    first tensor, followed by the non-contracted axes of the second.
    Examples
    --------
    A "traditional" example:
    >>> a = np.arange(60.).reshape(3,4,5)
    >>> b = np.arange(24.).reshape(4,3,2)
    >>> c = np.tensordot(a,b, axes=([1,0],[0,1]))
    >>> c.shape
    (5, 2)
    >>> c
    array([[4400., 4730.],
           [4532., 4874.],
           [4664., 5018.],
           [4796., 5162.],
           [4928., 5306.]])
    >>> # A slower but equivalent way of computing the same...
    >>> d = np.zeros((5,2))
    >>> for i in range(5):
    ...   for j in range(2):
    ...     for k in range(3):
    ...       for n in range(4):
    ...         d[i,j] += a[k,n,i] * b[n,k,j]
    >>> c == d
    array([[ True,  True],
           [ True,  True],
           [ True,  True],
           [ True,  True],
           [ True,  True]])
    An extended example taking advantage of the overloading of + and \\*:
    >>> a = np.array(range(1, 9))
    >>> a.shape = (2, 2, 2)
    >>> A = np.array(('a', 'b', 'c', 'd'), dtype=object)
    >>> A.shape = (2, 2)
    >>> a; A
    array([[[1, 2],
            [3, 4]],
           [[5, 6],
            [7, 8]]])
    array([['a', 'b'],
           ['c', 'd']], dtype=object)
    >>> np.tensordot(a, A) # third argument default is 2 for double-contraction
    array(['abbcccdddd', 'aaaaabbbbbbcccccccdddddddd'], dtype=object)
    >>> np.tensordot(a, A, 1)
    array([[['acc', 'bdd'],
            ['aaacccc', 'bbbdddd']],
           [['aaaaacccccc', 'bbbbbdddddd'],
            ['aaaaaaacccccccc', 'bbbbbbbdddddddd']]], dtype=object)
    >>> np.tensordot(a, A, 0) # tensor product (result too long to incl.)
    array([[[[['a', 'b'],
              ['c', 'd']],
              ...
    >>> np.tensordot(a, A, (0, 1))
    array([[['abbbbb', 'cddddd'],
            ['aabbbbbb', 'ccdddddd']],
           [['aaabbbbbbb', 'cccddddddd'],
            ['aaaabbbbbbbb', 'ccccdddddddd']]], dtype=object)
    >>> np.tensordot(a, A, (2, 1))
    array([[['abb', 'cdd'],
            ['aaabbbb', 'cccdddd']],
           [['aaaaabbbbbb', 'cccccdddddd'],
            ['aaaaaaabbbbbbbb', 'cccccccdddddddd']]], dtype=object)
    >>> np.tensordot(a, A, ((0, 1), (0, 1)))
    array(['abbbcccccddddddd', 'aabbbbccccccdddddddd'], dtype=object)
    >>> np.tensordot(a, A, ((2, 1), (1, 0)))
    array(['acccbbdddd', 'aaaaacccccccbbbbbbdddddddd'], dtype=object)
    """
    try:
        iter(axes)
    except Exception:
        axes_a = list(range(-axes, 0))
        axes_b = list(range(0, axes))
    else:
        axes_a, axes_b = axes
    try:
        na = len(axes_a)
        axes_a = list(axes_a)
    except TypeError:
        axes_a = [axes_a]
        na = 1
    try:
        nb = len(axes_b)
        axes_b = list(axes_b)
    except TypeError:
        axes_b = [axes_b]
        nb = 1

    a, b = asarray(a), asarray(b)
    as_ = a.shape
    nda = a.ndim
    bs = b.shape
    ndb = b.ndim
    equal = True
    if na != nb:
        equal = False
    else:
        for k in range(na):
            if as_[axes_a[k]] != bs[axes_b[k]]:
                equal = False
                break
            if axes_a[k] < 0:
                axes_a[k] += nda
            if axes_b[k] < 0:
                axes_b[k] += ndb
    if not equal:
        raise ValueError("shape-mismatch for sum")

    # Move the axes to sum over to the end of "a"
    # and to the front of "b"
    notin = [k for k in range(nda) if k not in axes_a]
    newaxes_a = notin + axes_a
    N2 = 1
    for axis in axes_a:
        N2 *= as_[axis]
    newshape_a = (int(multiply.reduce([as_[ax] for ax in notin])), N2)
    olda = [as_[axis] for axis in notin]

    notin = [k for k in range(ndb) if k not in axes_b]
    newaxes_b = axes_b + notin
    N2 = 1
    for axis in axes_b:
        N2 *= bs[axis]
    newshape_b = (N2, int(multiply.reduce([bs[ax] for ax in notin])))
    oldb = [bs[axis] for axis in notin]

    at = a.transpose(newaxes_a).reshape(newshape_a)
    bt = b.transpose(newaxes_b).reshape(newshape_b)
    res = dot(at, bt)
    return res.reshape(olda + oldb)
```

The first thing we'll notice is that more of this is docstring than actual code. That's actual really common. 
It often takes more effort to explain what a piece of code is doing than to actually write the code to do it.

In any case, let's walk through our checklist! I'm gonna be a bit more terse this time, though.

**Step 1**: function and arg names + docstring

Well function name is, obviously, `tensordot`, function args are called `a`, `b`, and `axes`...thus far kinda cryptic.

But look at that `docstring`! There's almost too _much_ info in it, but reading through that first paragraph we learn a few things
1. The function is trying to be like a normal dot product[<sup>3</sup>] but for tensors.
2. It takes two arrays and returns an array from them.
3. The `axes` argument has too many allowed values

Reading the docstring, it looks like `axes` _should_ be a two lists of integers for `a` and `b` respectively, like

```python
[[a_axis_1, a_axis_2, ...], [b_axis_1, b_axis_2, ...]]
```

but I guess there were some convenience cases to account for? Or maybe there were some historical ones?

In any case, this docstring is a great source of info, but we'll plow on to get a better sense for how it does what it does.

**Step 2**: look for comments

There's one comment block to look at 

```python
    # Move the axes to sum over to the end of "a"
    # and to the front of "b"
```

this isn't 100% helpful yet, but definitely show us that we're going to be doing some shifting around of the axes in our tensors (the formal name for rearranging axes is taking a _transpose_).

**Step 3**: look at the return value _name_ 

The return value is unnamed ;_;

```python
    return res.reshape(olda + oldb)
```

to understand what's going on there, we'll need to actually read the code.

**Step 4**: look for functions that use this function

None are in here, but we won't actually do this step since we had that great docstring to explain what the function takes and what it returns.

**Step 5**: Break the function into chunks

This will be a judgment call, but I think something like this works

Initialization:
```python
    try:
        iter(axes)
    except Exception:
        axes_a = list(range(-axes, 0))
        axes_b = list(range(0, axes))
    else:
        axes_a, axes_b = axes
    try:
        na = len(axes_a)
        axes_a = list(axes_a)
    except TypeError:
        axes_a = [axes_a]
        na = 1
    try:
        nb = len(axes_b)
        axes_b = list(axes_b)
    except TypeError:
        axes_b = [axes_b]
        nb = 1

    a, b = asarray(a), asarray(b)
    as_ = a.shape
    nda = a.ndim
    bs = b.shape
    ndb = b.ndim
    equal = True
    if na != nb:
        equal = False
    else:
        for k in range(na):
            if as_[axes_a[k]] != bs[axes_b[k]]:
                equal = False
                break
            if axes_a[k] < 0:
                axes_a[k] += nda
            if axes_b[k] < 0:
                axes_b[k] += ndb
    if not equal:
        raise ValueError("shape-mismatch for sum")
```

Transformation:
```python
    notin = [k for k in range(nda) if k not in axes_a]
    newaxes_a = notin + axes_a
    N2 = 1
    for axis in axes_a:
        N2 *= as_[axis]
    newshape_a = (int(multiply.reduce([as_[ax] for ax in notin])), N2)
    olda = [as_[axis] for axis in notin]

    notin = [k for k in range(ndb) if k not in axes_b]
    newaxes_b = axes_b + notin
    N2 = 1
    for axis in axes_b:
        N2 *= bs[axis]
    newshape_b = (N2, int(multiply.reduce([bs[ax] for ax in notin])))
    oldb = [bs[axis] for axis in notin]

    at = a.transpose(newaxes_a).reshape(newshape_a)
    bt = b.transpose(newaxes_b).reshape(newshape_b)
    res = dot(at, bt)
```

Prep for return:
```python
    return res.reshape(olda + oldb)
```

**Step 6**: Give transformations a name

Even though the "Initialization" block had so much in it, I'm mostly going to skip it, since it was largely just checking that the inputs were valid.

One important thing _did_ happen there, though, we had this assignment
```python
axes_a, axes_b = axes
```
which is just taking our `axes` argument and splitting it into the axes to take the dot product over for `a` and those for `b`.

Next, I'll name the blocks one-by-one

```python
def determine_not_dotted(axes, nd):
    notin = [k for k in range(nd) if k not in axes]
    return notin
def get_dottable_shape_a(notin, axes_a):
    newaxes_a = notin + axes_a
    N2 = 1
    for axis in axes_a:
        N2 *= as_[axis]
    newshape_a = (int(multiply.reduce([as_[ax] for ax in notin])), N2)
    return newaxes_a, newshape_a
def get_dottable_shape_b(notin, axes_b):
    newaxes_b = axes_b + notin
    N2 = 1
    for axis in axes_b:
        N2 *= bs[axis]
    newshape_b = (N2, int(multiply.reduce([bs[ax] for ax in notin])))
    return newaxes_b, newshape_b
def get_leftover_shape(axes_list, notin):
    old = [axes_list[axis] for axis in notin]
    return old
def prep_for_dotting(a, newaxes, newshape):
    at = a.transpose(newaxes).reshape(newshape)
    return at
```

and so the overall transformation ends up being

```python
notin = determine_not_dotted(axes_a, nda)
newaxes_a, newshape_a = get_dottable_shape_a(notin, axes_a)
olda = get_leftover_shape(as_, notin)

notin = determine_not_dotted(axes_b, ndb)
newaxes_b, newshape_b = get_dottable_shape_b(notin, axes_b)
oldb = get_leftover_shape(bs, notin)

at = prep_for_dotting(a, newaxes_a, newshape_a)
bt = prep_for_dotting(b, newaxes_b, newshape_b)
res = dot(at, bt)
```

and hopefully this is a bit cleaner to make sense of.

**Step 7**: tell the "story" of the function

> This is a function that takes two tensors and the respective sets of axes to dot together.
> It takes those axes specifications and rearranges the arrays so those axes come at the end and front of the rearranged arrays, respectively and then flattens the tensors down to 2D.
> After this, it takes a regular dot product, then reshapes back so that the overall shape of the tensor is a concatenation of the "undotted" shapes.
> After doing that, the resultant tensor is returned.

### Mathematica Code[<sup>4</sup>]

I waffled a bit on this, but I wanted to show that the idea doesn't _just_ apply to python/NumPy. 
To prove this, I took a [Mathematica function](https://github.com/b3m2a1/mathematica-ChemTools/blob/773b994efce8f11e7a6c1f668e1800b963add069/Packages/Compute/Structural.m#L58) I wrote a while back

```mathematica
ChemComputeInertialTensor[masses_List, positions_List]:=
  Total@
    MapThread[
      With[{m=#1,x=#2[[1]],y=#2[[2]],z=#2[[3]]},
        m*{ 
          {y^2+z^2,-x*y,-x*z},
          {-x*y,x^2+z^2,-y*z},
          {-x*z,-y*z,x^2+y^2}
        }]&,
      {masses,positions}
      ];
```

Okay...kinda a lot going on in here, I won't deny.
But we can still apply the ideas from before, just with a little bit of help with the Mathematica syntax. 
One big thing: in Mathematica you call functions using square brackets, so the function `bloop(...)` in python becomes `bloop[]` in Mathematica. Also instead of build compond names with `_` you build them using "camel case", i.e. by putting a capital letter at the start of each word, like the humps on a camel.

**Step 1**: function and arg names + docstring

So first off, the function seems to be called `ChemComputeInertialTensor`. Good sign. 
It's probably gonna take compute the "inertial tensor", or in normal people words, the "moment of inertia" tensor for whatever our system is.
What does it take as arguments?

Well we have `masses_List` and `positions_List`. 
The thing before the `_` is the variable name and the thing _after_ it is the type, so now we know what we're working with. 

This is a function that computes the moment of inertia tensor from a set of masses and (presumably) corresponding positions.

**Step 2**: look for comments

Sadly, I did not give you any comments ;_;

**Step 3**: look at the return value _name_ 

The function is basically one big transformation that just returns itself, so we don't have any...oops

**Step 4**: look for functions that use this function

We actually probably know at this point what this function takes, returns, and does, so we can probably skip this step again.

**Step 5**: Break the function into chunks

Okay as noted before this is just one massive transformation, so there's really just one chunk. 
This was bad programming practice on my part, but is also not uncommon.

**Step 6**: Give transformations a name

Even though it's just one big transformation, we can break up this transformation into _subparts_ and we'll name those

```mathematica
makeSingleMassPostionTensor[mass_, pos_]:=
  With[{m=mass,x=pos[[1]],y=pos[[2]],z=pos[[3]]},
    m*{ 
     {y^2+z^2,-x*y,-x*z},
     {-x*y,x^2+z^2,-y*z},
     {-x*z,-y*z,x^2+y^2}
     }
   ];
makeAllMassPosTensors[masses_List, positions_List]:=
  MapThread[makeSingleMassPostionTensor, {masses, positions}];
ChemComputeInertialTensor[masses_List, positions_List]:=
  Total@makeAllMassPosTensors[masses, positions];
```

and with the knowledge that `MapThread` loops over two lists at once (like `zip` with a [python comprehension](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html)) and that `Total` is equivalent to the python `sum`, this all should make sense, now.

**Step 7**: tell the "story" of the function

> This is a function that takes a set of masses and their positions and returns the moment of inertia tensor of the system
> It does this by looping over the masses and positions together and generating a subtensor.
> Once it has this list of subtensors it adds them all up and returns the total matrix.


## Adding in Context

Everything we've focused on thus far is in the context of single functions in isolation and figuring out what they do mechanistically.
Once thing that becomes especially relevant as the code becomes more complex is knowing the context in which the function was written.
Usually with a package this means looking at any documentation you can find, be it package or module level READMEs, posts, or git commit messages.

In the absence of requests, I'm not gonna give examples of this, but this basically changes the "story" that the function tells rather than anything else. I.e. instead of saying

> This is a function that takes a set of masses and their positions and returns the moment of inertia tensor of the system
> It does this by looping over the masses and positions together and generating a subtensor.
> Once it has this list of subtensors it adds them all up and returns the total matrix.

if we know this will be applied to molecular systems as part of a reaction-path calculation we could say

> This is a function that takes a set the masses and positions of the atoms in a molecular system and returns the moment of inertia tensor of the system. Its primary use case is for obtaining rotational eigenvectors.
> It does this by looping over the atoms and generating a moment of intertia tensor for that atom's rotations.
> Once it has this list of subtensors it adds them all up and returns the total matrix.

obviously the function can be applied to _any_ set of masses and positions, but the context makes the function a bit easier to remember/make sense of.

Next: [Reading Math](ReadingMath.md)<br/>
Previous: [A Hierachical View of Problem Solving](AHierarchicalViewOfProblemSolving.md)<br/>
Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)

---

1. <a id="fn1"></a> There are tons of different terms for different kinds pieces code. _scripts_ are little pieces of code that were written once without the intent to reuse--try to avoid writing scripts, they're sometimes quick, but they lack of reusability and the laziness with which they are often written means they're a bad habit and will probably cause you more grief than just writing the code well the first time. Other names for chunks of code: _functions_ are the smallest useful unit of code, _classes_ are single objects, _packages_ are small-to-medium sized accumulations of functions and classes intended for a single purpose, _libraries_ are large scale accumulations of functions and classes usually with a few different purposes that are written to be by other pieces of code, _interfaces_ are layers that either connect different libraries and packages together or feed user input into a library/package, _applications_ are collections of interfaces and libraries that serve a few purposes and are intended to hide all of the complexity of the code altogether. A well-designed application is a super powerful tool, but is also usually overkill. Aim to never write scripts, mostly write packages, and occasionally write a library.
2. <a id="fn2"></a> Matrix representations are a somewhat subtle (although not particularly challenging) concept, but I've written about them before at some length [here](https://stackoverflow.com/c/mccoygroup/questions/74).
3. <a id="fn3"></a> Unfortunately, linear algebra is pretty much unavoidable in quantum mechanics. On the plus side, it's some of the simpler math you'll ever have to learn! In essence, it's a _complexity hiding_ strategy for operations that can be expressed in terms of sums and products. The _dot product_ is just an operation where you multiply two lists of numbers by each other and then add them all up to get another number. It seems too simple to be useful, but actually ends up rearing its head all over the place. A _tensor_ is just a three- or higher-dimensional matrix. They suck to think about, but all the standard 2D matrix tricks end up generalizing quite nicely.
4. <a id="fn4"></a> [Mathematica](https://mathematica.stackexchange.com/) is a super powerful language and scientific platform _if you use it well_, but will likely cause you to cry tears of blood when you first start with it because it's so different from python-like programming languages. I highly recommend learning it if you have the time, but also totally understand that most people are time constrained. It took me ~2 years before I started to use it really well, but now I can do stuff that takes hundreds to thousands of lines of python code in tens of lines of Mathematica code. It's also a fun intro to [functional](https://mresources.github.io/tutorial/mathematica-programming/functional-programming/procedural-programming.html) and [rule-based](https://mresources.github.io/tutorial/mathematica-programming/code-structure/replacement-patterns.html) programming.

[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2
[<sup>3</sup>]: #fn3
[<sup>4</sup>]: #fn4

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Intro%20To%20Quantum/ReadingAFunction.md)
