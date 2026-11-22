# Bilder des Kapitels menschen-beschreiben (Seiten 2 bis 4). Wird von make_images.py geladen (alle Namen von dort sind da).


def face(cx, cy, r, fill, kind):
    """Ein Gesicht fuer das Barometer: happy, ok, tired, sad, angry."""
    s = f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#333" stroke-width="3"/>\n'
    ex, ey = r * 0.38, r * 0.2
    if kind == "tired":
        for sx in (-1, 1):
            s += (f'  <path d="M{cx+sx*ex-9} {cy-ey} Q{cx+sx*ex} {cy-ey+7} {cx+sx*ex+9} {cy-ey}" fill="none" stroke="#333" stroke-width="3" stroke-linecap="round"/>\n')
    else:
        for sx in (-1, 1):
            s += f'  <circle cx="{cx+sx*ex}" cy="{cy-ey}" r="5" fill="#222"/>\n'
    if kind == "angry":
        s += (f'  <path d="M{cx-ex-12} {cy-ey-16} L{cx-ex+10} {cy-ey-8}" stroke="#333" stroke-width="4" stroke-linecap="round"/>\n'
              f'  <path d="M{cx+ex+12} {cy-ey-16} L{cx+ex-10} {cy-ey-8}" stroke="#333" stroke-width="4" stroke-linecap="round"/>\n')
    my = cy + r * 0.38
    paths = {"happy": f"M{cx-20} {my-6} Q{cx} {my+16} {cx+20} {my-6}",
             "ok": f"M{cx-16} {my} L{cx+16} {my}",
             "tired": f"M{cx-12} {my} Q{cx} {my+6} {cx+12} {my}",
             "sad": f"M{cx-18} {my+8} Q{cx} {my-10} {cx+18} {my+8}",
             "angry": f"M{cx-18} {my+8} Q{cx} {my-8} {cx+18} {my+8}"}
    s += f'  <path d="{paths[kind]}" fill="none" stroke="#333" stroke-width="4" stroke-linecap="round"/>\n'
    if kind == "sad":
        s += f'  <path d="M{cx+ex} {cy-ey+8} q-4 10 0 14 q4 -4 0 -14 z" fill="#6fb6e8" stroke="#2c6fd8" stroke-width="1.5"/>\n'
    return s


# @image
@image
def barometer():
    b = ""
    cols = ["#9bd67a", "#d6dc7a", "#e9d083", "#f0b27a", "#ec7b6e"]
    names = ["happy", "OK", "tired", "sad", "angry"]
    kinds = ["happy", "ok", "tired", "sad", "angry"]
    b += '  <rect x="30" y="20" width="580" height="12" rx="6" fill="#ddd" stroke="#999" stroke-width="2"/>\n'
    for i, (c, n, k) in enumerate(zip(cols, names, kinds)):
        x = 70 + i * 125
        b += face(x, 105, 48, c, k) + text(x, 190, n, 24, weight="bold")
    return svg(640, 215, "Das Barometer: fünf Gesichter in einer Reihe, von fröhlich bis wütend, mit je einem englischen Wort darunter", b)


# @image
@image
def szene_personen_orte_beschreiben():
    b = wall()
    b += '  <rect x="255" y="30" width="130" height="110" rx="6" fill="#bfe0f0" stroke="#7a5a35" stroke-width="6"/>\n'
    b += line(320, 30, 320, 140, 4) + line(255, 85, 385, 85, 4)
    # Kleiderschrank links
    b += '  <rect x="20" y="70" width="110" height="200" rx="6" fill="#b88a55" stroke="#7a5a35" stroke-width="5"/>\n'
    b += line(75, 70, 75, 270, 3) + '  <circle cx="66" cy="170" r="5" fill="#7a5a35"/><circle cx="84" cy="170" r="5" fill="#7a5a35"/>\n'
    # Bett unter dem Fenster links
    b += '  <rect x="150" y="205" width="160" height="60" rx="8" fill="#8fb8e8" stroke="#7a5a35" stroke-width="4"/>\n'
    b += '  <rect x="150" y="190" width="45" height="30" rx="8" fill="#fff" stroke="#7a5a35" stroke-width="3"/>\n'
    b += '  <rect x="155" y="265" width="10" height="25" fill="#7a5a35"/><rect x="295" y="265" width="10" height="25" fill="#7a5a35"/>\n'
    # Schreibtisch rechts, Sophie schreibt
    b += kid("sophie", 460, 110, .75)
    b += table(400, 215, 220, 20)
    b += '  <rect x="470" y="196" width="46" height="20" fill="#fff" stroke="#333" stroke-width="2" transform="rotate(-4 493 206)"/>\n'
    b += line(478, 203, 506, 201, 2) + line(478, 209, 502, 207, 2)
    return svg(640, 340, "Ein Zimmer mit Fenster; ein Mädchen mit Zöpfen hält ein Blatt", b)


