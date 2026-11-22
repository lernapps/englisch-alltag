---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Alltag: Ich, meine Familie, mein Zuhause“: Explainer (Einheiten-App `subject: englisch`, Format 2, Sprache Deutsch, englische Beispiele). Auftrag: Issue lernapps/apps#477 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut Stufe 5-6: alle drei Kapitel und alle elf Bausteine. Spätere Stufen (7-8, 9-10) kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-21; Fokus `competency`, deshalb eine Einheiten-App über mehrere Stränge). Vorwissen: #470 bis #476 und #480; was die Kapitel davon brauchen, wiederholt je eine Wiederholungsseite. Nicht hier: Schule, Uhrzeit, Datum (#470); Stadt, Einkaufen, Reisen (#478); Meinungen zu Sport, Musik, Medien (#487); Geschichten erzählen (#479); Briefe an fremde Leser (#486); simple past und present perfect (#472).

## Competencies

Alle elf sind Lücken der Karte, Band 5-6. Eine Seite je Baustein. `competencies` im Seitenkopf nennt die Karten-Id (nie den Seitentitel); der „Ich kann“-Satz steht hier wortgleich wie in der Karte (nicht umformulieren) und auf den Wiederholungsseiten im Text.

1. Kapitel `menschen-beschreiben` („Menschen beschreiben“)
   - Wiederholung `das-brauchst-du` (`recap: [englisch/have-got, englisch/adjektive]`, ohne Übung, ohne `competencies`)
   - `familie-personen` (Musterseite): „Ich kann Familienmitglieder benennen und Menschen mit einfachen Wörtern nach Aussehen und Charakter beschreiben.“
   - `personen-orte-beschreiben`: „Ich kann in einem Text eine Person oder einen Ort anschaulich beschreiben.“
   - `gefuehle-freundschaft`: „Ich kann über Gefühle, Freundschaft und Streit sprechen, auch über Mobbing.“
   - `gesundheit`: „Ich kann Körperteile und Beschwerden benennen und beim Arzt oder in der Apotheke sagen, was mir fehlt.“
2. Kapitel `zuhause-parkers` („Zuhause bei den Parkers“)
   - Wiederholung `das-brauchst-du` (`recap: [englisch/there-is-are, englisch/simple-present, englisch/praepositionen-zeit]`)
   - `wohnen`: „Ich kann mein Zuhause beschreiben: Räume, Möbel und Garten.“
   - `tagesablauf`: „Ich kann meinen Tagesablauf beschreiben (I get up at seven …).“
   - `essen-trinken`: „Ich kann Lebensmittel und Mahlzeiten benennen und über Essgewohnheiten sprechen.“
   - `alltag-uk`: „Ich kann das Familienleben, das Wohnen und das Essen in Großbritannien beschreiben und mit meinem Alltag vergleichen.“
3. Kapitel `freizeit-nachrichten` („Freizeit und Nachrichten“)
   - Wiederholung `das-brauchst-du` (`recap: englisch/gruss-hoeflichkeit`)
   - `freizeit-hobbys`: „Ich kann über meine Hobbys, Haustiere und meine Freizeit sprechen.“
   - `kurznachricht`: „Ich kann eine kurze Nachricht, eine Notiz oder eine Einladung schreiben.“
   - `email-postkarte`: „Ich kann eine persönliche E-Mail, einen Brief oder eine Postkarte mit passender Anrede und passendem Schluss schreiben.“ (Kapitelschluss; schließt das Profil „All about me“.)

