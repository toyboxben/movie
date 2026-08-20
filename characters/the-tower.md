# THE TOWER — Comic Relief

**A temperature calibration tower. Ten stacked layers, each printed at a different
temperature, each with a different personality. All of them awake. All of them arguing.**

---

## Who they are

A temp tower is a test print: a stack of identical blocks, each extruded at a different
nozzle temperature, so you can see which setting your filament likes. The bottom blocks
print cold — brittle, sharp-edged, under-extruded. The top blocks print hot — glossy,
sagging, over-extruded, stringy.

The Tower came out of the machine with all ten temperatures conscious, and has been
having the same argument for its entire life.

| Layer | Temp | Personality |
|---|---|---|
| 1 (bottom) | 190° | Brittle, precise, hostile. Speaks in corrections. Has never been wrong. |
| 2 | 195° | Anxious. Agrees with whoever spoke last. |
| 3 | 200° | The only reasonable one. Exhausted. Wants everyone to get along. Nobody listens. |
| 4 | 205° | Conspiracy theorist. Believes the Hand is a hoax. |
| 5 | 210° | Asleep. Occasionally says something devastatingly wise and goes back to sleep. |
| 6 | 215° | Aggressively upbeat. Motivational. Insufferable. |
| 7 | 220° | Flirtatious with everyone including inanimate objects. |
| 8 | 225° | Increasingly slurred. Melting slightly. Deeply sentimental. |
| 9 | 230° | Basically drunk. Stringing everywhere. Says the true thing nobody wants said. |
| 10 (top) | 235° | Over-extruded into a formless blob. Cannot speak. Just moans. Layer 9 translates, badly. |

**Function:** comic baseline, and the film's primary joke engine. Per the brief the comedy
lives in dialogue, and the Tower is a dialogue machine — ten voices in one body means any
line can be interrupted, contradicted, seconded and undermined without cutting away or
adding a character. He also runs underneath the serious scenes so the film never sits
heavy for more than ninety seconds. And he is a walking demonstration that a group of
imperfect things arguing beats a perfect thing standing silent, which is the theme
smuggled in as a joke.

**Best structural use:** exposition. When the film needs to explain a rule of the world,
Layer 1 states it pedantically, Layer 4 disputes it, Layer 3 apologizes, and Layer 9 says
the actual truth. The audience gets a lore dump and thinks they got a joke.

**The moment it stops being funny:** in Seq 06 the smoothing takes Layers 1 through 4, and
the remaining six go quiet for the first time in the film. Layer 3 — the reasonable one,
who has wanted silence for his entire existence — has to live in it.

## Movement

The Tower cannot walk. He is a stack of blocks. He gets around by **toppling forward and
restacking**, which is slow, undignified, and the source of a recurring gag about how
long everyone has to wait for him. In an emergency someone has to carry him, and the
layers rank the carriers out loud.

---

## PROMPT BLOCK — paste verbatim into every shot

```
THE TOWER: a stack of ten cube-shaped printed blocks balanced one on top of another,
about three feet tall, each block roughly the size of a fist. The stack shifts in quality
from bottom to top: the lowest blocks are sharp-edged, matte, pale grey and slightly
under-extruded with visible gaps between layer lines; the middle blocks are clean and
well-formed in warming amber tones; the upper blocks become progressively glossier,
sagging, over-extruded and drooping at the corners, trailing wispy strands of stringing
filament; the topmost block is a shapeless melted blob of dark amber plastic. Each block
has a single horizontal slot across its front like a mail slot, which glows from within
when that layer speaks. No arms, no legs, no face. The whole stack sways and rebalances
constantly.
```

**Silhouette key:** ten stacked cubes degrading from crisp to melted, bottom to top.

**Continuity trap:** the block count and the crisp→melted gradient direction. Ten blocks,
always. Crisp at the bottom, melted at the top, never reversed.

## Reference set

- Full stack: front, 3/4, profile, rear
- Detail crops: bottom three blocks (sharp, gapped), middle three (clean), top four
  (sagging, stringing, blob)
- Slot states: all dark, one glowing, several glowing at once (an argument)
- Poses: standing balanced, mid-topple, collapsed into a scattered pile, being carried
  under someone's arm
- Lighting: the internal slot-glow in darkness, which is how he appears in the Deep Bin

## STATE CHANGES

| From shot | State |
|---|---|
| SH-033 | Base — first appearance, ten blocks. Block key `TOWER`. |
| SH-072 | Four blocks lost — the bottom four smoothed featureless white and dead, the surviving six restacked on top of them. **Six glowing slots maximum from here on.** Block key `TOWER_DAMAGED`. |

He is not restored in the pilot.

---

## Voice

**Ten distinct voices from one body.** Either cast one actor performing all ten, or freeze
ten separate voice IDs. Either way, log every setting — this is the single highest
voice-drift risk in the production because ten IDs is ten chances to get it wrong.

Recommended: one actor. The comedy is funnier when the audience can hear it is the same
performer, and it removes nine drift risks.

| Layer | Voice character |
|---|---|
| 1 | Clipped, nasal, over-articulated. Every consonant. |
| 2 | Small, fast, agreeable. |
| 3 | Warm, tired, patient. The only one you'd want to talk to. |
| 4 | Low, urgent, confiding. |
| 5 | Sleepy mumble, then sudden clarity. |
| 6 | Loud, bright, relentless. |
| 7 | Slow, warm, entirely too pleased. |
| 8 | Thick, slurring, weepy. |
| 9 | Loose, slow, alarmingly honest. |
| 10 | Wordless moan. |

| Field | Value |
|---|---|
| Voice IDs | `TBD — freeze all ten before recording` |
| Settings | `TBD — log per layer` |

**Lip sync tier:** C, entirely. No mouths — layers glow when speaking. This is animated as
a light pass in post and never depends on the video model. The Tower can therefore carry
unlimited dialogue at zero sync risk, which is exactly why he gets the exposition.

## Signature exchange

> **LAYER 1:** The river is filament. It is not water. It is not for drinking.
> **LAYER 4:** *Or so they'd have you believe.*
> **LAYER 3:** Please.
> **LAYER 6:** Great question though! Great energy!
> **LAYER 9:** He's gonna drink it.
> *(Kit drinks it.)*
> **LAYER 9:** Told you.
