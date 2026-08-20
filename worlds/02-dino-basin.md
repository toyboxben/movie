# 02 — DINO BASIN

**Seq 04. The crossing. First sight of the smoothing.**
**Category: dinosaurs and animals.**

---

## What it is

A wide dry canyon basin scoured out of the Bed, filled with drifting dust and heat haze,
where the herds move. Printed dinosaurs at every scale from thumb-sized to enormous, all
in bright non-naturalistic single colours — a hot pink triceratops, a translucent blue
stegosaurus, a marbled orange-and-green brachiosaurus the size of a building. They are not
intelligent. They migrate along the dry riverbeds, and when they move together the sound is
enormous.

The basin is scattered with the fossils of the world: broken struts, a colossal snapped
support tree half-buried in dust, the curled and warped base of something that failed a
long time ago and was left where it lay.

## Story function

- **The crossing.** Spectacle sequence. The herd is the obstacle, and it is also the most
  purely fun stretch in the film.
- **Colossus catches up** (SH-045). Kit says "that's not mine." June hears him.
- **Colossus can't make the jump** (SH-050). Kit almost turns back, and doesn't. June sees.
- **The Finished village** (SH-053). They come over a rise and find a settlement of blank
  white motionless figures, frozen mid-gesture. Nobody speaks. This is the film's first
  horror beat and it must be played completely straight and completely silent.
- **The clock starts.** From SH-053 the white horizon is visible in the background of every
  exterior shot in the film and never retreats.

## The beat that could only happen here

The herd is the reason they can't turn back, and the smoothed village is out here in the
middle of nowhere — which tells the audience, without a word, that this is not a local
problem and it is not being contained.

## Key light

**Camera left**, hard rust-orange, high and hazy. Heavy dust in every shot. Shafts and
god-rays through the dust are correct and encouraged.

---

## PLATE BLOCK — `WP-basin-wide` — paste verbatim

```
ENVIRONMENT: a vast dry canyon basin scoured out of a pale warm glassy plain, filled with
drifting rust-coloured dust and shimmering heat haze. Dry braided riverbeds wind across
the floor between eroded ridges. Scattered across the landscape are the enormous fossil
remains of printed plastic structures — a colossal snapped lattice support tree half
buried in dust, warped and curled plastic bases the size of hills, broken struts. Moving
through the haze in the middle distance is a herd of printed plastic dinosaurs at wildly
mismatched scales, from thumb-sized to building-sized, each one a bright non-naturalistic
single flat filament colour — hot pink, translucent blue, marbled orange and green — all
with visible horizontal 3D-printed layer striations. Far overhead the sky is the vast
wooden underside of an enormous desk. Hard rust-orange light from camera left, olive
shadow, thick dust, visible god-rays.
```

## PLATE BLOCK — `WP-basin-riverbed` — paste verbatim

```
ENVIRONMENT: the floor of a dry braided riverbed in a dusty canyon basin, cracked pale
glassy ground underfoot, low eroded banks of packed rust-coloured dust on either side,
scattered with broken printed plastic struts and debris in mismatched filament colours.
Heat haze shimmering along the ground. Hard rust-orange light from camera left, long olive
shadows, drifting dust.
```

## PLATE BLOCK — `WP-basin-herd` — paste verbatim

```
ENVIRONMENT: inside a moving herd of enormous printed plastic dinosaurs, seen from ground
level looking steeply up between their legs. The dinosaurs are at wildly mismatched scales
and each is a bright non-naturalistic single flat filament colour with visible horizontal
3D-printed layer striations and visible printed ball joints at the limbs. Vast columnar
legs stride past on either side, throwing up billowing rust-coloured dust. Shafts of hard
orange light break through the gaps between the bodies. Low camera, heavy dust, high
drama.
```

## PLATE BLOCK — `WP-basin-finished-village` — paste verbatim

```
ENVIRONMENT: a small abandoned settlement of printed plastic huts and scaffolding on a
rise in a dusty canyon basin. Standing throughout the settlement are dozens of blank
featureless matte-white figures of varying shapes and sizes, completely smooth with no
layer lines, no colour and no features, standing utterly motionless and frozen mid-gesture
— one with an arm half raised, one mid-stride, one turned as if it had been about to
speak. Dust has drifted against their feet. Nothing moves. The light here is noticeably
flatter and colder than the surrounding basin, with no rim light and almost no shadow.
Absolute stillness.
```

---

## The Smooth horizon — introduced here

From **SH-053** onward. The prompt builder appends the right phrase automatically from the
`smooth` value on each shot:

| Coverage | Prompt phrase |
|---|---|
| 25% | `on the distant horizon a thin hard line of pure flat white where the landscape simply stops having colour or texture` |
| 50% | `across the far half of the landscape everything has gone blank flat white and featureless, meeting the coloured world at a hard clean edge` |
| 75% | `most of the visible landscape is blank flat shadowless white, the last band of colour and texture squeezed into the near foreground` |

Tracked as a monotonic 0–100 value in `shots/ep01_shots.py`. The build script fails if it
ever goes backwards.

## Sound

Wind across dry ground, grit, the enormous distant clacking of the herd — thousands of
printed ball joints working at once, which at scale sounds like weather. In the Finished
village: nothing at all. Cut the ambient bed to silence the moment they crest the rise.
