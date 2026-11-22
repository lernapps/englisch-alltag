# Figures of the pages essen-trinken and alltag-uk (chapter zuhause-parkers). Loaded by make_images.py, which gives this
# file all its names (svg, kid, text, wall, table, card, line ...).


@image
def fruehstueck():
    b = wall()
    b += '  <rect x="40" y="25" width="150" height="110" rx="6" fill="#bfe0f0" stroke="#7a5a35" stroke-width="6"/>\n'
    b += line(115, 25, 115, 135, 4) + line(40, 80, 190, 80, 4)
    b += '  <circle cx="160" cy="55" r="16" fill="#f6d04d" stroke="#d9a600" stroke-width="3"/>\n'
    b += kid("ellie", 125, 100, .75) + kid("sophie", 240, 100, .75) + kid("peter", 442, 100, .6)
    b += table(140, 190, 360, 24)
    b += '  <rect x="140" y="214" width="360" height="40" fill="#e8d3a8" stroke="#7a5a35" stroke-width="3"/>\n'
    # cereal bowl, milk bottle, toast with jam on a plate, jam jar, glass of orange juice (no labels: the words are learned on the page)
    b += '  <path d="M163 176 Q185 206 207 176 Z" fill="#fff" stroke="#333" stroke-width="2.5"/>\n'
    b += '  <ellipse cx="185" cy="176" rx="22" ry="5" fill="#e8c27a" stroke="#333" stroke-width="2"/>\n'
    b += '  <rect x="236" y="150" width="18" height="40" rx="4" fill="#fff" stroke="#333" stroke-width="2.5"/><rect x="239" y="142" width="12" height="10" fill="#fff" stroke="#333" stroke-width="2"/>\n'
    b += '  <ellipse cx="305" cy="188" rx="30" ry="6" fill="#fff" stroke="#333" stroke-width="2.5"/>\n'
    b += '  <rect x="287" y="172" width="36" height="14" rx="3" fill="#e0b060" stroke="#333" stroke-width="2.5"/><rect x="291" y="175" width="28" height="5" fill="#b3202a"/>\n'
    b += '  <rect x="353" y="164" width="24" height="26" rx="4" fill="#b3202a" stroke="#333" stroke-width="2.5"/><rect x="351" y="158" width="28" height="8" rx="2" fill="#fff" stroke="#333" stroke-width="2"/>\n'
    b += '  <path d="M413 160 L437 160 L433 190 L417 190 Z" fill="#f7a823" stroke="#333" stroke-width="2.5"/>\n'
    return svg(640, 340, "Drei Kinder sitzen hinter einem Tisch, auf dem eine Schale, eine Flasche, ein Teller mit Brot, ein Glas mit rotem Deckel und ein Glas mit Saft stehen", b)


@image
def zwei_spalten():
    b = ""
    X0, X1, X2, W = 20, 150, 430, 640
    top = 20
    # header
    b += card(X1, top, 270, 44, "Ellies Alltag", 21, "#fbe3e0")
    b += card(X2, top, 190, 44, "Mein Alltag", 21, "#e2eefb")
    rows = (("family", "mum, dad, brother"), ("house", "two floors, garden"), ("breakfast", "cereal, toast, juice"),
            ("lunch", "packed lunch at school"), ("tea", "pasta at six o'clock"))
    for i, (k, v) in enumerate(rows):
        y = top + 54 + i * 54
        b += text(X0 + 55, y + 33, k, 21, "middle", INK, "bold")
        b += card(X1, y, 270, 46, v, 19)
        b += (f'  <rect x="{X2}" y="{y}" width="190" height="46" rx="8" fill="#fff" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>\n'
              f'  <line x1="{X2+12}" y1="{y+34}" x2="{X2+178}" y2="{y+34}" stroke="#aaa" stroke-width="2"/>\n')
    return svg(640, 350, "Eine Tabelle mit zwei Spalten: links Ellies Alltag in fünf Zeilen, rechts eine leere Spalte zum Ausfüllen", b)
