---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: explore
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-alltag, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

Kinder der Klassen 5-6 (erstes und zweites Lernjahr Englisch) beschreiben sich, ihre Familie, ihr Zuhause, ihren Tag und ihre Freizeit auf Englisch und schreiben eine Nachricht, eine Einladung, eine Postkarte und eine persönliche E-Mail. Sie füllen Seite für Seite ein eigenes Profil „All about me“ und vergleichen am Ende Ellies Alltag in Großbritannien mit ihrem eigenen. Erste Version: Stufe 5-6, alle drei Kapitel von Issue #477 (11 Bausteine).

## Key decisions

- Archetyp `explainer` (Einheiten-App, `subject: englisch`, Format 2): Die Kinder brauchen Erklärung mit Bildern und dann Übungen mit Rückmeldung; der Auftrag verlangt einen Explainer. Quiz trägt keine Erklärung, interactive wäre ein Spiel oder Training.
- Drei Kapitel, elf Bausteinseiten und je Kapitel eine Sammel-Wiederholung `das-brauchst-du` (`recap` mit einer Liste von Bausteinen anderer Explainer): Vorgabe Issue #477.
- Leitbild „All about me“: Sophie wohnt bei den Parkers; zu jedem Thema gibt es eine Szene im Haus der Familie und eine Nachricht, die Sophie nach Hause schickt. Ein Profil „All about me“ wächst Seite für Seite (Zeile je Seite, Ellie als Beispiel, das Kind schreibt die eigene Zeile), am Ende stehen zwei Spalten: Ellies Alltag und mein Alltag.
- „Josh“ aus dem Auftrag kommt nicht vor (Konventionen §7): Die Einladung kommt von Amir (Geburtstagsfeier, Amir 12. Oktober, Sophie 14. Oktober).
- Audio: Stimme `bf_emma`, nur ganze Sätze, Diktat und Nachsprechen je Seite (Konventionen §5).
- Kapitelreihenfolge innerhalb der Kapitel nach `requires` der Karte; Schulfest-Lagerraum (#475) und Ausstellung „Our Millbrook“ (#476) werden nicht als Szene benutzt.
- Keine Komponente, keine Datendateien (wie #472 und #476) (guess).
- Selbsteinschätzung: ja, in jedem Kapitel (`chapter.yaml`), je Seite zwei schreibende oder auswählende Übungen.
- `scope` in `src/app.yaml` und auf jeder Seite, weil die App `open-task` enthält.

## Notes

- Fach: Englisch, Einheiten-App (`subject: englisch`), Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet 2026-11-21), `explainerFocus: competency`, Band 5-6. Alle elf Bausteine sind Lücken der Karte (`practisedBy` leer).
- Kapitel 1 · Menschen beschreiben (`menschen-beschreiben`): Ich kann meine Familie und andere Menschen nach Aussehen, Charakter und Gefühlen beschreiben und sagen, wie es mir geht.
  - Wiederholung `das-brauchst-du` (recap `englisch/have-got`, `englisch/adjektive`): `familie-personen` verlangt `have-got` und `adjektive`, `gesundheit` verlangt `have-got`, `gefuehle-freundschaft` verlangt `adjektive`. Beide stammen aus anderen Explainern (#472 und #476).
  - `familie-personen` · Familie und Personenbeschreibung (Schritt 4, öffnet 3): „Ich kann Familienmitglieder benennen und Menschen mit einfachen Wörtern nach Aussehen und Charakter beschreiben.“ Szene: Stammbaum der Parkers, Steckbrief je Mitglied.
  - `personen-orte-beschreiben` · Personen und Orte beschreiben (Schritt 5, öffnet 1): „Ich kann in einem Text eine Person oder einen Ort anschaulich beschreiben.“ Szene: Sophie beschreibt ihre neue Familie und ihr Zimmer in einem kurzen Text.
  - `gefuehle-freundschaft` · Gefühle und Freundschaft (Schritt 4, öffnet 0): „Ich kann über Gefühle, Freundschaft und Streit sprechen, auch über Mobbing.“ Szene: Barometer mit Gesichtern, ein Streit unter Freunden.
  - `gesundheit` · Körper und Gesundheit (Schritt 3, öffnet 0): „Ich kann Körperteile und Beschwerden benennen und beim Arzt oder in der Apotheke sagen, was mir fehlt.“ Szene: beim Arzt.
- Kapitel 2 · Zuhause bei den Parkers (`zuhause-parkers`): Ich kann mein Zuhause, meinen Tagesablauf und mein Essen beschreiben und mit dem Alltag in Großbritannien vergleichen.
  - Wiederholung `das-brauchst-du` (recap `englisch/there-is-are`, `englisch/simple-present`, `englisch/praepositionen-zeit`): `wohnen` verlangt `there-is-are`; `tagesablauf` verlangt `simple-present` und `praepositionen-zeit`; `essen-trinken` verlangt `simple-present`. Quellen: #475 (there-is-are, praepositionen-zeit) und #472 (simple-present).
  - `wohnen` · Wohnen und Zuhause (Schritt 4, öffnet 1): „Ich kann mein Zuhause beschreiben: Räume, Möbel und Garten.“ Szene: Haus zum Aufklappen.
  - `tagesablauf` · Tagesablauf (Schritt 4, öffnet 0): „Ich kann meinen Tagesablauf beschreiben (I get up at seven …).“ Szene: ein Tag bei den Parkers als Bildleiste vom Aufstehen bis zum Abendessen.
  - `essen-trinken` · Essen und Trinken (Schritt 3, öffnet 1): „Ich kann Lebensmittel und Mahlzeiten benennen und über Essgewohnheiten sprechen.“ Szene: Frühstück, packed lunch, tea am Abend.
  - `alltag-uk` · Alltag in Großbritannien (Schritt 5, öffnet 0): „Ich kann das Familienleben, das Wohnen und das Essen in Großbritannien beschreiben und mit meinem Alltag vergleichen.“ Szene: zwei Spalten, Ellies Alltag und mein Alltag. Braucht `familie-personen` (Kapitel 1), `wohnen` und `essen-trinken` (Kapitel 2, davor).
- Kapitel 3 · Freizeit und Nachrichten (`freizeit-nachrichten`): Ich kann über meine Hobbys sprechen, eine Einladung oder kurze Nachricht schreiben und eine persönliche E-Mail oder Postkarte verfassen.
  - Wiederholung `das-brauchst-du` (recap `englisch/gruss-hoeflichkeit`): `email-postkarte` verlangt `gruss-hoeflichkeit` (#470). `simple-present` (für `freizeit-hobbys`) und `praepositionen-zeit` (für `kurznachricht`) stehen schon im Recap von Kapitel 2.
  - `freizeit-hobbys` · Freizeit und Hobbys (Schritt 3, öffnet 3): „Ich kann über meine Hobbys, Haustiere und meine Freizeit sprechen.“
  - `kurznachricht` · Kurznachricht und Einladung (Schritt 4, öffnet 0): „Ich kann eine kurze Nachricht, eine Notiz oder eine Einladung schreiben.“ Szene: Amir lädt zur Geburtstagsfeier ein.
  - `email-postkarte` · Persönliche E-Mail und Postkarte (Schritt 2, öffnet 3): „Ich kann eine persönliche E-Mail, einen Brief oder eine Postkarte mit passender Anrede und passendem Schluss schreiben.“ Szene: Sophie schreibt eine Postkarte nach Hause; Bauplan Anrede, Text, Gruß (#486 greift ihn später auf). Steht als Schluss des Kapitels, obwohl der Schritt niedrig ist: Sie nutzt die Seiten davor und braucht nur `gruss-hoeflichkeit`; eine Seite darf vorrücken (Skill `lernapps-map-assignment`), das Profil schließt hier.
- Karte der Seiten: Kapitel 1 `das-brauchst-du` (recap) → `familie-personen` → `personen-orte-beschreiben` → `gefuehle-freundschaft` → `gesundheit`; Kapitel 2 `das-brauchst-du` (recap) → `wohnen` → `tagesablauf` → `essen-trinken` → `alltag-uk`; Kapitel 3 `das-brauchst-du` (recap) → `freizeit-hobbys` → `kurznachricht` → `email-postkarte`. Kein `ahead` (alle `requires` liegen auf früheren Seiten oder Recaps).
- Ablauf der Seiten (Konvention aus #472/#476): `einstieg`, `neu`, `uebung` (mindestens vier, leicht → schwer), `anwenden`, `weiter`; höchstens 350 Wörter Text, Bild oder Übung in den ersten vier Blöcken. Wiederholungsseiten: nur Text und Tabelle, keine Übung, keine `competencies`.
- Wörter: Quelle ist der Grundwortschatz A1/A2 (`https://lernapps.net/apps/map/englisch/grundwortschatz/`, geöffnet 2026-11-21; Wörterliste lokal als Prüfgrundlage). Wörter außerhalb der Liste stehen auf der Seite mit Bedeutung und werden im Inhaltsführer gelistet.
- Grenzen (Scope): drin: Familie, Aussehen, Charakter, Gefühle, Streit und Mobbing (in einfachen Sätzen), Körperteile, Beschwerden (I've got a headache, My throat hurts), Arzt und Apotheke, Räume, Möbel, Garten, Tagesablauf mit Uhrzeit und Zeitangaben, Mahlzeiten und Lebensmittel, Hobbys, Haustiere, Freizeit, Einladung, Notiz, Postkarte, persönliche E-Mail, Alltag in Großbritannien im Vergleich. Draußen: Schule, Uhrzeit, Datum (#470); Stadt, Einkaufen, Reisen (#478); Meinung zu Sport, Musik, Medien (#487); Geschichten erzählen (#479); Briefe für fremde Leser (#486); present perfect und simple past (#472).
- Wie die Kinder dorthin kommen und was die Rückmeldung fängt, je Baustein: wird im Abschnitt „Content method“ und im Inhaltsführer geführt (Muster: Steckbrief ergänzen, Text ordnen, Barometer wählen, Arztdialog bauen, Haus beschriften, Bildleiste in Reihenfolge, Mahlzeiten zuordnen, zwei Spalten vergleichen, Hobby-Sätze, Einladung nach Bauplan, Postkarte nach Bauplan). Typische Fehler (je mit eigener Meldung): mother/mum, Fehlendes -s (She like), my/her verwechselt, I have a headache statt I've got, He hurts statt His arm hurts, go to home, in the morning/at the morning, I eat the breakfast, I like swim (Verb nach like).
- Wie die Kinder dorthin kommen, je Baustein (sie leiten ab, sie lesen nicht nur ab) und was die Rückmeldung fängt:
  - `familie-personen`: Sie lesen den Stammbaum der Parkers, ergänzen Steckbriefe (Wer ist wer? Aussehen mit has got/is, Charakter mit is) und leiten ab, dass Aussehen mit „has got“ oder „is“ und Charakter nur mit „is“ geht. Fängt: Peter is a brother of Ellie (statt Ellie’s brother), Ellie have red hair, she/her und my/her verwechselt.
  - `personen-orte-beschreiben`: Sie ordnen die Sätze eines kurzen Textes (Wer? Aussehen? Charakter? Ort?) und schreiben dann einen eigenen Absatz nach dem Muster. Fängt: Satzreihenfolge, fehlendes Subjekt, he/she verwechselt, Adjektiv nach dem Nomen.
  - `gefuehle-freundschaft`: Sie ordnen Gesichter auf dem Barometer (happy – OK – sad – angry) und wählen eine passende Antwort in einem Streit; Streit und Mobbing in einfachen Sätzen (Don’t do that. That’s unkind. I’m sorry. I’ll tell my teacher.). Fängt: I am boring (statt bored), I’m angry on you (with), sorry/please verwechselt.
  - `gesundheit`: Sie beschriften den Körper, bauen kurze Dialoge beim Arzt (What’s the matter? – I’ve got a headache. / My leg hurts.) und leiten ab: bei Körperteilen „hurts“ oder „I’ve got a … ache“. Fängt: I have headache (Artikel), My head hurt (-s), I am a headache.
  - `wohnen`: Sie klappen das Haus auf, ordnen Möbel den Räumen zu und beschreiben mit There is/are und Präposition. Fängt: Is a sofa in the living room (Wortstellung), There is two chairs, in/on-Verwechslung.
  - `tagesablauf`: Sie ordnen die Bildleiste und bilden Sätze mit Zeit (I get up at seven. Ellie goes to school at 8:30.). Fängt: in the morning/at the morning, She get up, go to home, I eat breakfast at morning.
  - `essen-trinken`: Sie ordnen Speisen den Mahlzeiten zu und sprechen über Gewohnheiten (I usually have … for breakfast. Peter likes … but doesn’t like …). Fängt: I eat the breakfast, He like, I don’t likes.
  - `alltag-uk`: Sie vergleichen zwei Spalten (Ellies Alltag, mein Alltag) und schreiben Sätze mit but/and. Fängt: Verwechslung lunch/dinner/tea, packed lunch, Mrs Parker cooks tea at six (Fakt) statt Ableitung, falsche Verallgemeinerung („Alle Briten …“): Rückmeldung nennt „viele“ und „oft“.
  - `freizeit-hobbys`: Sie ordnen Hobbys Orten und Tagen zu und schreiben eigene Sätze mit I like …ing, I play + Spiel, I go + Aktivität. Fängt: I like swim (-ing), I play swimming, I go to swimming statt go swimming.
  - `kurznachricht`: Sie ordnen eine Einladung (Wer lädt ein? Was? Wann? Wo? Antworten) in die Kästchen und schreiben eine Nachricht mit On Saturday at 3 pm. Fängt: Datum ohne on, at/in/on, Fehlendes please/thank you, zu lang für eine Notiz.
  - `email-postkarte`: Sie ordnen Teile einer Postkarte in den Bauplan Anrede, Text, Gruß und wählen passende Anreden und Grüße; sie schreiben die eigene Postkarte. Fängt: Dear Mum (Komma), Dear Mrs Parker, Hi + Namen, Love/Best wishes/Yours verwechselt, Gruß ohne Namen.
- Daten und Sprachen: keine Datendatei; Wörter ausschließlich aus A1/A2 (außer was auf der Seite erklärt und im Inhaltsführer gelistet ist). Sprachen: Deutsch (Erklärungen), Englisch (Beispiele, Audio), britisches Englisch.
- Quellen (nur Fakten, geöffnet 2026-11-21): Wikipedia „Tea (meal)“ (tea ist ein Oberbegriff für mehrere Mahlzeiten mit Essen, oft mit Tee dazu; im Alltag auch die frühe Abendmahlzeit) und „Packed lunch“ (Mittagessen, das man von zu Hause mitbringt, oft in Schule oder Arbeit) und „Terraced house“. Nicht geprüft (Wikipedia antwortete mit HTTP 429): „Semi-detached house“, „Full breakfast“, „Sunday roast“: diese Fakten stehen nur dann auf einer Seite, wenn sie eine Quelle haben, sonst entfallen sie. Nicht geprüft: deutsche Wikipedia, Klexikon. Kein Satz wird kopiert; die Beispielsätze sind eigene. Material der Ersteller:in: keines.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [ ] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

Antworten der Orchestrator-Session (in der Rolle der Ersteller:in): aus dem Auftrag (Issue #477, „unverändert“) und den Konventionen #489. Es gab kein Gespräch; wo der Auftrag schweigt, steht „(guess)“. Die Startnachricht gibt Ziel, Umfang (alle drei Kapitel) und Vorbilder vor.

- Goal: „Ich kann mich, meine Familie, mein Zuhause, meinen Tag und meine Freizeit beschreiben und mit dem Alltag von Jugendlichen in Großbritannien vergleichen.“ Das Profil „All about me“ trägt den Explainer.
- Learners: Klassen 5-6, erstes und zweites Lernjahr Englisch; Vorwissen aus den Explainern #470 bis #476 (Wiederholungsseiten holen den Rest).
- Model and focus: Vorbilder `englisch-zeiten`, `englisch-saetze-bauen`, `englisch-dinge-mengen-orte`, `englisch-adjektive-adverbien`, `englisch-pronomen`, `englisch-verbketten`. Wichtig sind Übungen mit Rückmeldung und Bilder (Stammbaum, Barometer, Haus, Bildleiste, Bauplan). Kein Spielgefühl.
- Hurdles: (guess) mum/mother, -s bei he/she/it, my/her, I have a headache statt I've got, at/in/on bei Zeit, I like swim, Anrede und Gruß im Brief.
- Content: aus Quellen, von mir geschrieben; kein eigenes Material.
- Amount: erste Version alle drei Kapitel, 11 Bausteine, Stufe 5-6; spätere Stufen als Inkremente.
- Languages: Deutsch (Erklärungen), englische Beispiele, britisches Englisch.
- Look and feel: fixed by the archetype (ruhig wie ein Arbeitsblatt, Dunkelmodus folgt dem Gerät).
- Terms: „Ausdruck“, „Klassenzimmer-Poster“, „Schulkalender“ (Konventionen); „All about me“ (das Profil), „Steckbrief“, „Bauplan“ (Brief: Anrede, Text, Gruß).
- Finding the app: (guess) englisch alltag familie zuhause beschreiben hobbys einladung postkarte e-mail klasse 5 6.

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [ ] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [ ] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [ ] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [ ] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [ ] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [ ] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [ ] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [ ] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [ ] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
<!-- tasks: pattern: the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
<!-- tasks: pages: the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
