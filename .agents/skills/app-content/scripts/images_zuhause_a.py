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


@image
def haus_querschnitt():
    b = ""
    b += '  <polygon points="0,76 240,14 480,76" fill="#b5651d" stroke="#333" stroke-width="3"/>\n'
    b += '  <rect x="470" y="372" width="170" height="28" fill="#9bd18b"/>\n'
    b += C(590, 52, 26, "#f6d04d")
    # upper floor: five rooms of 92, y 76-212
    up = ["bathroom", "Ellie's|room", "Peter's|room", "Sophie's|room", "parents'|bedroom"]
    for i, name in enumerate(up):
        x = 10 + i * 92
        b += R(x, 76, 92, 136, "#efe7d3", 0, 3)
        for j, part in enumerate(name.split("|")):
            b += text(x + 46, 98 + j * 20, part, 17)
    # lower floor: two rooms of 230, y 212-372
    b += R(10, 212, 230, 160, "#f3ead0", 0, 3) + R(240, 212, 230, 160, "#e9eed8", 0, 3)
    b += text(125, 236, "kitchen", 18) + text(355, 236, "living room", 18)
    b += '  <rect x="10" y="372" width="630" height="28" fill="#9bd18b"/>\n'
    # signs on the upper floor (floor line y = 210)
    b += s_bath(16, 178) + s_toilet(70, 170) + s_sink(40, 134)
    # Ellie's room (x 102-194)
    b += s_poster(108, 122) + s_bed(106, 172, 42) + s_desk(150, 178) + s_lamp(176, 124)
    # Peter's room (x 194-286)
    b += s_bed(198, 172, 32) + s_toys(234, 182) + s_shelf(240, 150)
    # Sophie's room (x 286-378): small, bed, desk, wardrobe, window
    b += s_window(296, 128, 34, 34) + s_wardrobe(340, 138) + s_bed(292, 176, 40) 
    # parents' bedroom (x 378-470)
    b += s_bed(388, 172, 62) + s_lamp(452, 164)
    # kitchen
    b += s_fridge(22, 300) + s_cooker(66, 322) + s_sink(120, 330) + s_table(164, 334) + s_chair(160, 330) + s_chair(220, 330)
    # living room
    b += s_sofa(256, 330) + s_armchair(342, 330) + s_bookshelf(398, 304) + s_lamp(440, 322) + s_tv(260, 262)
    # garden
    b += text(556, 206, "garden", 18) + s_tree(520, 280) + s_flowers(536, 348) + s_bench(584, 346)
    return svg(640, 400, "Querschnitt eines Hauses mit zwei Stockwerken, Garten rechts. Die Zimmer tragen Namen, die Möbel sind kleine Zeichen", b)


@image
def szene_wohnen():
    b = wall()
    b += s_window(300, 40, 120, 110)
    b += s_bed(40, 190, 150) + s_wardrobe(560, 120) + s_desk(440, 190)
    b += kid("sophie", 220, 70, .85) + kid("ellie", 120, 120, .6)
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
