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

# Abbreviations

example: this is HTML (right after paragraph)
*[HTML]: Hyper Text Markup Language

*[HTML]: Hyper Text Markup Language

# Attribute Lists

{: #someid .someclass somekey='some value' }
{: #an_id .a_class }
{: #someid }
{: #some_id }
{: #some-id }
{: .someclass }
{: somekey='some value' }
{: somekey="some value" somekey="some value" }
{: #an_id somekey="some value" somekey="some value" #sad .a_class somekey="some value" somekey="some value" }

This is a paragraph.
{: #an_id .a_class }

- list
- list
{: #someid .someclass somekey='some value' }


A setext style header {: #setext }
==================================


A setext style header {: #setext2 }
-----------------------------------


### A hash style header ### {: #hash3 }

[link](http://example.com){: class="foo bar" title="Some title!" }

[linkref][linkref]

![img](url){: #id .class}
![img][linkref]

[linkref]: http://alaki.com "optional title" {: #id .class}

![img][linkref]

[linkref]: http://alaki.com "optional title"

# Footnotes

That's some text with a footnote.[^1]
This line has a multiline footnote[^2]
Footnotes[^1] have a label[^label] and a definition[^!DEF].

[^1]: This is a footnote
[^2]: The first paragraph of the definition.
    Paragraph two of the definition.
    
    > A blockquote with
    > multiple lines.

        a code block
    A final paragraph. of footnote
[^label]: A footnote on "label"
[^!DEF]: The definition of a footnote.

Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]: A footnote on the label: "@#$%".
A footnote label must start with a caret ^ and may contain any inline text (including spaces) between a set of square brackets []. Only the first caret has any special meaning.

A footnote content must start with the label followed by a colon and at least one space. The label used to define the content must exactly match the label used in the body (including capitalization and whitespace). The content would then follow the label either on the same line or on the next line. The content may contain multiple lines, paragraphs, code blocks, blockquotes and most any other markdown syntax. The additional lines must be indented one level (four spaces or one tab).

When working with multiple blocks, it may be helpful to start the content on a separate line from the label which defines the content. This way the entire block is indented consistently and any errors are more easily discernible by the author.

[^1]: 
    The first paragraph of the definition.

    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.

# Math

### Multi Markdown Latex based formulas

An example of math within a paragraph --- \\({e}^{i\pi }+1=0\\)
--- easy enough.
    
And an equation on it's own:
    
\\[ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\]
