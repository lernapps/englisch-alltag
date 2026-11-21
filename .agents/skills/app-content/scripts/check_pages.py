# Checks of the content rules that `lernapps check` cannot see (konventionen.md, Abschnitt 7).
# Run from the app folder: python3 .agents/skills/app-content/scripts/check_pages.py [--words]
#  1. No sentence of a dictation or a speaking task stands, whole or nearly (same words but one), in any other text of the
#     same page (text, tables, captions, options, items, cues, targets).
#  2. --words: English words of targets, cues, options and tables that are not in the basic vocabulary (A1/A2).
import glob, json, os, re, sys, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
pages = sorted(p for p in glob.glob("src/*/*.yaml") if not p.endswith("chapter.yaml"))


def norm(s):
    s = s.replace("’", "'").lower()
    return re.findall(r"[a-z']+", s)


def walk(node, out, skip_audio):
    """Collects (kind, text) of all strings; the target and text of dictation and speaking items are skipped."""
    if isinstance(node, dict):
        is_audio_item = "audio" in node and ("target" in node or "text" in node)
        for k, v in node.items():
            if is_audio_item and k in ("target", "text"):
                skip_audio.append(v)
                continue
            if k in ("audio", "id", "image", "source", "licence", "url", "type", "competencies", "recap"):
                continue
            walk(v, out, skip_audio)
    elif isinstance(node, list):
        for v in node:
            walk(v, out, skip_audio)
    elif isinstance(node, str):
        out.append(node)


def expand(s):
    """Expands (a|b) groups of an answer into all versions (at most 64)."""
    m = re.search(r"\(([^()]*\|[^()]*)\)", s)
    if not m:
        return [s]
    res = []
    for alt in m.group(1).split("|"):
        res += expand(s[:m.start()] + alt + s[m.end():])
    return res[:64]


bad = 0
for p in pages:
    d = yaml.safe_load(open(p, encoding="utf-8"))
    out, audio = [], []
    walk(d.get("blocks", []), out, audio)
    texts = []
    for t in out:
        for v in expand(re.sub(r"[\[\]]", "", t)):
            texts.append(norm(v))
    for a in audio:
        aw = norm(a)
        for tw in texts:
            n = len(aw)
            for i in range(0, max(1, len(tw) - n + 1)):
                seg = tw[i:i + n]
                if len(seg) == n and sum(x != y for x, y in zip(seg, aw)) <= 1 and n >= 4:
                    print(f"{p}: Hörsatz steht (fast) im Text der Seite: '{a}' ~ '{' '.join(seg)}'")
                    bad += 1
                    break
if "--words" in sys.argv:
    gw = {l.split()[0] for l in open(os.path.join(HERE, "grundwortschatz.txt"), encoding="utf-8")}
    FUNCTION = set("i you he she it we they me him her us them my your his its our their a an the is are am be was were do does did "
                   "have has got can will to of in on at for with and or but not no yes please thank thanks hello hi dear love mrs mr".split())

    def stem(w):
        for suf in ("'s", "s", "es", "ed", "d", "ing", "ly", "er", "est", "ies"):
            if w.endswith(suf) and (w[:-len(suf)] in gw or w[:-len(suf)] + "y" in gw):
                return w[:-len(suf)]
        return w

    def english(node, acc):
        """Strings of the keys target, cue, distractors, answer, text of speaking items and the options of choices."""
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("target", "cue", "answer", "distractors") or (k == "text" and "audio" in node):
                    for t in (v if isinstance(v, list) else [v]):
                        for u in (t if isinstance(t, list) else [t]):
                            if isinstance(u, str):
                                acc.append(u)
                else:
                    english(v, acc)
        elif isinstance(node, list):
            for v in node:
                english(v, acc)

    extra = {}
    for p in pages:
        d = yaml.safe_load(open(p, encoding="utf-8"))
        acc = []
        english(d.get("blocks", []), acc)
        for t in acc:
            for v in expand(t):
                for w in norm(v):
                    if w not in gw and stem(w) not in gw and w not in FUNCTION and not w.endswith("'s"):
                        extra.setdefault(w, set()).add(os.path.basename(p))
    for w, f in sorted(extra.items()):
        print("nicht in A1/A2:", w, sorted(f))
print("fertig;", bad, "Fund(e) bei den Hörsätzen")
sys.exit(1 if bad else 0)
