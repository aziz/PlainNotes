
# Inline styles

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

~~There may be a keyboard shortcut like <kbd>Enter</kbd> inside strikethroughed text.~~

__There may be ~~strikethroughed text~~ inside bold text.__
_There may be ~~strikethroughed text~~ inside italic text._

~~ If there is a space in the beginning or end, it won't work as per the [GFM][GFM] docs ~~

~~Strikethrough can be applied to
multiple lines. Just keep in mind
not to put any space in the beginning or end.~~


***

`raw more`

``dobule ` raw``

`raw \` more`

# URL Highlight

An email <example@example.com> link.
Simple inline link <http://chenluois.com>
Normal plain link http://example.com/
Complex url https://github.com/SublimeText-Markdown/MarkdownEditing/issues?page=1&state=closed

# Test: Image Links

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

# Headings

heading 1
=========


heading 2
---------

## heading 2

### heading 3

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

# Code block

    asdfsdafasdf
    This is code.
    Isn't it pretty!

# Quotes


> Here is a quote block
This quote continues on.  Line breaking is OK in markdown
> Here it is again
> Lah-di-dah
> I should really match headings in here too:
> ## This is a heading in a block quote
>
> - list items
> - inside block
> - quote
>
> `sadsd` **sads** *sdsad*

# Horizontal lines

***

* * *

___

__ __ __

- - -

----------------

# Fenced Code Blocks

## In / Near List Items

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

## In / Near Paragraphs

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

***

Below is not any type of code block. It _should not_ be highlighted.

Paragraph
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```


# Keyboard Shortcuts

A keyboard shortcut <kbd>Enter</kbd> can be in paragraph.

* A keyboard shortcut <kbd>Enter</kbd> can be in list.

_A keyboard shortcut <kbd>Enter</kbd> can be in italic._
__A keyboard shortcut <kbd>Enter</kbd> can be in bold.__

~~A keyboard shortcut <kbd>Enter</kbd> can be in deleted text.~~

<p>A keyboard shortcut <kbd>Enter</kbd> can be in HTML.</p>

<div>
    A keyboard shortcut <kbd>Enter</kbd> can be in block level tags.
</div>

# Footnotes

That's some text with a footnote.[^1]

[^1]: And that's the footnote.


# Tables

| First Header | Second Header | Third Header |
|--------------|---------------|--------------|
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

First Header | Second Header | Third Header
------------ | ------------- | ------------
Content Cell | Content Cell  | Content Cell
Content Cell | Content Cell  | Content Cell

| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

First Header | Second Header | Third Header
:----------- | :-----------: | -----------:
Left         | Center        | Right
Left         | Center        | Right