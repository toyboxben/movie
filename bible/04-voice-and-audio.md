# Voice & Audio

Voice drift is as damaging as visual drift and far easier to prevent, because voice models
are deterministic in a way video models are not. Lock a voice ID per character before
recording a single line, and never regenerate it.

---

## Rule 1 — One frozen voice ID per character

Cast once, record a 20-second sample, and store the exact voice ID, model version,
stability, similarity, and style settings in the character file. Every line for that
character uses those exact settings. A voice generated at different settings six weeks
apart will not match, and audiences catch voice drift faster than visual drift.

## Rule 2 — Record all dialogue before generating any video

The edit is cut to dialogue. Generate the full voice track first, lay it on a timeline,
and let real line lengths decide whether a shot is 5s or 10s. Doing it the other way
produces clips that are the wrong length for their lines and a film full of dead air.

`script/ep01-script.md` is the recording script. Line IDs (`L-###`) map to shot cards.

## Rule 3 — Lip sync strategy

Neither model reliably lip syncs from a prompt. Three tiers:

| Tier | Use | Method |
|---|---|---|
| A — full sync | Kit's dialogue close-ups, the Finisher's monologue | Generate the clip, then a dedicated lipsync pass (Higgsfield Lipsync Studio) |
| B — implied | June, most toy dialogue | Simple or absent mouths; cut to reactions and over-shoulders on long lines |
| C — off-screen | exposition, banter during travel | Line plays over a shot of something else. Cheapest, most reliable, and often better filmmaking |

**The design absorbs the constraint.** Most toys are built with simple or non-moving
mouths *on purpose*. Benchy has no mouth — he's a boat. The Tower's ten layers glow when
speaking. Colossus is non-verbal. This removes the single largest failure mode in
AI-generated dialogue and it is why the film can afford to be talky.

**Budget: no more than 15 Tier-A shots.** Kit gets almost all of them.

## Rule 4 — Ambience is per-world and continuous

One continuous ambient bed per world, laid in the edit, not generated per clip. This does
more to make 86 separate generations feel like one film than any visual technique.

| World | Bed |
|---|---|
| The Bedroom | room tone, distant house, the printer's stepper whine and fan |
| The Raft | creaking plastic, lapping river, crowd murmur, rigging |
| Dino Basin | wind, dry grit, distant low clacking |
| Gearhaven | machine hum, hydraulic hiss, dripping, sodium buzz |
| The Deep Bin | enormous dead air, far-off settling, low sub |
| The Smooth | near-total silence and a high sine tone. Uncomfortable. |

## Rule 5 — The printer is the film's signature sound

The stepper-motor melody of a 3D printer is the first sound in the film, a musical phrase
threaded through the score, and the last sound. In the Toybox it is understood as the
voice of god, and characters react to it. **When the Hand stops at SH-043, this sound
stops — and it does not come back until SH-081. Its absence is the loudest thing in the
episode.**

## Rule 6 — The Smooth is defined by subtraction

When the smoothing approaches, the mix does not add a monster sound. It removes: first
ambience, then reverb tails, then the low end, until only dialogue and a thin sine remain.
Silence is the villain's sound design.

---

## Casting

| Character | Direction | Tier |
|---|---|---|
| **KIT** | 11, real kid, fast and confident and constantly selling. Not a cartoon-kid performance. He talks like someone who has already won the argument. The comedy is total conviction. His one quiet scene — the Deep Bin admission — should be the only time in the film he's slow, and it should be ugly, not pretty. | A |
| **JUNE** | 11-ish, flat, dry, impatient. Never shouts, never explains twice. She is the only character who is never impressed, and the film's biggest laughs are her one-word responses to Kit's speeches. | B |
| **COLOSSUS** | Non-verbal. Servo whirs, a two-tone boot-up chime, and a broken-off attempt at a bark that never completes. Never a real bark until the final shot. | — |
| **BENCHY** | Gravel, weathered, economical. Late-fifties harbor pilot annoyed at being asked directions. Never raises his voice. Comedy comes from how little he gives. | C |
| **THE TOWER** | Ten voices from one body. **Cast one actor doing all ten** — funnier, and it removes nine drift risks. | C |
| **THE FINISHER** | Warm, unhurried, genuinely kind. Delighted to meet Kit. Sorry about the pain. Never raises his voice, never threatens, never uses a hostile word. Every line must be deliverable unchanged by someone tucking a child into bed. The note for the actor: *he is not performing kindness, he means it.* | A |

## Score

Orchestral with a mechanical underlay — the printer motif sequenced into the rhythm
section. Each world shifts instrumentation rather than getting a new theme. Kit has one
melody that plays incomplete every single time and only resolves in the final shot, over
the sound of a print starting.
