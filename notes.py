import sublime, sublime_plugin
import os, fnmatch, re, time

from gzip import GzipFile
from pickle import load, dump

ST3 = int(sublime.version()) >= 3000

def settings():
  return sublime.load_settings('Notes.sublime-settings')

def file_id(path):
  return os.path.relpath(path, root)

class NotesListCommand(sublime_plugin.ApplicationCommand):

  def run(self):
     root = os.path.normpath(os.path.expanduser(settings().get("root")))
     window = sublime.active_window()
     self.notes_dir = os.path.expanduser(root)
     self.file_list = self.find_notes(root)
     window.show_quick_panel([f[0] for f in self.file_list], self.open_note)

  def find_notes(self, root):
     note_files = []
     for path, subdirs, files in os.walk(self.notes_dir, topdown=False):
       relpath = os.path.relpath(path, root)
       for name in files:
         for ext in settings().get("note_file_extensions"):
           if (not relpath.startswith(".brain")) and fnmatch.fnmatch(name, "*." + ext):
             title = re.sub('\.' + ext + '$', '', name)
             tag = path.replace(root, '').replace(os.path.sep, '')
             if not tag == '':
              tag = tag + ': '
             note_files.append((re.sub('\.' + ext + '$', '', tag + title),
                        os.path.join(path, name),
                        os.path.getmtime(os.path.join(path, name)),
                        tag
                       ))
     note_files.sort(key=lambda item: item[2], reverse=True)
     return note_files

  def open_note(self, index):
     if index == -1:
       return
     file_path = self.file_list[index][1]
     sublime.run_command("notes_open", {"file_path": file_path})

class NotesRenameCommand(sublime_plugin.ApplicationCommand):

  def run(self):
     root = os.path.normpath(os.path.expanduser(settings().get("root")))
     window = sublime.active_window()
     self.notes_dir = os.path.expanduser(root)
     self.file_list = self.find_notes(root)
     window.show_quick_panel([f[0] for f in self.file_list], self.rename_note)

  def find_notes(self, root):
     note_files = []
     for path, subdirs, files in os.walk(self.notes_dir, topdown=False):
       relpath = os.path.relpath(path, root)
       for name in files:
         for ext in settings().get("note_file_extensions"):
           if (not relpath.startswith(".brain")) and fnmatch.fnmatch(name, "*." + ext):
             title = re.sub('\.' + ext + '$', '', name)
             tag = path.replace(root, '').replace(os.path.sep, '')
             if not tag == '':
              tag = tag + ': '
             note_files.append((re.sub('\.' + ext + '$', '', tag + title),
                        os.path.join(path, name),
                        os.path.getmtime(os.path.join(path, name)),
                        tag
                       ))
     note_files.sort(key=lambda item: item[2], reverse=True)
     return note_files

  def rename_note(self, index):
     if index == -1:
       return
     self.file_path = self.file_list[index][1]
     self.window = sublime.active_window()
     self.window.show_input_panel("New Name:", "", self.rename_file, None, None)

  def rename_file(self, title):
    filename = title.split("/")
    if len(filename) > 1:
      title = filename[len(filename)-1]
      directory = self.notes_dir +"/"+ filename[0]
      tag = filename[0]
    else:
      title = filename[0]
      directory = self.notes_dir
      tag = ""
    if not os.path.exists(directory):
      os.makedirs(directory)

    ext = "." + settings().get("note_save_extension")
    fname = os.path.join(directory, title + ext)
    os.path.isfile(fname)
    pardir = os.path.abspath(os.path.join(self.file_path, '..'))
    if not os.path.isfile(fname):
      os.rename(self.file_path,fname)
      sublime.run_command("notes_open", {"file_path": fname})
    else:
      sublime.error_message("Note already exists!")
      self.window.show_input_panel("New Name:", "", self.rename_file, None, None)


