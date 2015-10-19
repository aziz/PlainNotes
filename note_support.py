import sublime, sublime_plugin
import webbrowser

class NoteOpenUrlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        s = self.view.sel()[0]

        # Expand selection to possible URL
        start = s.a
        end = s.b

        view_size = self.view.size()
        terminator = ['\t', ' ', '\"', '\'', '(', ')']

        while (start > 0
                and not self.view.substr(start - 1) in terminator
                and self.view.classify(start) & sublime.CLASS_LINE_START == 0):
            start -= 1

        while (end < view_size
                and not self.view.substr(end) in terminator
                and self.view.classify(end) & sublime.CLASS_LINE_END == 0):
            end += 1

        # Check if this is URL
        url = self.view.substr(sublime.Region(start, end))

        if url.startswith(('http://', 'https://')):
            webbrowser.open_new_tab(url)

    def is_enabled(self):
        is_note = sublime.active_window().active_view().settings().get("is_note")
        if is_note:
            return is_note
        else:
            return False
