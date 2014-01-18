import sublime
import sublime_plugin

import os


# on plugin_load read settings
# on plugin_load create notes directory if it does not exists

class NoteChangeColorCommand(sublime_plugin.WindowCommand):

    def __init__(self, view):
        self.colors = ["Orange", "Yellow", "Green", "GreenLight", "Blue", "BlueLight", "Purple", "Pink", "Gray", "White"]

    def on_select(self, index):
        if index == -1:
            self.window.active_view().settings().set("color_scheme", self.original_cs)
        else:
            path = os.path.join("Packages" , "SublimeNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")
            self.window.active_view().settings().set("color_scheme", path)

    def on_highlight(self, index):
        path = os.path.join("Packages" , "SublimeNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")
        self.window.active_view().settings().set("color_scheme", path)

    def run(self):
        self.window = sublime.active_window()
        self.original_cs = self.window.active_view().settings().get("color_scheme")
        current_color = os.path.basename(self.original_cs).replace("Sticky-","").replace(".tmTheme", "")
        # show_quick_panel(items, on_done, <flags>, <selected_index>, <on_highlighted>)
        self.window.show_quick_panel(self.colors, self.on_select, 0, self.colors.index(current_color), self.on_highlight)

