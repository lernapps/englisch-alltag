# Figures of chapter zuhause-parkers, part A: szene-wohnen, haus-querschnitt, tagesablauf-leiste.
# make_images.py loads this file and passes its helpers (svg, kid, text, line, ...) and the decorator image.

def R(x, y, w, h, fill="#fff", rx=3, sw=2):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="#333" stroke-width="{sw}"/>\n'


def C(x, y, r, fill="#fff", sw=2):
    return f'  <circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#333" stroke-width="{sw}"/>\n'


def L(x1, y1, x2, y2, sw=2):
    return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="{sw}"/>\n'


# small furniture signs; (x, y) is the top left corner, every sign stands on y + its height
def s_sofa(x, y):
    return R(x + 4, y, 62, 22, "#c0504d") + R(x, y + 14, 70, 24, "#c0504d") + R(x - 6, y + 10, 14, 28, "#a63d3a") + R(x + 62, y + 10, 14, 28, "#a63d3a")


def s_armchair(x, y):
    return R(x + 3, y, 34, 20, "#d9a441") + R(x, y + 14, 40, 24, "#d9a441") + R(x - 5, y + 10, 11, 28, "#b8872c") + R(x + 34, y + 10, 11, 28, "#b8872c")


def s_tv(x, y):
    return R(x, y, 40, 26, "#444") + R(x + 4, y + 4, 32, 18, "#9fd0f0", 1) + R(x + 14, y + 26, 12, 6, "#444")


def s_bookshelf(x, y):
    b = R(x, y, 36, 62, "#a0703a")
    for i, c in enumerate(("#d33", "#2c6fd8", "#138d75")):
        yy = y + 4 + i * 20
        b += L(x, yy + 16, x + 36, yy + 16) + R(x + 5, yy + 3, 6, 13, c, 1, 1) + R(x + 13, yy + 5, 6, 11, "#e9c46a", 1, 1) + R(x + 21, yy + 2, 6, 14, c, 1, 1)
    return b


def s_lamp(x, y):
    return L(x + 10, y + 14, x + 10, y + 46, 3) + R(x + 2, y + 44, 16, 4, "#555", 1) + f'  <path d="M{x} {y+14} L{x+5} {y} L{x+15} {y} L{x+20} {y+14} Z" fill="#f4d35e" stroke="#333" stroke-width="2"/>\n'


def s_fridge(x, y):
    return R(x, y, 34, 66, "#eef") + L(x, y + 24, x + 34, y + 24) + L(x + 27, y + 8, x + 27, y + 18, 3) + L(x + 27, y + 30, x + 27, y + 42, 3)


def s_cooker(x, y):
    return R(x, y, 42, 44, "#bbb") + C(x + 11, y + 9, 5, "#666", 1) + C(x + 31, y + 9, 5, "#666", 1) + R(x + 7, y + 20, 28, 18, "#888", 2, 1)


def s_table(x, y):
    return R(x, y, 60, 8, "#c58b4a") + L(x + 6, y + 8, x + 6, y + 36, 4) + L(x + 54, y + 8, x + 54, y + 36, 4)


def s_chair(x, y):
    return L(x, y, x, y + 36, 4) + R(x, y + 18, 22, 5, "#c58b4a", 1) + L(x + 20, y + 22, x + 20, y + 36, 4)


def s_desk(x, y):
    return R(x, y, 50, 7, "#c58b4a") + L(x + 5, y + 7, x + 5, y + 32, 4) + R(x + 30, y + 7, 18, 25, "#a0703a", 1)


def s_bed(x, y, w=50):
    return R(x, y + 12, w, 20, "#8fb8e8") + R(x + 2, y + 5, 14, 9, "#fff", 3, 1) + L(x, y + 32, x, y + 38, 3) + L(x + w, y + 32, x + w, y + 38, 3)


def s_wardrobe(x, y):
    return R(x, y, 38, 70, "#a0703a") + L(x + 19, y, x + 19, y + 70) + C(x + 15, y + 36, 2.5, "#333", 1) + C(x + 23, y + 36, 2.5, "#333", 1)


def s_window(x, y, w=40, h=44):
    return R(x, y, w, h, "#bfe0f0", 2, 3) + L(x + w / 2, y, x + w / 2, y + h) + L(x, y + h / 2, x + w, y + h / 2)


def s_bath(x, y):
    return R(x, y, 62, 24, "#fff", 8) + L(x + 6, y + 24, x + 6, y + 30, 3) + L(x + 56, y + 24, x + 56, y + 30, 3)


