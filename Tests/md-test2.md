
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

# Code Inline

`raw more`

``dobule ` raw``

`raw \` more`

# Code block

    This is code.
    Isn't it pretty!

    single line

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

# Lists

 * This *is a list!*
 * This is another list item.
   But this one spans *two* lines.
 * Another list item with __inline__ formatting
 * This one is tricky
 * *This is a list*

  Because this should still be a list item.

1. This is a list item too
2. This list is numbered
    3. This is a list item too
    4. This is a list item too
        5. This is a list item too
        6. This is a list item too
    7. This is a list item too
    8. This is a list item too
9. This is a list item too
10. This is a list item too

***

* this is a list
* another item
  * with nested
  * items
    * item
    * item
  * another

* this is a list
    * with nested
    * items
    * another

1986\. This shouldn't be a list.

### Testing list immediately after paragraph
this is a paragraph
- and this
- is a list

### Testing blockquote and code blocks inside a list
* this is a list

   > This is a blockquote.

 this is still part of the 
 list item.

* Lorem ipsum

        This is a code block  
* list continues
* list continues

### More Testing for nested

 + ✔ sadsad

0. normal list
1. ✔ Orange
2. ✘ Yellow
3. ☐ Green
4. Green Light
5. Blue * + - 1. dfsdf
    * dsfsdfdsf
        * ✔ Orange
        + ✘ Yellow
        - ☐ Yellow 
    * sdf * + - 1. ✔ ✘ ☐
    * sdfsdf
    11. sdsa
    12. asdsad
✔ Orange
    ✔ Orange
    ✔ Orange
    ✔ Orange
✘ Yellow
    ✔ Orange
        ✔ Orange
        ☐ Green
        ☐ Green
☐ Green

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
> ---
>
> `code` **bold** *italic* [Link]() [[internal link]] :tag:
>
> > This is nested blockquote.
>
>     return shell_exec("echo $input | $markdown_script");
>

>
>   >  
>   >   > # very deeply nested 
>   >  
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

# Fenced Code Blocks

## In/Near List Items

Below fenced code blocks _should_ be highlighted.

* List item

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

* List item

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

Below are not valid fenced code blocks according to the [GFM docs][GFM].
It says there must be a blank line before the code block. However, GitHub highlights them. So, they _should_ be highlighted.


* List item
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

* List item
```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

### In/Near Paragraphs

Below is _not_ a _fenced_ code block, just a normal code block.

Paragraph

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

***

Below 2 blocks are fenced code blocks. They _should_ be highlighted.

Paragraph

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

Paragraph
```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

~~~js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
~~~

~~~~~~~~~~~~~~~~~js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
~~~~~~~~~~~~~~~~~


***

Below is not any type of code block. It _should not_ be highlighted.

