# Production Pipeline

The exact click path, in order. Do not skip a phase — every phase exists because
skipping it produces drift you can only fix by regenerating everything after it.

---

## Phase 0 — Read (once, before anything)

1. `bible/03-continuity-rules.md` — the law
2. `bible/02-visual-style-lock.md` — the look
3. `bible/05-double-read-rule.md` — why nobody says the word "filament"
4. `script/ep01-script.md` — the film

---

## Phase 1 — Voice (before any picture)

The edit is cut to dialogue, so the dialogue has to exist first. Doing this after the
video produces clips that are the wrong length for their lines and a film full of dead
air.

1. Cast all six voices. Record a 20-second sample each.
2. **Freeze the settings** — voice ID, model version, stability, similarity, style — into
   each character's `.md` file. Never regenerate a voice at different settings.
3. Generate every line in `script/ep01-script.md`, named by line ID: `L-001.wav`.
4. Lay them on a timeline in order. **Check the total.** If a sequence runs long or short
   against `script/ep01-beatsheet.md`, adjust shot durations in `shots/ep01_shots.py`
   now — not later.
5. Build the Colossus sound library: boot-up chime, servo whir, the cut-off bark, the
   descending whine. **Do not record a complete bark except for SH-080.**

---

## Phase 2 — Freeze still packs (before any shot)

Identity is the image, not the prompt.

1. Generate turnaround sheets (Kit's is done: `refs/kit/CANONICAL-turnaround.jpg`).
2. Split into single views and upload:
   `python production/prepare_kit_refs.py`
3. Cull. Freeze. Never regenerate the pack mid-production.

## Phase 3 — Per-shot loop

Work in sequence order, and assemble as you go.

For each shot Kit is in:

```
1. Read the card            shots/sequences/seq-##.md
2. Pick the matching view   refs/kit/manifest.json  (height → view)
3. Compose the keyframe     Higgsfield soul/reference
                            image_reference_url = that view's public URL
                            prompt = action + environment only (from prompts/SH-###.txt)
                            → approve → KF-###
4. Animate                  Seedance I2V (Higgsfield
                            /bytedance/seedance/v1/pro/fast/image-to-video)
                            image_url = KF-###
                            prompt = camera + motion only
5. If chain_from is set     skip step 3; first frame = last frame of the previous clip
6. QC                       bible/03 checklist
7. Cut it in immediately
```

Do not paste Kit's appearance paragraph into Seedance and hope. The first frame is Kit.

### Chaining

If the card lists **Chain from**, export the last frame of that shot and use it as this
shot's first frame. That is what makes cuts actually match.

If the card says **First+last frame: YES**, author both keyframes and use Seedance's
first-and-last mode. Keep the two frames similar in composition and scale, and prefer 5s
— a 10s first+last across a big compositional change is the main cause of rushed,
drifting motion.

### Tool split

| Use | Tool | Why |
|---|---|---|
| Compose a keyframe from Kit's pack | Higgsfield `soul/reference` | `image_reference_url` holds the face |
| Animate that keyframe 5–10s | Seedance I2V via Higgsfield | `image_url` = the keyframe |
| First+last frame land | Seedance I2V with last frame | chain / match cuts |
| Specific camera move | Higgsfield Cinema Studio | only after the keyframe is approved |

---

## Phase 4 — Assembly

1. Lay the voice track down first. Cut picture to it.
2. Lay the six ambient beds — one continuous bed per world, in the edit, never generated
   per clip. This does more to make 86 generations feel like one film than any visual
   technique.
3. Grade to the saturation curve in `worlds/05-the-smooth.md`. The four-second overshoot
   at SH-081 is the single most important grading decision in the film, and it only works
   because Seq 06 and the first half of Seq 07 were starved.
4. Score. Kit's melody plays incomplete every time and resolves only on the last shot.
5. Matte to 2.39:1 if you generated 21:9.

---

## Rebuilding after a change

Everything downstream of the blocks is generated. If you change a character's look, a
plate, or a shot:

```bash
python production/build_prompts.py
```

That regenerates `prompts/`, `shots/ep01-shotlist.csv`, and `shots/sequences/`, and runs
the continuity validator. **Any FAIL must be fixed before you generate anything.**

The validator currently checks: duplicate IDs, illegal durations, unknown blocks, broken
chain references, more than one camera move per shot, the Smooth horizon never retreating,
Colossus never being whole before SH-080, and total runtime.

> Note that `shots/ep01-shotlist.csv` is overwritten on every build. Track generation
> status in your own copy, or in the tool, rather than editing it in place.

---

## Cost and time estimate

At Seedance 1080p pricing of roughly \$1.22 per 10s clip and \$0.61 per 5s clip:

| | Count | Cost |
|---|---|---|
| Keyframes (image, ~4 attempts each) | ~350 | ~\$15 |
| 5s clips at 1080p | 47 | ~\$29 |
| 10s clips at 1080p | 39 | ~\$48 |
| Reroll allowance at 3× | — | ~\$230 |
| Turnarounds | ~200 images | ~\$10 |
| **First-pass total** | | **~\$330** |

Draft at 480p while you are testing prompt behaviour — it is roughly a fifth of the price
and tells you almost everything about whether a shot will work.

The real cost is time in the QC loop, not generation. Budget the rerolls: Colossus's
missing back half and June's wireframe side will be your two biggest reroll sinks by a
wide margin.
