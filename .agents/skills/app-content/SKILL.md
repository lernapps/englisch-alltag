---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Alltag: Ich, meine Familie, mein Zuhause“: Explainer (Einheiten-App `subject: englisch`, Format 2, Sprache Deutsch, englische Beispiele). Auftrag: Issue lernapps/apps#477 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut Stufe 5-6: alle drei Kapitel und alle elf Bausteine. Spätere Stufen (7-8, 9-10) kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-21; Fokus `competency`, deshalb eine Einheiten-App über mehrere Stränge). Vorwissen: #470 bis #476 und #480; was die Kapitel davon brauchen, wiederholt je eine Wiederholungsseite. Nicht hier: Schule, Uhrzeit, Datum (#470); Stadt, Einkaufen, Reisen (#478); Meinungen zu Sport, Musik, Medien (#487); Geschichten erzählen (#479); Briefe an fremde Leser (#486); simple past und present perfect (#472).

## Competencies

Alle elf sind Lücken der Karte, Band 5-6. Eine Seite je Baustein; die „Ich kann“-Sätze stehen wortgleich wie in der Karte in `competencies` des Seitenkopfs und im Text (nicht umformulieren).

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

Übungs-IDs: Präfix = Seite (`familie-personen-platz`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`, Anwenden `<seite>-profil` (Profil-Zeile) und `<seite>-text`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Bausteinseite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Bild, Merke-Kasten, Poster-Tabelle, höchstens eine kurze Wörter-Tabelle), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` und `open-task`), `weiter` (Profil-Zeile „All about me“ und nächster Schritt; am Kapitelende ein Rückblick). Titel sagen, was der Abschnitt tut. Die Wiederholungsseite hat nur Text und Tabellen.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken; Seiten mit mehr als etwa 25 Items oder 10 Übungen kürzen. Jede Seite bringt einen neuen Schritt (`explainer-one-step`).
- Audio: 6 Sätze je Bausteinseite (3 Diktat, 3 Nachsprechen), 66 insgesamt, Liste `.agents/skills/app-content/scripts/audio-texte.json`. Kein Hörsatz steht (auch fast) wörtlich im Text, Poster, Merke, in einer Auswahl-, Ordnungs-, Schreib- oder Übersetzungsübung derselben Seite.
- Selbsteinschätzung: je Kapitel in `chapter.yaml`, zwei schreibende oder auswählende Übungen je Bausteinseite (nicht die Wiederholungsseiten).
- Geschichte: Sophie (11-12, aus Deutschland) wohnt im ersten Schuljahr bei den Parkers in Millbrook und schickt ihrer Familie zu Hause Nachrichten. Jede Seite hat eine Szene im Haus der Familie oder unterwegs mit den Kindern und einen Satz, den Sophie nach Hause schreibt. Das Profil „All about me“ wächst: Jede Seite endet in `weiter` mit einer Tabelle „All about me · <Thema>“ (Ellies Beispiel) und einer Aufgabe, die das Kind in sein Heft schreibt (nichts wird gespeichert); `email-postkarte` zeigt am Ende alle Zeilen zusammen (Ellies Beispiel). Zwei Spalten „Ellies Alltag und mein Alltag“ stehen auf `alltag-uk`. Gefühle und Gesundheit bleiben altersgerecht: kleine Beschwerden (Kopf, Bauch, Husten), Mobbing nur als „Don’t do that. Tell a teacher.“
- Figuren und Orte wie in #470 und `konventionen.md` (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (Englischlehrer, graue Haare, braune Jacke), Mrs Parker (Ellies Mutter, Sophies Gastmutter); aus #477: Mr Parker (Ellies und Peters Vater, kurze braune Haare, graue Strickjacke), Grandma Parker (graue Haare zum Dutt, lila Strickjacke) nur im Stammbaum und als Beispiele, Sophies Eltern nur „Mum and Dad“ (Sophies Mum blond, kleines Foto im Stammbaum, ohne Namen). Millbrook School, Schultag ab 8:45; Geburtstage Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Keine weiteren Figuren ohne Rückfrage. Nicht benutzen: Lagerraum und Schulfest (#475), Ausstellung „Our Millbrook“ (#476). Die Einladung in `kurznachricht` kommt von Amir (Geburtstag 12. Oktober, ein Samstag, kein Jahr genannt).
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
- Ordnen: `ordering` (Sätze eines Textes, Schritte des Tages, Teile einer Einladung, Teile einer Postkarte).
- Lücke wählen: `language-task` mode `choice` mit `distractors`; Form bilden: mode `write` mit englischem `cue`; übersetzen mit `source`; korrigieren: ein Fehler im Satz.
- Hören und schreiben: `language-task` mit `audio` (Diktat, drei ganze Sätze je Seite); Nachsprechen: `speaking-task` (drei andere Sätze); Frei: `open-task` mit Punkten und Musterlösung (Profil-Zeile, Text, Einladung, Postkarte, E-Mail).
- Typische Fehler (je eigene Meldung): Peter is a brother of Ellie (Ellie’s brother), Ellie have red hair, she/her und my/her verwechselt, I have a headache ohne Artikel, My head hurt (-s), I am boring (statt bored), angry on you, There is two chairs, in the morning/at the morning, She get up, go to home, I eat the breakfast, He like tea, I like swim, I go to swimming, On Saturday ohne on, Dear Mum ohne Komma, Gruß ohne Namen.
- Keine Komponente (`prefer-built-in-block`), keine Datendatei: jede Tatsache steht einmal in ihrer Seite.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py` (Aufruf im App-Ordner: `python3 .agents/skills/app-content/scripts/make_images.py [name …]`; nie die SVG von Hand ändern). Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, bei 360 px lesbar. Skizzen in `.vibe/sketches/`.
- Die vier Kinder sind die `<g id>` aus `millbrook-klassenzimmer.svg` von hello-millbrook (#470), unverändert kopiert; Mrs Parker, Mr Hill, Mr Parker und Grandma Parker zeichnet `make_images.py` im selben Stil nach den Beschreibungen oben. Keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. `alt` sagt, was das Bild zeigt, nie die Lösung der Übung auf derselben Seite. Die Bildunterschrift nennt, wer wer ist (Sophie Zöpfe, Ellie roter Pferdeschwanz, Amir Brille, Peter gelbe Jacke).
- Bilder: Szenen `szene-<seite>.svg`, Stammbaum der Parkers, Barometer, Körperfigur, Haus im Querschnitt, Bildleiste des Tages, Frühstückstisch, Einladungskarte, Postkarte mit Bauplan. (Stand der Liste: Abschnitt „Adding a chapter or round“ nachführen.)
- Tabellen: „Klassenzimmer-Poster · …“, „Schulkalender · …“, „All about me · …“ als `table`-Blöcke; je Seite höchstens eine kurze Tabelle „Wörter dieser Seite“.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-21); Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2, geöffnet 2026-11-21; Wörter der Übungen kommen aus A1 und A2, ein Wort außerhalb steht auf der Seite mit Bedeutung und in der Liste unten). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-21: `Tea (meal)` (tea ist ein Oberbegriff für mehrere Mahlzeiten; im Alltag auch die frühe Abendmahlzeit), `Packed lunch` (Mittagessen, das man von zu Hause mitbringt), `Terraced house`. Nicht geprüft (HTTP 429): `Semi-detached house`, `Full breakfast`, `Sunday roast`: Fakten dazu stehen nicht auf den Seiten. Nicht geprüft: deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines. Wörter außerhalb von A1/A2, jeweils auf der Seite mit Bedeutung: (wird beim Bauen der Seiten ergänzt).

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen (`recap` mit Karten-Ids).
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen; Kapitel in `src/app.yaml` eintragen.
3. Bilder: Funktion in `make_images.py` ergänzen und das Skript starten; Zeile für „All about me“ und die Poster-Tabellen ergänzen.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 2 je Seite in `selfAssessment` (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz, 6 je Seite: 3 Diktat, 3 Nachsprechen), erzeugt mit `python3 .agents/skills/app-content/scripts/regen_audio.py .agents/skills/app-content/scripts/audio-texte.json [Satz …]` (schneidet das Ausklingen ab); Sätze nicht zwischen Seiten wiederholen, Namen am Satzende zweisilbig.
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
- Hinweise und Meldungen einer Selbsteinschätzungs-Übung nennen weder „Spalte“ noch „Poster“ noch „oben“.
- `ordering` zeigt Auswahlfelder statt Karten (Eigenheit der Vorlage); `punctuation: hint` meldet bei richtiger Antwort „Achte auf die Satzzeichen“.