class NotesOpenCommand(sublime_plugin.ApplicationCommand):

  def run(self, file_path):
    sublime.set_timeout(lambda: self.async_open(file_path) , 0)

  def async_open(self, file_path):
    view = sublime.active_window().open_file(file_path, sublime.ENCODED_POSITION)
    f_id = file_id(file_path)
    if db.get(f_id) and db[f_id]["color_scheme"]:
      view.settings().set("color_scheme", db[f_id]["color_scheme"])
      view.settings().set("is_note", True)


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
    filename = title.split("/")
    if len(filename) > 1:
      title = filename[len(filename)-1]
      directory = self.notes_dir +"/"+ filename[0]
      tag = filename[0]
    else:
      title = filename[0]
      directory = self.notes_dir
      tag = ""
    if not os.path.exists(directory):
      os.makedirs(directory)

    ext = "." + settings().get("note_save_extension")
    file = os.path.join(directory, title + ext)
    if not os.path.exists(file):
      open(file, 'w+').close()
    view = sublime.active_window().open_file(file)
    self.insert_title_scheduled = False
    self.insert_title(title, tag, view)

  def insert_title(self, title, tag, view):
    if view.is_loading():
      if not self.insert_title_scheduled:
        self.insert_title_scheduled = True
        sublime.set_timeout(lambda: self.insert_title(title, tag, view), 100)
      return
    else:
      view.run_command("note_insert_title", {"title": title, "tag" : tag})


class NotesEvents(sublime_plugin.EventListener):
  def on_load_async(self, view):
    if view.settings().get("is_note") or not view.file_name():
      return
    if os.path.realpath(view.file_name()).startswith(root):
      f_id = file_id(view.file_name())
      if db.get(f_id) and db[f_id]["color_scheme"]:
        view.settings().set("color_scheme", db[f_id]["color_scheme"])
        view.settings().set("is_note", True)


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
    self.colors = ["Orange", "Yellow", "Green", "GreenLight", "Blue", "BlueLight", "Purple", "Pink", "Gray", "White"]
    self.window = sublime.active_window()
    self.original_cs = self.window.active_view().settings().get("color_scheme")
    current_color = os.path.basename(self.original_cs).replace("Sticky-","").replace(".tmTheme", "")
    # show_quick_panel(items, on_done, <flags>, <selected_index>, <on_highlighted>)
    self.window.show_quick_panel(self.colors, self.on_select, 0, self.colors.index(current_color), self.on_highlight)

  def on_select(self, index):
    global db
    if index == -1:
      self.window.active_view().settings().set("color_scheme", self.original_cs)
    else:
      path = os.path.join("Packages" , "PlainNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")
      view = self.window.active_view()
      view.settings().set("color_scheme", path)
      f_id = file_id(view.file_name())
      if not db.get(f_id):
        db[f_id] = {}
      db[f_id]["color_scheme"] = path
      save_to_brain()

  def on_highlight(self, index):
    path = os.path.join("Packages" , "PlainNotes", "Color Schemes", "Sticky-" + self.colors[index] + ".tmTheme")
    self.window.active_view().settings().set("color_scheme", path)

  def is_enabled(self):
    return self.window.active_view().settings().get("syntax").endswith("Note.tmLanguage")


class NoteArchiveCommand(sublime_plugin.WindowCommand):

  def run(self):
    pass

class NoteRemoveCommand(sublime_plugin.WindowCommand):

  def run(self):
    pass

class NoteRenameCommand(sublime_plugin.WindowCommand):

  def run(self):
    pass

def save_to_brain():
  print("SAVING TO DISK-----------------")
  print(db)
  gz = GzipFile(db_file, 'wb')
  dump(db, gz, -1)
  gz.close()

def cleanup_brain():
  print("Cleaning Up My Brain -----------------")
  # print(db)
  print(len(db))
  to_delete = []
  for nfile in db:
    if not os.path.exists(os.path.join(root,nfile)):
      print("✘" + nfile)
      to_delete.append(nfile)
  print(to_delete)
  for x in to_delete:
    db.pop(x, None)
  print(len(db))
  save_to_brain()

def plugin_loaded():
  global db, root, db_file
  # creating root if it does not exist
  root = os.path.normpath(os.path.expanduser(settings().get("root")))
  if not os.path.exists(root):
    os.makedirs(root)
  # open db
  db = {}
  db_file = os.path.join(root, '.brain', 'brain.bin.gz')
  try:
    os.makedirs(os.path.dirname(db_file))
  except:
    pass
  try:
    gz = GzipFile(db_file, 'rb')
    db = load(gz)
    gz.close()
  except:
    db = {}

if not ST3:
  plugin_loaded()
