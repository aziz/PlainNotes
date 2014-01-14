import sublime
import sublime_plugin

import os
import fnmatch
import re

# on plugin_load read settings
# on plugin_load create notes directory if it does not exists

class NotesListCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        self.notes_dir = os.path.expanduser("~/Dropbox/Notes/")

    def find_notes(self, file):
        if fnmatch.fnmatch(file, '*.note'):
            return re.sub('\.note$', '', file)

    def open_note(self, index):
        if index == -1:
            return
        file = os.path.join(self.notes_dir, self.file_list[index] + ".note")
        # self.window.run_command("new_pane",{"move": True})
        view = sublime.active_window().open_file(file)

    def run(self):
        window = sublime.active_window()
        self.file_list = [self.find_notes(file) for file in os.listdir(self.notes_dir)]
        window.show_quick_panel(self.file_list, self.open_note)


class NotesNewCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        self.notes_dir = os.path.expanduser("~/Dropbox/Notes/")

    def create_note(self, title):
        file = os.path.join(self.notes_dir, title + ".note")
        if not os.path.exists(file):
            open(file, 'w+').close()
        view = sublime.active_window().open_file(file)

    def run(self, title=None):
        self.window = sublime.active_window()
        if title is None:
            self.window.show_input_panel("Title", "", self.create_note, None, None)
        else:
            self.create_note(title)

