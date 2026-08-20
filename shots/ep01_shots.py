"""FIRST LAYER — Episode 01 shot list. 86 shots, 605s (10:05).

Source of truth for the shot list. Run `python production/build_prompts.py` to expand
into paste-ready prompt files, the CSV tracker, and the human-readable sequence cards.

Field reference
---------------
id        SH-###
seq       sequence number
dur       5 or 10 ONLY (bible/03 rule 1)
tool      seedance | higgsfield
plate     key into blocks.PLATES
chars     ordered list of keys into blocks.CHARACTERS
lens      18mm | 35mm | 50mm | 85mm | macro
move      one move only, never two
height    toy | eye | high | ground | n/a
action    what happens. Shot-specific prompt text.
lines     dialogue line IDs from script/ep01-script.md
chain     shot id whose LAST FRAME becomes this shot's FIRST FRAME, or None
firstlast True if this shot needs both a first and a last keyframe
dir       L>R | R>L | static | down | up
smooth    0-100 Smooth horizon coverage. MUST be non-decreasing from SH-055.
hand      building | stopped | restarted | None
kit_state wet | stained | damaged | glowing | None
extra     any additional prompt phrases
note      production note for the human
"""

SEQUENCES = {
    1: ("THE BEDROOM", "WP-bedroom-night", "key: hot orange camera-right, cool blue camera-left"),
    2: ("THE RAFT — ARRIVAL", "WP-raft-wide", "key: honey-gold camera-left"),
    3: ("THE RAFT — THE CROWNING", "WP-raft-plaza", "key: honey-gold camera-left"),
    4: ("DINO BASIN", "WP-basin-wide", "key: hard rust-orange camera-left"),
    5: ("GEARHAVEN", "WP-gearhaven-wide", "key: cyan/sodium camera-RIGHT — the key flips here, deliberately"),
    6: ("THE DEEP BIN", "WP-bin-wide", "key: single pale shaft from directly above"),
    7: ("THE SMOOTH", "WP-smooth-void", "NO key, NO rim, NO shadow — the law breaks here"),
    8: ("THE BEDROOM — RETURN", "WP-bedroom-return", "key: identical to Seq 01, plus dawn"),
}

