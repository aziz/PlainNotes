
# [PlainNotes](https://github.com/aziz/PlainNotes)
Simple and pleasant authoring and note taking for SublimeText.

With PlainNotes you can:
 - Organize notes and thoughts
 - Maintain todo-lists
 - Write documents
 - and probably more

PlainNotes stores and organizes all your notes in a folder and make them
accessible with a single shortcut or mouse click. It also provides you with an
enhanced version of Markdown markup and some good looking color schemes for
note taking.
It's been designed with these ground rules in mind:
 - Plain text is the holy grail
 - Plain text shouldn't be that plain
 - Simple and Sexy is Sublime

<p align="center">
<img src="http://cl.ly/image/21143i2m3e0n/ss2.png" width="727" height="416">
</p>

**Note:** Although PlainNotes works under SublimeText 2, some features might
not be available. We're not actively testing it under SublimeText 2 but will
do our best to make it compatible and usable. We appreciate bug reports and
pull requests.

## Organizing notes

Most of PlainNotes commands are accessible from the SublimeText main menu. You
should have a menu item called `Notes` right after `Help`. Although, there are
faster and easier ways of running those commnads that are mentioned below.

#### Starting a new note (`super+F4`)
- **Command palette**: Open command palette and search for `Notes: new`
  command (typing `nn` will probably find it for you).
  - To save note in a subfolder of the root directory use `/`:
    `"subfolder name"/"note name"`.

- **Shortcut**: By default pressing <kbd>super+F4</kbd> will create a new
  note. For customizing the shortcut see [Keyboard Shortcuts]() section.

#### Opening an existing note (`F4`)
- **Command palette**: Open command palette and search for `Notes: List…`
  command (typing `nl` will probably find it for you), the command will show
  the *Latest Notes quick panel* from which you can select or search for your
  file.
  The *Latest Notes quick panel* is sorting files based on their last-edit
  time, so the note that you have been working on recently should be on top of
  the list.

- **Shortcut**: By default pressing <kbd>F4</kbd> will open the
  *Latest Notes quick panel*. For customizing the shortcut see
  [Keyboard Shortcuts]() section.

#### Jotter (`F1`)
Jotter will let you jot down your thoughts and ideas quickly without
disturbing your work-flow. It opens a *Note Panel* at the bottom of the editor
which is ready to take your note. When you press <kbd>ESC</kbd> it
automatically closes the panel and saves your note with a time stamp in your
*Inbox*.

It can be accessed by pressing <kbd>F1</kbd> (that can be customized in your
Key-bindings if it conflicts with your other key-bindings) or through
`Notes: Jotter` in command palette.
The default color scheme of the jotter panel can be customized in user
settings (`Preferences -> Package Settings -> PlainNotes -> Settings - User`):

```json
{ "jotter_color_scheme": "Packages/PlainNotes/Color Schemes/Sticky-Yellow.tmTheme" }
```

#### Inbox
Inbox is where all your quick notes from *Jotter* live. You can view inbox
through `Notes: Inbox` in command palette or via the Notes main menu.
The date and time format of the note headers in inbox can be customized in user
settings (`Preferences -> Package Settings -> PlainNotes -> Settings - User`):

```json
{
    "jotter_date_format": "%d %b %Y",
    "jotter_time_format": "%I:%M %p"
}
```

#### Notes Index Card (`ctrl+F4`)
Pressing <kbd>ctrl+F4</kbd> or selecting `Notes: Index` from the command
palette will give you the *Notes Index Card* with the list of all notes sorted
alphabetically.
Pressing <kbd>Enter</kbd> on any note will open it in a new tab.

#### Change note color
Open command palette and search for `Note: Change Color…`. it will give you a
list of 10 different colors that is shown in the above image. Pressing up and
down will give you a preview.
Color of the note is remembered by PlainNotes and whenever you open that file,
PlainNotes will set the color-scheme automatically.

