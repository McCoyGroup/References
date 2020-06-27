# Tips and Tricks

We have no hope of getting every single tip/trick down here that we use.
On the other hand, hopefully we can get the big ones down.
Especially when it comes to mathematical programming there are things we do in the group that are only ever explained on the internet in super technical ways. We don't want that.
Our goal with this is to make sure that there's an _approachable_ explanation of everything we do + sample code to show that it's totally manageable.
As opposed to the [Examples](../Examples), what we're showing here are simple things that can be done quickly and simply, but which can be hard to find good references for.

With that in mind, here are some of our favorite tips and tricks

## Interpolation

Interpolation is a way to approximate a function. Say we've got a potential energy at a bunch of points from an electronic structure PES scan or something.
If we now want to evaluate the energy at points that weren't in our scan, we can make an interpolating function out of the scan points and energies and evaluate that instead.
Here's some pseudo-code

```
# insert code to do a 1D interpolation of a function
```

## Fitting

Another way to solve the issue of being able to evaluate a function at points not on the grid of values we have is through fitting.
This is probably something you've done before in Excel.
You can really easily do it for yourself, though.

```
# insert code to do a 1D fit of a function to a polynomial
```

## Finite Difference

Another technique that uses a function evaluated at a bunch of grid points.
This one is a way to get an approximation derivative of a function without knowing its analytic form.

```
# insert code to do a 1D second derivative of a function
```

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/TipsAndTricks/index.md)

