# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os, fnmatch, re, time
import copy
import json

from .lib import helpers

ST3 = int(sublime.version()) >= 3000

if not ST3:
    from codecs import open


def settings():
    return sublime.load_settings('Notes.sublime-settings')


def get_root():
    project_settings = sublime.active_window().active_view().settings().get('PlainNotes')
    if project_settings:
        return os.path.normpath(os.path.expanduser(project_settings.get('root', settings().get("root"))))
    else:
        return os.path.normpath(os.path.expanduser(settings().get("root")))


def file_id(path):
    return os.path.relpath(path, root)

def brain_dir():
    brain_settings = settings().get("jotter_dir")
    if brain_settings:
        return brain_settings
    else:
        return ".brain"


def find_notes(self, root, exclude):
    note_files = []
    for path, subdirs, files in os.walk(root, topdown=True):
        if exclude:
            subdirs[:] = [d for d in subdirs if d not in exclude]
        relpath = os.path.relpath(path, root)
        for name in files:
            for ext in settings().get("note_file_extensions"):
                if (not relpath.startswith(brain_dir())) and fnmatch.fnmatch(name, "*." + ext):
                    title = re.sub('\.' + ext + '$', '', name)
                    tag = path.replace(root, '').replace(os.path.sep, '')
                    if not tag == '':
                        tag = tag + ': '
                    modified_str = time.strftime("Last modified: %d/%m/%Y %H:%M", time.gmtime(os.path.getmtime(os.path.join(path, name))))
                    # created_str = time.strftime("Created: %d/%m/%Y %H:%M", time.gmtime(os.path.getctime(os.path.join(path, name))));
                    note_files.append([re.sub('\.' + ext + '$', '', tag + title), os.path.join(path, name), tag, modified_str])

    note_files.sort(key=lambda item: os.path.getmtime(item[1]), reverse=True)
    return note_files


def setup_notes_list(file_list):
    # list display options
    try:
        display_modified_date = settings().get("list_options").get("display_modified_date")
        display_folder = settings().get("list_options").get("display_folder")
        display_full_path = settings().get("list_options").get("display_full_path")
    except:
        display_modified_date = True
        display_folder = True
        display_full_path = False

    indices = [0]
    if display_modified_date:
        indices.append(3)
    if display_folder:
        indices.append(2)
    if display_full_path:
        indices.append(1)

    return helpers.return_sublist(file_list, indices)


def update_color(old_file_path, new_file_path):
    # update color scheme db
    f_id_old = file_id(old_file_path)

    if db.get(f_id_old):
        f_id_new = file_id(new_file_path)
        if not db.get(f_id_new):
            db[f_id_new] = {}

        db[f_id_new]["color_scheme"] = db[f_id_old]["color_scheme"]

        # delete old
        db.pop(f_id_old, None)

        save_to_brain()


class NotesListCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        exclude = set([settings().get("archive_dir"), brain_dir()])
        root = get_root()
        self.notes_dir = root
        self.file_list = find_notes(self, root, exclude)
        rlist = setup_notes_list(self.file_list)
        window = sublime.active_window()
        window.show_quick_panel(rlist, self.open_note)

    def open_note(self, index):
        if index == -1:
            return
        file_path = self.file_list[index][1]
        sublime.run_command("notes_open", {"file_path": file_path})


class NotesOpenCommand(sublime_plugin.ApplicationCommand):

    def run(self, file_path):
        sublime.set_timeout(lambda: self.async_open(file_path), 0)

    def async_open(self, file_path):
        view = sublime.active_window().open_file(file_path, sublime.ENCODED_POSITION)
        f_id = file_id(file_path)
        view.settings().set("is_note", True)
        if db.get(f_id):
            view.settings().set("color_scheme", db[f_id]["color_scheme"])