Übungs-IDs: Präfix = Seite (`familie-personen-haare`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`, Anwenden `<seite>-profil` (Profil-Zeile) und `<seite>-text`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Bausteinseite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Bild, Merke-Kasten, Poster-Tabelle, höchstens eine kurze Wörter-Tabelle), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task`, dann Tabelle „All about me · <Thema>“ mit Ellies Beispiel und der `open-task` der Profil-Zeile), `weiter` (Sophies Nachricht und der nächste Schritt in einer kurzen Zeile; am Kapitelende ein Rückblick). Titel sagen, was der Abschnitt tut. Die Wiederholungsseite hat nur Text und Tabellen.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken; Seiten mit mehr als etwa 25 Items oder 10 Übungen kürzen. Jede Seite bringt einen neuen Schritt (`explainer-one-step`).
- Audio: 6 Sätze je Bausteinseite (3 Diktat, 3 Nachsprechen), 66 insgesamt, Liste `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz). Jeder Satz endet auf ein zweisilbiges Wort, meist einen Namen (Sophie, Peter, Ellie, Amir) oder ein zweisilbiges Wort wie family, people, clever, funny, happy, pretty, garden, table, bathroom, weekend, sofa, today; die Sätze, die nicht auf einen Namen enden, sollte die Ersteller:in gezielt anhören (Aufnahmen sind nicht abgehört). Kein Hörsatz steht (auch fast) wörtlich im Text, Poster, Merke, in einer Auswahl-, Ordnungs-, Schreib- oder Übersetzungsübung derselben Seite.
- Selbsteinschätzung: je Kapitel in `chapter.yaml`, zwei schreibende oder auswählende Übungen je Bausteinseite (nicht die Wiederholungsseiten).
- Geschichte: Sophie (11-12, aus Deutschland) wohnt im ersten Schuljahr bei den Parkers in Millbrook und schickt ihrer Familie zu Hause Nachrichten. Jede Seite hat eine Szene im Haus der Familie oder unterwegs mit den Kindern und einen Satz, den Sophie nach Hause schreibt. Das Profil „All about me“ wächst: Jede Seite hat in `anwenden` eine Tabelle „All about me · <Thema>“ (Ellies Beispiel) und eine offene Aufgabe, die das Kind in sein Heft schreibt (nichts wird gespeichert; die Aufgabe ist offen formuliert, keine Familienform gilt als Normalfall, die Musterlösung hat ein zweites Beispiel ohne Standardfamilie); `email-postkarte` zeigt am Ende alle Zeilen zusammen (Ellies Beispiel). Zwei Spalten „Ellies Alltag und mein Alltag“ stehen auf `alltag-uk`. Gefühle und Gesundheit bleiben altersgerecht: kleine Beschwerden (Kopf, Bauch, Husten), Mobbing nur als „Don’t do that. Tell a teacher.“
- Figuren und Orte wie in #470 und `konventionen.md` (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (Englischlehrer, graue Haare, braune Jacke), Mrs Parker (Ellies Mutter, Sophies Gastmutter); aus #477: Mr Parker (Ellies und Peters Vater, kurze braune Haare, graue Strickjacke), Grandma Parker (graue Haare zum Dutt, lila Strickjacke) nur im Stammbaum und als Beispiele, Sophies Eltern nur „Mum and Dad“ (Sophies Mum blond, kleines Foto im Stammbaum, ohne Namen). Millbrook School, Schultag ab 8:45; Geburtstage Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Keine weiteren Figuren ohne Rückfrage. Nicht benutzen: Lagerraum und Schulfest (#475), Ausstellung „Our Millbrook“ (#476). Die Einladung in `kurznachricht` kommt von Amir (Geburtstag 12. Oktober; die Einladung nennt nur „Saturday afternoon“, kein Datum und kein Jahr).
- Anrede „du“.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence (ab #470). Tabellen heißen „Klassenzimmer-Poster · …“, „Schulkalender · …“ und „All about me · …“ und wachsen von Seite zu Seite.
- Feste Wörter dieser App: „All about me“ (das Profil), „Steckbrief“ (Karte mit Name, Alter, Aussehen, Charakter), „Stammbaum“, „Barometer“ (Gefühle, fünf Gesichter), „Bildleiste“ (der Tag), „Bauplan“ (Brief: Anrede, Text, Gruß), „Anrede“ und „Gruß“.
- Britisches Englisch (favourite, colour, mum, biscuit, tea). Englische Aufgaben enthalten kein deutsches Wort. Englisches immer mit deutscher Bedeutung, wo ein Wort neu ist.
- Aussprache: keine Lesehilfe und keine Lautschrift (IPA gehört zu #482); Hörtexte nur als ganze Sätze.

## Exercise patterns

Aufbau leicht → schwer: lesen/wählen → zuordnen → ordnen → Lücke → schreiben mit Cue → übersetzen/korrigieren → frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`; `punctuation: ok`, `case: hint`.

