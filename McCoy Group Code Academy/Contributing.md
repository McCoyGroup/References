---
---

# Contributing

If you'd like to contribute, first off, thanks!

This page exists to hopefully make it easier for you to add to the site / make your content look the way you want

We're running everything through GitHub Pages, so you can edit all the content on GitHub itself.
Even this page can be edited using the link at the bottom at the page.

New pages can be made using GitHub's built-in Add File mechanism, and files can be uploaded using the Upload File button.

We'll keep adding more details on how everything should be set up as we work through it.

<div class="container alert alert-secondary bg-light">
 <div class="row">
  <div class="col">
   <span class="text-muted">Markdown:</span>
  </div>
  <div class="col" markdown="1">
   [Headers](#Markdown_headers)
  </div>
  <div class="col" markdown="1">
   [Links](#Markdown_links)
  </div>
  <div class="col" markdown="1">
   [Italics](#Markdown_font-styles)
  </div>
  <div class="col" markdown="1">
   [Code](#Markdown_code)
  </div>
  <div class="col" markdown="1">
   [Quotes](#Markdown_quotes)
  </div>
 </div>
 <div class="row">
  <div class="col"></div>
  <div class="col" markdown="1">
   [Lists](#Markdown_lists)
  </div>
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
 <div class="row">
  <div class="col">
   <span class="text-muted">Customization:</span>
  </div>
  <div class="col" markdown="1">
   [Footnotes](#footnotes)
  </div>
  <div class="col" markdown="1">
   [Styling](#styling)
  </div>
  <div class="col" markdown="1">
   [Sublinks](#direct-content-links)
  </div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
 <div class="row">
  <div class="col">
   <span class="text-muted">Standards:</span>
  </div>
  <div class="col" markdown="1">
   [Next/Prev](#nextprevious-buttons)
  </div>
  <div class="col" markdown="1">
   [Footer](#footer)
  </div>
  <div class="col" markdown="1">
   [Unfinished](#unfinished-content)
  </div>
  <div class="col" markdown="1">
   [Jumps](#jump-links)
  </div>
  <div class="col"></div>
 </div>
</div>

---

Markdown
---

All pages on the site are written in [Markdown](https://www.markdownguide.org/getting-started/).
Markdown is a miniature mark-up language that tries to include 90% of what people need to do when writing content for the web.
Here's the brief overview.

<a id="Markdown_headers"></a>
* `#`, `##`, and `###` generate headers

# This is a main header
## This is a subheader
### This is a subsubheader
```
# This is a main header
## This is a subheader
### This is a subsubheader
```

<a id="Markdown_links"></a>
[This is a link](https://thisisalink.fake)<br/>
![This tries to load an image](https://thisisanimage.fake)
```
[This is a link](https://thisisalink.fake)
![This tries to load an image](https://thisisanimage.fake)
```

<a id="Markdown_font-styles"></a>
_this is italic_<br/>
**this is bold**
```
_this is italic_
**this is bold**
```

<a id="Markdown_code"></a>
You can create inline code blocks using backticks, e.g `this` comes from the Markdown ``\`this\```.
You can create code blocks using three backticks + a language, e.g.
```python
def this_is_a_python_block():
   ...
```
````lang-none
```python
def this_is_a_python_block():
   ...
```
````

<a id="Markdown_quotes"></a>
You can create block quotes using `>`, like
> this is a quote
> and it continues
```lang-none
> this is a quote
> and it continues
```

<a id="Markdown_lists"></a>
You can create lists quotes using `* ` or numbers like `1.`
* this is
* a list
  * with a sublist
1. this is
2. a numbered list
   * with a regular sublist
3. but the regular one continues
```lang-none
* this is 
* a list
  * with a sublist
1. this is
2. a numbered list
   * with a regular sublist
3. but the regular one continues
```

As you want to do more and more stuff, there are tons of Markdown resources out there so definitely give them a look.

---

Customization
-------------

There are lots of ways to add more intricate content to your pages. Here are a few of them.

### Footnotes

If you want to add footnotes, you can do that too.
For an example, see [this](https://github.com/McCoyGroup/References/edit/gh-pages/References/Intro%20To%20Quantum/PracticalQuantumMechanics.md).
To do that, you'll first put a link inside the text like
```
This is my contentious statement.[<sup>1</sup>]
```

Then in the footer you'll put a link to `#fn1` and the browser will scroll to the bottom of the page when clicked. So something like
```
This is my contentious statement.[<sup>1</sup>]
This is another contentious statement.[<sup>2</sup>]

...

---
[<sup>1</sup>]: #fn1
[<sup>2</sup>]: #fn2

1. <a id="fn1"></a> This is my justification for the first contentious statement.
2. <a id="fn2"></a> This is my justification for the second contentious statement.

[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```

### Styling

If you're comfortable with the languages of web programming, here are some helpful hints.

GitHub pages uses Jekyll to render its Markdown by default.
Our config file for this is [here](../_config.yml).

As of when I write this, we're using [Kramdown](https://kramdown.gettalong.org/quickref.html) as our Markdown renderer. The theme is one I developed specifically for this, which you can find [here](https://github.com/McCoyGroup/finx).

This is important, because Kramdown supports a non-standard syntax to add styling to elements which looks like
```lang-none
This is a test
{: .test-class}
```

where `test-class` is a CSS class.

Now combining that with the fact that the theme builds off of [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) we can make use of their huge library of styling classes to add stuff to our text, e.g.

You can do this too!
{: .alert-primary .rounded-pill .p-3}

```lang-none
You can do this too!
{: .alert-primary .rounded-pill .p-3}
```

I also wrote a syntax layer for doing pattern matching and adding annotations on the generated HTML. You can see an example of that [here](https://github.com/b3m2a1/annotateMD/blob/master/annotations/simple_transforms.ts). That's all done in TypeScript, so feel free to dive into it if you want to add more complex interactions to the pages.
This will definitely be a steeper learning curve than the Bootstrap CSS, though.

### Direct Content Links

All modern browsers support a URL syntax like

```lang-none
https://path.to/site#Header_In_Site
```

where `Header_In_Site` is attached to the `id` attribute of the header. The browser will try to scroll directly to that header.

Headers on this site automatically get an `id` tag associated with them, so you can directly link to them. On the other hand, you can make your own custom element, by adding a tag like

```lang-none
<a id="name-of-link"></a>
```

at any point in your content and then you can link to it by adding `#name-of-link` to the URL you link to.

---

Standard Elements
-----------------

We've got a few "standard" elements that define the visual style we're going for with the site.
It'd be good to go with them, at least for now.
As we add more ideas we can add more stuff here.

Most of this stuff _should_ be pushed into the theme and configured with page variables, but for now we're showing how to add it in hard-coded style.
We'll move stuff to the theme when we can, though.

### Next/Previous Buttons

In lots of our content we introduce pagination, where we have Next/Previous links. For these we're introducing a syntax that looks like

<span class="text-muted">Next:</span>
 [Next Page](NextPage.md)<br/>
<span class="text-muted">Previous:</span>
 [Previous Page](PreviousPage.md)
```lang-none
<span class="text-muted">Next:</span>
 [Next Page](NextPage.md)<br/>
<span class="text-muted">Previous:</span>
 [Previous Page](PreviousPage.md)
```

This just helps separate the links from the content that came before it.

### Footer

To make it easy to edit files, we're providing a standardized footer at the bottom of our pages, which in Markdown looks like

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```lang-none
---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```

For pages where we can foresee questions, we're putting a link above the `---` so that it looks like

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```
Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask).
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/References/McCoy%20Group%20Code%20Academy/<Path/To/Page.md>)
```

If we want to give external people places to report issues, we can provide a link to the GitHub issues page

Find an issue? [Report it!](https://github.com/McCoyGroup/References/issues/new)
{: .alert .alert-warning}
```
Find an issue? [Report it!](https://github.com/McCoyGroup/References/issues/new)
{: .alert .alert-warning}
```

### Unfinished Content

We're also adding a standard way to show that a segment still needs to be finished.

This will look like

...<br/>
[EDIT](https://github.com/McCoyGroup/References/edit/gh-pages/path/to/file.md)
{: .alert .alert-warning}

```
...<br/>
[EDIT](https://github.com/McCoyGroup/References/edit/gh-pages/path/to/file.md)
{: .alert .alert-warning}
```

### Jump Links

For long pages, it can be helpful to have a collection of jump links at the top of a page (i.e. like the one on this page).
This is built as a Markdown list, but we wrap it in some styling for thematic consistency.

We use the Bootstrap [grid](https://getbootstrap.com/docs/4.5/layout/grid/) layout system for these, which basically has you designate an outer `container` and a set of `row` objects which contain a series of `column` objects.
It's a little confusing at first, but surprisingly easier to maintain than a Markdown table.

<div class="container alert alert-secondary bg-light">
 <div class="row">
  <div class="col" markdown="1">
   [A Content Link](#Header_To_Link_To)
  </div>
  <div class="col" markdown="1">
   [Another Content Link](#Header_To_Link_To2)
  </div>
  <div class="col" markdown="1">
   [Yet Another Content Link](#Header_To_Link_To3)
  </div> <div class="col" markdown="1">
   [We Can Do Up To 12](#Header_To_Link_To4)
  </div>
 </div>
 <div class="row">
  <div class="col" markdown="1">
   [And We](#Header_To_Link_To2_1)
  </div>
  <div class="col" markdown="1">
   [Can Have](#Header_To_Link_To2_2)
  </div>
  <div class="col" markdown="1">
   [As Many](#Header_To_Link_To2_3)
  </div>
  <div class="col" markdown="1">
   [Rows As](#Header_To_Link_To2_4)
  </div>
  <div class="col" markdown="1">
   [We Want](#Header_To_Link_To2_5)
  </div>
 </div>
 <div class="row">
  <div class="col" markdown="1">
   This isn't even a link...{: .text-muted}
  </div>
  <div class="col" markdown="1">
   [Here's a Third Row](#Header_To_Link_To4)
  </div>
 </div>
</div>

Admittedly you'll probably have no more than one row... If you don't want the links to stretch, you can make "empty" columns. Here's a good example. I've personally found that a 6-column layout isn't bad.

<div class="container alert alert-secondary bg-light">
 <div class="row">
  <div class="col" markdown="1">
   [Header 1](#Header_1)
  </div>
  <div class="col" markdown="1">
   [Header 2](#Header_2)
  </div>
  <div class="col" markdown="1">
   [Header 3](#Header_3)
  </div>
  <div class="col" markdown="1">
   [Header 4](#Header_4)
  </div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
 <div class="row">
  <div class="col" markdown="1">
   [Header 1](#Header_1)
  </div>
  <div class="col" markdown="1">
   [Header 2](#Header_2)
  </div>
  <div class="col" markdown="1">
   [Header 3](#Header_3)
  </div>
  <div class="col" markdown="1">
   [Header 4](#Header_4)
  </div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
</div>

```html
<div class="container alert alert-secondary bg-light">
 <div class="row">
  <div class="col" markdown="1">
   [Header 1](#Header_1)
  </div>
  <div class="col" markdown="1">
   [Header 2](#Header_2)
  </div>
  <div class="col" markdown="1">
   [Header 3](#Header_3)
  </div>
  <div class="col" markdown="1">
   [Header 4](#Header_4)
  </div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
 ...
</div>
```


---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/Contributing.md)
