import sublime, sublime_plugin
import os

class NotesBufferCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.new_file()
        view.set_scratch(True)
        view.set_name("✎ Notes Index")
        view.set_syntax_file('Packages/SublimeNotes/Notes Index.hidden-tmLanguage')
        view.settings().set('color_scheme', 'Packages/SublimeNotes/Color Schemes/Notes-Index.hidden-tmTheme')
        self.window.focus_view(view)
        view.run_command('notes_buffer_refresh')

class NotesBufferRefreshCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        v.set_read_only(False)
        v.erase(edit, sublime.Region(0, self.view.size()))
        v.insert(edit, 0, "\n\nTEST")
        v.set_read_only(True)

