"""Canonical prompt blocks.

This is the machine-readable source of truth for prompt assembly. The creative
documentation in characters/ and worlds/ contains the same text for humans to read;
if you change a look, change it HERE and re-run build_prompts.py, then update the
matching .md file.
"""

from __future__ import annotations

STYLE_LOCK = (
    "STYLE: painterly 3D animation, hand-painted textures over dimensional forms, "
    "visible brushstroke in the shadows, thick graphic silhouettes, painted volumetric "
    "light, rich saturated color with deep teal shadows and warm amber key light, "
    "cinematic depth of field, subtle film grain, 24fps, 21:9 cinematic framing. High "
    "contrast rim lighting separating subject from background. No text, no logos, no "
    "watermarks, no subtitles."
)

NEGATIVE_LOCK = (
    "NEGATIVE: photorealistic, live action, uncanny realistic human skin, glossy plastic "
    "CGI sheen, flat even lighting, muddy desaturated color, extra fingers, deformed "
    "hands, warped face, morphing features, text, watermark, logo, subtitles, vertical "
    "framing, blurry low-detail background, anime, flat cel shading"
)

ON_TWOS = "Toy characters move with slightly stepped, on-twos animation."


# ---------------------------------------------------------------- characters

CHARACTERS = {
    "KIT": (
        "KIT: an 11-year-old Black boy, dark brown skin, round open face, a light scattering "
        "of freckles across the nose, large dark brown eyes, a small nose, and a wide friendly "
        "smile. Short densely curled black hair faded on the sides and taller on top. He wears "
        "a bright saturated yellow pullover hoodie with a kangaroo pocket, ribbed cuffs, and "
        "the hood down; dark teal cargo shorts with large side pockets; white ribbed crew "
        "socks; and bright red high-top canvas sneakers with white laces and white rubber "
        "soles. A dark grey messenger bag with a single strap crossing from his left shoulder "
        "to his right hip. A thick red marker with a white band tucked behind his right ear. Kit's "
        "skin is smooth with no ring lines at all, in deliberate contrast to the visible "
        "stacked horizontal 3D-printed layer striations on every other character."
    ),
    "JUNE": (
        "JUNE: a girl-shaped printed creature about two feet tall, clearly hand-designed "
        "and one-of-a-kind rather than mass-produced — an inventive original design with a "
        "rounded angular head, large expressive dark eyes, a small simple mouth, and a "
        "swept crest of sculpted material instead of hair. Her RIGHT side is fully "
        "complete: solid, beautifully finished, printed in deep plum and burnt orange with "
        "crisp stacked horizontal 3D-printed layer striations across every surface and a "
        "warm satin sheen. Her LEFT side is unfinished — a hollow open wireframe of thin "
        "translucent pale-grey struts tracing the outline of an arm, a shoulder, half a "
        "torso and half a leg, with nothing filled in, so you can see straight through her. "
        "The boundary between the two halves runs cleanly down her centre line. She moves "
        "with her solid side leading and holds the wireframe arm close to her body."
    ),
    "JUNE_REBUILT": (
        "JUNE: the same one-of-a-kind girl-shaped printed creature, now complete on both "
        "sides but visibly repaired by hand. Her right side remains deep plum and burnt "
        "orange with crisp horizontal 3D-printed layer striations. Her left side is newly "
        "filled in with warm amber material that does not match the original at all — "
        "slightly the wrong shape, the arm a little too long, the shoulder set a few "
        "degrees too high, the seam down her centre line lumpy and over-built where the new "
        "material meets the old. Her layer striations run at a slightly different angle on "
        "the new side. She stands square, using both arms."
    ),
    "COLOSSUS": (
        "COLOSSUS: a small printed robot dog, about eight inches tall, that is only forty "
        "percent built. He has a boxy angular head with two round amber lens eyes and one "
        "folded ear, a chest, and two sturdy front legs — and then his body simply STOPS in "
        "a clean flat cross-section just behind the shoulders, cut off mid-layer, hollow "
        "and open so you can see straight into the empty interior lattice inside him. He "
        "has NO back half, NO hind legs and NO tail whatsoever. He is printed in bright "
        "cobalt blue with orange accent panels, with crisp stacked horizontal 3D-printed "
        "layer striations across every surface. He drags himself along enthusiastically on "
        "his two front legs, hindquarters absent."
    ),
    "COLOSSUS_SMOOTHED": (
        "COLOSSUS: the small forty-percent-built robot dog, now blank featureless matte "
        "white — all colour drained away, all layer striations dissolved into a glassy "
        "seamless surface, his amber lens eyes sealed over into smooth blank domes. He is "
        "frozen completely motionless, caught mid-stride with one front paw raised. He "
        "still has no back half. He does not move at all."
    ),
    "COLOSSUS_FINISHED": (
        "COLOSSUS: the small printed robot dog, now complete but visibly finished in a "
        "hurry by hand. His front half is the original bright cobalt blue with orange "
        "accents and crisp horizontal 3D-printed layer striations. His new back half is a "
        "mismatched warm amber, noticeably a different scale from the front, with one hind "
        "leg longer than the other, an over-built lumpy seam across his middle where new "
        "meets old, and a tail that is little more than a thick scribbled loop of material. "
        "He stands crooked and lopsided on four uneven legs, tail wagging hard."
    ),
    "BENCHY": (
        "BENCHY: a small chunky tugboat character about the size of a human hand, made of "
        "printed plastic in weathered sea-green and cream, with a squat rounded hull, a "
        "single square wheelhouse with one round porthole window and one rectangular "
        "window, a short smokestack and a low chimney. Pronounced horizontal 3D-printed "
        "layer striations across the entire hull catching the light in bands. Scuffed, "
        "salt-crusted, dried residue along the waterline, one corner of the bow chipped "
        "away. He has no face and no mouth — he expresses entirely through the tilt of his "
        "hull and the glow behind his porthole, which brightens when he speaks."
    ),
    "TOWER": (
        "THE TOWER: a stack of exactly ten cube-shaped printed blocks balanced one on top "
        "of another, about three feet tall, each block roughly the size of a fist. The "
        "stack shifts in quality from bottom to top: the lowest blocks are sharp-edged, "
        "matte, pale grey and slightly under-extruded with visible gaps between layer "
        "lines; the middle blocks are clean and well-formed in warming amber tones; the "
        "upper blocks become progressively glossier, sagging, over-extruded and drooping at "
        "the corners, trailing wispy strands; the topmost block is a shapeless melted blob "
        "of dark amber plastic. Each block has a single horizontal slot across its front "
        "which glows from within when that layer speaks. No arms, no legs, no face. The "
        "stack sways and rebalances constantly."
    ),
    "TOWER_DAMAGED": (
        "THE TOWER: the stack of ten cube-shaped printed blocks, but the bottom four blocks "
        "are now blank featureless matte white with no layer lines, no texture and no slot, "
        "completely dead and inert. The six surviving blocks above them retain their colour, "
        "their layer lines and their glowing horizontal front slots. The stack shifts from "
        "clean amber in its lower surviving blocks to sagging, over-extruded and drooping "
        "at the top, ending in a shapeless melted blob. No arms, no legs, no face."
    ),
    "FINISHER": (
        "THE FINISHER: a tall slender featureless humanoid figure, roughly seven feet tall "
        "in a world of small toys, moulded from perfectly seamless matte-white material "
        "with absolutely no layer lines, no seams, no texture and no visible joints "
        "anywhere on his body. Smooth blank oval head with no face at all — no eyes, no "
        "mouth, no nose, only an unbroken curved surface with a faint pearlescent sheen. "
        "Long elegant limbs, narrow shoulders, elongated smooth hands with fingers slightly "
        "too long. He wears nothing. He stands and moves with patient, unhurried, almost "
        "gentle grace, always upright, never hunched. He casts no visible shadow and light "
        "falls on him flatly with no rim highlight."
    ),
}


