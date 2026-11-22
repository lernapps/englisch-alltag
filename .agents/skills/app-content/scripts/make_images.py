# Draws the figures of this app into src/images/ (scenes with the children and the adults, family tree, barometer,
# house, picture strip, cards). Run from the app folder: python3 .agents/skills/app-content/scripts/make_images.py [name ...]
# The four children are the <g id> of millbrook-klassenzimmer.svg of hello-millbrook (#470), copied unchanged.
# The adults (Mrs Parker, Mr Hill, Mr Parker, Grandma Parker) are drawn here in the same style, after the descriptions in
# konventionen.md. More figures live in images_*.py beside this file; each registers its functions with @image.
import re, sys, os, glob, importlib.util, urllib.request

SRC = "https://raw.githubusercontent.com/lernapps/hello-millbrook/main/src/images/millbrook-klassenzimmer.svg"
CACHE = "/tmp/millbrook-klassenzimmer.svg"
if not os.path.exists(CACHE):
    open(CACHE, "wb").write(urllib.request.urlopen(SRC).read())
KIDS = re.search(r"<defs>(.*?)</defs>", open(CACHE, encoding="utf-8").read(), re.S).group(1)

BG = "#f4efe2"; BLUE = "#2c6fd8"; ORANGE = "#d35400"; GREEN = "#138d75"; INK = "#333"
OUT = "src/images/"


def adult(gid, jacket, hair, bun=False, glasses=False, tall=1.0):
    """An adult in the style of the children: same body, other colours. bun: hair in a bun on top."""
    hairpath = (f'<path d="M18 54 Q14 14 50 12 Q86 14 82 54 Q80 34 62 28 Q40 36 22 40 Z" fill="{hair}"/>')
    if bun:
        hairpath += f'<circle cx="50" cy="8" r="13" fill="{hair}"/>'
    return (f'<g id="{gid}" stroke="#333" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">'
            f'<path d="M12 168 C6 120 20 88 50 84 C80 88 94 120 88 168 C70 178 30 178 12 168 Z" fill="{jacket}"/>'
            f'<ellipse cx="50" cy="52" rx="30" ry="32" fill="#f1cdb0"/>{hairpath}'
            f'<circle cx="40" cy="56" r="3" fill="#222"/><circle cx="60" cy="56" r="3" fill="#222"/>'
            f'<path d="M42 68 Q50 75 58 68" fill="none"/></g>')


ADULTS = (adult("mrs-parker", "#2a9d8f", "#b5501e", bun=True)
          + adult("mr-hill", "#8a5a2b", "#aaa")
          + adult("mr-parker", "#8d99a6", "#6b3f1e")
          + adult("grandma", "#8e5bb5", "#bbb", bun=True))
DEFS = f"<defs>{KIDS}{ADULTS}</defs>"


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">\n  <title>{title}</title>\n  {DEFS}\n'
            f'  <rect width="{w}" height="{h}" fill="{BG}"/>\n{body}\n</svg>\n')


def kid(name, x, y, s=0.85):
    return f'  <use href="#{name}" transform="translate({x},{y}) scale({s})"/>\n'


