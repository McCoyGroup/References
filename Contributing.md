---
---

# Contributing

If you'd like to contribute, first off, thanks!

This page exists to hopefully make it easier for you to add to the site / make your content look the way you want

We'll keep adding more details on how everything should be set up as we work through it.

<div class="container alert alert-secondary bg-light">
 <div class="row">
  <div class="col">
   <span class="text-muted">GitHub Pages:</span>
  </div>
  <div class="col" markdown="1">
   [Intro](#GH_Pages)
  </div>
  <div class="col" markdown="1">
   [Edit](#editing-pages)
  </div>
  <div class="col" markdown="1">
   [New](#new-pages)
  </div>
  <div class="col" markdown="1">
   [Upload](#upload-files)
  </div>
  <div class="col" markdown="1">
   [Jekyll](#jekyll)
  </div>
 </div>
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
  <div class="col" markdown="1">
   [Images](#boostrap-images)
  </div>
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
 <div class="row">
  <div class="col">
   <span class="text-muted">Plugins:</span>
  </div>
  <div class="col" markdown="1">
   [SEO](#jekyll-seo-tag)
  </div>
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
 </div>
</div>

---

GitHub Pages
------------

<a id="GH_Pages"></a>
We're running everything through [GitHub Pages](https://pages.github.com/), so you can edit all the content on GitHub itself.
GitHub Pages is designed so that people can write content in a GitHub repository, and then GitHub will do the hard work of turning that into a website that people an view.

You'll notice that our website lives at [mccoygroup.github.io/References/](https://mccoygroup.github.io/References/). That's because it's served from the [References](https://github.com/McCoyGroup/References) repository under the [McCoy Group](https://github.com/McCoyGroup) GitHub organization.

This means if you want to get maximum editing convenience/power you can clone the repository, edit locally, and push back to the cloud once you're done.

### Editing Pages

Everything on this site can be editing. 
Even this page can be edited using the link at the bottom at the page.

That edit link works because it takes us to the file as hosted on GitHub (i.e. [here](https://github.com/McCoyGroup/References/blob/gh-pages/Contributing.md)) and then goes straight to the [Edit](https://github.com/McCoyGroup/References/edit/gh-pages/Contributing.md) tab.

### New Pages

If you want to make a new page, the same idea applies. In this case, let's say we want to make a new file under the McCode Academy section. 
We can do this one of two ways. The first is through GitHub's user-interface. We first go to the [main repository](https://github.com/McCoyGroup/References), then click through the file tree to the folder we want to add a file to, i.e. [here](https://github.com/McCoyGroup/References/tree/gh-pages/McCoy%20Group%20Code%20Academy), and then we use the `Add File` mechanism on the page to create a new file.

The second option is to go directly to the appropriate link. 
This is powerful if we want to make it easy for people to add content to a specific section the site.
Instead of going through the UI, we just start with the base new-page URL: [https://github.com/McCoyGroup/References/new/gh-pages/](https://github.com/McCoyGroup/References/new/gh-pages/) and then add on the subpath to our folder, in this case that's `McCoy%20Group%20Code%20Academy/`, giving us the direct new page link [https://github.com/McCoyGroup/References/new/gh-pages/McCoy%20Group%20Code%20Academy/](https://github.com/McCoyGroup/References/new/gh-pages/McCoy%20Group%20Code%20Academy/).

### Uploading 

We can upload files, as well, using this mechanism. For that, we can use the same UI as for creating a new page, but instead of creating a new file, we choose to upload one.

Alternately, we can use a direct upload link, e.g. if we want to upload to the exercises `Data` folder in the McCode Academy section we would give people the link: [github.com/McCoyGroup/References/upload/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Data](https://github.com/McCoyGroup/References/upload/gh-pages/McCoy%20Group%20Code%20Academy/Exercises/Data).

### Jekyll & Finx

GitHub pages uses [Jekyll](https://jekyllrb.com/) to convert our content into HTML pages. Jekyll is a powerful little program, written in the [ruby](https://www.ruby-lang.org/en/) programming language. 
We won't get into the details of how to use Jekyll here, but if you ever have questions about how to do something with it, the internet is a great resource.

Jekyll uses a site theme mechanism so that every page can look basically the same. I wrote us a theme that I called [finx](https://github.com/McCoyGroup/finx) (for fake [Sphinx](https://www.sphinx-doc.org/en/master/)). I am not opposed to other people going in an customizing it to change up the look. You can easily do that by editing the [styles.css file](https://github.com/McCoyGroup/finx/blob/master/assets/css/style.css).

If you want to test changes locally before committing them in full, you can clone the References repository, clone finx, and use Jeklly locally to run a server on your laptop after tweaking the [_config.yml](https://github.com/McCoyGroup/References/blob/gh-pages/_config.yml) file. This is a standard thing that web developers do.

If you want to do larger theme edits, you'll also want to learn about the [Liquid template language](https://jekyllrb.com/docs/liquid/).

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


### Boostrap Images

Since we're using Kramdown and Bootstrap, we can leverage the power of Bootstrap's image utilities.

If we want a little [thumbnail image](https://getbootstrap.com/docs/4.0/content/images/#image-thumbnails), that means we can do

```lang-none
![logo](../img/logo_m.png){:.img-thumbnail width="100px"}
```
![logo](../img/logo_m.png){:.img-thumbnail width="100px"}

or if we want a big banner we can do

```lang-none
![logo](../img/logo_banner.png){:.img-fluid}
```
![logo](../img/logo_banner.png){:.img-fluid}

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

Plugins
---

Jekyll supports a pretty rich plugin mechanism so that you can add new features without having to do a bunch of work yourself.
If we add plugins, we'll want to discuss them here.

### SEO

Jekyll has a standard plugin for making stuff work with usual search engine optimization/social media frameworks. This this is called [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag). We added it to the site so that links would look better when shared on Slack.

This thing is super useful, and allows you to specify an image, or description, or all sorts of stuff on a page-by-page basis & have that show up when you share a link with someone. Check out the [docs](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md) for more.


---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Contributing.md)