# ---------------------------------------------------------------- environments

PLATES = {
    "WP-bedroom-night": (
        "ENVIRONMENT: a small cluttered eleven-year-old boy's bedroom at night, seen at "
        "human scale. A wooden desk pushed against a window with cool blue moonlight "
        "falling across it from the left. On the desk sits a compact cube-shaped 3D printer "
        "with a glowing warm-orange interior chamber, the brightest light in the room, "
        "throwing hard orange light across the desk and up the wall. Beside it a crowded "
        "pen cup, scattered paper, a metal ruler, and a shelf above holding neatly arranged "
        "finished printed plastic models. The wall above the desk is covered in pinned-up "
        "pencil sketches of robots and machines, all of them clearly unfinished, several "
        "stopping mid-line into blank paper. A desk drawer hangs open, overstuffed. An "
        "unmade bed in the shadowed background. Warm dust in the air, deep teal shadows, "
        "single hot orange point light."
    ),
    "WP-bedroom-drawer": (
        "ENVIRONMENT: an open desk drawer seen from above, crammed with dozens of abandoned "
        "half-built printed plastic robot dog parts — heads with no bodies, single legs, "
        "torsos that stop abruptly mid-layer, chassis with no limbs, all in mismatched "
        "filament colours, piled on top of a thick layer of folded and crumpled pencil "
        "sketches. Nothing in the drawer is complete. Cool blue light from above, deep "
        "shadow in the depths of the drawer."
    ),
    "WP-bedroom-chamber": (
        "ENVIRONMENT: extreme macro interior of a 3D printer chamber, warm orange light, a "
        "brass nozzle extruding a glowing thread of molten material that cools from bright "
        "amber to solid colour as it is laid down, building an object one visible horizontal "
        "layer at a time on a textured glass bed. Shallow depth of field, dust motes "
        "drifting, the soft blur of a cooling fan behind. Every layer line crisp and "
        "distinct."
    ),
    "WP-bedroom-return": (
        "ENVIRONMENT: the same small cluttered bedroom, identical angle and identical "
        "lighting to the opening — cool blue window light from the left, hot orange printer "
        "glow from the right, now with the first pale grey of dawn beginning at the window. "
        "The pen cup on the desk holds only pens. The wall of unfinished sketches is "
        "unchanged. A fresh sheet of paper sits centred on the desk."
    ),
    "WP-raft-wide": (
        "ENVIRONMENT: an enormous harbour shanty-city built on a vast warm glassy plain "
        "that stretches to the horizon like frosted glass. The city is constructed entirely "
        "from lattice scaffolding, ramps, gantries and open walkways lashed together into "
        "leaning towers, all built from pale printed plastic strut work. Buildings are made "
        "from repurposed giant everyday objects at wildly mismatched scales — a keychain "
        "the size of a bus, a colossal bag clip forming an archway, phone stands the size "
        "of cathedrals, giant planters converted into houses — every one a different flat "
        "single filament colour with visible horizontal 3D-printed layer striations. Open "
        "channels of slow-moving warm glowing molten material run between the buildings "
        "like canals. Far overhead the sky is the vast wooden underside of an enormous "
        "desk, impossibly distant, with thick cables hanging down through the golden haze. "
        "Honey-gold late afternoon light from camera left, long soft shadows, warm dust."
    ),
    "WP-raft-market": (
        "ENVIRONMENT: a dense crowded market street inside a shanty-city of printed plastic "
        "— narrow, canopied with mismatched awnings, stalls stacked three levels high on "
        "scaffolding, strung with lines of small glowing beads. The street is packed with "
        "living printed plastic objects at wildly mismatched scales, each a different "
        "single flat filament colour, all with visible horizontal 3D-printed layer "
        "striations — keychains, bag clips, cable organisers, tiny planters, phone stands, "
        "hooks and brackets, all animate and jostling. Stalls sell ladled cups of glowing "
        "molten material, spare struts, loose beads. Honey-gold late afternoon light "
        "slanting between the awnings from camera left, warm dust, deep amber shadow."
    ),
    "WP-raft-dock": (
        "ENVIRONMENT: a low working dock on the edge of a wide slow river of warm glowing "
        "molten material, built from lashed printed plastic scaffolding and worn plank "
        "walkways stained with dried residue. Mooring posts, coils of filament rope, "
        "stacked crates in mismatched filament colours. The far bank is lost in golden "
        "haze. The vast wooden underside of a desk hangs impossibly far overhead. "
        "Honey-gold late afternoon light from camera left, glowing reflections rippling on "
        "the underside of the dock."
    ),
    "WP-raft-plaza": (
        "ENVIRONMENT: a wide open plaza in a printed plastic shanty-city, ringed by leaning "
        "scaffold towers with crowds packed onto every level of the surrounding balconies "
        "and walkways looking down into the centre. The plaza floor is warm glassy frosted "
        "plain. A low empty plinth stands off to one side. Strings of small glowing beads "
        "criss-cross overhead. Honey-gold late afternoon light from camera left, thousands "
        "of small mismatched filament colours in the watching crowd."
    ),
    "WP-raft-river": (
        "ENVIRONMENT: a wide slow river of warm glowing semi-molten material, its colour "
        "shifting along its length from amber to deep teal, moving between low banks of "
        "pale glassy ground scattered with printed plastic debris. Glowing reflections on "
        "everything. The vast wooden underside of a desk hangs impossibly far overhead in "
        "golden haze. Honey-gold late afternoon light from camera left."
    ),
    "WP-basin-wide": (
        "ENVIRONMENT: a vast dry canyon basin scoured out of a pale warm glassy plain, "
        "filled with drifting rust-coloured dust and shimmering heat haze. Dry braided "
        "riverbeds wind across the floor between eroded ridges. Scattered across the "
        "landscape are the enormous fossil remains of printed plastic structures — a "
        "colossal snapped lattice support tree half buried in dust, warped and curled "
        "plastic bases the size of hills, broken struts. Moving through the haze in the "
        "middle distance is a herd of printed plastic dinosaurs at wildly mismatched "
        "scales, from thumb-sized to building-sized, each one a bright non-naturalistic "
        "single flat filament colour — hot pink, translucent blue, marbled orange and green "
        "— all with visible horizontal 3D-printed layer striations. Far overhead the sky is "
        "the vast wooden underside of an enormous desk. Hard rust-orange light from camera "
        "left, olive shadow, thick dust, visible god-rays."
    ),
    "WP-basin-riverbed": (
        "ENVIRONMENT: the floor of a dry braided riverbed in a dusty canyon basin, cracked "
        "pale glassy ground underfoot, low eroded banks of packed rust-coloured dust on "
        "either side, scattered with broken printed plastic struts and debris in mismatched "
        "filament colours. Heat haze shimmering along the ground. Hard rust-orange light "
        "from camera left, long olive shadows, drifting dust."
    ),
    "WP-basin-herd": (
        "ENVIRONMENT: inside a moving herd of enormous printed plastic dinosaurs, seen from "
        "ground level looking steeply up between their legs. The dinosaurs are at wildly "
        "mismatched scales and each is a bright non-naturalistic single flat filament "
        "colour with visible horizontal 3D-printed layer striations and visible printed "
        "ball joints at the limbs. Vast columnar legs stride past on either side, throwing "
        "up billowing rust-coloured dust. Shafts of hard orange light break through the "
        "gaps between the bodies. Low camera, heavy dust, high drama."
    ),
    "WP-basin-finished-village": (
        "ENVIRONMENT: a small abandoned settlement of printed plastic huts and scaffolding "
        "on a rise in a dusty canyon basin. Standing throughout the settlement are dozens "
        "of blank featureless matte-white figures of varying shapes and sizes, completely "
        "smooth with no layer lines, no colour and no features, standing utterly motionless "
        "and frozen mid-gesture — one with an arm half raised, one mid-stride, one turned "
        "as if it had been about to speak. Dust has drifted against their feet. Nothing "
        "moves. The light here is noticeably flatter and colder than the surrounding basin, "
        "with no rim light and almost no shadow. Absolute stillness."
    ),
    "WP-gearhaven-wide": (
        "ENVIRONMENT: an enormous industrial city built into a sheer cliff wall out of "
        "working printed plastic mechanisms — gears the size of buildings turning slowly "
        "against one another, printed chain drives running between towers, colossal hinges, "
        "brackets, clamps and threaded rods, all in mismatched flat filament colours with "
        "visible horizontal 3D-printed layer striations. Catwalks and gantries thread "
        "between the moving parts. Everything is in slow constant motion. Steam and vapour "
        "vent from gaps in the machinery. The floor far below is wet and reflective. Cyan "
        "industrial glow from above, sodium-vapour orange practical lights at ground level, "
        "hard light from camera right, deep teal shadow, slick reflections everywhere."
    ),
    "WP-gearhaven-street": (
        "ENVIRONMENT: a narrow wet street at the base of an industrial city of working "
        "printed plastic machinery, flanked by turning gears and hissing vents. The ground "
        "is a slick reflective wet plastic surface throwing back the light. Boxy industrial "
        "printed mech figures move unhurriedly through the street on visible printed gears "
        "and pin joints, each a different flat filament colour with visible horizontal layer "
        "striations. Sodium-vapour orange practicals on the walls, cyan glow from high "
        "above, hard key light from camera right, steam drifting at ankle height."
    ),
    "WP-gearhaven-archive": (
        "ENVIRONMENT: the interior of an immense cathedral-like archive, hundreds of feet "
        "tall, walled floor to ceiling on every side with narrow shelving slots stretching "
        "up into darkness — tens of thousands of slots, each holding one single small "
        "printed plastic object. Rolling ladders and cantilevered gantries run along the "
        "shelf faces. Dust hangs in the still air. A vast open floor of polished dark "
        "plastic below. Shafts of cyan light fall from unseen windows far above, with warm "
        "sodium practicals glowing at the base of the shelves. Hard key from camera right, "
        "immense scale, deep shadow between the stacks."
    ),
    "WP-gearhaven-firstslot": (
        "ENVIRONMENT: a single archive shelving slot in extreme close-up, at the very "
        "bottom of an enormous wall of identical slots, lit by one warm practical light. "
        "The slot is empty except for a thin layer of dust and a faint clean outline on the "
        "shelf surface where an object stood for a very long time and is no longer there. "
        "Cyan rim light from above."
    ),
    "WP-bin-wide": (
        "ENVIRONMENT: an immense dim cavern far beneath the world, its floor a vast deep "
        "drift of discarded broken printed plastic — warped and curled bases, snapped "
        "lattice supports, figures missing limbs, shapes that stop abruptly mid-layer, "
        "models printed at the wrong scale, and tangled fused clumps of collapsed melted "
        "strands, piled hundreds of feet deep and receding into darkness in every "
        "direction. Far, far overhead a single narrow shaft of pale cold light falls from "
        "an impossible height and strikes the drift in one small circle. Everything else is "
        "near-monochrome charcoal darkness with faint bounce light. Enormous scale, "
        "enormous emptiness, drifting dust."
    ),
    "WP-bin-drift": (
        "ENVIRONMENT: close on the surface of a deep drift of discarded broken printed "
        "plastic objects underfoot — warped bases, snapped struts, half-built limbs, fused "
        "tangled clumps, all in filament colours drained nearly to grey by the darkness, "
        "with visible horizontal 3D-printed layer striations catching the faint light. The "
        "pile is unstable and slides. Near-monochrome charcoal, one faint pale light source "
        "from very far above, deep shadow."
    ),
    "WP-bin-lost": (
        "ENVIRONMENT: a gathering of broken and half-built printed plastic figures standing "
        "quietly in near-darkness on a drift of discarded material — figures missing arms "
        "and legs, models with warped curled-up bases, shapes that simply stop mid-layer, "
        "things built at the wrong scale. They are not hostile or frightening; they stand "
        "gently and still, watching, waiting. Their filament colours are drained almost to "
        "grey. Near-monochrome charcoal, a single distant pale shaft of light from far "
        "above, faint rim light on their edges."
    ),
    "WP-bin-shaft": (
        "ENVIRONMENT: the base of a single narrow shaft of pale cold light falling from an "
        "impossible height into an immense dark cavern, striking a drift of broken printed "
        "plastic in one small bright circle on the ground. Dust drifts slowly through the "
        "beam. The darkness beyond the circle is total. Near-monochrome, extreme contrast "
        "between the lit circle and the black."
    ),
    "WP-smooth-void": (
        "ENVIRONMENT: a landscape that has been rendered completely blank — hills, "
        "buildings and ground still recognisable in shape but all of it flat featureless "
        "matte white with no colour, no texture, no layer lines, no visible edges and no "
        "shadows anywhere. Blown-out flat white void with the faintest lilac gradient in "
        "place of a horizon. No key light direction, no rim light, no cast shadow, no "
        "atmospheric depth. Objects are legible only by the faintest tonal separation. "
        "Empty, silent, wrong."
    ),
    "WP-smooth-finished-crowd": (
        "ENVIRONMENT: a blown-out flat white void of blank featureless landscape, filled "
        "with hundreds of blank white motionless figures of every shape and size standing "
        "frozen mid-gesture where they were caught — arms half raised, mid-stride, heads "
        "turned as if about to speak. All completely smooth with no colour, no layer lines "
        "and no features. No shadows, no rim light, no separation between the figures and "
        "the ground. Absolute stillness, receding into white haze."
    ),
    "WP-smooth-edge": (
        "ENVIRONMENT: the advancing boundary of the blankness, seen from ground level — on "
        "one side a warm richly coloured landscape of printed plastic structures with "
        "visible horizontal layer striations, deep teal shadows and warm rim light; on the "
        "other side the same landscape rendered flat featureless matte white with no "
        "colour, no texture and no shadow. Between them a hard clean edge cutting across "
        "the ground and up through the buildings, where colour, texture and shadow all "
        "simply stop mid-object."
    ),
    "WP-smooth-colour-return": (
        "ENVIRONMENT: a blown-out flat white blank landscape into which colour is flooding "
        "back in a spreading wave from the outer edges inward — warm amber, deep plum, "
        "cobalt and orange washing across the blankness, horizontal 3D-printed layer "
        "striations reappearing across every surface as the colour reaches it, shadows "
        "returning, warm rim light returning. Ahead of the wave the world is still flat "
        "dead white; behind it everything is saturated and textured and alive again. "
        "Hundreds of small newly-made lopsided printed objects scattered across the ground "
        "where the colour has already passed."
    ),
}