#### Archive note
Open command palette and search for `Note: Archive`. This will move the note
into an archive folder than can be specified in the settings -- The default
archive directory is `.archive`. Archiving a note hides it from the Index and
List.

#### Unarchive notes
Open command palette and search for `Note: Unarchive...`. This will open a
list of archived notes sorted by modification date. Selecting one from the
list will unarchive that note.

#### Delete note
Open a note and then open command palette and search for `Note: Delete`.

#### Rename note
Open a note and then open command palette and search for `Note: Rename`.

#### Change note file extension
You can change the note file extension in settings. To do so, go to
`Preferences -> Package Settings -> PlainNotes -> Settings - User` and modify
`"note_save_extension":`. The default note type is `.note` which has the
possibility of setting different note colors and some special markup.
Alternatively you can use any note extension you want such as markdown `.md`.

#### Add yaml front matter to notes
Go to `Preferences -> Package Settings -> PlainNotes -> Settings - User` and
modify `"enable_yaml"`

By default, the following yaml items are added:
```yaml
title:
date:
tags:
```

To add more yaml items you can add them to the settings by modifying `note_yaml:`:

```json
{ "note_yaml" : ["categories"] }
```

#### Other features
- **Open URLs**: place cursor on the link then press `enter` to open a url in
  the browser.
- **Preview images inline**: place cursor on a markdown image with inline image url and press `enter` to a preview popup of that image. You should have ST 3070 or newer for this feature to work.

#### Per-project notes

To have a different notes directory for a project, add the following in your
`.sublime-project` file:

```json
"settings": {
    "PlainNotes": {
        "root": "path/to/notes/dir"
    }
}
```

## Authoring notes
PlainNotes provides an enhanced version of Markdown. It means that you can
write your notes in plain markdown without learning anything new. In addition,
it gives you some extra markups to improve the look and feel of your
documents, since markdown sometime feels too simple to format a real document.

If you are new to markdown here is a cheat-sheet:

|    Markup   |            Markdown Syntax            |
|-------------|---------------------------------------|
| Italic      | `_italic_` or `*italic*`              |
| Bold        | `__bold__` or `**bold**`              |
| Images      | `![Image Title](http://url_to.image)` |
| Links       | `[Link Text](http://link.url)`        |
| Inline Code | `` `code` ``                          |
| Quotes      | `> Here is a quote block`             |
| Separators  | `----` or `*****`                     |
| Heading 1   | `# Heading 1`                         |
| Heading 2   | `## Heading 2`                        |
| Heading 3   | `### Heading 3`                       |
| Heading 4   | `#### Heading 4`                      |

### Extra Markup

#### Admonitions
When writing a note, you might need to distinguish a block or section by
giving it a special title and box. These sections might appear several times
in your document. Some examples would be *Note*, *Tip* or *Caution* blocks in
an article.

Here is how to create an admonition block

    !!! ADMONITION_TYPE "Optional title in quotes"
        Any number of other indented markdown elements.

<img width="640" src="https://cloud.githubusercontent.com/assets/3202/10559318/3d5e5420-74ee-11e5-89b9-0eca42750aca.png" >

By default admonitions block have a purplish background color (that might be
different based on the color scheme), but giving it a specific type from table
below can change the color. Predefined admonition types are listed in table
below and are shown in image above. Note that admonition types can be lower-
case, upper-case or title-case.

| Predefined Admonition Type | Block Color |
|----------------------------|-------------|
| `hint` or `tip`            | bluish      |
| `warning` or `caution`     | yellowish   |
| `danger` or `error`        | reddish     |
| `attention`                | greenish    |

Admonition blocks can have any PlainNotes enhanced markdown inside them and
they customize the look and feel so that everything looks sublime.

<img align="center" width="380" src="https://cloud.githubusercontent.com/assets/3202/10559414/c9a61ff6-74f0-11e5-8209-1c881ebd8506.png" >

## License

Copyright 2014-2015 [Allen Bargi](https://twitter.com/aziz).
Licensed under the MIT License