class NotesNewCommand(sublime_plugin.ApplicationCommand):

    def run(self, title=None):
        self.notes_dir = get_root()
        self.window = sublime.active_window()
        if title is None:
            self.window.show_input_panel("Title", "", self.create_note, None, None)
        else:
            self.create_note(title)

    def create_note(self, title):
        filename = title.split("/")
        if len(filename) > 1:
            title = filename[len(filename) - 1]
            directory = os.path.join(self.notes_dir, filename[0])
            tag = filename[0]
        else:
            title = filename[0]
            directory = self.notes_dir
            tag = ""
        if not os.path.exists(directory):
            os.makedirs(directory)

        if any(title.endswith("." + ext) for ext in settings().get("note_file_extensions")):
            ext = ""
        else:
            ext = "." + settings().get("note_save_extension")

        file = os.path.join(directory, title + ext)
        if not os.path.exists(file):
            open(file, 'w+').close()
        view = sublime.active_window().open_file(file)
        color_scheme = settings().get("note_color_scheme")
        if color_scheme:
            view.settings().set("color_scheme", color_scheme)
            f_id = file_id(file)
            if not db.get(f_id):
                db[f_id] = {}
            db[f_id]["color_scheme"] = color_scheme
            save_to_brain()
        self.insert_title_scheduled = False
        self.insert_title(title, tag, view)

    def insert_title(self, title, tag, view):
        if view.is_loading():
            if not self.insert_title_scheduled:
                self.insert_title_scheduled = True
                sublime.set_timeout(lambda: self.insert_title(title, tag, view), 100)
            return
        else:
            view.run_command("note_insert_title", {"title": title, "tag": tag})


class NotesEvents(sublime_plugin.EventListener):

    def on_load_async(self, view):
        root = get_root()
        if view.settings().get("is_note") or not view.file_name():
            return
        if os.path.realpath(view.file_name()).startswith(root):
            f_id = file_id(view.file_name())
            view.settings().set("is_note", True)
            if db.get(f_id) and db[f_id]["color_scheme"]:
                view.settings().set("color_scheme", db[f_id]["color_scheme"])


class NoteInsertTitleCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        if settings().get("enable_yaml"):
            header = "---\n"
            header = header + "title: " + kwargs["title"].capitalize() + "\n"
            header = header + "date: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n"
            header = header + "tags: " + kwargs["tag"] + "\n"
            for yaml_el in settings().get("note_yaml"):
                header = header + yaml_el + ":\n"
            header = header + "---\n"
            self.view.insert(edit, 0, header)


class NoteChangeColorCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.colors = ["Orange", "Yellow", "Green", "GreenLight", "Blue", "BlueLight", "Purple", "Pink", "Gray", "White", "Dark"]
        self.window = sublime.active_window()
        self.original_cs = self.window.active_view().settings().get("color_scheme")
        current_color = os.path.basename(self.original_cs).replace("Sticky-", "").replace(".tmTheme", "")
        if ST3:
            self.window.show_quick_panel(self.colors, self.on_select, 0, self.colors.index(current_color), self.on_highlight)
        else:
            self.window.show_quick_panel(self.colors, self.on_select, 0, self.colors.index(current_color))

    def on_select(self, index):
        global db
        if index == -1:
            self.window.active_view().settings().set("color_scheme", self.original_cs)
        else:
            try:
                path = sublime.find_resources("Sticky-" + self.colors[index] + ".tmTheme")
                path = path[0]
            except:
                path = os.path.join("Packages", "PlainNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")

            view = self.window.active_view()
            view.settings().set("color_scheme", path)
            f_id = file_id(view.file_name())
            if not db.get(f_id):
                db[f_id] = {}
            db[f_id]["color_scheme"] = path
            save_to_brain()

    def on_highlight(self, index):
        try:
            path = sublime.find_resources("Sticky-" + self.colors[index] + ".tmTheme")
            path = path[0]
        except:
            path = os.path.join("Packages", "PlainNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")

        self.window.active_view().settings().set("color_scheme", path)

    def is_enabled(self):
        syntax = self.window.active_view().settings().get("syntax")
        return syntax.endswith("Note.tmLanguage") or syntax.endswith("Note.sublime-syntax")


class NoteArchiveCommand(sublime_plugin.WindowCommand):

    def run(self):
        window = sublime.active_window()
        self.notes_dir = get_root()
        self.archive_note()
        sublime.status_message("    Note Archived.")

    def archive_note(self):
        file_path = self.window.active_view().file_name()
        f_id = file_id(file_path)
        archive_dir = os.path.join(self.notes_dir, settings().get("archive_dir"))
        new_file_path = os.path.join(archive_dir, f_id)

        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
        if not os.path.isfile(new_file_path):
            os.renames(file_path, new_file_path)
            self.window.run_command("close_file")

            # update color scheme db
            update_color(file_path, new_file_path)

    def is_enabled(self):
        is_note = self.window.active_view().settings().get("is_note")
        if is_note:
            return is_note
        else:
            return False


class NoteUnarchiveCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        self.notes_dir = get_root()
        archive_dir = os.path.join(self.notes_dir, settings().get("archive_dir"))
        self.file_list = find_notes(self, archive_dir, [])
        rlist = setup_notes_list(self.file_list)
        window = sublime.active_window()
        if rlist:
            window.show_quick_panel(rlist, self.unarchive_note)
        else:
            window.show_quick_panel(['There are no notes to unarchive.'], [])

    def unarchive_note(self, index):
        if index == -1:
            return
        file_path = self.file_list[index][1]
        new_file_path = file_path.replace(os.path.sep + settings().get("archive_dir"), '')
        # print(file_path)
        # print(new_file_path)
        if not os.path.isfile(new_file_path):
            os.renames(file_path, new_file_path)

            # update color scheme db
            update_color(file_path, new_file_path)

            sublime.run_command("notes_open", {"file_path": new_file_path})

    def is_enabled(self):
        return True


class NoteRemoveCommand(sublime_plugin.WindowCommand):

    def run(self):
        f_path = self.window.active_view().file_name()
        delete = sublime.ok_cancel_dialog('Are you sure you want to delete this note?', 'Yes')
        if delete:
            # Set the view to scratch and close it so ST doesn't prompt again.
            self.window.active_view().set_scratch(True)
            self.window.run_command("close_file")
            os.remove(f_path)

    def is_enabled(self):
        is_note = self.window.active_view().settings().get("is_note")
        if is_note:
            return is_note
        else:
            return False


class NoteRenameCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("New Name:", "", self.rename_note, None, None)

    def rename_note(self, title):
        global db
        self.notes_dir = os.path.expanduser(root)
        self.file_path = self.window.active_view().file_name()
        filename = title.split("/")
        if len(filename) > 1:
            title = filename[len(filename) - 1]
            directory = self.notes_dir + os.path.sep + filename[0]
            tag = filename[0]
        else:
            title = filename[0]
            directory = self.notes_dir
            tag = ""
        if not os.path.exists(directory):
            os.makedirs(directory)

        if any(title.endswith("." + ext) for ext in settings().get("note_file_extensions")):
            ext = ""
        else:
            ext = "." + settings().get("note_save_extension")

        new_file_path = os.path.join(directory, title + ext)
        # pardir = os.path.abspath(os.path.join(self.file_path, '..'))
        if not os.path.isfile(new_file_path):
            os.rename(self.file_path, new_file_path)
            self.window.run_command("close_file")
            sublime.run_command("notes_open", {"file_path": new_file_path})

            # update color scheme db
            update_color(self.file_path, new_file_path)

        else:
            sublime.error_message("Note already exists!")
            self.window.show_input_panel("New Name:", "", self.rename_note, None, None)

    def is_enabled(self):
        is_note = self.window.active_view().settings().get("is_note")
        if is_note:
            return is_note
        else:
            return False


def save_to_brain():
    # print("SAVING TO DISK-----------------")
    # print(db)
    with open(db_json_file, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4, sort_keys=True)


def cleanup_brain():
    # print("Cleaning Up My Brain -----------------")
    # print(db)
    # print(len(db))
    to_delete = []
    for nfile in db:
        if not os.path.exists(os.path.join(root, nfile)):
            # print("✘" + nfile)
            to_delete.append(nfile)
    # print(to_delete)
    for x in to_delete:
        db.pop(x, None)
    # print(len(db))
    save_to_brain()


def plugin_loaded():
    global db, root, db_json_file
    # creating directory structure and files in root
    db = {}
    root = get_root()
    brain = os.path.join(root, brain_dir())
    inbox = os.path.join(root, brain_dir(), 'Inbox.note')
    db_json_file = os.path.join(root, brain_dir(), 'brain.json')

    if not os.path.exists(brain):
        os.makedirs(brain)
    if not os.path.isfile(inbox):
        open(inbox, mode='a', encoding='utf-8').close()

    try:
        with open(db_json_file, 'r') as f:
            db = json.load(f)
        cleanup_brain()
    except:
        db = {}

if not ST3:
    plugin_loaded()