# ---------------------------------------------------------------- world state

HAND = {
    "building": (
        "On the far horizon a colossal nozzle hangs from the sky, patiently laying down "
        "glowing molten lines of light, building something enormous one visible layer at a "
        "time."
    ),
    "stopped": (
        "On the far horizon a colossal nozzle hangs motionless and dark from the sky, "
        "frozen mid-line, a half-finished glowing shape cooling beneath it."
    ),
    "restarted": (
        "On the far horizon the colossal nozzle moves again, laying down a bright new line "
        "of molten light."
    ),
}

SMOOTH_HORIZON = {
    25: (
        "On the distant horizon a thin hard line of pure flat white where the landscape "
        "simply stops having colour or texture."
    ),
    50: (
        "Across the far half of the landscape everything has gone blank flat white and "
        "featureless, meeting the coloured world at a hard clean edge."
    ),
    75: (
        "Most of the visible landscape is blank flat shadowless white, the last band of "
        "colour and texture squeezed into the near foreground."
    ),
}


def smooth_phrase(value: int) -> str | None:
    """Nearest defined horizon phrase for a 0-100 coverage value."""
    if value <= 0:
        return None
    tier = min(SMOOTH_HORIZON, key=lambda t: abs(t - value))
    return SMOOTH_HORIZON[tier]


CROWD = (
    "A crowd of printed plastic objects at wildly mismatched scales, each a different "
    "single flat filament colour, all with visible horizontal 3D-printed layer striations."
)

KIT_STATES = {
    "wet": "His hoodie is soaked dark and dripping wet, his hair flattened and damp.",
    "stained": (
        "A wide streak of dried teal material stains his right sleeve and hoodie pocket."
    ),
    "damaged": (
        "Grey dust covers his clothes, his right knee is scraped raw, and his bag strap "
        "is torn and re-knotted."
    ),
    "glowing": (
        "His hands glow faintly amber with wisps of light trailing from his fingertips."
    ),
}

SMOOTHING_FX = (
    "Its printed layer striations dissolve into a glassy featureless surface, colour "
    "draining from the extremities inward toward the centre, features softening and "
    "sealing over into blank white, motion slowing to a complete stop mid-gesture."
)