def s_toilet(x, y):
    return R(x + 4, y, 16, 22, "#fff", 2) + f'  <ellipse cx="{x+14}" cy="{y+30}" rx="14" ry="8" fill="#fff" stroke="#333" stroke-width="2"/>\n'


def s_sink(x, y):
    return R(x, y, 32, 12, "#fff", 4) + L(x + 16, y - 10, x + 16, y, 3) + L(x + 10, y - 10, x + 22, y - 10, 3) + L(x + 16, y + 12, x + 16, y + 34, 4)


def s_toys(x, y):
    return R(x, y + 14, 16, 16, "#d33", 2) + R(x + 18, y + 20, 14, 10, "#2c6fd8", 2) + C(x + 42, y + 22, 8, "#f4d35e") + R(x + 8, y, 14, 14, "#138d75", 2)


def s_poster(x, y):
    return R(x, y, 26, 34, "#e9c46a", 2) + f'  <path d="M{x+4} {y+28} L{x+11} {y+14} L{x+16} {y+22} L{x+20} {y+17} L{x+24} {y+28} Z" fill="#138d75"/>\n'


def s_shelf(x, y):
    return R(x, y, 42, 6, "#a0703a", 1) + R(x + 5, y - 14, 8, 14, "#2c6fd8", 1, 1) + R(x + 15, y - 11, 8, 11, "#d33", 1, 1)


def s_tree(x, y):
    return R(x - 6, y, 12, 92, "#8a5a2b", 2) + C(x, y - 14, 38, "#7cc47a")


def s_flowers(x, y):
    f = ""
    for i, c in enumerate(("#d33", "#f4d35e", "#e56bb0")):
        xx = x + i * 14
        f += L(xx, y, xx, y + 24) + C(xx, y - 2, 6, c, 1.5)
    return f


def s_bench(x, y):
    return R(x, y, 46, 7, "#c58b4a", 1) + R(x, y - 12, 46, 6, "#c58b4a", 1) + L(x + 4, y + 7, x + 4, y + 24, 4) + L(x + 42, y + 7, x + 42, y + 24, 4)


def s_chair_r(x, y):
    """A chair that looks to the left: back on the right."""
    return L(x + 22, y, x + 22, y + 36, 4) + R(x, y + 18, 22, 5, "#c58b4a", 1) + L(x + 2, y + 22, x + 2, y + 36, 4)


def s_chair_back(x, y):
    """A chair seen from the front (it stands behind the table, drawn before it); (x, y) is the top left of the back."""
    return (R(x, y, 22, 22, "#c58b4a", 2) + R(x - 2, y + 32, 26, 5, "#c58b4a", 1)
            + L(x, y + 37, x, y + 56, 4) + L(x + 22, y + 37, x + 22, y + 56, 4))


@image
def haus_querschnitt():
    b = ""
    b += '  <polygon points="0,76 275,14 550,76" fill="#b5651d" stroke="#333" stroke-width="3"/>\n'
    b += '  <rect x="10" y="372" width="630" height="28" fill="#9bd18b"/>\n'
    b += C(590, 52, 24, "#f6d04d")
    # upper floor: five rooms, y 76-212 (widths differ: Sophie's room is small, but has to hold four things)
    up = [("bathroom", 10, 110), ("Ellie's|room", 120, 116), ("Peter's|room", 236, 88), ("Sophie's|room", 324, 120), ("parents'|bedroom", 444, 96)]
    for name, x, w in up:
        b += R(x, 76, w, 136, "#efe7d3", 0, 3)
        for j, part in enumerate(name.split("|")):
            b += text(x + w / 2, 100 + j * 24, part, 22)
    # lower floor: two rooms, y 212-372
    b += R(10, 212, 265, 160, "#f3ead0", 0, 3) + R(275, 212, 265, 160, "#e9eed8", 0, 3)
    b += text(142, 240, "kitchen", 24) + text(407, 240, "living room", 24)
    # bathroom (floor line y = 210)
    b += s_sink(40, 130) + s_bath(14, 178) + s_toilet(80, 170)
    # Ellie's room: poster, bed, chair, desk with a lamp on it
    b += s_poster(124, 120) + s_bed(122, 172, 36) + s_chair(161, 174) + s_desk(184, 178) + s_lamp(202, 130)
    # Peter's room: bed, toys, shelf
    b += s_shelf(258, 150) + s_bed(240, 172, 30) + s_toys(272, 182)
    # Sophie's room: small, with a blue bed, a desk, a wardrobe and a window
    b += s_window(330, 128, 30, 32) + s_wardrobe(404, 140) + s_bed(328, 176, 28) + s_desk(358, 178)
    # parents' bedroom
    b += s_bed(450, 172, 56) + s_lamp(512, 162)
    # kitchen: fridge, cooker, sink, table with two chairs
    b += s_fridge(20, 302) + s_cooker(60, 324) + s_sink(110, 334)
    b += s_table(182, 332) + s_chair(156, 332) + s_chair_r(246, 332)
    # living room: sofa, armchair, bookshelf, TV and two lamps
    b += s_tv(298, 262) + s_sofa(284, 330) + s_lamp(362, 320) + s_armchair(388, 330) + s_bookshelf(444, 306) + s_lamp(490, 320)
    # garden: tree, flowers, bench
    b += text(590, 206, "garden", 22) + s_tree(585, 280) + s_flowers(548, 348) + s_bench(594, 346)
    return svg(640, 400, "Querschnitt eines Hauses mit zwei Stockwerken, Garten rechts. Die Zimmer tragen Namen, die Möbel sind kleine Zeichen", b)


