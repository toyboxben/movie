# Continuity Law

Read before generating a single frame. These rules come from what Higgsfield and Seedance
actually do, not from what we wish they did.

---

## Tool reality check (verified Aug 2026)

**Seedance 1.0 Pro**
- Durations: 5s or 10s in the UI, 2–12s via API. 24fps. 720p/1080p.
- Supports **first frame** and **first + last frame**. Last frame requires first.
- The end frame is *approximated*, not guaranteed. The further apart the two keyframes,
  the looser the landing.
- Native multi-shot generation exists. **We do not use it** — it hands cut timing to the
  model. We cut in the edit.
- 21:9 available. Use it.

**Higgsfield**
- ~8s max per generation on standard tiers.
- Cinema Studio: explicit camera body, lens, focal length, multi-axis move.
- **Soul ID trains on 20–80 photos of a real person.** It does not work for invented
  non-human characters.
- Elements: reference-image based, supports multiple consistent subjects per scene.

**Practical split:** Seedance I2V for 5s/10s clips from an approved keyframe.
Higgsfield `soul/reference` for composing that keyframe from the frozen still pack.
Higgsfield Cinema Studio only when a specific camera move matters more than identity.

---

## Rule 1 — Every shot is exactly 5s or 10s

Not 7, not 12. Shots that need to feel like 7 seconds are authored as 10s generations
trimmed in the edit, and that trim is planned on the shot card, not discovered later.

Budget for 10 minutes: **86 shots**, ~610s of used footage.

## Rule 2 — Nothing is text-to-video. Identity comes from stills.

```
frozen still pack in refs/<character>/
        ↓  (matching angle as image_reference)
  shot keyframe via Higgsfield soul/reference  →  human approval  →  KF-###
        ↓  (KF-### as image_url / first frame)
  Seedance image-to-video
```

The turnaround sheet is **not** a first frame. Feeding a 5-across character sheet into
Seedance produces a video of a character sheet. Crop to one view, compose the shot,
then animate.

A rejected keyframe costs cents. A rejected 1080p clip costs minutes and money.

## Rule 3 — One still pack per character, frozen

**Kit:** `refs/kit/CANONICAL-turnaround.jpg` and the cropped views in `refs/kit/views/`.
Public URLs live in `refs/kit/manifest.json`. Pass those URLs into Higgsfield/Seedance.
Do not re-describe his face in the hope the model will invent the same kid.

**Toys:** same system, once their sheets exist in `refs/<character>/`. Higgsfield Elements
can hold the pack; Seedance still needs a composed keyframe as first frame.

Never regenerate a frozen pack mid-production. If a sheet is wrong, fix it before shot 1.

## Rule 4 — Chain frames across cuts within continuous action

When shot N+1 continues the same action in the same space, export the **last frame of
SH-N** and use it as the **first frame of SH-N+1**. The shot card's `chain_from` field
records this. Do not chain across a scene change — you want a clean break there.

## Rule 5 — First+last frame for anything that must land

If a shot has to end in a specific composition (a character positioned for the next shot,
a reveal settling, a match cut), author both keyframes. Keep them similar in composition
and scale, and prefer 5s — a 10s first+last with a big compositional change is the number
one cause of rushed, drifting motion.

## Rule 6 — Wardrobe and prop locks are absolute

A character's appearance never changes unless a shot card declares a **STATE CHANGE**.
State changes are enumerated in each character file with the shot number where they start.
Any generation showing an undeclared state is a reject, even if it looks great.

**Kit's marker is a locked prop, not a framing requirement.** Thick red marker, white band,
rests behind his right ear. In the Toybox it is his wand: whatever he draws becomes real,
like a 3D print. He fights with it. It does not need to be in every frame. If a shot shows
his right ear or his drawing hand, the marker should be there — ear or hand, never gone.
The only time it leaves him is SH-076, and he picks it up in the same shot.

## Rule 7 — Screen direction

Outbound journey runs **left to right** for the entire first two acts. The return in Seq
07–08 runs **right to left**. A character exiting frame right enters the next shot from
frame left. Tracked as `screen_dir` on every card. This is the difference between an
assembly that reads as a journey and one that reads as a playlist.

## Rule 8 — The Smooth horizon advances monotonically

From SH-053 the white horizon appears in the background of exterior shots and never
retreats. Position is a 0–100 value on every card. `production/build_prompts.py` validates
this automatically — if it reports a retreat, fix the shot list before generating.

## Rule 9 — One key light direction per scene

Declared at the top of each sequence file. If the key is camera-left in SH-040 it is
camera-left in SH-041. Models will happily flip it; keyframe approval is where you catch
that.

## Rule 10 — Generate in sequence order and assemble as you go

Generate a sequence, cut it, watch it, then move on. Drift compounds, and it is far
cheaper to catch at shot 12 than at shot 80.

## Rule 11 — Colossus never has a back half

Not in a wide, not in shadow, not in a blurred background, not for one frame. Models will
complete him because dogs have four legs. This is the single highest-frequency continuity
failure in the film. Check it on every keyframe he appears in.

## Rule 12 — June's unfinished side is always camera-consistent

Her **right** side is complete and her **left** side is wireframe, from her own point of
view. When she faces camera, the wireframe is on **frame right**. When she turns, it
follows her body. Models will flip this constantly. Check every keyframe.

---

## Per-shot QC checklist

Before a clip is marked `approved`:

- [ ] Character matches the reference sheet — silhouette, palette, proportions
- [ ] Kit has no rings; every toy does
- [ ] Colossus has no back half
- [ ] June's wireframe side is on the correct side of her body
- [ ] Wardrobe and prop state matches the declared state for this shot number
- [ ] Camera height matches the rule (toy eye height unless declared otherwise)
- [ ] Key light direction matches the sequence declaration
- [ ] Screen direction correct
- [ ] Smooth horizon value correct and non-decreasing
- [ ] Toy motion reads on-2s, Kit's on-1s
- [ ] No text, watermark, or logo in frame
- [ ] Exactly 5s or 10s, 24fps, 1080p, 21:9
- [ ] Last frame clean enough to chain from, if the next shot chains
