import sublime, sublime_plugin
import os, fnmatch, re

def settings():
    return sublime.load_settings('Notes.sublime-settings')

class NotesBufferCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.new_file()
        view.set_scratch(True)
        view.set_name("✎ Notes Index")
        view.set_syntax_file('Packages/PlainNotes/Notes Index.hidden-tmLanguage')
        view.settings().set('color_scheme', 'Packages/PlainNotes/Color Schemes/Notes-Index.hidden-tmTheme')
        self.window.focus_view(view)
        view.run_command('notes_buffer_refresh')

class NotesBufferRefreshCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        v.set_read_only(False)
        v.erase(edit, sublime.Region(0, self.view.size()))

        root = os.path.normpath(os.path.expanduser(settings().get("root")))
        lines = self.list_files(root)
        v.insert(edit, 0, "\n"+"\n".join(lines))
        v.set_read_only(True)

    def list_files(self, path):
        lines = []
        for root, dirs, files in os.walk(path, topdown=False):
            level = root.replace(path, '').count(os.sep) - 1
            indent = ' ' * 4 * (level)
            relpath = os.path.relpath(root, path)
            if  not (relpath == "." or relpath == ".brain"):
                lines.append('{0}▣ {1}'.format(indent, os.path.relpath(root, path)))
            if  not (relpath == ".brain"):
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    lines.append('{0}≡ {1}'.format(subindent, re.sub('\.note$', '', f)))
        return lines
