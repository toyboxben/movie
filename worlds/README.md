# Worlds

Six environments. Each is a Toybox catalog category rendered as a civilization, and each
must contain **a story beat that could not happen anywhere else** — the only rule standing
between a world tour and a product carousel.

| # | World | Category | Story function | Seq | Screen dir |
|---|---|---|---|---|---|
| 00 | [The Bedroom](00-the-bedroom.md) | the real world | Ordinary world, call, threshold, return | 01, 08 | — |
| 01 | [The Raft](01-the-raft.md) | everyday small prints | Wonder. Mentor. The crowning. | 02, 03 | L→R |
| 02 | [Dino Basin](02-dino-basin.md) | dinosaurs & animals | The crossing. First sight of the smoothing. | 04 | L→R |
| 03 | [Gearhaven](03-gearhaven.md) | robots, mechs, functional prints | Midpoint. The archive. The Finisher arrives. | 05 | L→R |
| 04 | [The Deep Bin](04-the-deep-bin.md) | failed & abandoned prints | The Ordeal. | 06 | descent |
| 05 | [The Smooth](05-the-smooth.md) | the absence of category | The climax. | 07 | R→L |

## Shared world laws

True everywhere, never contradicted:

1. **Everything is printed and knows it.** The rings on your body are a birthmark, not a
   defect. Being smooth is obscene, and everyone is being very polite about Kit.
2. **The rivers** run between all regions — slow, warm, semi-molten, colour shifting along
   their length. They are the only transport network. They are potable, load-bearing and
   sacred, **in that order**.
3. **Scale is chaotic.** A thumb-sized dinosaur and a bus-sized dragon are neighbours,
   because different people printed them on different machines. Nobody finds this strange.
   Kit finds it constantly disorienting.
4. **The sky is the underside of a desk** — vast, wooden, impossibly far up, with cables
   hanging down through it like weather systems.
5. **Weather is human activity.** A drawer closing is thunder. A lamp is sunrise. A window
   opening is a storm front. The toys have a full theology built on misreading this, and
   Kit recognises every single one and says nothing.
6. **The Hand** is the god on the horizon — a colossal nozzle that builds new life one
   glowing layer at a time. Nobody knows what it's making. It has never stopped.

   At **SH-043**, it stops.

## Plate blocks

Each file contains a **PLATE BLOCK** pasted verbatim into every shot set in that world.
Never describe an environment freehand. Worlds with multiple states have one block per
state, each with its own ID.

## The Hand

Visible on the horizon from the Raft, Dino Basin, and Gearhaven. It is the film's clock and
its mystery box, so its state is tracked per shot.

| State | Shots | Block key |
|---|---|---|
| Building | SH-019 → SH-042 | `HAND["building"]` |
| **Stopped** | SH-043 → SH-080 | `HAND["stopped"]` |
| Restarted | SH-081 → SH-083 | `HAND["restarted"]` |

The exact phrases live in `production/blocks.py` and are injected automatically by the
prompt builder — you never paste them by hand.

## The Smooth horizon

From **SH-053** an advancing white line is visible in the background of every exterior
shot, and it never retreats. Coverage phrases at 25 / 50 / 75 percent live in
`production/blocks.py`. The value per shot is in `shots/ep01_shots.py`, and
`production/build_prompts.py` fails the build if it ever goes backwards.
