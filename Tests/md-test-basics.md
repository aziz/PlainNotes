[TOC]

# Italic and Bold

_italic_
_italic one_ not italic _italic two_
_italic\__
_italic \__
*italic__*
_all _ italic_
\\\\_italic\\_
\\\\_italic\\\_\\\\_
\\\\_italic\\_

***

stuff * not italic*
\_ not italic _
_not italic _
\\\\_not italic\_
_not italic \_
\\\_not italic\\_
_not italic
not end italic_

***

__bold__

**bold\***

***

***bold and italic***
**_bold and italic_**
*__bold and italic__*
___bold and italic___
__*bold and italic*__
_**bold and italic**_

### Multi line bold and italic

_italic
end italic_

__multi line bold
end bold__

### Underscore In Words

The word `complicated` must be neither bold nor italic below:

perform_complicated_task
perform__complicated__task

But the first part below is italic and bold respectively:

_perform_complicated_task
__perform__complicated__task

# Strikethrough

~~This text should be parsed as _strikethroughed_.~~

~~There may be __bold__ or _italic_ text inside strikethroughed text.~~

~~There may be ![Mou icon](mo.com) a keyboard `complicated` shortcut like [GFM][GFM] inside strikethroughed text.~~

__There may be ~~strikethroughed text~~ inside bold text.__
_There may be ~~strikethroughed text~~ inside italic text._

~~ If there is a space in the beginning or end, it won't work as per the [GFM][GFM] docs ~~

~~Strikethrough can be applied to
multiple lines. Just keep in mind
not to put any space in the beginning or end.~~

# URLs

An email <example@example.com> link.
Simple inline link <http://chenluois.com>
Normal plain link http://example.com/
Complex url https://github.com/SublimeText-Markdown/MarkdownEditing/issues?page=1&state=closed

# Image Links

![Mou icon](http://mouapp.com/Mou_128.png)
![Alt text](/path/to/img.jpg "Optional title")

# Links

[empty link][]
[Smaller](http://smallerapp.com)
[Resize](http://resizesafari.com "a Safari extension")
[reference style][id]
[test][1]

# Link References

[foo]: http://example.com/

[2]: http://example.com/  "Optional Title Here"

[3]: http://example.com/  'Optional Title Here'

[4]: http://example.com/  (Optional Title Here)

[4]: http://example.com/  (Optional Title Here)

# Code Inline

`raw more`

``dobule ` raw``

`raw \` more`

# Code block

    This is code.
    Isn't it pretty!

    single line

# Headings

heading 1
=========       

heading 2
---------

## heading 2

### heading 3

#### heading 4

##### heading 5

###### heading 6

# Quotes


> Here is a quote block
This quote continues on.  Line breaking is OK in markdown
> Here it is again
> Lah-di-dah
> I should really match headings in here too:
>
> ## This is a heading in a block quote
> 
> - list items
> - inside block
> - quote
> 
> 1. numbered list 
> 2. numbered list another
>
> ✔ done todo
> ✘ cancelled todo
> ☐ pending todoa
>
> - [x] complete with x
> - [X] complete with X
> - [✔] complete with special character
> - [ ] incompleted
> - [ ] last element
> 
> 1. [ ] a task list item
> 2. [ ] list syntax required
> 3. [ ] normal **formatting**, @mentions, #1234 refs
> 3. [ ] incomplete
> 3. [x] completed
> 
> ---
>
> `code` **bold** *italic* [Link]() [[internal link]] :tag:
>
> > This is nested blockquote.
>
>     return shell_exec("echo $input | $markdown_script");
>

>
> >  
> > > # very deeply nested 
> >  
>

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

# Horizontal lines

***

* * *

___

__ __ __

- - -

----------------

# HTML

<!-- Here is HTML Comment -->

<!--
multi line html comment
can go here
-->

<span class="inline">test inside **span**  [link][]</span>

<span class="inline">
test inside **span**  [link][]
</span>

<div class="block">test inside **block**  [link][]</div>

<div class="block">
test inside **block**  [link][]
</div>

<ul id="ProjectSubmenu">
    <li><a href="#2" title="Markdown Project">Main</a></li>
    <li><a href="#1" title="Markdown Basics">Basics</a></li>
</ul>

``` html
<span class="inline">test inside **span**  [link][]</span>
```

``` html
<div class="block">
test inside **block**  [link][]
</div>
```

``` html
<ul id="ProjectSubmenu">
    <li><a href="#2" title="Markdown Project">Main</a></li>
    <li><a href="#1" title="Markdown Basics">Basics</a></li>
</ul>
```