# @image
@image
def szene_gefuehle_freundschaft():
    b = wall()
    b += '  <rect x="230" y="25" width="180" height="100" rx="6" fill="#bfe0f0" stroke="#7a5a35" stroke-width="6"/>\n'
    b += line(320, 25, 320, 125, 4)
    b += kid("ellie", 285, 75, .75) + kid("amir", 40, 105, .8) + kid("sophie", 540, 120, .7) + kid("peter", 410, 135, .65)
    # Spielschachtel zwischen Amir und Peter, zwei Haende ziehen
    b += '  <rect x="205" y="215" width="80" height="50" rx="4" fill="#e8b84a" stroke="#333" stroke-width="3"/>\n'
    b += '  <circle cx="230" cy="240" r="9" fill="#d33"/><circle cx="262" cy="240" r="9" fill="#2c6fd8"/>\n'
    b += '  <path d="M125 230 L205 235" stroke="#f1cdb0" stroke-width="12" stroke-linecap="round"/>\n'
    b += '  <path d="M425 250 L286 245" stroke="#f1cdb0" stroke-width="12" stroke-linecap="round"/>\n'
    b += '  <path d="M80 100 l10 -22 l6 14 l12 -26" fill="none" stroke="#d33" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>\n'
    b += '  <path d="M440 125 l10 -22 l6 14 l12 -26" fill="none" stroke="#d33" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>\n'
    return svg(640, 340, "Zwei Jungen ziehen an einer Spielschachtel, zwischen ihnen steht ein Mädchen, ein weiteres Mädchen schaut zu", b)


# @image
@image
def szene_gesundheit():
    b = wall()
    # Tuer mit gruenem Kreuz
    b += '  <rect x="440" y="40" width="130" height="222" rx="6" fill="#d9b98a" stroke="#7a5a35" stroke-width="6"/>\n'
    b += '  <rect x="480" y="62" width="50" height="50" rx="6" fill="#fff" stroke="#138d75" stroke-width="3"/>\n'
    b += '  <path d="M505 70 v34 M488 87 h34" stroke="#138d75" stroke-width="10"/>\n'
    # Bank
    b += '  <rect x="90" y="215" width="300" height="22" rx="6" fill="#d9b98a" stroke="#7a5a35" stroke-width="3"/>\n'
    b += '  <rect x="100" y="237" width="10" height="40" fill="#7a5a35"/><rect x="370" y="237" width="10" height="40" fill="#7a5a35"/>\n'
    b += kid("mrs-parker", 110, 85, .85) + kid("peter", 270, 105, .75)
    # Peter haelt sich den Bauch
    b += '  <path d="M270 190 Q300 215 330 192" stroke="#d33" stroke-width="12" fill="none" stroke-linecap="round" opacity=".0"/>\n'
    b += '  <circle cx="321" cy="205" r="9" fill="#f3d2b3" stroke="#333" stroke-width="2"/>\n'
    b += '  <path d="M345 200 l12 -6 M347 212 l14 0 M345 224 l12 6" stroke="#d33" stroke-width="4" stroke-linecap="round"/>\n'
    return svg(640, 340, "Ein Wartezimmer: Eine Frau und ein Junge sitzen auf einer Bank, der Junge hält sich den Bauch, rechts eine Tür mit grünem Kreuz", b)


