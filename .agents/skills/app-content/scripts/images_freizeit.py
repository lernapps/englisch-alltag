# Figures of chapter freizeit-nachrichten: Wochenplan, Einladungskarte, Postkarte mit Bauplan.
# Loaded by make_images.py (which gives this file its helper functions).

@image
def wochenplan():
    b = ""
    cols = [(230, "Monday"), (390, "Wednesday"), (550, "Saturday")]
    for cx, d in cols:
        b += text(cx, 34, d, 20, weight="bold")
    plan = [("ellie", "Ellie", ["swim", "play the guitar", "ride a bike"]),
            ("peter", "Peter", ["play football", "draw", "swim"]),
            ("amir", "Amir", ["read", "play football", "play the guitar"]),
            ("sophie", "Sophie", ["dance", "read", "ride a bike"])]
    for i, (k, name, acts) in enumerate(plan):
        y = 50 + i * 92
        b += f'  <rect x="10" y="{y}" width="620" height="84" rx="8" fill="#fff" stroke="{INK}" stroke-width="2"/>\n'
        b += kid(k, 62, y + 2, .27) + text(76, y + 80, name, 17)
        for (cx, _), a in zip(cols, acts):
            b += card(cx - 70, y + 20, 140, 44, a, 18, fill="#e6f0fb")
    return svg(640, 424, "Wochenplan mit vier Kindern: Für jedes Kind steht an drei Tagen ein Hobby", b)


@image
def einladung():
    b = f'  <rect x="30" y="20" width="580" height="370" rx="14" fill="#fff" stroke="{BLUE}" stroke-width="5"/>\n'
    b += text(60, 62, "Party invitation", 26, "start", BLUE, "bold")
    b += kid("amir", 500, 24, .32)
    b += text(60, 100, "Dear Sophie, Ellie and Peter,", 20, "start")
    rows = [("Who", "I am Amir."), ("What", "my birthday party"), ("When", "on Saturday afternoon, from three to six"),
            ("Where", "at my house"), ("Answer", "yes or no, please")]
    for i, (l, v) in enumerate(rows):
        y = 150 + i * 46
        b += f'  <rect x="50" y="{y-24}" width="100" height="34" rx="6" fill="{BLUE}"/>\n' + text(100, y, l, 20, fill="#fff", weight="bold")
        b += text(166, y, v, 19, "start")
        b += line(50, y + 16, 590, y + 16, 1)
    b += text(60, 378, "Love, Amir", 20, "start")
    return svg(640, 410, "Eine Einladungskarte mit fünf Feldern: Who, What, When, Where und Answer", b)


@image
def postkarte():
    b = f'  <rect x="20" y="20" width="430" height="320" rx="10" fill="#fff" stroke="#7a5a35" stroke-width="4"/>\n'
    parts = [(46, 86, BLUE, "1", "Anrede"), (104, 230, GREEN, "2", "Text"), (258, 306, ORANGE, "3", "Gruß")]
    for y1, y2, c, n, lab in parts:
        b += f'  <rect x="30" y="{y1}" width="350" height="{y2-y1}" rx="6" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-width="2"/>\n'
        b += f'  <line x1="452" y1="{(y1+y2)//2}" x2="380" y2="{(y1+y2)//2}" stroke="{c}" stroke-width="3"/>\n'
        b += text(466, (y1 + y2) // 2 + 7, f"{n} {lab}", 22, "start", c, "bold")
    b += text(44, 74, "Dear Mum and Dad,", 22, "start")
    for i, t in enumerate(["It is sunny in Millbrook today.", "We play in the garden.", "I am happy here."]):
        b += text(44, 138 + i * 36, t, 19, "start")
    b += text(44, 292, "Love, Sophie", 22, "start")
    return svg(640, 360, "Eine Postkarte mit drei farbigen Teilen: oben eine Zeile, in der Mitte drei Zeilen, unten eine Zeile", b)