def text(x, y, t, size=24, anchor="middle", fill=INK, weight="normal"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>\n'


def wall(h=340, floor=262):
    return f'  <rect y="{floor}" width="640" height="{h-floor}" fill="#c9a77a"/>\n  <rect width="640" height="{floor}" fill="#efe7d3"/>\n'


def frame(x, y, w, h, inner=""):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" stroke="#7a5a35" stroke-width="6"/>\n{inner}'


def card(x, y, w, h, t, size=24, fill="#fff", dash=False):
    d = ' stroke-dasharray="6 4"' if dash else ""
    return (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{INK}" stroke-width="2"{d}/>\n'
            + text(x + w / 2, y + h / 2 + size / 3, t, size))


def line(x1, y1, x2, y2, w=3, dash=False):
    d = ' stroke-dasharray="6 5"' if dash else ""
    return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="{w}"{d}/>\n'


def table(x, y, w, h):
    return (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#d9b98a" stroke="#7a5a35" stroke-width="3"/>\n'
            f'  <rect x="{x+10}" y="{y+h}" width="10" height="50" fill="#7a5a35"/><rect x="{x+w-20}" y="{y+h}" width="10" height="50" fill="#7a5a35"/>\n')


IMAGES = {}


def image(f):
    IMAGES[f.__name__.replace("_", "-")] = f
    return f


# ---------------------------------------------------------------- Kapitel 1

@image
def szene_familie_personen():
    b = wall()
    b += '  <rect x="250" y="25" width="140" height="100" rx="6" fill="#bfe0f0" stroke="#7a5a35" stroke-width="6"/>\n'
    b += line(320, 25, 320, 125, 4) + line(250, 75, 390, 75, 4)
    b += kid("mrs-parker", 20, 100, .9) + kid("mr-parker", 520, 100, .9)
    b += table(140, 190, 360, 24)
    b += kid("ellie", 175, 105, .75) + kid("sophie", 290, 105, .75) + kid("peter", 410, 140, .6)
    b += '  <path d="M200 175 Q212 200 240 196" stroke="#d33" stroke-width="13" fill="none" stroke-linecap="round"/>\n'
    b += '  <circle cx="243" cy="195" r="7" fill="#f3d2b3" stroke="#333" stroke-width="2"/>\n'
    b += '  <rect x="239" y="162" width="24" height="38" rx="4" fill="#333"/><rect x="242" y="166" width="18" height="28" fill="#9fd0f0"/>\n'
    return svg(640, 340, "Eine Familie sitzt am Tisch in der Küche: zwei Erwachsene und drei Kinder, ein Kind hält ein Handy", b)


@image
def stammbaum():
    b = ""
    # row 0: Grandma Parker above her son; row 1: the parents; row 2: the children. Sophie is a guest (dashed line),
    # her parents a small photo. A figure drawn at (x, y) with scale s has its centre at x + 50 * s.
    b += kid("grandma", 332, 2, .45) + text(355, 98, "Grandma Parker", 17)
    b += line(355, 104, 355, 122, 3)
    b += kid("mrs-parker", 190, 112, .55) + text(217, 232, "Mrs Parker", 17)
    b += kid("mr-parker", 330, 120, .55) + text(357, 240, "Mr Parker", 17)
    b += line(217, 246, 217, 262, 3) + line(357, 246, 357, 262, 3) + line(217, 262, 357, 262, 3) + line(287, 262, 287, 272, 3)
    b += line(165, 272, 422, 272, 3) + line(165, 272, 165, 300, 3) + line(422, 272, 422, 300, 3)
    # Sophie is a guest: a thick dashed line, easy to see
    b += '  <line x1="295" y1="272" x2="295" y2="302" stroke="#d35400" stroke-width="6" stroke-dasharray="7 5"/>\n'
    b += kid("ellie", 140, 302, .5) + text(165, 412, "Ellie", 17)
    b += kid("sophie", 270, 302, .5) + text(295, 412, "Sophie", 17)
    b += kid("peter", 400, 312, .45) + text(422, 412, "Peter", 17)
    b += '  <rect x="30" y="130" width="70" height="80" rx="4" fill="#fff" stroke="#7a5a35" stroke-width="4"/>\n'
    b += '  <ellipse cx="65" cy="165" rx="16" ry="18" fill="#f1cdb0" stroke="#333" stroke-width="1.5"/><path d="M49 162 Q48 144 65 143 Q82 144 81 162 Q76 152 65 152 Q54 154 49 162 Z" fill="#d9b45a"/>\n'
    b += text(65, 230, "Sophie's", 16) + text(65, 249, "Mum and Dad", 16)
    return svg(640, 430, "Stammbaum: oben Grandma Parker, darunter Mrs Parker und Mr Parker, darunter Ellie, Sophie als Gast und Peter, links ein Foto von Sophies Eltern", b)


# ---------------------------------------------------------------- weitere Bilder (images_*.py)
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec)
    m.__dict__.update({k: v for k, v in globals().items() if not k.startswith("__")})
    spec.loader.exec_module(m)

if __name__ == "__main__":
    names = sys.argv[1:] or list(IMAGES)
    for n in names:
        open(OUT + n + ".svg", "w", encoding="utf-8").write(IMAGES[n]())
        print("wrote", OUT + n + ".svg")
