# JUNE — Second Lead

**One of a kind. Some other kid designed her from nothing and stopped halfway. She has
been seventy percent finished for a very long time.**

---

## Who she is

Everyone else in the Toybox came from the catalog — thousands of copies of the same
cheerful things. June was drawn by hand by a child who was making something that had never
existed, and got most of the way through, and stopped.

Her right side is complete and it is *beautiful* — a bold, strange, wonderfully designed
creature, better than anything in the catalog, clearly made with love. Her left side is an
empty wireframe: the outline of what she was supposed to be, hollow, translucent, a ghost
of a plan. She can barely use that arm. She has learned to do everything one-handed and
she does it faster than most people do it with two.

She is dry, impatient, and completely unimpressed by anybody. She does not explain herself
twice. She has spent years watching the Hand and trying to reach it, because the Hand is
the only thing that could ever finish her.

**Her name is also unfinished.** The maker's mark on her heel reads `JUNIPER` with only
the first four letters actually built. She goes by June. She has never told anyone this,
and when it comes out it is the quietest, worst moment in the film.

**Function:** she is the consequence. She's what happens to the things Kit starts, standing
right in front of him, while he does it again to a dog.

## Why she works

She is not a love interest, not a sidekick, and not a mentor, and she does not warm up
gradually. The order is strict:

1. She's correct about Kit on sight and says so publicly, in front of the crowd crowning
   him, which is the rudest possible moment.
2. He proves her correct. Twice, with Colossus, while she watches.
3. Only *after* he does the work does she revise her opinion — and even then she does it
   in about four words.

That order is the whole reason she lands. If she softens early she becomes furniture.

## What she wants vs. what she does

She wants to belong to a maker who didn't leave more than she has ever wanted to be
filled in, and she would rather die than ask. When Kit finally offers, in Seq 07, her
first answer is no. He does it anyway, badly, while she's mid-sentence.

**She is not completed at the end.** He adds a crooked left side in four seconds — wrong
colour, wrong shape, lumpy at the seam — and it is *hers.* She is still unfinished. She
is still in the world. That is the gift.

## Arc

| Point | State |
|---|---|
| Seq 03 | Cuts through the crowd at SH-040. "You're not going to finish it." |
| Seq 04 | Guides them, reluctantly, because she wants the Hand restarted for her own reasons. |
| Seq 05 | Learns the Hand was stopped on purpose. Realises she has been waiting for something that was murdered. |
| Seq 06 | Her name comes out. She tells Kit the truth about who made her and what he did. |
| Seq 07 | Refuses help. Gets helped. Is furious and then is not. |
| Seq 08 | Not present — Kit is home. Her file is on his screen in the last shot. |

---

## PROMPT BLOCK — paste verbatim into every shot

```
JUNE: a girl-shaped printed creature about two feet tall, clearly hand-designed and
one-of-a-kind rather than mass-produced — an inventive original design with a rounded
angular head, large expressive dark eyes, a small simple mouth, and a swept crest of
sculpted material instead of hair. Her RIGHT side is fully complete: solid, beautifully
finished, printed in deep plum and burnt orange with crisp stacked horizontal 3D-printed
layer striations across every surface and a warm satin sheen. Her LEFT side is unfinished — a hollow open
wireframe of thin translucent pale-grey struts tracing the outline of an arm, a shoulder,
half a torso and half a leg, with nothing filled in, so you can see straight through her.
The boundary between the two halves runs cleanly down her centre line. She moves with her
solid side leading and holds the wireframe arm close to her body. A small maker's mark is
stamped on her heel.
```

**Silhouette key:** solid on one side, empty outline on the other, split down the middle.
The most distinctive silhouette in the film — she is unmistakable in pure black.

**Continuity trap — the most frequently broken rule in the film:** her wireframe is on
**her own left**, which means it appears on **frame right** when she faces camera. Models
flip this constantly. Check every single keyframe. Also: models will try to *fill in* the
wireframe. It is empty. You can see the background through it.

## STATE CHANGES

| From shot | State |
|---|---|
| SH-040 | Base — first appearance |
| SH-082 | **Rebuilt.** Her left side is filled in — but in a completely different material: warm amber, slightly the wrong shape, lumpy at the seam where new meets old, the arm too long, the shoulder set a few degrees too high. Block key `JUNE_REBUILT`. |

SH-082 is the transition itself, so it is authored as a first+last frame shot: starts
wireframe, ends filled.

## PROMPT BLOCK — JUNE_REBUILT (SH-082 onward) — paste verbatim

```
JUNE-REBUILT: the same one-of-a-kind girl-shaped printed creature, now complete on both
sides but visibly repaired by hand. Her right side remains deep plum and burnt orange with
crisp horizontal 3D-printed layer striations. Her left side is newly filled in with warm
amber material that does
not match the original at all — slightly the wrong shape, the arm a little too long, the
shoulder set a few degrees too high, the seam down her centre line lumpy and over-built
where the new material meets the old. Her ring striations run at a slightly different
angle on the new side. She stands square for the first time, using both arms.
```

---

## Reference set

Generate both versions separately. Paste-ready prompts in [turnarounds.md](turnarounds.md).

- Turnaround: front, 3/4 L, profile L, 3/4 R, profile R, rear — the profile shots matter
  most here, because they are the only angles that show the two halves cleanly separated
- The wireframe side isolated, lit from behind so it reads as genuinely empty
- Expressions: flat, unimpressed, a small dry smile, genuine anger, the one moment of hurt
- Poses: standing with the solid side forward, walking, one-handed climbing, holding the
  wireframe arm protectively
- Detail crop: the maker's mark on her heel reading a partial word
- Scale reference: beside Kit's hand, beside Colossus

---

## Voice

Flat, dry, impatient. Roughly 11. Never shouts, never explains twice, never impressed.
Most of the film's biggest laughs are her one-word answers to Kit's speeches, so the
performance has to be genuinely deadpan rather than sardonic — she isn't doing a bit, she
just doesn't have time.

She raises her voice exactly once, in the Deep Bin, and it should be shocking.

| Field | Value |
|---|---|
| Voice ID | `TBD — freeze before recording` |
| Settings | `TBD` |

**Lip sync tier:** B. Small simple mouth, so partial sync reads fine. Cut to Kit reacting
on her longer lines.

## Signature lines

- "You're not going to finish it." (her first line, to a cheering crowd)
- "Cool." (to a three-sentence boast)
- "I've met you before. You had a different face."
- "Don't. You'll get halfway and then you'll feel bad and then I'll have to watch that too."
- Last line: "It's crooked." / KIT: "Yeah." / JUNE: "...Okay."
