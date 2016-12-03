import sublime
import plistlib
import re

# TODO:
# whitest
# blackest

WHEEL = {
    'red':       0,
    'orange':    30,
    'yellow':    60,
    'lime':      90,
    'green':     120,
    'teal':      150,
    'cyan':      180,
    'lightblue': 210,
    'blue':      240,
    'purple':    270,
    'magenta':   300,
    'pink':      330,
}
MARGIN = 15


def get_range(value, margin):
    min = value - margin
    max = value + margin
    if min < 0:
        min = 360 + min
    if max >= 360:
        max = max - 360
    if min > max:
        return [(min, 360), (0, max)]
    else:
        return [(min, max)]


def rgbToHsl(r, g, b):
    r /= 255
    g /= 255
    b /= 255
    cmax = max([r, g, b])
    cmin = min([r, g, b])
    l = (cmax + cmin) / 2

    if (cmax == cmin):
        h = s = 0  # achromatic
    else:
        d = cmax - cmin
        s = (d / (2 - cmax - cmin)) if l > 0.5 else (d / (cmax + cmin))
        if cmax == r:
            plus = 6 if g < b else 0
            h = (g - b) / d + plus
        elif cmax == g:
            h = (b - r) / d + 2
        elif cmax == b:
            h = (r - g) / d + 4
        h /= 6
    return (h, s, l)


def hue2rgb(p, q, t):
    if (t < 0):
        t += 1
    if (t > 1):
        t -= 1
    if (t < 1/6):
        return p + (q - p) * 6 * t
    if (t < 1/2):
        return q
    if (t < 2/3):
        return p + (q - p) * (2/3 - t) * 6
    return p


def hslToRgb(h, s, l):
    if s == 0:
        r = g = b = l  # achromatic
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)
    return [int(r * 255), int(g * 255), int(b * 255)]


def RgbToHex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)


def variance(c, k):
    dh = abs(WHEEL[k] - c[0]*360)
    if dh > 180:
        dh = 360 - dh
    x = (100 - (c[1]*100)) + abs(50 - (c[2]*100)) + (dh*3)
    return c + (x,)


class CSColorExtractor():
    def __init__(self, color_scheme_path):
        self.color_scheme_path = color_scheme_path
        self.color_scheme = sublime.load_resource(color_scheme_path)
        self.schemecolors = set()
        self.hsl_colors = set()
        self.palette = {
            'red':       set(),
            'orange':    set(),
            'yellow':    set(),
            'lime':      set(),
            'green':     set(),
            'teal':      set(),
            'cyan':      set(),
            'lightblue': set(),
            'blue':      set(),
            'purple':    set(),
            'magenta':   set(),
            'pink':      set()
        }
        self.general_colors = {}
        self.colors = {}
        self.load_scheme()
        self.extract_colors_in_hsl()
        self.generate_palette()
        self.palette_single_color()

    def load_scheme(self):
        color_scheme_removed_comments = re.sub(r"<!--.+-->", '', self.color_scheme)
        plist_file = plistlib.readPlistFromBytes(bytes(color_scheme_removed_comments, 'UTF-8'))

        for rule in plist_file["settings"]:
            if rule.get('settings', {}).get('caret', None):
                self.general_colors = rule.get('settings', {})
            for setting in ['foreground', 'background']:
                c = rule.get('settings', {}).get(setting, None)
                c and self.schemecolors.add(c)

    def extract_colors_in_hsl(self):
        # converting to hsl
        for c in self.schemecolors:
            if len(c) == 4:
                c = '#' + c[1]*2 + c[2]*2 + c[3]*2
            rgb = tuple(int(c[1:7][i:i + 2], 16) for i in (0, 2, 4))
            hsl = rgbToHsl(rgb[0], rgb[1], rgb[2])
            # lightness of less than 10% or over 90% is not useful
            # saturation of less than 10% is not useful
            if (hsl[2] >= 0.1 and hsl[2] <= 0.9 and hsl[1] > 0.1):
                self.hsl_colors.add(hsl)

    def generate_palette(self):
        for (k, v) in WHEEL.items():
            c_ranges = get_range(v, MARGIN)
            for c_range in c_ranges:
                for c in self.hsl_colors:
                    hue = c[0]*360
                    if hue >= c_range[0] and hue <= c_range[1]:
                        self.palette[k].add(c)

        coeff = 1
        runs = 1
        while not (all(len(v) > 1 for (k, v) in self.palette.items())) or runs > 3:
            runs += 1
            coeff += 1
            for (k, v) in self.palette.items():
                if not (len(v) > 1):
                    c_ranges = get_range(WHEEL[k], MARGIN*coeff)
                    for c_range in c_ranges:
                        for c in self.hsl_colors:
                            hue = c[0]*360
                            if hue >= c_range[0] and hue <= c_range[1]:
                                self.palette[k].add(c)
        # print('===> ', runs)

    def palette_single_color(self):
        for (k, v) in self.palette.items():
            with_cost = map(lambda x: variance(x, k), v)
            sorted_colors = sorted(with_cost, key=lambda x: x[3])
            self.colors[k] = RgbToHex(*hslToRgb(
                sorted_colors[0][0], sorted_colors[0][1], sorted_colors[0][2]))

    def css(self):
        output = "\n\n\n"
        for (k, v) in self.palette.items():
            output += ".{} {{\n".format(k)
            with_cost = map(lambda x: variance(x, k), v)
            for c in with_cost:
                output += "\tcolor: hsl({h}, {s}%, {l}%); /* σ = {c} */\n".format(
                    h="%3.f" % (c[0]*360),
                    s="%3.f" % (c[1]*100),
                    l="%3.f" % (c[2]*100),
                    c="%7.3f" % (c[3]),
                )
            output += '}\n'
        return output

    def css_single(self):
        output = "\n\n\n"
        for (k, v) in self.colors.items():
            output += ".{} {{\n".format(k)
            output += "\tcolor: {}\n".format(v)
            output += '}\n'
        return output


def plugin_loaded():
    settings = sublime.load_settings('Preferences.sublime-settings')
    color_scheme_path = settings.get('color_scheme')
    color_extractor = CSColorExtractor(color_scheme_path)
    # print(color_extractor.palette)
    # print(color_extractor.css())
    # print(color_extractor.colors)
    # print(color_extractor.css_single())
    # print(color_extractor.general_colors)