Paragraph
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```
# Tables

| First Header | Second Header | Third Header |
|--------------|---------------|--------------|
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |
|              |               |              |

| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

| Name | Phone |
| Name | Phone |
| _    |       |

|    Name   |   Phone   |
|-----------|-----------|
| Anna      | 123456789 |
| Alexander | 987654321 |
| _         |           |

| Name | Phone |
|======|=======|
| _    |       |

|    Name   |   Phone   |
|===========|===========|
| Anna      | 123456789 |
|-----------|-----------|
| Alexander | 987654321 |
|-----------|-----------|
| _         |           |

|    Name   |   |   Phone   |
|-----------|---|-----------|
| Anna      |   | 123456789 |
| Alexander |   | 987654321 |
|           | _ |           |

|    Name   | Age |   Phone   |
|-----------|-----|-----------|
| Anna      |  32 | 123456789 |
| Alexander |  28_| 987654321 |


|    Name   |   Phone   | Age |             Position             |
|-----------|-----------|-----|----------------------------------|
| Anna      | 123456789 |  32 | Senior Software                  |
|           |           |     | Engineer_                        |
|-----------|-----------|-----|----------------------------------|
| Alexander | 987654321 |  28 | Senior Software Testing Engineer |


| column 1 | column 2 | column 3 |
| <<<<<<<< | >>>>>>>> | ######## |
|----------|----------|----------|
| 1        |    row 1 |    c1    |
| 2        |    row 2 |    c2    |
| 3        |    row 3 |    c3    |
|          |          |          |

| Unordered  List |   Order List  |
|-----------------|---------------|
| - item 1        | # item 1      |
|   - subitem 1   |   # subitem 1 |
|   - subitem 2   | # item 2      |
| - item 2        |   # subitem 2 |

|   *First Header*  | **Second Header** | ~~Third Header~~ |
|-------------------|-------------------|------------------|
| `Content Cell`    | [Content Cell][2] | ![Image][3]      |
| http://google.com | <me@ssd.com>      | some text        |

| Unordered  List | Order List |
|-----------------|------------|
| C++             | D--        |
| E::             | X==        |
|                 |            |


### Supported Syntaxes

**Simple**

|    Name   | Age |
|-----------|-----|
| Anna      |  20 |
| Alexander |  27 |

**EmacsOrgMode**

|    Name   | Age |
|-----------+-----|
| Anna      |  20 |
| Alexander |  27 |

**Pandoc Grid Tables**

+-----------+-----+
|    Name   | Age |
+===========+=====+
| Anna      |  20 |
+-----------+-----+
| Alexander |  27 |
+-----------+-----+

**Pandoc Pipe tables**

**Multi Markdown/Pandoc Pipe tables**

Alignment:

|    Name   | Phone | Age Column |
| :-------- | :---: | ---------: |
| Anna      |   12  |         20 |
| Alexander |   13  |         27 |

| Right | Left | Default | Center |
| ----: | :--- | ------- | :----: |
|    12 | 12   |      12 |   12   |
|   123 | 123  |     123 |  123   |
|     1 | 1    |       1 |   1    |

**RestructuredText**

|    Name   | Age |
+-----------+-----+
| Anna      |  20 |
| Alexander |  27 |

### Column spanning in multimarkdown tables

| First Header  | Second Header | Third Header         |
| :------------ | :-----------: | -------------------: |
| First row     | Data          | Very long data entry |
| Second row    | **Cell**      | *Cell*               |
| Third row     | Cell that spans across two columns  ||
[Table caption, works as a reference][section-mmd-tables-table1] 

| Column 1 | Column 2 | Column 3 | Column 4 |
| -------- | :------: | -------- | -------- |
| No span  | Span across three columns    |||

|               |          Grouping           ||
| First Header  | Second Header | Third Header |
| ------------  | :-----------: | -----------: |
| Content       |          *Long Cell*        ||
| Content       |   **Cell**    |         Cell |
|               |               |              |
| New section   |     More      |         Data |
| And more      |            And more         ||
[Prototype table][]

### table with spacing before and after
*before*

  | Name | Phone |
  | Name | Phone |
  | _    |       |

*after*

| Name | Phone |   
| Name | Phone |   
| _    |       |   

  | Name | Phone |   
  | Name | Phone |   
  | _    |       |  

## NOT SUPPORTED 

### Tables with no pipe at the begining or end

First Header | Second Header | Third Header
------------ | ------------- | ------------
Content Cell | Content Cell  | Content Cell
Content Cell | Content Cell  | Content Cell

First Header | Second Header | Third Header
:----------- | :-----------: | -----------:
Left         | Center        | Right
Left         | Center        | Right

# TODO list items

- normal list
☐ pending todo
✔ done todo
✘ cancelled todo

☐ pending todo
☐ pending todo
✔ done todo
- normal list
- normal list
☐ pending todo
✘ cancelled todo
    ☐ pending todoa
    ✔ done todo
    ✘ cancelled todo
    ☐ pending todoa
    ✔ done todo
✘ cancelled todo

**Should** highlight at the beginning of normal list

- ✔ done inside normal tag
- ✘ cancelled todo
- ☐ pending todo

---

*Should not* highlight

- done ✔ inside normal tag
- cancelled  ✘ todo
- pending ☐ todo

done ✔ inside normal tag
cancelled  ✘ todo
pending ☐ todo

# Internal links

[[internal link]]
[[internal link]][[internal link]]
empty internal link [[]]

an [[internal link]] inside a paragraph
### an [[internal link]] inside a heading
✔ an [[internal link]] inside a done todo
✘ an [[internal link]] inside a cancelled todo
☐ an [[internal link]] inside a pending todo
- inside a list [[internal link]] 

> in block qoute [[internal link]] 

**an [[internal link]] inside a bold text**
*an [[internal link]] inside a italic text*
~~an [[internal link]] inside a Strikethrough text~~

---

*Should not* work with spaces after [[ and before ]]
[[space after ]]
[[ space before]]
[[ space around ]]
[[    a lof of space   ]]

inside_a_word_[[internal_link]]should_not_work
inside_a_word[[internal_link]]should_not_work
inside_a_word[[internal_link]]_should_not_work
inside_a_word_[[internal_link]]_should_not_work

conected_to_a_word_[[internal_link]]
conected_to_a_word[[internal_link]]

connected on right [[internal_link]]should_not_work
connected on right [[internal_link]]_should_not_work


*Should not* work inside code blocks
`an [[internal link]] inside a inline code block`

```
an [[internal link]] inside a fenced block of code 
```

    an [[internal link]] inside a normal block of code 

# Tags

**should work**

:tag:
:multiple:tags:after:eachother:
at the end of sentense :tag:
in the middle :tag: of sentense

### inside a heading :tag:

✔ a inside a done todo :tag:
✘ a inside a cancelled todo :tag:
☐ a inside a pending todo :tag:
- inside a list :tag:

### inside a heading :multiple:tags:after:eachother:
✔ a inside a done todo :multiple:tags:after:eachother:
✘ a inside a cancelled todo :multiple:tags:after:eachother:
☐ a inside a pending todo :multiple:tags:after:eachother:
- inside a list :multiple:tags:after:eachother:

> in block qoute :tag:

### a :tag: inside a heading
✔ a :tag: inside a done todo
✘ a :tag: inside a cancelled todo
☐ a :tag: inside a pending todo
- inside a list :tag: in the middle 

> in block qoute :tag: in the middle

### a :multiple:tags:after:eachother: inside a heading
✔ a :multiple:tags:after:eachother: inside a done todo
✘ a :multiple:tags:after:eachother: inside a cancelled todo
☐ a :multiple:tags:after:eachother: inside a pending todo
- inside a list :multiple:tags:after:eachother: in the middle 

> in block qoute :multiple:tags:after:eachother: in the middle

:tag_with_underscore:

:tag-with-dash:

:a: :b: :c: 

---

*should not work*

::tag::
:space middle:
:space_after :
: space_before:
: space_around :
:    a_lof_of_space   :
inside_a_word_:tag:should_not_work
inside_a_word:tag:should_not_work
inside_a_word:tag:_should_not_work
inside_a_word_:tag:_should_not_work
connected on right :tag:should_not_work
connected on right :tag:_should_not_work
**a :tag: inside a bold text**
*a :tag: inside a italic text*
~~a :tag: inside a Strikethrough text~~

*should not work* but it works and it's not a big deal, very hard to fix: 

conected_to_a_word_:tag:
conected_to_a_word:tag:

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

# Math

### Multi Markdown Latex based formulas

An example of math within a paragraph --- \\({e}^{i\pi }+1=0\\)
--- easy enough.
    
And an equation on it's own:
    
\\[ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\]

# Footnotes

That's some text with a footnote.[^1]
Footnotes[^1] have a label[^label] and a definition[^!DEF].

[^1]: This is a footnote
[^label]: A footnote on "label"
[^!DEF]: The definition of a footnote.

### Multi-line footnote

[^1]: The first paragraph of the definition.
        Paragraph two of the definition.

        > A blockquote with
        > multiple lines.

            a code block

        A final paragraph. of footnote


