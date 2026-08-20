# Cast

Every character has a **PROMPT BLOCK** in their file, pasted verbatim into every shot they
appear in. Never describe a character freehand in a shot prompt.

**Generate [turnarounds.md](turnarounds.md) before you make a single video clip.**

| Character | Role | File | Continuity method | Lipsync |
|---|---|---|---|---|
| **KIT** | Protagonist, 11, human | [kit.md](kit.md) | Frozen still pack `refs/kit/` → Seedance first frame | A |
| **JUNE** | Second lead, unfinished original creation | [june.md](june.md) | Elements + turnaround | B |
| **COLOSSUS** | Kit's 40%-printed robot dog | [colossus.md](colossus.md) | Elements + turnaround | — (non-verbal) |
| **BENCHY** | Mentor, ferryman tugboat | [benchy.md](benchy.md) | Elements + turnaround | C (no mouth) |
| **THE TOWER** | Comic engine, ten arguing blocks | [the-tower.md](the-tower.md) | Elements + turnaround | C (glowing slots) |
| **THE FINISHER** | Antagonist | [the-finisher.md](the-finisher.md) | Elements + turnaround | A (static, no mouth) |

**Identity lock:** the stills in `refs/`, not the prompt. Kit is frozen at
`refs/kit/CANONICAL-turnaround.jpg`. Compose each shot as a keyframe from those views,
then Seedance image-to-video from the keyframe. See `refs/README.md`.

---

## Relationship map

```
                          THE FINISHER
                       (Kit's flaw, grown up)
                                │
                          ▼ threatens ▼
                                │
      BENCHY ──── ferries ──── KIT ──── follows ──── COLOSSUS
     (tells him                 │                  (his shame,
      the truth once)           │                   in public)
                                │
                  ┌─────────────┴─────────────┐
                JUNE                     THE TOWER
        (the consequence —          (won't shut up, ten of
         what he does to             him, carries the lore)
         things, standing              │
         right there)          ⟵ can't stand ⟶
                                     BENCHY
```

**Design logic:** each character supplies exactly one thing Kit lacks, and nobody supplies
two.

- **June** has the receipts. She is what he does to things, and she is unimpressed.
- **Colossus** has unconditional love, which Kit has not earned and cannot get rid of.
- **Benchy** has judgment. He states the theme once and refuses to solve anything.
- **The Tower** has knowledge, distributed across ten idiots who cannot agree on it.
- **The Finisher** has Kit's exact flaw, fully grown, and shows him where it ends.

---

## Cast discipline

Six speaking parts in ten minutes is already at the ceiling, and two of them
(Colossus, and Benchy on a good day) barely talk. **Do not add a character.** If a scene
needs a new function, give it to someone who is already there — that is what the Tower's
ten layers are for.

---

## Supporting populations

No individual files. These are crowds and one-scene players, defined here so background
prompts stay consistent. Reference plates are in
[turnarounds.md §7](turnarounds.md#7-background-populations).

| Group | World | Description |
|---|---|---|
| **The Brim** | The Raft | The dockside crowd — keychains, bag clips, cable organisers, tiny planters, phone stands. Loud, mercantile, credulous. They crown Kit, and in the climax they are the ones who start drawing. |
| **MISS FILLET** | The Raft | The harbourmaster. A large articulated printed fish, gill-plates clacking, entirely businesslike. Two lines, both about docking fees. |
| **The Basin Herd** | Dino Basin | Printed dinosaurs from thumb-sized to enormous, all in bright non-naturalistic single colours — a hot pink triceratops, a translucent blue stegosaurus. They migrate. They are not intelligent. |
| **The Gearhaven Union** | Gearhaven | Boxy industrial mechs moving on visible printed gears. Bureaucratic, unionised, deeply unhelpful. They run the archive. |
| **The Bin-Lost** | The Deep Bin | Broken, half-built and abandoned things. They are not hostile — they are gentle, and still, and waiting, which is far worse. |
| **The Finished** | everywhere, increasing | Smoothed victims. Blank white, motionless, frozen mid-gesture. The count only ever goes up, and they are never cleared from a location once they appear. |

**Background continuity rule.** Every crowd is built from *printed objects at wildly
mismatched scales in mismatched single colours*. That mismatch — a catalog printed by a
thousand different people on a thousand different machines — is what makes the Toybox look
like the Toybox instead of a generic fantasy world. Paste into crowd prompts:

```
a crowd of printed plastic objects at wildly mismatched scales, each a different single
flat filament colour, all with visible horizontal 3D-printed layer striations
```
