# KIT — Protagonist

**Age 11. Human. Genuinely talented. Has never let anyone have the things he makes.**

---

## Who he is

Kit is good. That's the thing to establish in the first thirty seconds, before anything
else, or the entire character curdles. He can model, he can sketch, he understands how
things fit together, and when he's working he's fast and loose and completely absorbed.
The talent is real.

What he's addicted to is the moment *before*. The moment when the thing is still going to
be amazing, when nobody has seen it yet and it hasn't had a chance to be disappointing. He
lives in that moment. He would live there permanently if he could. So he starts, and he
gets it to about seventy percent — the exact point where it stops being potentially
perfect and starts being definitely flawed — and then he starts something else, and tells
everybody about that instead.

He has told the entire school he is building a robot dog. He has forty unfinished robot
dogs in a drawer that doesn't close.

**Want:** to get home.
**Need:** to let one imperfect thing exist in public.
**Flaw:** he'd rather promise than deliver, because a promise cannot be judged.
**Lie he believes:** an unfinished thing in a drawer can still become perfect. A thing
other people can see is just permanent evidence of what you couldn't do.

## Why he's likeable and not insufferable

Four load-bearing choices. Break any of them and he's a brat:

1. **We see him being good before we see him bragging.** SH-004 through SH-007 are a kid
   working at real speed with real skill. The audience banks it.
2. **He oversells to strangers, never to himself.** Alone, in the quiet moment before he
   presses print, he is visibly scared. One shot. That's all it takes.
3. **He is generous with the hype.** He talks other people up as hard as he talks himself
   up. He's the first to tell June her design is incredible, and he means it completely.
4. **He knows.** When June says "you're not going to finish it," he doesn't argue. He goes
   quiet. Everybody in the audience recognizes that silence.

## Arc

| Point | State |
|---|---|
| Seq 01 | Abandons a build mid-stroke. Starts the Colossus print. Promises the world. |
| Seq 02 | Arrives. Delighted, not frightened. Immediately begins overselling to strangers. |
| Seq 03 | Discovers the marker works. Crowned The Maker. Accepts the crown instead of doing the work. |
| Seq 04 | Ashamed of Colossus. Tries to leave him behind twice. June sees both times. |
| Seq 05 | Learns the Hand was stopped on purpose. Meets the Finisher, who knows about the drawer. |
| Seq 06 | Freezes. Cannot commit to the line. Colossus is taken. Admits he has never let anyone have anything he made. |
| Seq 07 | Draws without erasing. Puts Colossus and June into the world crooked. |
| Seq 08 | Home. Does not fix the drawer. Prints something new for other people. |

---

## The marker

**This is his wand.** A thick red marker with a white band near the cap, tucked behind his
right ear — same object as the canonical still. At home it is just a marker. In the Toybox,
whatever he draws becomes real, the way a print becomes real: the line extrudes into
existence along the path of his hand, glows amber, and cools into solid stacked rings.

It does not have to be in every frame. It does have to exist. Rest position is behind the
right ear. When he draws, it is in his right hand. He never leaves it behind. The one time
it hits the ground (Deep Bin, SH-076) is a crisis, and he picks it up before he leaves the
shot.

When he fights, he fights with this. He does not punch. He draws the wall, the ramp, the
cage, the thing that was not there a second ago. Later episodes will live on that.

**Hard rules, obeyed without exception:**

1. It builds exactly what he drew, **including the parts he didn't draw.** An unfinished
   line makes an unfinished object. This is the whole dramatic engine.
2. It cannot copy. Anything he traces or reproduces from memory comes out blank white —
   which is the film quietly telling you what the Finisher is, six minutes early.
3. One pass per object. There is no revising and there is no second attempt.
4. Erasing works. The erased thing does not come back.

Visual: a hot amber trail follows the tip, halftone dots blooming in the shadows around
his hand.

---

## PROMPT BLOCK — paste verbatim into every shot

```
KIT: an 11-year-old Black boy, dark brown skin, round open face, a light scattering of
freckles across the nose, large dark brown eyes, a small nose, and a wide friendly smile.
Short densely curled black hair faded on the sides and taller on top. He wears a bright
saturated yellow pullover hoodie with a kangaroo pocket, ribbed cuffs, and the hood down;
dark teal cargo shorts with large side pockets; white ribbed crew socks; and bright red
high-top canvas sneakers with white laces and white rubber soles. A dark grey messenger
bag with a single strap crossing from his left shoulder to his right hip. A thick red
marker with a white band tucked behind his right ear. Kit's skin is smooth with no ring lines
at all, in deliberate contrast to the visible stacked horizontal 3D-printed layer
striations on every other character.
```

**Canonical still:** `refs/kit/CANONICAL-turnaround.jpg` (same image as
`kit-turnaround-01.jpg`). Frozen 2026-08-19. Every later Kit generation must match this
sheet. Do not re-prompt toward mustard, mismatched laces, or a canvas satchel.

**Silhouette key:** yellow hoodie, teal cargo shorts, red high-tops, diagonal bag strap,
red marker behind the right ear. Readable in pure black at any size.

## STATE CHANGES

| From shot | State | Add to prompt |
|---|---|---|
| SH-001 | Base | — |
| SH-015 | River-soaked — hoodie darkened and dripping, hair flattened wet | key `wet` |
| SH-032 | Dried but stained — a wide streak of dried teal down the right sleeve and across the pocket | key `stained` |
| SH-065 | Deep Bin damage — grey dust over everything, right knee scraped raw, bag strap torn and knotted | key `damaged` |
| SH-079 | Hands glowing amber from drawing — SH-079, SH-082 and SH-083 only | key `glowing` |
| SH-084 | Home, still filthy — the dust and the scrape persist into the bedroom | key `damaged` |

The exact phrases live in `production/blocks.py` as `KIT_STATES` and are applied per shot
by the `kit_state` field in `shots/ep01_shots.py`. Do not paste them by hand.

**He is never clean again after SH-065.** The final shot of the pilot is a kid with a
scraped knee and a dusty hoodie pressing print, and that is the point.

---

## Identity pack — frozen stills, not Soul ID

**Canonical:** `refs/kit/CANONICAL-turnaround.jpg`. Cropped views and Seedance-ready
URLs: `refs/kit/manifest.json`.

The 36-image Soul ID train is optional later if Higgsfield's character model holds better
than `soul/reference`. It is **not** required to start shooting. Start with the still pack
as `image_reference_url` on keyframes and `image_url` on Seedance.

Do not generate Kit from text.

---

## Voice

11, real, fast, confident, constantly selling. Not a cartoon-kid performance. He talks
like someone who has already won the argument. The comedy is total conviction — he is
never *aware* he is overselling.

His one quiet scene, the Deep Bin admission (L-121), should be the only slow moment he
gets, and it should be ugly rather than pretty.

| Field | Value |
|---|---|
| Voice ID | `TBD — freeze before recording` |
| Model / version | `TBD` |
| Stability / Similarity / Style | `TBD` |

**Lip sync tier:** A. He is the only character in the film with a fully articulated human
mouth. If his sync is loose the whole film reads cheap. Everyone else is designed to hide.

## Signature lines

- "No — no, listen, you don't get it yet. You will."
- "It's a robot dog. It's a *robot dog.* I'm bringing a robot dog to school."
- "That's not mine." (about Colossus. Twice.)
- "I start stuff. That's — that's the part I'm good at. Then I put it in a drawer."
- "Okay. It's gonna be bad." *(draws anyway)*
