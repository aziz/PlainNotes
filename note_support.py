import sublime, sublime_plugin
import webbrowser


class NoteOpenUrlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        s = v.sel()[0]
        link_region = v.extract_scope(s.a)
        url = v.substr(link_region)
        webbrowser.open_new_tab(url)

    def is_enabled(self):
        return 'Note.tmLanguage' in self.view.settings().get("syntax")