SHOTS = [
    # ============================================================ SEQ 01 — 95s
    dict(id="SH-001", seq=1, dur=5, tool="seedance", plate="WP-bedroom-chamber", chars=[],
         lens="macro", move="locked off", height="n/a", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="A brass nozzle lays down one single glowing line of molten material across a glass bed, left to right. The line cools from bright amber to solid colour behind it. Nothing else moves.",
         extra="Extreme shallow depth of field. The glowing line is the only bright thing in frame.",
         note="COLD OPEN. First frame of the film. The stepper-motor melody starts here."),

    dict(id="SH-002", seq=1, dur=10, tool="seedance", plate="WP-bedroom-night", chars=["KIT"],
         lens="35mm", move="slow pull out", height="eye", dir="static", smooth=0, hand=None,
         chain="SH-001", firstlast=True, kit_state=None, lines=[],
         action="Pulling back and out through the printer's chamber glass to reveal the whole bedroom: Kit hunched at the desk, lit hard orange from the printer on his right and cool blue from the window on his left, absorbed in the screen in front of him.",
         extra="A small blank white featureless figurine sits half-buried among the pens in the pen cup on the desk, clearly visible but not emphasised in any way.",
         note="THE PLANT. The figurine must be readable in this frame. Do not light it specially, do not centre it. This keyframe is also the source for SH-084 — save it."),

    dict(id="SH-003", seq=1, dur=5, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="50mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Over Kit's shoulder onto the screen: a detailed robot dog model rotating slowly in a 3D modelling program, wireframe over solid.",
         extra="Screen glow on his face and shoulder. No readable text or UI anywhere on the screen.",
         note="No text in frame — models will try to add UI labels. Reject any with legible type."),

    dict(id="SH-004", seq=1, dur=10, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Close on Kit working: eyes flicking, jaw set, hands moving fast and loose and confident. He is completely absorbed and he is very good at this. He does not speak.",
         extra="Warm screen light on his face. Small unconscious movements — he mouths something, tilts his head.",
         note="THE MOST IMPORTANT SHOT IN SEQ 01. This is where the audience banks that he has real talent, which is the only thing keeping him likeable for the next nine minutes. Do not shorten it."),

    dict(id="SH-005", seq=1, dur=5, tool="seedance", plate="WP-bedroom-night", chars=[],
         lens="macro", move="lateral track", height="n/a", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Macro tracking across the wall above the desk: pinned-up pencil sketches of robots and machines, beautifully drawn, every single one stopping mid-line into blank paper.",
         extra="Shallow focus travelling across the drawings. Cool blue window light.",
         note="Character established without a word. The drawings must be visibly GOOD — that's the point."),

    dict(id="SH-006", seq=1, dur=5, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="50mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-001", "L-002"],
         action="Kit leans back in his chair, satisfied, and stretches. He is talking to a phone propped against the pen cup.",
         extra="The small blank white figurine is visible in the pen cup beside the phone.",
         note="PLANT reinforcement. Tier A lipsync."),

    dict(id="SH-007", seq=1, dur=10, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="50mm", move="handheld follow", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-003", "L-004", "L-005", "L-006", "L-007", "L-008", "L-009", "L-010"],
         action="Kit talking, animated, gesturing with both hands, completely certain — and then the certainty leaks out of him on the last line and he goes still.",
         extra="He is selling hard for eight seconds and then he isn't.",
         note="Tier A lipsync. The performance turn at L-010 is the whole shot."),

    dict(id="SH-008", seq=1, dur=5, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="35mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Kit reaches down without looking and pulls open the desk drawer beside his knee.",
         extra="",
         note="Chain the last frame into SH-009."),

    dict(id="SH-009", seq=1, dur=5, tool="seedance", plate="WP-bedroom-drawer", chars=[],
         lens="35mm", move="slow push in", height="high", dir="static", smooth=0, hand=None,
         chain="SH-008", firstlast=False, kit_state=None, lines=[],
         action="Looking straight down into the open drawer. Forty abandoned half-built robot dogs. Nothing in it is finished.",
         extra="",
         note="THE DRAWER. One shot, no dialogue, entire character. Do not cut away early."),

    dict(id="SH-010", seq=1, dur=5, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="85mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-011", "L-012"],
         action="Kit's face, lit from below by the open drawer. He closes it with his foot without looking at it, and hangs up the phone.",
         extra="",
         note="Tier A lipsync."),

    dict(id="SH-011", seq=1, dur=10, tool="higgsfield", plate="WP-bedroom-night", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-013"],
         action="Kit alone in a silent room, looking at the screen. His hand rests on the mouse and does not move. For three full seconds he is visibly, quietly frightened. Then he breathes out and says one word.",
         extra="Very still. Almost no motion in frame at all.",
         note="THE SHOT THAT MAKES HIM LIKEABLE. Under no circumstances cut this for time. Tier A lipsync."),

    dict(id="SH-012", seq=1, dur=5, tool="seedance", plate="WP-bedroom-chamber", chars=[],
         lens="macro", move="locked off", height="n/a", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-014"],
         action="The printer chamber lights up warm orange from the inside. The bed shifts. The nozzle moves into position and begins to lay down the first layer.",
         extra="",
         note="L-014 plays over this shot — Kit off-screen. Tier C."),

    dict(id="SH-013", seq=1, dur=10, tool="seedance", plate="WP-bedroom-night", chars=["KIT"],
         lens="35mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=True, kit_state=None, lines=[],
         action="Kit leans in close to the chamber glass to watch. The chamber light pulses once, brightly. His sneakers dissolve into a lattice of glowing horizontal lines, then his shins — he looks down, then up — and he is drawn upward into the machine layer by layer from the feet up until he is gone.",
         extra="The dissolve reads as un-printing: he comes apart into stacked glowing horizontal lines that rise and vanish. Ben-Day halftone dot texture in the shadow areas.",
         note="THRESHOLD. The hardest VFX shot in Seq 01 — author both keyframes. The blank white figurine is visible in the pen cup throughout."),

    dict(id="SH-014", seq=1, dur=5, tool="seedance", plate="WP-bedroom-night", chars=[],
         lens="35mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain="SH-013", firstlast=False, kit_state=None, lines=[],
         action="The empty chair, still turning slightly. The printer runs on. Nobody is there.",
         extra="The blank white figurine sits in the pen cup.",
         note="Hold the silence. Cut to SEQ 02 on the printer sound bridging into the river."),

    # ============================================================ SEQ 02 — 110s
    dict(id="SH-015", seq=2, dur=5, tool="seedance", plate="WP-raft-river", chars=["KIT"],
         lens="35mm", move="slow pull out", height="n/a", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=[],
         action="Submerged inside the warm glowing river, looking up toward a distorted amber surface. Kit is suspended in it, turning slowly, silhouetted against the light above.",
         extra="Thick, warm, slow, muffled. Everything is amber.",
         note="Sound: heavily filtered. The printer motif from SH-014 bridges into here."),

    dict(id="SH-016", seq=2, dur=5, tool="seedance", plate="WP-raft-dock", chars=["KIT"],
         lens="35mm", move="handheld follow", height="toy", dir="L>R", smooth=0, hand=None,
         chain="SH-015", firstlast=False, kit_state="wet", lines=[],
         action="Kit breaks the surface, gasping, and hauls himself up onto the plank dock, dripping glowing material that cools on the boards.",
         extra="",
         note="Camera at toy height from here on — establish the grammar immediately."),

    dict(id="SH-017", seq=2, dur=5, tool="seedance", plate="WP-raft-dock", chars=["BENCHY"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-015"],
         action="A small weathered tugboat sits in the river a few feet away, watching. His porthole glows as he speaks.",
         extra="",
         note="BENCHY first appearance. Tier C — porthole glow only, no mouth."),

    dict(id="SH-018", seq=2, dur=5, tool="higgsfield", plate="WP-raft-dock", chars=["KIT"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=["L-016", "L-017"],
         action="Kit on his hands and knees, coughing, having already swallowed a great deal of the river. He looks up, confused, then looks at the glowing material dripping off his chin.",
         extra="",
         note="The joke is entirely in the timing of the cut. Tier A lipsync."),

    dict(id="SH-019", seq=2, dur=10, tool="seedance", plate="WP-raft-wide", chars=["KIT"],
         lens="18mm", move="crane up reveal", height="toy", dir="static", smooth=0, hand="building",
         chain=None, firstlast=True, kit_state="wet", lines=[],
         action="Kit stands and turns around. The camera cranes up and back off the dock to reveal the full width of the Raft opening out in front of him — the shanty-city running to the horizon.",
         extra="Kit is a small figure at the bottom of frame, dwarfed. Honey-gold light. Hold on the scale.",
         note="THE REVEAL. The single most important image in the film for making the world feel worth saving. Generate this one many times and pick the best. No dialogue."),

    dict(id="SH-020", seq=2, dur=5, tool="seedance", plate="WP-raft-wide", chars=[],
         lens="35mm", move="lateral track", height="toy", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Tracking laterally across the city — leaning scaffold towers, walkways crowded with tiny figures going about their business, glowing canals running underneath.",
         extra="Nobody in frame is looking at camera. Everybody is busy.",
         note="WONDER DISCIPLINE: the world was here first and does not care that he arrived."),

    dict(id="SH-021", seq=2, dur=5, tool="higgsfield", plate="WP-raft-dock", chars=["KIT"],
         lens="85mm", move="slow push in", height="ground", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=[],
         action="Extreme low angle looking steeply up at Kit as he tips his head back to look at the sky. Awe, not fear.",
         extra="",
         note="The signature Kit angle. Reference image 1d-1 from turnarounds.md."),

    dict(id="SH-022", seq=2, dur=5, tool="seedance", plate="WP-raft-wide", chars=[],
         lens="18mm", move="slow push in", height="ground", dir="up", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Straight up: the sky is the vast wooden underside of an enormous desk, impossibly far above, with thick cables hanging down through the golden haze like weather systems.",
         extra="",
         note="Newcomers read this as a strange beautiful sky. It should be legible as a desk on the second watch, not the first."),

    dict(id="SH-023", seq=2, dur=10, tool="seedance", plate="WP-raft-wide", chars=[],
         lens="18mm", move="slow push in", height="toy", dir="static", smooth=0, hand="building",
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="The horizon. The Hand — a colossal nozzle suspended from nothing — patiently laying down glowing lines, building something vast and unrecognisable, one layer at a time. In the foreground, silhouetted, dozens of small figures on the walkways have stopped to watch it.",
         extra="",
         note="MYSTERY BOX POSED. Everybody watches it the way people watch weather. Nobody explains it."),

    dict(id="SH-024", seq=2, dur=5, tool="higgsfield", plate="WP-raft-dock", chars=["KIT"],
         lens="85mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=["L-018"],
         action="Kit's face. Pure delight. He is the only person in film history to fall into another dimension and immediately start thinking about who he can talk to.",
         extra="",
         note="Tier A lipsync. Delight, NOT fear — this is a key character choice."),

    dict(id="SH-025", seq=2, dur=5, tool="higgsfield", plate="WP-raft-market", chars=["KIT"],
         lens="35mm", move="handheld follow", height="toy", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=["L-019"],
         action="Kit strides up to the nearest stranger — a living keychain the size of a wardrobe — with his hands already out, mid-pitch.",
         extra="",
         note="Tier A lipsync."),

    dict(id="SH-026", seq=2, dur=5, tool="higgsfield", plate="WP-raft-market", chars=["KIT"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="wet", lines=["L-020"],
         action="Kit, delivering the worst sentence in the language with total warmth and an enormous smile.",
         extra="",
         note="Tier A lipsync. Play it entirely innocent."),

    dict(id="SH-027", seq=2, dur=10, tool="seedance", plate="WP-raft-market", chars=[],
         lens="35mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Every single object in the market street has stopped and turned to look at camera. Total silence. In the middle distance a stall-holder quietly begins to cry.",
         extra=("A crowd of printed plastic objects at wildly mismatched scales, each a different "
                "single flat filament colour, all with visible horizontal 3D-printed layer "
                "striations, all completely motionless and staring directly at camera."),
         note="Hold the full ten seconds. The longer it runs the funnier and the more unsettling it gets."),

    dict(id="SH-028", seq=2, dur=5, tool="seedance", plate="WP-raft-dock", chars=["BENCHY"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-021", "L-022", "L-023"],
         action="Benchy, level in the water, porthole glowing. He does not elaborate.",
         extra="",
         note="Tier C."),

    dict(id="SH-029", seq=2, dur=10, tool="seedance", plate="WP-raft-dock", chars=["KIT", "BENCHY"],
         lens="35mm", move="locked off", height="toy", dir="static", smooth=0, hand="building",
         chain=None, firstlast=False, kit_state="wet", lines=["L-024", "L-025", "L-026", "L-027", "L-028", "L-029", "L-030"],
         action="Two-shot on the dock. Benchy noses in against the boards and lays out the rule four words at a time. On the last exchange he tilts to indicate the Hand on the far horizon, and Kit turns to look at it.",
         extra="",
         note="THE PREMISE, delivered in nine seconds. Benchy Tier C, Kit's reactions Tier B — stay wide, cut to his face only after."),

    dict(id="SH-030", seq=2, dur=5, tool="seedance", plate="WP-raft-market", chars=[],
         lens="35mm", move="lateral track", height="toy", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="A procession of two dozen identical small printed figures moves through the market carrying one single enormous key above their heads, chanting.",
         extra="",
         note="UNEXPLAINED THING 1. Never acknowledged, never explained, never returned to."),

    dict(id="SH-031", seq=2, dur=5, tool="seedance", plate="WP-raft-market", chars=[],
         lens="35mm", move="lateral track", height="toy", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="A stall ladling cups of glowing river material to a long patient queue. Behind it, two colossal gears are having an argument we join too late and leave too early.",
         extra="",
         note="UNEXPLAINED THINGS 2 and 3."),

    dict(id="SH-032", seq=2, dur=10, tool="seedance", plate="WP-raft-market", chars=["KIT"],
         lens="18mm", move="crane up reveal", height="toy", dir="L>R", smooth=0, hand="building",
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="Kit walks away from camera into the enormous market street, very small, grinning like an idiot. The camera cranes up over him. Off to one side, a door stands freely in the middle of a plaza with a queue of people waiting to walk through it, opening onto nothing.",
         extra="",
         note="UNEXPLAINED THING 4. End of the wonder sequence. Kit's hoodie has now dried to the stained state — this is the STATE CHANGE shot."),

    # ============================================================ SEQ 03 — 85s
    dict(id="SH-033", seq=3, dur=10, tool="seedance", plate="WP-raft-market", chars=["TOWER", "KIT"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-031", "L-032", "L-033", "L-034", "L-035", "L-036"],
         action="A stack of ten blocks topples into frame and restacks itself in front of Kit. Different horizontal slots light up as different layers speak, interrupting each other constantly.",
         extra="Individual horizontal front slots on the stack glow warmly one at a time and sometimes several at once as each layer speaks.",
         note="THE TOWER, first appearance. Tier C entirely — glow animation is a post pass, never a model dependency. Count the blocks: exactly ten."),

    dict(id="SH-034", seq=3, dur=5, tool="seedance", plate="WP-raft-market", chars=["TOWER"],
         lens="50mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain="SH-033", firstlast=False, kit_state=None, lines=["L-037", "L-038", "L-039", "L-040"],
         action="Closer on the stack. The upper sagging blocks glow in turn. The topmost melted blob does not speak.",
         extra="",
         note="Tier C. Layer 5's line lands because it comes out of a block that has been asleep."),

    dict(id="SH-035", seq=3, dur=10, tool="higgsfield", plate="WP-raft-market", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=True, kit_state="stained", lines=[],
         action="Kit, bored, waiting out the argument, has absently taken the thick red marker from behind his ear and is doodling in the air. The line he draws GLOWS and then BUILDS — extruding into existence along the exact path his hand travelled, cooling into a small crooked solid object that drops into his palm.",
         extra=("A hot amber trail follows the marker tip and cools into solid material. Ben-Day "
                "halftone dot texture blooms in the shadow areas around his hand."),
         note="THE PENCIL. Author both keyframes — start on the empty gesture, end on the object in his palm. Permitted Spider-Verse device (halftone), 1 of 12."),

    dict(id="SH-036", seq=3, dur=5, tool="higgsfield", plate="WP-raft-market", chars=["KIT"],
         lens="85mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain="SH-035", firstlast=False, kit_state="stained", lines=[],
         action="Kit stops dead. He looks at the small crooked object in his palm, then up, then back down at it.",
         extra="",
         note="No dialogue. Let him figure it out on camera."),

    dict(id="SH-037", seq=3, dur=5, tool="seedance", plate="WP-raft-market", chars=["TOWER"],
         lens="35mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-041", "L-042"],
         action="The entire street has stopped. Every object is staring at Kit's hand. Two slots on the Tower glow in turn.",
         extra="Every printed object in the street is motionless and staring at the same point off-camera.",
         note="Tier C."),

    dict(id="SH-038", seq=3, dur=10, tool="seedance", plate="WP-raft-plaza", chars=["KIT", "BENCHY"],
         lens="18mm", move="crane up reveal", height="toy", dir="static", smooth=0, hand="building",
         chain=None, firstlast=False, kit_state="stained", lines=["L-043", "L-044", "L-045"],
         action="Hard cut to chaos: Kit up on the plinth in the plaza with several hundred small objects packed onto every balcony and walkway around him, screaming. Somebody has put something on his head. The camera cranes up to reveal the scale of the crowd.",
         extra=("Crowds of printed plastic objects at wildly mismatched scales, each a different "
                "single flat filament colour, packed onto scaffold balconies at every level."),
         note="THE CROWNING. Benchy's line L-045 is thrown away flat under the noise — Tier C, off-screen."),

    dict(id="SH-039", seq=3, dur=10, tool="higgsfield", plate="WP-raft-plaza", chars=["KIT"],
         lens="35mm", move="slow push in", height="ground", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-046", "L-047"],
         action="Low angle looking steeply up at Kit on the plinth with both hands raised, backlit honey-gold, in full flight. The biggest, most charming, most completely unbacked speech of his life.",
         extra="",
         note="THE REFUSAL, disguised as a triumph — he takes the crown instead of the job. Tier A lipsync, and give the actor room to be genuinely funny."),

    dict(id="SH-040", seq=3, dur=5, tool="seedance", plate="WP-raft-plaza", chars=["JUNE"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-048"],
         action="A single flat voice from the front of the crowd. June, two feet tall, standing perfectly still while everything around her cheers.",
         extra="",
         note="JUNE first appearance. RULE 12 — her hollow wireframe side is on FRAME RIGHT when she faces camera. Tier B."),

    dict(id="SH-041", seq=3, dur=10, tool="seedance", plate="WP-raft-plaza", chars=["JUNE", "KIT"],
         lens="35mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-049", "L-050", "L-051"],
         action="The crowd parts around her. June steps forward into clear space and the light goes through the empty half of her body. She looks at Kit for about a second longer than is comfortable, and says it again.",
         extra="Backlight passing cleanly through the hollow wireframe half of her body so it reads as genuinely empty.",
         note="Her full reveal. The backlight through the empty half is the shot. Tier B."),

    dict(id="SH-042", seq=3, dur=5, tool="higgsfield", plate="WP-raft-plaza", chars=["KIT"],
         lens="85mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="Kit, still up on the plinth with his hands half raised. He does not argue. He goes quiet.",
         extra="",
         note="No dialogue. Everyone in the audience recognises this silence — that recognition is the whole shot."),

    dict(id="SH-043", seq=3, dur=10, tool="seedance", plate="WP-raft-plaza", chars=["KIT", "BENCHY"],
         lens="18mm", move="crane up reveal", height="toy", dir="static", smooth=0, hand="stopped",
         chain=None, firstlast=True, kit_state="stained", lines=["L-052", "L-053"],
         action="Every sound in the world stops at once. Every single object in the plaza turns and looks at the horizon at the same moment. The Hand hangs motionless and dark, frozen mid-line, a half-finished shape cooling beneath it.",
         extra="",
         note=("THE HAND STOPS. Hard mid-point of the film. Audio: cut EVERYTHING, including the "
               "stepper-motor motif, which does not return until SH-081. Author both keyframes — "
               "start on the crowd cheering, end on total stillness.")),

    # ============================================================ SEQ 04 — 85s
    dict(id="SH-044", seq=4, dur=10, tool="seedance", plate="WP-basin-riverbed", chars=["KIT", "JUNE", "TOWER"],
         lens="35mm", move="lateral track", height="toy", dir="L>R", smooth=0, hand="stopped",
         chain=None, firstlast=False, kit_state="stained", lines=["L-054", "L-055", "L-056", "L-057", "L-058", "L-059", "L-060", "L-061", "L-062"],
         action="The group moves left to right along the dry riverbed: Kit and June ahead, the Tower toppling and restacking at the back, struggling to keep up. Walk and talk.",
         extra="Drifting rust-coloured dust, heat haze along the ground.",
         note="Mostly Tier C — keep the camera wide and let the dialogue play over the walk. June's L-061 kills the conversation dead."),

    dict(id="SH-045", seq=4, dur=5, tool="seedance", plate="WP-basin-riverbed", chars=["COLOSSUS"],
         lens="35mm", move="handheld follow", height="ground", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Something is catching up, fast. Colossus drags himself along the riverbed on two front legs at astonishing speed, thrilled, throwing up dust. He emits a two-tone rising boot-up chime.",
         extra="",
         note=("COLOSSUS first appearance and SETUP 1 of 3. RULE 11 — he has NO back half in this "
               "shot or any other. Check the frame. Sound: boot-up chime, never a complete bark.")),

    dict(id="SH-046", seq=4, dur=5, tool="higgsfield", plate="WP-basin-riverbed", chars=["KIT", "JUNE"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-063", "L-064", "L-065"],
         action="June looks at the dog, then at Kit. Kit does not look at the dog at all. June's reply is one word and she holds his eye while she says it.",
         extra="",
         note="Kit's first lie. Kit Tier A, June Tier B."),

    dict(id="SH-047", seq=4, dur=10, tool="seedance", plate="WP-raft-river", chars=["KIT", "BENCHY"],
         lens="50mm", move="locked off", height="toy", dir="L>R", smooth=0, hand="stopped",
         chain=None, firstlast=False, kit_state="stained", lines=["L-066", "L-067", "L-068"],
         action="On the river. Benchy carries them downstream. Kit sits at the bow with his back to everyone, looking ahead. Benchy's porthole glows behind him. Neither of them looks at the other.",
         extra="",
         note=("THE THEME, stated once, and never referenced again. Do NOT cut to Kit's face at any "
               "point in this shot — we do not check whether he heard it. Tier C.")),

    dict(id="SH-048", seq=4, dur=10, tool="seedance", plate="WP-basin-herd", chars=["KIT", "JUNE"],
         lens="18mm", move="handheld follow", height="ground", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="Inside the herd. Enormous columnar dinosaur legs stride past on every side, throwing up billowing dust, while Kit and June run between them. Shafts of hard orange light break through the gaps between the bodies.",
         extra="Single-frame graphic impact burst with hard-edged shapes and chromatic offset as an enormous foot lands close to camera.",
         note="THE HERD. The most purely fun ten seconds in the film. Permitted Spider-Verse device (impact frame), 2 of 12."),

    dict(id="SH-049", seq=4, dur=5, tool="seedance", plate="WP-basin-riverbed", chars=["KIT", "JUNE", "TOWER"],
         lens="35mm", move="lateral track", height="toy", dir="L>R", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="A wide crack in the ground. Kit clears it easily. June clears it one-handed. The Tower topples across it and restacks on the far side.",
         extra="",
         note="Chain the last frame into SH-050."),

    dict(id="SH-050", seq=4, dur=10, tool="seedance", plate="WP-basin-riverbed", chars=["COLOSSUS", "KIT"],
         lens="50mm", move="locked off", height="ground", dir="static", smooth=0, hand=None,
         chain="SH-049", firstlast=False, kit_state="stained", lines=[],
         action="Colossus reaches the edge of the crack and cannot make it. He scrabbles at the lip with his two front legs and stops. He makes a broken-off attempt at a bark that never completes. Kit, on the far side, slows. Almost turns back. Doesn't. Walks on.",
         extra="",
         note=("SETUP 2 of 3, and the cruellest shot in act two. The bark MUST cut off halfway — a "
               "complete bark is not permitted anywhere before SH-080.")),

    dict(id="SH-051", seq=4, dur=5, tool="seedance", plate="WP-basin-riverbed", chars=["JUNE"],
         lens="85mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="June, stopped, watching Kit not turn back. She says nothing at all.",
         extra="",
         note="No dialogue. She logs it. This is the shot that makes her later verdict land."),

    dict(id="SH-052", seq=4, dur=5, tool="seedance", plate="WP-basin-wide", chars=["KIT", "JUNE", "TOWER"],
         lens="35mm", move="slow push in", height="toy", dir="L>R", smooth=0, hand="stopped",
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="The group crests a ridge — and stops dead. Reverse on their faces as they see what is below.",
         extra="",
         note="Chain the last frame into SH-053. Cut all ambient sound at the top of this shot."),

    dict(id="SH-053", seq=4, dur=10, tool="seedance", plate="WP-basin-finished-village", chars=[],
         lens="18mm", move="slow push in", height="toy", dir="static", smooth=25, hand=None,
         chain="SH-052", firstlast=False, kit_state=None, lines=[],
         action="The settlement below. Dozens of blank white motionless figures standing in the streets and doorways, frozen mid-gesture. Dust has drifted against their feet. Nothing moves at all.",
         extra="",
         note=("THE FIRST HORROR BEAT. Ten seconds, no dialogue, no music, no ambience. Play it "
               "completely straight. If it reads as scary rather than desolate, regenerate.")),

    dict(id="SH-054", seq=4, dur=5, tool="seedance", plate="WP-basin-finished-village", chars=[],
         lens="85mm", move="slow push in", height="toy", dir="static", smooth=25, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-069"],
         action="Close on one blank white figure, caught with one arm half raised and its head turned as if it had been about to speak.",
         extra="",
         note="Layer 3's single quiet line plays over this. Tier C."),

    dict(id="SH-055", seq=4, dur=5, tool="seedance", plate="WP-basin-wide", chars=["KIT", "JUNE", "TOWER"],
         lens="18mm", move="slow pull out", height="toy", dir="L>R", smooth=25, hand="stopped",
         chain=None, firstlast=False, kit_state="stained", lines=[],
         action="The group very small at the bottom of frame, walking away from the settlement. The camera pulls back to reveal, on the far horizon behind them, a thin hard line of pure flat white.",
         extra="",
         note=("THE CLOCK STARTS. From this shot onward the Smooth horizon appears in every "
               "exterior and NEVER retreats. Verify the smooth column is non-decreasing before "
               "generating any later batch.")),

    # ============================================================ SEQ 05 — 70s
    dict(id="SH-056", seq=5, dur=10, tool="seedance", plate="WP-gearhaven-wide", chars=[],
         lens="18mm", move="crane up reveal", height="toy", dir="L>R", smooth=30, hand="stopped",
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Gearhaven. Building-sized gears turning slowly against one another, chain drives running between towers, steam venting, everything in slow constant motion, the wet floor far below throwing back the light.",
         extra="",
         note="KEY FLIPS TO CAMERA RIGHT for this entire sequence. Deliberate — this is the turn."),

    dict(id="SH-057", seq=5, dur=10, tool="higgsfield", plate="WP-gearhaven-street", chars=["KIT"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=30, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-070", "L-071", "L-072", "L-073", "L-074", "L-075"],
         action="A counter. Behind it a boxy industrial mech that has not moved in some time. Kit talks, faster and faster, and gets the same single word back three times, and runs out of road.",
         extra="A boxy industrial printed mech figure behind a counter, moving on visible printed gears and pin joints, entirely still.",
         note="First real crack in him — his charm has worked on everything up to now. Kit Tier A, mech Tier C."),

    dict(id="SH-058", seq=5, dur=10, tool="seedance", plate="WP-gearhaven-street", chars=["TOWER"],
         lens="35mm", move="locked off", height="toy", dir="static", smooth=30, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-076", "L-077", "L-078", "L-079", "L-080", "L-081", "L-082", "L-083"],
         action="The Tower rolls up to the counter and argues with the bureaucracy using all ten of its layers simultaneously. Slots fire in rapid sequence. The mech gives way to Layer 7.",
         extra="Individual horizontal front slots on the stack glowing in rapid overlapping sequence.",
         note="BEST COMEDY SET PIECE IN THE FILM. Give it the full ten seconds and cut nothing. Tier C throughout — zero lipsync risk, which is exactly why we can afford it."),

    dict(id="SH-059", seq=5, dur=10, tool="seedance", plate="WP-gearhaven-archive", chars=["KIT", "JUNE"],
         lens="18mm", move="crane up reveal", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-084", "L-085", "L-086"],
         action="The Archive. The camera cranes up the face of the stacks — tens of thousands of shelf slots climbing into darkness, one small object in each — with Kit and June tiny at the bottom.",
         extra="",
         note="Interior — no Smooth horizon. Machine noise drops away to a huge dry acoustic. Tier C."),

    dict(id="SH-060", seq=5, dur=5, tool="seedance", plate="WP-gearhaven-archive", chars=["TOWER", "KIT"],
         lens="50mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-087", "L-088", "L-089"],
         action="Layer 1's slot glows. He states it twice, and the second time he changes one word.",
         extra="",
         note="THE HALF-ANSWER. Tier C."),

    dict(id="SH-061", seq=5, dur=5, tool="seedance", plate="WP-gearhaven-firstslot", chars=[],
         lens="macro", move="slow push in", height="n/a", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-090", "L-091", "L-092", "L-093", "L-094", "L-095", "L-096"],
         action="Slot one, at the very bottom of the stacks. Empty. Dust, and a clean outline on the shelf where something stood for a very long time and is no longer there.",
         extra="",
         note="The mystery half-turns here. All dialogue off-screen over the empty slot — Tier C, and much stronger for never cutting to a face."),

    dict(id="SH-062", seq=5, dur=5, tool="seedance", plate="WP-gearhaven-archive", chars=["JUNE", "COLOSSUS"],
         lens="85mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-097", "L-098"],
         action="June stands very still, looking out through a gap in the machinery at the frozen Hand. Behind her, Colossus drags something small and useless over and drops it at Kit's feet, and Kit picks it up without looking at him.",
         extra="",
         note="SETUP 3 of 3 for Colossus, played in the background of June's beat. June Tier B."),

    dict(id="SH-063", seq=5, dur=10, tool="seedance", plate="WP-gearhaven-archive", chars=["FINISHER", "KIT"],
         lens="35mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="stained", lines=["L-099", "L-100", "L-101", "L-102", "L-103", "L-104", "L-105", "L-106"],
         action="He is simply there, standing between the stacks. He does not approach. He speaks with genuine warmth and real affection, and on the fourth exchange Kit goes absolutely still.",
         extra="Heavy red and cyan chromatic offset at the frame edges. He has no rim light and casts no shadow, unlike everything else in the shot.",
         note=("THE FINISHER, first appearance. Tier A — but inverted: he has no mouth, so hold him "
               "completely static and let the warm voice do the work. Permitted Spider-Verse device "
               "(chromatic aberration), 3 of 12.")),

    dict(id="SH-064", seq=5, dur=5, tool="seedance", plate="WP-gearhaven-street", chars=["FINISHER"],
         lens="35mm", move="locked off", height="toy", dir="R>L", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-107"],
         action="He turns, unhurried, and walks away down the wet reflective street. In the far background of frame, one of the blank white figures very slightly turns its head.",
         extra="He casts no reflection on the wet floor while everything else does.",
         note=("The missing reflection is the detail people will rewatch for. The background figure "
               "turning its head is never acknowledged by any character and the camera does not "
               "push in on it.")),

    # ============================================================ SEQ 06 — 70s
    dict(id="SH-065", seq=6, dur=5, tool="seedance", plate="WP-bin-wide", chars=["KIT", "JUNE"],
         lens="18mm", move="slow push in", height="toy", dir="down", smooth=0, hand=None,
         chain=None, firstlast=True, kit_state="damaged", lines=[],
         action="Descending into the Deep Bin. The colour drains out of the film as they go down — saturation falling away shot by shot until almost nothing is left.",
         extra="",
         note=("Kit's STATE CHANGE to damaged happens here. Grade: this sequence runs at near-zero "
               "saturation, and it is starving the film on purpose so the colour return at SH-081 "
               "hits. Author both keyframes to control the desaturation ramp.")),

    dict(id="SH-066", seq=6, dur=5, tool="seedance", plate="WP-bin-lost", chars=[],
         lens="35mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=[],
         action="Figures come out of the dark. Broken, half-built, missing limbs. They stop at a polite distance, look, and stay. None of them want anything.",
         extra="",
         note=("THE BIN-LOST. Never stage them as a threat — no looming, no reaching, no crowding. "
               "If a take reads as scary rather than sad, it is wrong. Two of them must be visibly "
               "hand-designed originals like June, and one of them is looking at June.")),

    dict(id="SH-067", seq=6, dur=5, tool="seedance", plate="WP-bin-drift", chars=["KIT", "JUNE"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=["L-108", "L-109"],
         action="June sits down on the drift of discarded material. She does not elaborate.",
         extra="",
         note="June Tier B."),

    dict(id="SH-068", seq=6, dur=10, tool="seedance", plate="WP-bin-drift", chars=["JUNE"],
         lens="85mm", move="slow push in", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-110", "L-111", "L-112"],
         action="June, lit by the single distant shaft. She turns her heel toward the light. Stamped into the plum material: a maker's mark reading J U N I P E R, where only the first four letters have actually been built and the rest is a faint unbuilt outline trailing off into nothing.",
         extra="Macro insert on the maker's mark stamped into the heel, four letters raised in solid material and the remainder only a faint unbuilt outline.",
         note="The quietest and worst moment in the film. Tier B, and stay on the heel for the last line rather than her face."),

    dict(id="SH-069", seq=6, dur=5, tool="seedance", plate="WP-bin-drift", chars=["FINISHER", "COLOSSUS"],
         lens="50mm", move="locked off", height="ground", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-113", "L-114"],
         action="The Finisher is crouched down — the only time in the film he is not upright — in front of Colossus, at the little dog's eye level, speaking gently.",
         extra="",
         note=("The ONE permitted exception to his staging law. Everywhere else he is upright and "
               "still. Tier A, static.")),

    dict(id="SH-070", seq=6, dur=10, tool="higgsfield", plate="WP-bin-drift", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=["L-115", "L-116"],
         action="Kit gets the marker up. The tip glows. He starts a line — and stops. Erases it. Starts again from a different angle. Stops. His hand is shaking. He cannot pick which line to draw, so he draws none of them, and the half-begun shape hangs in the air, glowing and wrong.",
         extra="A faltering amber trail that starts, stops, is erased, and starts again, never completing. Ben-Day halftone dot texture in the shadow areas around his hand.",
         note=("HE FAILS BY DOING THE EXACT THING HE ALWAYS DOES. Not weakness — habit. This is the "
               "most important performance beat in the film. Kit Tier A. Permitted Spider-Verse "
               "device (halftone), 4 of 12.")),

    dict(id="SH-071", seq=6, dur=5, tool="seedance", plate="WP-bin-drift", chars=["COLOSSUS", "FINISHER"],
         lens="50mm", move="locked off", height="ground", dir="static", smooth=0, hand=None,
         chain=None, firstlast=True, kit_state=None, lines=[],
         action="The Finisher rests one long smooth hand on Colossus's head. The cobalt drains out of the little dog from his cut-off rear end inward. His layer lines dissolve. His amber eyes seal over into blank domes. He stops, mid-stride, with one front paw off the ground.",
         extra=("His printed layer striations dissolve into a glassy featureless surface, colour "
                "draining from the extremities inward toward the centre, features softening and "
                "sealing over into blank white, motion slowing to a complete stop mid-gesture."),
         note=("THE PAYOFF. Author both keyframes — start on full cobalt, end on the smoothed state. "
               "Audio: total silence, no sub, no ambience, nothing. From here to SH-079 Colossus is "
               "a statue and must not move a single frame.")),

    dict(id="SH-072", seq=6, dur=5, tool="seedance", plate="WP-bin-drift", chars=["TOWER_DAMAGED"],
         lens="35mm", move="locked off", height="toy", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-117"],
         action="Behind them the bottom four blocks of the Tower go white and dead. The stack settles by four blocks. Six glowing slots remain, and for the first time in the film none of them say anything at all. Then one does, quietly, to itself.",
         extra="",
         note="TOWER STATE CHANGE. Six glowing slots maximum from here to the end of the episode. Tier C."),

    dict(id="SH-073", seq=6, dur=5, tool="higgsfield", plate="WP-bin-drift", chars=["KIT"],
         lens="85mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=["L-118", "L-119", "L-120"],
         action="Kit on his knees in the drift. The half-drawn shape cools above him and falls apart into fragments.",
         extra="",
         note="Tier A."),

    dict(id="SH-074", seq=6, dur=10, tool="higgsfield", plate="WP-bin-drift", chars=["KIT", "JUNE"],
         lens="50mm", move="locked off", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=["L-121", "L-122", "L-123", "L-124", "L-125", "L-126"],
         action="Kit says it out loud, flat, to the one person in the universe it will hurt most. June does not comfort him. She stands up and gives him a deadline instead, and walks toward the light.",
         extra="",
         note=("THE ADMISSION. Kit's only slow scene in the film and it should be ugly, not pretty. "
               "June's answer is a deadline, not encouragement — if the read is warm, do it again. "
               "Kit Tier A, June Tier B.")),

    dict(id="SH-075", seq=6, dur=5, tool="higgsfield", plate="WP-bin-shaft", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=[],
         action="Kit alone in the dark. He looks at the thick red marker on the ground in front of him. He picks it up.",
         extra="",
         note="No dialogue. End of act two. Cut hard to white."),

    # ============================================================ SEQ 07 — 60s
    dict(id="SH-076", seq=7, dur=10, tool="seedance", plate="WP-smooth-finished-crowd", chars=["FINISHER", "KIT"],
         lens="35mm", move="slow push in", height="toy", dir="R>L", smooth=75, hand="stopped",
         chain=None, firstlast=False, kit_state="damaged", lines=["L-127", "L-128", "L-129", "L-130"],
         action="White. The Finisher stands among hundreds of frozen blank figures and explains himself, calmly, without self-pity. He does not move toward Kit at any point.",
         extra="No rim light anywhere in frame, no cast shadows, no separation between subjects and background.",
         note=("THE LIGHTING LAW BREAKS HERE, deliberately, and it should be physically uncomfortable "
               "after six sequences of hard graphic silhouettes. Tier A, completely static.")),

    dict(id="SH-077", seq=7, dur=10, tool="seedance", plate="WP-smooth-void", chars=["FINISHER"],
         lens="50mm", move="slow push in", height="toy", dir="static", smooth=75, hand=None,
         chain=None, firstlast=False, kit_state=None, lines=["L-131", "L-132", "L-133", "L-134", "L-135"],
         action="He extends one long hand, palm up. His only gesture in the entire film. He makes the offer with total kindness.",
         extra="",
         note=("THE OFFER, and it must be genuinely tempting — he is offering Kit exactly what Kit "
               "already wants. Tier A, static, no movement other than the hand.")),

    dict(id="SH-078", seq=7, dur=5, tool="higgsfield", plate="WP-smooth-void", chars=["KIT"],
         lens="85mm", move="slow push in", height="eye", dir="static", smooth=75, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=[],
         action="Kit's face. He hesitates. Really hesitates — long enough that it costs something, long enough that the audience sees it. Then he looks past the Finisher at a small blank white dog frozen mid-stride with one paw up.",
         extra="",
         note="No dialogue. The hesitation must be legible or the choice afterward is worthless."),

    dict(id="SH-079", seq=7, dur=10, tool="higgsfield", plate="WP-smooth-void", chars=["KIT"],
         lens="35mm", move="handheld follow", height="eye", dir="static", smooth=75, hand=None,
         chain=None, firstlast=True, kit_state="glowing", lines=["L-136", "L-137"],
         action="Kit draws. Fast, ugly, wide committed sweeping strokes with no hesitation and no erasing, amber light screaming off the tip of the marker.",
         extra=("Brilliant amber trails follow the marker in fast wide arcs, cooling into solid "
                "material. Ben-Day halftone dot texture blooming in the shadow areas. Split into "
                "hard-edged comic panels within the frame at the peak of the sequence."),
         note=("THE RESURRECTION. Author both keyframes. Permitted Spider-Verse devices (halftone + "
               "panel split), 5 and 6 of 12. Kit Tier A.")),

    dict(id="SH-080", seq=7, dur=5, tool="seedance", plate="WP-smooth-void", chars=["COLOSSUS_FINISHED"],
         lens="50mm", move="slow push in", height="ground", dir="static", smooth=75, hand=None,
         chain="SH-079", firstlast=True, kit_state=None, lines=["L-138", "L-139"],
         action="The white drains off Colossus from the nose backward and cobalt floods in. A mismatched amber back half arrives — wrong colour, wrong scale, one hind leg longer than the other, a tail that is barely more than a scribble. He lands on four uneven legs. And he barks. All the way through.",
         extra="Colour flooding back across his body from the nose backward, horizontal layer striations reappearing across every surface as it passes.",
         note=("THE EMOTIONAL PEAK OF THE FILM. The first complete bark in the episode — verify no "
               "earlier clip contains one. Author both keyframes: start smoothed and white, end "
               "finished and crooked.")),

    dict(id="SH-081", seq=7, dur=10, tool="seedance", plate="WP-smooth-colour-return", chars=[],
         lens="18mm", move="crane up reveal", height="toy", dir="static", smooth=50, hand="restarted",
         chain=None, firstlast=True, kit_state=None, lines=["L-140"],
         action="At the edge of the white, the crowd has come. A small bag clip at the front scratches a line into the air with a strut — and it works, and a lopsided terrible entirely original thing clatters onto the ground. Then all of them are doing it. Hundreds of arms, hundreds of crooked lines, hundreds of ugly finished things hitting the ground at once. Colour floods back across the white in a wave. On the horizon the Hand moves again.",
         extra=("A crowd of printed plastic objects at wildly mismatched scales, each a different "
                "single flat filament colour, all with visible horizontal 3D-printed layer "
                "striations, all drawing glowing lines in the air at once."),
         note=("THE THESIS BEAT — the chosen one is replaced by a crowd of amateurs. Grade: overshoot "
               "past the Raft's peak saturation for four seconds, then settle. Audio: everything "
               "returns at once, including the stepper-motor motif, absent since SH-043. Author both "
               "keyframes to control the colour wave.")),

    dict(id="SH-082", seq=7, dur=5, tool="seedance", plate="WP-smooth-colour-return", chars=["JUNE_REBUILT", "KIT"],
         lens="50mm", move="locked off", height="toy", dir="static", smooth=25, hand="restarted",
         chain=None, firstlast=True, kit_state="glowing", lines=["L-141", "L-142"],
         action="Kit raises the marker at June. She tells him not to. He is already drawing. Four seconds — fast and crooked and complete. Warm amber floods into her empty wireframe half.",
         extra="Amber material filling into the hollow wireframe outline of her left side, over-built and lumpy at the seam.",
         note="JUNE STATE CHANGE to rebuilt. Author both keyframes: start wireframe, end filled. Tier B."),

    dict(id="SH-083", seq=7, dur=5, tool="seedance", plate="WP-smooth-colour-return", chars=["JUNE_REBUILT", "KIT"],
         lens="85mm", move="locked off", height="toy", dir="static", smooth=25, hand="restarted",
         chain="SH-082", firstlast=False, kit_state="glowing", lines=["L-143", "L-144", "L-145", "L-146"],
         action="June looks down at her own mismatched left hand. Closes it. Opens it. Three lines between them. Kit starts a fourth — and dissolves upward from the feet, layer by layer, mid-word, and is gone. June is left standing with her hand still open.",
         extra="Kit comes apart into stacked glowing horizontal lines that rise and vanish.",
         note=("He does not get to say goodbye. That is the point. Hold on June alone for the last "
               "second and a half.")),

    # ============================================================ SEQ 08 — 30s
    dict(id="SH-084", seq=8, dur=10, tool="seedance", plate="WP-bedroom-return", chars=["KIT"],
         lens="35mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=[],
         action="The chair. Kit is in it mid-breath, filthy, knee scraped, dust on his hoodie, exactly as he left. Grey dawn at the window. The printer beeps: done. Inside the chamber sits Colossus — finished, cobalt front, amber back, one hind leg longer than the other, a scribble for a tail. Crooked as anything.",
         extra="The pen cup on the desk holds only pens.",
         note=("THE STING. Generate this from the saved SH-002 keyframe, modified — do not "
               "regenerate the room from scratch or the bookend will not match. The figurine is "
               "gone and the camera does not comment on it in any way.")),

    dict(id="SH-085", seq=8, dur=10, tool="seedance", plate="WP-bedroom-drawer", chars=["KIT"],
         lens="35mm", move="locked off", height="high", dir="static", smooth=0, hand=None,
         chain=None, firstlast=False, kit_state="damaged", lines=[],
         action="Kit pulls open the drawer. Forty unfinished things look back at him. He does not fix any of them. He closes it.",
         extra="",
         note="Same angle as SH-009. No dialogue. He is not required to solve his whole life in one night."),

    dict(id="SH-086", seq=8, dur=10, tool="seedance", plate="WP-bedroom-return", chars=["KIT"],
         lens="50mm", move="slow push in", height="eye", dir="static", smooth=0, hand=None,
         chain=None, firstlast=True, kit_state="damaged", lines=["L-147"],
         action="Kit turns to the screen and opens a new file. It is June — both sides, complete, drawn from memory, every line of her finished. His cursor moves to the print control and does not hesitate at all. He presses it. The chamber light pulses once.",
         extra="On the screen, a complete 3D model of a one-of-a-kind girl-shaped creature, solid and finished on both sides. No readable text or UI anywhere on the screen.",
         note=("LAST SHOT. Smash to black on the pulse. The stepper-motor melody resolves all the way "
               "to the end of its phrase for the first time in the film. Author both keyframes.")),
]
