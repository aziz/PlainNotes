import sublime, sublime_plugin
import os, fnmatch, re

TAB_SIZE = 2
COL_WIDTH = 30

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
        v.insert(edit, 0, "\n".join([f[0] + (COL_WIDTH-len(f[0]))*" " + f[1] for f in lines]))
        v.set_read_only(True)

    def list_files(self, path):
        lines = []
        for root, dirs, files in os.walk(path, topdown=False):
            level = root.replace(path, '').count(os.sep) - 1
            indent = ' ' * TAB_SIZE * (level)
            relpath = os.path.relpath(root, path)
            if  not (relpath == "." or relpath == ".brain"):
                line_str = '{0}▣ {1}'.format(indent, os.path.relpath(root, path))
                lines.append( (line_str, root) )
            if  not (relpath == ".brain"):
                subindent = ' ' * TAB_SIZE * (level + 1)
                for f in files:
                    line_str = '{0}≡ {1}'.format(subindent, re.sub('\.note$', '', f))
                    line_path = os.path.normpath(os.path.join(root, f))
                    lines.append( (line_str, line_path)  )
        return lines


class NotesBufferOpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            file_index = self.view.rowcol(sel.a)[0]
            print(file_index)
