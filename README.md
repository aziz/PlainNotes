
# [PlainNotes](https://github.com/aziz/PlainNotes)
Simple and pleasant note taking for SublimeText.

With PlainNotes you can:
- Organize notes and thoughts
- Maintain todo-lists
- Write documents

PlainNotes stores and organizes all your notes in a folder and make them accessible with a single shortcut or mouse click.
It also provides you with an enhanced version of Markdown markup and some good looking color schemes for note taking.
It's been designed with these ground rules in mind:
- Plain text is the holy grail
- Plain text shouldn't be that plain
- Simple and Sexy is Sublime

<p align="center">
<img src="http://cl.ly/image/21143i2m3e0n/ss2.png" width="727" height="416"> 
</p>

## Usage
Most of PlainNotes commands are accessible from the SublimeText main menu. You should have a menu item called `Notes` right after `Help`. Although, there are faster and easier ways of running those commnads that are mentioned below.

#### Starting a new note (`super+F4`)
- **Command palette**: Open command palette and search for `Notes: new` command (typing `nn` will probably find it for you).
    + To save note in a subfolder of the root directory use `/`: `"subfolder name"/"note name"`.
- **Shortcut**: By default pressing <kbd>super+F4</kbd> will create a new note. For customizing the shortcut see [Keyboard Shortcuts]() section. 

#### Opening an existing note (`F4`)
- **Command palette**: Open command palette and search for `Notes: List…` command (typing `nl` will probably find it for you), the command will show the *Latest Notes quick panel* from which you can select or search for your file.   
The *Latest Notes quick panel* is sorting files based on their last-edit time, so the note that you have been working on recently should be on top of the list. 
- **Shortcut**: By default pressing <kbd>F4</kbd> will open the *Latest Notes quick panel*. For customizing the shortcut see [Keyboard Shortcuts]() section.

#### Notes Index Card (`ctrl+F4`)
Pressing <kbd>ctrl+F4</kbd> or selecting `Notes: Index` from the command palette will give you the *Notes Index Card* with the list of all notes sorted alphabetically.  
Pressing <kbd>Enter</kbd> on any note will open it in a new tab.

<p align="center">
<img src="http://cl.ly/image/1u0o1x0a2J3c/plainnotes-index.png" width="515" height="437">
</p>

 
#### Change note color
Open command palette and search for `Note: Change Color…`. it will give you a list of 10 different colors that is shown in the above image. Pressing up and down will give you a preview.  
Color of the note is remembered by PlainNotes and whenever you open that file, PlainNotes will set the color-scheme automatically.

#### Change note file extension
You can change the note file extension in settings. To do so, go to `Preferences -> Package Settings -> PlainNotes -> Settings - User` and modify `"note_save_extension":`

### Add yaml front matter to notes
go to `Preferences -> Package Settings -> PlainNotes -> Settings - User` and modify `"enable_yaml"`

## License

Copyright 2014 [Allen Bargi](https://twitter.com/aziz). Licensed under the MIT License

