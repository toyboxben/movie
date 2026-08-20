# FIRST LAYER — Pilot Episode

A **10:10 animated pilot** for **Toybox.com**, generated shot by shot with Higgsfield and
Seedance and assembled into one film. 86 shots.

> **Logline.** When eleven-year-old Kit finally starts printing the robot dog he's been
> promising everyone for a year, he's pulled inside the machine — into a world built from
> everything people have ever made — and learns he can only get home when the print
> completes. Then the print fails, and the only way out is to let something imperfect
> exist, in public, for other people.

---

## Start here

```bash
python production/build_prompts.py
```

That validates continuity and writes everything you actually use:

| Output | What it is |
|---|---|
| `prompts/SH-###.txt` | **fully assembled, paste-ready prompt per shot** — 86 of them |
| `prompts/_ALL.md` | every prompt in one scrollable file |
| `shots/ep01-shotlist.csv` | the production tracker |
| `shots/sequences/seq-##.md` | human-readable shot cards, with the note for every shot |

Then read `production/pipeline.md`, which is the exact click path in order.

---

## Repo layout

```
bible/          Story, theme, style lock, continuity law, audio, accessibility. Read first.
characters/     One file per character + turnarounds.md — the sheets you generate FIRST.
worlds/         One file per environment.
script/         Beat sheet, then the full dialogue script with line IDs.
shots/          ep01_shots.py is the shot list source of truth. sequences/ is generated.
production/     blocks.py (prompt source of truth), build_prompts.py, pipeline.md.
prompts/        GENERATED. Paste these in.
refs/           Your approved turnaround sheets go here.
```

### Where things are edited vs. generated

**Edit these:**
- `production/blocks.py` — every character description, environment plate, and style lock
- `shots/ep01_shots.py` — the 86 shots
- everything in `bible/`, `characters/`, `worlds/`, `script/`

**Never edit these — they are overwritten on every build:**
- `prompts/`
- `shots/sequences/`
- `shots/ep01-shotlist.csv`

---

## The four things that will break continuity

The build script checks the mechanical ones automatically. These four are on you, and
they're checked at keyframe approval:

1. **Colossus never has a back half** before SH-080. Models complete him because dogs have
   four legs. This is the highest-frequency failure in the production.
2. **June's hollow side is on her own left** — frame right when she faces camera — and it
   is genuinely empty. Models flip it and fill it in.
3. **Kit is smooth, everything else has rings.** The one visual law the whole film rests on.
4. **The Finisher has no texture, no rim light, and no shadow,** even when everything
   around him does.

## The order of operations

1. **Voice first.** Record every line before generating a single frame — the edit is cut
   to dialogue.
2. **Turnarounds second.** `characters/turnarounds.md`. Kit → Soul ID, everyone else →
   Elements. Freeze them.
3. **Shots third,** in sequence order, cutting as you go. Never generate all 86 and then
   edit; drift compounds.

Full detail in `production/pipeline.md`.

---

## Naming

| Asset | Format | Example |
|---|---|---|
| Shot | `SH-###` | `SH-042` |
| Keyframe still | `KF-###` | `KF-042` |
| Dialogue line | `L-###` | `L-118` |
| World plate | `WP-<world>-<state>` | `WP-raft-plaza` |
| Sequence | `SEQ-##` | `SEQ-04` |

Every shot is **exactly 5s or 10s** — Seedance's UI durations — and never anything
between. See `bible/03-continuity-rules.md` for why.
