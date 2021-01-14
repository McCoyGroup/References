# <a id="McUtils.Zachary.Surfaces">McUtils.Zachary.Surfaces</a>
    
This provides a unified interface for handling "surfaces" i.e. functions that map from coordinate space to the real line
The interface provides multiple different modes of surface specification, allowing for Taylor series data,
expansions basis expansions, or analytic representations.
The idea is to provide a unified interface that represents the _concept_ while allowing for flexibility in implementation.
Specific types of surfaces, like PES and dipole surfaces can be layered on top as superclasses and provided their own bespoke importers.

### Members:

  - [BaseSurface](Surfaces/BaseSurface/BaseSurface.md)
  - [TaylorSeriesSurface](Surfaces/BaseSurface/TaylorSeriesSurface.md)
  - [LinearExpansionSurface](Surfaces/BaseSurface/LinearExpansionSurface.md)
  - [LinearFitSurface](Surfaces/BaseSurface/LinearFitSurface.md)
  - [InterpolatedSurface](Surfaces/BaseSurface/InterpolatedSurface.md)
  - [Surface](Surfaces/Surface/Surface.md)
  - [MultiSurface](Surfaces/Surface/MultiSurface.md)

### Examples:



___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/Zachary/Surfaces.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/Zachary/Surfaces.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/McUtils/Zachary/Surfaces.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/McUtils/Zachary/Surfaces.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/McUtils/edit/master/Zachary/Surfaces/__init__.py?message=Update%20Docs)