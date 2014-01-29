import sublime
import sublime_plugin

import os
import fnmatch
import re

def settings():
    return sublime.load_settings('Notes.sublime-settings')

class NotesListCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        root = settings().get("root")
        window = sublime.active_window()
        self.notes_dir = os.path.expanduser(root)
        self.file_list = self.find_notes()
        window.show_quick_panel([f[0] for f in self.file_list], self.open_note)

    def find_notes(self):
        note_files = []
        for path, subdirs, files in os.walk(self.notes_dir):
            for name in files:
                for ext in settings().get("note_file_extensions"):
                    if fnmatch.fnmatch(name, "*." + ext):
                        note_files.append( ( re.sub('\.' + ext + '$', '', name),
                                             os.path.join(path, name),
                                             os.path.getmtime(os.path.join(path, name))
                                            )
                                          )
        note_files.sort(key=lambda item: item[2], reverse=True)
        return note_files

    def open_note(self, index):
        if index == -1:
            return
        file = self.file_list[index][-1]
        # self.window.run_command("new_pane",{"move": True})
        view = sublime.active_window().open_file(file)


class NotesNewCommand(sublime_plugin.ApplicationCommand):

    def run(self, title=None):
        root = settings().get("root")
        self.notes_dir = os.path.expanduser(root)

        self.window = sublime.active_window()
        if title is None:
            self.window.show_input_panel("Title", "", self.create_note, None, None)
        else:
            self.create_note(title)

    def create_note(self, title):
        file = os.path.join(self.notes_dir, title + ".note")
        if not os.path.exists(file):
            open(file, 'w+').close()
        view = sublime.active_window().open_file(file)
        self.insert_title_scheduled = False
        self.insert_title(title, view)

    def insert_title(self, title, view):
        if view.is_loading():
            if not self.insert_title_scheduled:
                self.insert_title_scheduled = True
                sublime.set_timeout(lambda: self.insert_title(title, view), 100)
            return
        else:
            view.run_command("note_insert_title", {"title": title})


class NoteInsertTitleCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        header = "# " + kwargs["title"].capitalize() + "\n"
        self.view.insert(edit, 0, header)

def plugin_loaded():
    # creating root if it does not exist
    root = settings().get("root")
    if not os.path.exists(root):
        os.makedirs(root)
