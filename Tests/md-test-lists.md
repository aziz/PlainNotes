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

☐ this is a list
☐ another item
  ☐ with nested
  ☐ items
    ☐ item
    ☐ item
  ☐ another

☐ this is a list
    ☐ with nested
    ☐ items
    ☐ another

asdsadsadsadsas
✘ this is a list
✘ another item
  ✘ with nested
  ✘ items
    ✘ item
    ✘ item
  ✘ another

✘ this is a list
    ✘ with nested
    ✘ items
    ✘ another

### after paragraph
asdsadsadsads
✔ this is a list
✔ another item
  ✔ with nested
  ✔ items
    ✔ item
    ✔ item
  ✔ another

✔ this is a list
    ✔ with nested
    ✔ items
    ✔ another


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
    * sdf * ✘ ☐
    * sdf * + ✔ ✘ ☐
    * sdf * + - ☐ ✘ ☐
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

# TODO list items

- normal list
☐ pending todo

sadasd

✔ done todo

sdasdsdsd
✘ cancelled todo

sads

☐ pending todo

sadsa
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

# Tasklists Github Style 

- [x] complete with x
- [X] complete with X
    - [X] complete with X
    - [X] complete with X
    - [ ] incompleted
- [✔] complete with special character
- [ ] incompleted
- [ ] last element

1. [ ] a task list item
2. [ ] list syntax required
    1. [X] a task list item
    1. [X] a task list item
    1. [X] a task list item
3. [ ] normal **formatting**, @mentions, #1234 refs
3. [ ] incomplete
3. [x] completed

1. [X] a task list item
2. [ ] list syntax required
3. [✔] normal **formatting**, @mentions, #1234 refs
3. [ ] incomplete
3. [x] completed

* [X] a task list item
* [x] list syntax required
* [X] normal **formatting**, @mentions, #1234 refs
* [✘] incomplete
* [x] completed

- [] invalid
- invalid in [ ] between
- invalid at end [ ]


