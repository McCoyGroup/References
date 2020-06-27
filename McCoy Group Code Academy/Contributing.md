---
---
# Contributing

If you'd like to contribute, first off, thanks!

Secondly, we're running everything through GitHub Pages, so you can edit all the content on GitHub itself.
Even this page can be edited using the link at the bottom at the page.

New pages can be made using GitHub's built-in Add File mechanism, and files can be uploaded using the Upload File button.

We'll keep adding more details on how everything should be set up as we work through it.
For now, feel free to reach out to any of the group members for info.

If you have questions, you can also always ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).

# Markdown

All pages on the site are written in [Markdown](https://www.markdownguide.org/getting-started/).
Markdown is a miniature mark-up language that tries to include 90% of what people need to do when writing content for the web.
Here's the brief overview.

* `#`, `##`, and `###` generate headers

# This is a main header
## This is a subheader
### This is a subsubheader
```
# This is a main header
## This is a subheader
### This is a subsubheader
```

[This is a link](https://thisisalink.fake)<br/>
![This tries to load an image](https://thisisanimage.fake)
```
[This is a link](https://thisisalink.fake)
![This tries to load an image](https://thisisanimage.fake)
```

_this is italic_<br/>
**this is bold**
```
_this is italic_
**this is bold**
```

As you want to do more and more stuff, there are tons of Markdown resources out there so definitely give them a look.

### Footer

To make it easy to edit files, we're providing a standardized footer at the bottom of our pages, which in Markdown looks like

```lang-none
---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```

For pages where we can foresee questions, we're putting a link above the `---` so that it looks like
```
Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```

If we want to give external people places to report issues, we can provide a link to the GitHub issues page
```
Find an issue? [Report it!](https://github.com/McCoyGroup/References/issues/new)
```

If you want to add footnotes, you can do that too.
For an example, see [this](https://github.com/McCoyGroup/References/edit/gh-pages/References/Intro%20To%20Quantum/PracticalQuantumMechanics.md).
To do that, you'll first put a link inside the text like
```
This is my contentious statement.[<sup>1</sup>]
```

Then in the footer you'll put a link to `#fn1` and the browser will scroll to the bottom of the page when clicked. So with all of these bits, the page might look like
```
This is my contentious statement.[<sup>1</sup>]
This is another contentious statement.[<sup>2</sup>]

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).

---
[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2

1. <a id="fn1"></a> This is my justification for the first contentious statement.
2. <a id="fn2"></a> This is my justification for the second contentious statement.

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```


---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/Contributing.md)