# @image
@image
def koerper():
    b = ""
    SK = "#f1cdb0"
    b += '  <g transform="translate(-28,10) scale(.7)">\n'
    # Vorderansicht (Mitte x=190)
    b += f'  <rect x="168" y="118" width="44" height="30" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M120 150 Q190 130 260 150 L268 300 L112 300 Z" fill="#7fb8e8" stroke="#333" stroke-width="3"/>\n'
    for sx in (-1, 1):
        x0 = 190 + sx * 76
        b += f'  <path d="M{x0} 158 L{x0+sx*34} 270" stroke="#7fb8e8" stroke-width="30" stroke-linecap="round"/>\n'
        b += f'  <circle cx="{x0+sx*38}" cy="286" r="17" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
        lx = 190 + sx * 28
        b += f'  <rect x="{lx-22}" y="298" width="44" height="115" rx="12" fill="#3f5f8a" stroke="#333" stroke-width="3"/>\n'
        b += f'  <ellipse cx="{lx+sx*8}" cy="424" rx="32" ry="12" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += f'  <circle cx="148" cy="78" r="11" fill="{SK}" stroke="#333" stroke-width="3"/><circle cx="232" cy="78" r="11" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += f'  <ellipse cx="190" cy="72" rx="45" ry="52" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M146 62 Q148 20 190 20 Q232 20 234 62 Q220 40 190 42 Q160 40 146 62 Z" fill="#8a5a2b"/>\n'
    b += '  <circle cx="174" cy="68" r="5" fill="#222"/><circle cx="206" cy="68" r="5" fill="#222"/>\n'
    b += '  <path d="M190 74 l-5 14 h10" fill="none" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M170 98 Q190 118 210 98 Z" fill="#fff" stroke="#333" stroke-width="3"/><rect x="186" y="99" width="9" height="8" fill="#fff" stroke="#333" stroke-width="1.5"/>\n'
    b += '  </g>\n'
    # Rueckansicht (Mitte x=500)
    b += '  <g transform="translate(-60,10) scale(.7)"><g transform="translate(-20,0)">\n'
    b += f'  <rect x="500" y="118" width="40" height="30" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M455 150 Q520 130 585 150 L592 300 L448 300 Z" fill="#7fb8e8" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M520 150 L520 290" stroke="#333" stroke-width="3" stroke-dasharray="8 6"/>\n'
    b += f'  <ellipse cx="520" cy="72" rx="45" ry="52" fill="#8a5a2b" stroke="#333" stroke-width="3"/>\n'
    for sx in (-1, 1):
        x0 = 520 + sx * 72
        b += f'  <path d="M{x0} 158 L{x0+sx*30} 270" stroke="#7fb8e8" stroke-width="28" stroke-linecap="round"/>\n'
        b += f'  <circle cx="{x0+sx*34}" cy="286" r="16" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
        lx = 520 + sx * 26
        b += f'  <rect x="{lx-21}" y="298" width="42" height="115" rx="12" fill="#3f5f8a" stroke="#333" stroke-width="3"/>\n'
        b += f'  <ellipse cx="{lx+sx*8}" cy="424" rx="32" ry="12" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += '  </g></g>\n'
    # grosses Gesicht rechts: Augen, Ohren, Nase und Mund mit Zaehnen, weit auseinander
    b += f'  <circle cx="392" cy="172" r="19" fill="{SK}" stroke="#333" stroke-width="3"/><circle cx="608" cy="172" r="19" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += f'  <ellipse cx="500" cy="165" rx="108" ry="118" fill="{SK}" stroke="#333" stroke-width="3"/>\n'
    b += '  <path d="M394 140 Q392 50 500 46 Q608 50 606 140 Q580 84 500 88 Q420 84 394 140 Z" fill="#8a5a2b"/>\n'
    b += '  <circle cx="460" cy="135" r="9" fill="#222"/><circle cx="540" cy="135" r="9" fill="#222"/>\n'
    b += '  <path d="M500 142 l-12 38 h24" fill="none" stroke="#333" stroke-width="4"/>\n'
    b += '  <path d="M458 225 Q500 262 542 225 Z" fill="#fff" stroke="#333" stroke-width="4"/><path d="M473 227 v10 M487 229 v12 M500 230 v13 M513 229 v12 M527 227 v10" stroke="#aaa" stroke-width="2"/>\n'
    return svg(640, 330, "Eine Figur von vorn und von hinten und daneben ein großes Gesicht", b)
