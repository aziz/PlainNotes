# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os, time

ST3 = int(sublime.version()) >= 3000
if not ST3:
    from codecs import open


def settings():
    return sublime.load_settings('Notes.sublime-settings')


def get_root():
    return os.path.normpath(os.path.expanduser(settings().get("root")))


class JotterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        output = self.view.window().get_output_panel("jotter")
        self.view.window().run_command("show_panel", {"panel": "output.jotter"})
        output.settings().set("color_scheme", settings().get("jotter_color_scheme"))
        output.settings().set("is_jott", True)
        output.set_syntax_file("Packages/PlainNotes/Note.tmLanguage")
        sublime.status_message(u"    ✎ Jot down your note and press ESC when done. It will be saved to your 'Inbox'")
        output.set_read_only(False)
        window.focus_view(output)


class SaveJotAndHidePanelCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        v = self.view
        w = self.view.window()

        if not v.settings().get("is_jott"):
            w.run_command("hide_panel", {"cancel": True})
            return

        text = v.substr(sublime.Region(0, v.size()))
        if not text or text.isspace():
            w.run_command("hide_panel", {"cancel": True})
            return

        jot = '# ' + time.strftime(settings().get("jotter_date_format")) + u' — ' + time.strftime(settings().get("jotter_time_format")) + u'\n' + text.rstrip(u'\r\n') + u'\n\n'

        with open(os.path.join(get_root(), ".brain", "Inbox.note"), mode='r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(jot + content)

        w.run_command("hide_panel", {"cancel": True})


class OpenInboxCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        root = get_root()
        inbox = os.path.join(root, '.brain', 'Inbox.note')
        sublime.active_window().open_file(inbox)

