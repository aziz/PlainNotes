import sublime, sublime_plugin
import webbrowser
import urllib.request
import base64
import io
import struct

ST3072 = int(sublime.version()) >= 3072


class NoteOpenUrlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        s = v.sel()[0]
        link_region = v.extract_scope(s.a)
        url = v.substr(link_region)
        webbrowser.open_new_tab(url)

    def is_enabled(self):
        return 'Note.tmLanguage' in self.view.settings().get("syntax")

if ST3072:
    class NotePreviewImageCommand(sublime_plugin.TextCommand):

        def run(self, edit):
            v = self.view
            s = v.sel()[0]
            link_region = v.extract_scope(s.a)
            url = v.substr(link_region)

            req = urllib.request.Request(url, headers={"Range": "5000"})
            r = urllib.request.urlopen(req)
            mime, w, h = self.getImageInfo(r.read())
            max_w, max_h = v.viewport_extent()
            print(mime, w, h, max_w, max_h)
            if 'image' in mime:
                response = urllib.request.urlopen(url)
                data = response.read()
                b64 = base64.b64encode(data)
                win_w, win_h = self.getPreviewDimensions(w, h, max_w, max_h)
                print(win_w, win_h)
                style = '<style>body, html {margin: 0; padding: 0}</style>'
                html = style + '<img height="' + str(win_h) + '" width="' + str(win_w) + '" src="data:image/png;base64,' + b64.decode('utf-8') + '">'
                v.show_popup(html, max_width=win_w, max_height=win_h, location=link_region.a)

        def getPreviewDimensions(self, w, h, max_w, max_h):
            margin = 100
            if w > (max_h - margin) or h > (max_h - margin):
                ratio = w / (h * 1.0)
                if max_w >= max_h:
                    height = (max_h - margin)
                    width = height * ratio
                else:
                    width = (max_w - margin)
                    height = width / ratio
                return (width, height)
            else:
                return (w, h)

        def getImageInfo(self, data):
            data = data
            size = len(data)
            height = -1
            width = -1
            content_type = ''

            # handle GIFs
            if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
                # Check to see if content_type is correct
                content_type = 'image/gif'
                w, h = struct.unpack(b"<HH", data[6:10])
                width = int(w)
                height = int(h)

            # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
            # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
            # and finally the 4-byte width, height
            elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n') and
                  (data[12:16] == b'IHDR')):
                content_type = 'image/png'
                w, h = struct.unpack(b">LL", data[16:24])
                width = int(w)
                height = int(h)

            # Maybe this is for an older PNG version.
            elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
                # Check to see if we have the right content type
                content_type = 'image/png'
                w, h = struct.unpack(b">LL", data[8:16])
                width = int(w)
                height = int(h)

            # handle JPEGs
            elif (size >= 2) and data.startswith(b'\377\330'):
                content_type = 'image/jpeg'
                jpeg = io.BytesIO(data)
                jpeg.read(2)
                b = jpeg.read(1)
                try:
                    while (b and ord(b) != 0xDA):
                        while (ord(b) != 0xFF): b = jpeg.read(1)
                        while (ord(b) == 0xFF): b = jpeg.read(1)
                        if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                            jpeg.read(3)
                            h, w = struct.unpack(b">HH", jpeg.read(4))
                            break
                        else:
                            jpeg.read(int(struct.unpack(b">H", jpeg.read(2))[0])-2)
                        b = jpeg.read(1)
                    width = int(w)
                    height = int(h)
                except struct.error:
                    pass
                except ValueError:
                    pass

            return content_type, width, height

        def is_enabled(self):
            return 'Note.tmLanguage' in self.view.settings().get("syntax")