- Bild lesen: `single-choice` (mindestens drei Optionen, jede mit `info`) und `true-false` zum Bild des Einstiegs.
- Zuordnen: `matching` (Körperteil ↔ Beschwerde, Möbel ↔ Raum, Mahlzeit ↔ Speise, Gefühl ↔ Gesicht, Teil ↔ Feld des Bauplans).
- Ordnen: `ordering` (Sätze eines Textes, Schritte des Tages, Teile einer Einladung).
- Lücke wählen: `language-task` mode `choice` mit `distractors`; Form bilden: mode `write` mit englischem `cue`; übersetzen mit `source`; korrigieren: ein Fehler im Satz.
- Hören und schreiben: `language-task` mit `audio` (Diktat, drei ganze Sätze je Seite); Nachsprechen: `speaking-task` (drei andere Sätze); Frei: `open-task` mit Punkten und Musterlösung (Profil-Zeile, Text, Einladung, Postkarte, E-Mail).
- Typische Fehler (je eigene Meldung; Mr/Mrs und my/his/her werden geübt): Peter is a brother of Ellie (Ellie’s brother), Ellie have red hair, she/her und my/her verwechselt, I have a headache ohne Artikel, My head hurt (-s), I am boring (statt bored), angry on you, There is two chairs, in the morning/at the morning, She get up, go to home, I eat the breakfast, He like tea, I like swim, I go to swimming, On Saturday ohne on, Dear Mum ohne Komma, Gruß ohne Namen.
- Keine Komponente (`prefer-built-in-block`), keine Datendatei: jede Tatsache steht einmal in ihrer Seite.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py` (Aufruf im App-Ordner: `python3 .agents/skills/app-content/scripts/make_images.py [name …]`; nie die SVG von Hand ändern). Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, bei 360 px lesbar. Skizzen in `.vibe/sketches/`.
- Die vier Kinder sind die `<g id>` aus `millbrook-klassenzimmer.svg` von hello-millbrook (#470), unverändert kopiert; Mrs Parker, Mr Hill, Mr Parker und Grandma Parker zeichnet `make_images.py` im selben Stil nach den Beschreibungen oben. Keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. `alt` sagt, was das Bild zeigt, nie die Lösung der Übung auf derselben Seite. Die Bildunterschrift nennt, wer wer ist (Sophie Zöpfe, Ellie roter Pferdeschwanz, Amir Brille, Peter gelbe Jacke).
- Bilder (`src/images/`, erzeugt von `make_images.py` und den Dateien `images_menschen.py`, `images_zuhause_a.py`, `images_zuhause_b.py`, `images_freizeit.py` im selben Ordner): `szene-familie-personen`, `stammbaum`, `szene-personen-orte-beschreiben`, `barometer`, `szene-gefuehle-freundschaft`, `koerper`, `szene-gesundheit`, `szene-wohnen`, `haus-querschnitt`, `tagesablauf-leiste`, `fruehstueck`, `zwei-spalten`, `wochenplan`, `einladung`, `postkarte`. Ein neues Bild: Funktion mit `@image` in einer `images_*.py` ergänzen und `make_images.py <name>` starten.
- Tabellen: „Klassenzimmer-Poster · …“, „Schulkalender · …“, „All about me · …“ als `table`-Blöcke; je Seite höchstens eine kurze Tabelle „Wörter dieser Seite“.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-21); Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2, geöffnet 2026-11-21; Wörter der Übungen kommen aus A1 und A2, ein Wort außerhalb steht auf der Seite mit Bedeutung und in der Liste unten). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-21: `Tea (meal)` (tea ist ein Oberbegriff für mehrere Mahlzeiten; im Alltag auch die frühe Abendmahlzeit) und `Packed lunch` (Mittagessen, das man von zu Hause mitbringt). Nicht geprüft: deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines. Wörter außerhalb von A1/A2 (nicht in der Liste oder schwerer), jeweils auf der Seite im Poster „Wörter dieser Seite“ mit Bedeutung (Stand der gebauten Seiten): `familie-personen` glasses, ponytail, kind, helpful, curly, short / long, clever; `personen-orte-beschreiben` wardrobe, shelf, curly, quiet, there is / there are; `gefuehle-freundschaft` sad / tired / angry, excited, bored, worried, afraid, best friend; `gesundheit` stomach, throat, sore throat, tooth, cough (neck und medicine stehen im Text); `wohnen` wardrobe, armchair, cooker, sink, bookshelf, bench, toys; `tagesablauf` get up, have tea, do homework, go home, at night; `essen-trinken` cereal, jam, yoghurt, vegetables, packed lunch; `alltag-uk` cereal, packed lunch, at the Parkers’, everybody; `freizeit-hobbys` basketball, violin, parrot, hiking, at the weekend; `kurznachricht` invitation, I’d love to come, Back at six, buy (can, can’t, cannot im Text erklärt); `email-postkarte` postcard, best wishes, subject, cold (hier: kalt). Nicht geprüft und nicht benutzt: Fakten zu `Semi-detached house`, `Full breakfast`, `Sunday roast` (HTTP 429) und zu `Terraced house` (Seite nicht gelesen, nur der Titel kam an): Auf den Seiten stehen als Fakten über Großbritannien nur „tea“ (Oberbegriff für mehrere Mahlzeiten, auch die frühe Abendmahlzeit) und „packed lunch“ (zu Hause vorbereitetes Mittagessen), alles andere nur „bei den Parkers“.

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen (`recap` mit Karten-Ids).
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen; Kapitel in `src/app.yaml` eintragen.
3. Bilder: Funktion in `make_images.py` ergänzen und das Skript starten; Zeile für „All about me“ und die Poster-Tabellen ergänzen.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 2 je Seite in `selfAssessment` (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz, 6 je Seite: 3 Diktat, 3 Nachsprechen), erzeugt mit `~/.cache/lernapps/audio/venv/bin/python .agents/skills/app-content/scripts/regen_audio.py .agents/skills/app-content/scripts/audio-texte.json [Satz …]` (schneidet das Ausklingen ab); Sätze nicht zwischen Seiten wiederholen, Namen am Satzende zweisilbig.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus #470 bis #476 und Abschnitt 7 der Konventionen übernommen:
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen. Wörter außerhalb von A1/A2 stehen auf der Seite erklärt und im Inhaltsführer.
- Eine Tabelle oder ein Bild, das eine Übung beantwortet, steht nicht direkt darüber; Poster, Merke, Einstieg und Bild nennen andere Beispielsätze und Wörter als die Übungen darunter.
- Diktat und Nachsprechen bringen neue Sätze: kein Hörsatz steht (auch fast wörtlich, mit getauschtem Namen oder getauschter Farbe) im Einstieg, Poster, Merke, Bildtext oder in einer Auswahl-, Ordnungs-, Schreib- oder Übersetzungsübung derselben Seite.
- Englische Aufgaben enthalten kein deutsches Wort; der Cue ist englisch, der deutsche Hinweis steht in `source` oder in der Aufgabe.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen (auch Kurzformen); `accepted` einer Sprach-Aufgabe wirkt nicht; `punctuation: ok` setzen; `case: wrong` nur dort, wo die Seite Großschreibung unterrichtet.
- Distraktoren nur echte Lernerfehler (keine Unwörter, keine erfundenen Schreibfehler); jeder Distraktor und jedes typische Fehlerbild hat eine eigene Meldung. Ein Einstiegs-`single-choice` hat mindestens drei Optionen. Im Modus `choice` zeigt die Vorlage `mistakes` nicht: Plane die Übungen danach.
- Höchstens eine kurze Wörtertabelle je Seite; einfache Wörter gelten als bekannt.
- Audio: das Ausklingen der Stimme am Satzende abschneiden (`regen_audio.py`), Namen am Satzende zweisilbig (Sophie, Peter, Ellie, Amir).
- Bilder: Beschriftungen innerhalb des `viewBox`; `alt` verrät nie die Lösung; die Bildunterschrift nennt, wer wer ist.
- `competencies:` sind Karten-Ids, nie Seitentitel; Wiederholungsseiten haben keine.
- Wo die Meldung eines Fehlers wichtig ist, kein `mode: choice` (zeigt `mistakes` nicht), sondern `single-choice` mit `info` je Option oder `mode: gap`/`write` mit `mistakes`; ein Distraktor im `matching` hat keine eigene Meldung: Die Erklärung nennt ihn.
- Typische Fehler, die der Inhaltsführer nennt (my/her, Mr/Mrs), werden auch geübt.
- Hinweise und Meldungen einer Selbsteinschätzungs-Übung nennen weder „Spalte“ noch „Poster“ noch „oben“.
- `ordering` zeigt Auswahlfelder statt Karten (Eigenheit der Vorlage); `punctuation: hint` meldet bei richtiger Antwort „Achte auf die Satzzeichen“.
Aus dem Bau dieser App (Prüfungen der Seiten durch Sub-Agenten, Kind Klasse 5-6 und Sprachprüfung):
- `accepted` wirkt in `language-task` nicht und zeigt dem Kind den Rohtext: alle richtigen Fassungen stehen als `(a|b)`-Gruppen in `target` (nicht verschachtelt, höchstens 64 Fassungen).
- Zahl, Farbe, Zeit und Ort im Bild stimmen mit jedem Satz überein (Stühle, Lampen, Bettfarbe in Sophies Zimmer, Zeiten von Ellies Tag); Figuren und Fakten der Geschichte stehen in `facts` des Plans und gelten auf jeder Seite (Peter mag keine Suppe, Ellies Tag).
- Fehlt ein Wort oder eine Regel, bevor eine Übung sie braucht (can, doesn’t, goes), steht sie vorher auf der Seite oder die Übung entfällt; Schluss und Einstieg zweier Seiten passen zusammen.
- `punctuation: wrong` nur dort, wo die Seite das Satzzeichen lehrt (Komma vor but, Komma nach der Anrede); sonst `ok`.
- Typische Fehler mit Meldung nur in `write` und `single-choice` (nicht `choice`, `gap`, `matching`, `ordering`); `alt` eines Bildes verrät nie die Lösung.
- Die Gesamttabelle „All about me“ am Ende von `email-postkarte` übernimmt die Sätze der Profil-Tabellen der Seiten wörtlich (bei Änderung einer Profil-Zeile hier nachziehen).