def scaled(s, x, y, body):
    return f'  <g transform="translate({x},{y}) scale({s})">\n{body}  </g>\n'


@image
def szene_wohnen():
    b = wall()
    b += s_window(330, 36, 110, 100)
    # furniture drawn small and scaled up; the feet stand on the floor line
    b += scaled(2.4, 20, 270 - 38 * 2.4, s_bed(0, 0, 50))
    b += scaled(2, 548, 270 - 70 * 2, s_wardrobe(0, 0))
    b += scaled(2.2, 430, 270 - 32 * 2.2, s_desk(0, 0))
    b += kid("ellie", 120, 120, .6) + kid("sophie", 230, 70, .85)
    # Sophie holds up a phone
    b += R(200, 120, 26, 40, "#333", 4) + R(204, 126, 18, 28, "#9fd0f0", 1, 1)
    return svg(640, 340, "Ein kleines Zimmer mit einem Bett, einem Schreibtisch, einem Schrank und einem Fenster. Zwei Mädchen stehen darin, eines hält ein Handy", b)


@image
def tagesablauf_leiste():
    b = ""
    labels = ["7:00", "7:30", "8:15", "12:30", "4:30", "6:00"]
    for i, t in enumerate(labels):
        x = 10 + (i % 3) * 208
        y = 10 + (i // 3) * 200
        b += R(x, y, 198, 190, "#fffaf0", 8, 3)
        b += text(x + 99, y + 176, t, 28, weight="bold")
    # 1 get up: bed, sun
    x, y = 10, 10
    b += s_bed(x + 20, y + 100, 90) + kid("ellie", x + 110, y + 40, .6) + C(x + 40, y + 40, 18, "#f6d04d")
    # 2 breakfast: table, bowl, cup
    x, y = 218, 10
    b += s_table(x + 14, y + 112) + C(x + 60, y + 104, 12, "#e9c46a") + R(x + 90, y + 98, 14, 14, "#fff", 3) + kid("ellie", x + 110, y + 40, .6)
    # 3 go to school: school bag, houses
    x, y = 426, 10
    b += R(x + 14, y + 50, 70, 70, "#c58b4a", 2) + f'  <polygon points="{x+10},{y+50} {x+49},{y+22} {x+88},{y+50}" fill="#b5651d" stroke="#333" stroke-width="2"/>\n' + R(x + 40, y + 88, 18, 32, "#8a5a2b", 1)
    b += kid("ellie", x + 100, y + 40, .6) + R(x + 118, y + 108, 18, 22, "#2c6fd8", 3)
    # 4 lunch: lunch box, apple
    x, y = 10, 210
    b += R(x + 20, y + 96, 70, 36, "#8fb8e8", 6) + L(x + 20, y + 112, x + 90, y + 112) + C(x + 110, y + 118, 12, "#d33") + kid("ellie", x + 120, y + 40, .6)
    # 5 homework: desk, book
    x, y = 218, 210
    b += s_desk(x + 20, y + 108) + R(x + 34, y + 94, 24, 14, "#2c6fd8", 1) + kid("ellie", x + 110, y + 40, .6)
    # 6 tea: plate, fork
    x, y = 426, 210
    b += s_table(x + 14, y + 112) + C(x + 50, y + 106, 14, "#fff") + L(x + 76, y + 92, x + 76, y + 108, 3) + kid("ellie", x + 110, y + 40, .6)
    return svg(640, 410, "Sechs Bilder in zwei Reihen: ein Mädchen mit rotem Pferdeschwanz bei sechs Tätigkeiten, unter jedem Bild eine Uhrzeit", b)
