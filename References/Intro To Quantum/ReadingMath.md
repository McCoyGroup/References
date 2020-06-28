# Reading Math

This is the section where I'm hoping to convince you that the math we work with is really not so bad and that you can do it too.
So pls be convinced.
We're going to treat mathematical expressions the exact same way we treated our code, that is we'll say

> A math expression...
* Takes a set of inputs
* Applies a series of transformations to the data to return an output
* Tells a "story"

What's pretty convenient is these expressions are inherently hierarchical, so if we're given the expression

$$
\int _0^{2 \pi }\int _0^{\infty }f (\theta) g(r)+ \frac{\partial f}{\partial \theta }(\theta_e)g(r) dr d\theta
$$

we can restructure this like

$$
\begin{array}{c}
 \left(\int _0^{\, 2\pi }f(\theta )d\, \theta  \right) * \left(\int _0^{\, \infty }g(r)d\, r\right) \\
 + \\
 \left(\frac{\partial f}{\partial \theta }\left(\theta _e\right)\right) * \left(\int _0^{\, 2\pi }d\, \theta \right) * \left(\int _0^{\, \infty }g(r)d\, r\, \right) \\
\end{array}
$$

then we can replace the expressions with a symbolic equivalent

```lang-none
Plus[
  Times[
    Integrate[f[Theta], {Theta, 0, 2Pi}], 
    Integrate[g[r], {r, 0, Infinity}]
    ],
  Times[
   Derivative[f[Theta]][Theta_e]
   Integrate[{Theta, 0, 2Pi}],
   Integrate[g[r], {r, 0, Infinity}]
   ]
  ]
```

and hopefully the hierarchy of statements is pretty clear there. 

What's also noteworthy is that _all_ mathematical expressions can be represented like this.

Keep in mind, too, that this isn't the only possible partitioning.
We could just have easily split it up like

$$
\left(\int _0^{\, \infty }g(r)d\, r\right)*\left(\int _0^{\, 2\pi }f(\theta ) +\frac{\partial f}{\partial \theta }\left(\theta _e\right)d\, \theta \right)
$$

and then gotten

```lang-none
Times[
  Integrate[g[r], {r, 0, Infinity}],
  Integrate[
    Plus[f[Theta], Derivative[f[Theta]][Theta_e]],
    {Theta, 0, 2Pi}
    ]
  ]
```

where the only difference is whether we choose to have the outer-most operation be a multiplication or an addition.0

Why does that matter? Well let's think about how we'd turn this expression into a function.

If we took our original expression we'd have

```python
def my_integral(f, g, df, theta_e):
  """Computes the integral as we had it in the beginning"""
  def integrand(theta, r):
     g(r)*f(theta) + df(theta_e)*g(r)
  return integrate(integrand, [0, 2*math.pi], [0, math.infinity])
```

and this requires that our `integrate` function both be able to handle 2D integrals and also probably be very efficient, since our `integrand` isn't particularly simple.

If we were to tell the story of this function it might be

> `my_integral` integrates a two-dimensional integrand over an infinite disk

which isn't particularly compelling. No rising action, no climax, no denouement.

Looking at our next two versions, maybe things are somewhat better

```python
def my_integral_2(f, g, df, theta_e):
  """Computes the integral as we had it in the second form"""
  g_int = integrate(g, [0, math.infinity])
  f_int = integrate(f, [0, 2*math.pi])
  df_te = df(theta_e)
  disk = 2*math.pi
  return g_int*f_int + df_te*disk*g_int
```

and maybe for this one we'd say

> `my_integral_2` integrates two 1D functions and multiplies them together and then by the area of a disk

and for our last version we might have

```python
def my_integral_3(f, g, df, theta_e):
  """Computes the integral as we had it in the third form"""
  g_int = integrate(g, [0, math.infinity])
  def f_integrand(theta):
    df(theta_e) * f(theta)
  f_int = integrate(f_integrand, [0, 2*math.pi])
  return g_int*f_int
```

for which maybe we could say

> `my_integral_3` integrates a radial function `g` and an angular function `f` and takes their product

Of course, you might be thinking "well...okay yes we could do this, but isn't this a distinction without a difference?" and to some degree, yes it is. All of these expressions are equivalent after all.

On the other hand, depending about what we know, this difference could really matter. In particular, let's look at the terms involving $f$.
If we write this as

$$
\int _0^{\, 2\pi }f(\theta ) +\frac{\partial f}{\partial \theta }\left(\theta _e\right)d\, \theta
$$

this is (maybe) harder for the code to integrate than just

$$
\int _0^{\, 2\pi }f(\theta ) d\, \theta
$$

but, crucially, we might know something ourselves about that first integral, like it might be a physical observable or maybe it's part of a different model that we know how to solve.

If that's the case the former is preferable to the latter. Otherwise I'd wager the latter is preferable to the former.

## Breaking Down an Expression

Unfortunately I don't have a set of 100% foolproof rules to be able to assess which is better, but I _do_ have a strategy for how to pick apart an expression and figure out how to make sense of it.

This is effectively five steps:
1. Determine the _context_ of the expression
2. Determine the indivisible components of the expression
3. Try to assign physical meaning to each component
4. Look for those components in related expressions from the broader context
5. Try different groupings of components

Will this always work? Probably not. Will this work for you? Maybe not, but I'm hopeful.

### Examples

TBD.

I think I'd like to break down the expressions involved in an Eckart transformation, the expression for the intensity of an absorption, and then something more abstract like the core idea for a DVR.

Next: [Translating Math Into Code](TranslatingMathIntoCode.md)<br/>
Previous: [Reading a Function](ReadingAFunction.md)<br/>
Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)

---

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/Intro%20To%20Quantum/ReadingMath.md)