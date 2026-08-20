# Visual Style Lock

The most common cause of drift across a 90-shot AI-generated film is style language that
varies between prompts. The blocks below are **verbatim copy-paste**. Do not paraphrase,
do not improve them mid-project, and do not add adjectives because a shot feels flat — fix
flatness with lighting and camera, never with new style words.

---

## Reference target

Base look: **Arcane** — painterly 3D, hand-painted texture over dimensional form, visible
brushwork in shadow, graphic silhouettes, painted light.
Accent: **Spider-Verse** — halftone, chromatic offset, on-2s stepping, impact frames —
used only on designated beats, never as the baseline.

Arcane is the base because painterly 3D survives independent generations far better than
comic compositing does. Full Spider-Verse on every shot would drift badly by shot 40.

---

## STYLE LOCK — append to every prompt, unchanged

```
STYLE: painterly 3D animation, hand-painted textures over dimensional forms, visible
brushstroke in the shadows, thick graphic silhouettes, painted volumetric light, rich
saturated color with deep teal shadows and warm amber key light, cinematic depth of
field, subtle film grain, 24fps, 21:9 cinematic framing. High contrast rim lighting
separating subject from background. No text, no logos, no watermarks, no subtitles.
```

## NEGATIVE LOCK — append wherever negatives are supported

```
NEGATIVE: photorealistic, live action, uncanny realistic human skin, glossy plastic CGI
sheen, flat even lighting, muddy desaturated color, extra fingers, deformed hands, warped
face, morphing features, text, watermark, logo, subtitles, vertical framing, blurry
low-detail background, anime, flat cel shading
```

---

## The Two-Material Law

The most important visual rule in the film, and it does structural work.

**Kit is smooth. Everything else is built from rings.**

| | KIT (human) | Every printed being |
|---|---|---|
| Surface | soft painterly skin, subsurface warmth, no striation | stacked horizontal rings across every curved surface, like tree rings |
| Sheen | matte — skin and cloth | faint waxy sheen catching light in horizontal bands |
| Edges | soft painterly falloff | faceted, slight stair-stepping on diagonals |
| Motion | on 1s — fluid | on 2s — slightly stepped, toy-like |

In any frame containing Kit and a toy, the audience instantly knows what he is. It also
keeps our two continuity systems — Soul ID for Kit, Elements for the toys — from ever
competing for the same visual space.

**Include in every shot containing Kit:**
`Kit's skin is smooth and painterly with no ring lines, in deliberate contrast to the visible stacked ring striations on every other character.`

---

## Palette

Teal shadow / amber key globally. Each world overrides only the **accent**, never the
base. This is what keeps one film from becoming a set of unrelated clips.

| World | Prompt phrase |
|---|---|
| The Bedroom | `cool blue night interior, single hot orange point light` |
| The Raft | `honey-gold late afternoon light, sun-bleached pastel colors` |
| Dino Basin | `rust-orange canyon light, olive shadow, heavy dust haze` |
| Gearhaven | `cyan industrial glow, sodium-vapor orange practicals, wet reflective floor` |
| The Deep Bin | `near-monochrome charcoal darkness, single pale shaft of light from far above` |
| The Smooth | `blown-out flat white void, shadowless, faint lilac gradient, no horizon` |

The Smooth is the only world that breaks the lighting law — no rim light, no shadow — and
that is exactly what makes it feel wrong.

---

## Camera language

Locked lens set. Use these and nothing else.

| Lens | Use |
|---|---|
| 18mm | Kit's POV of scale, world reveals, the Hand |
| 35mm | default coverage, walk-and-talk |
| 50mm | dialogue mediums |
| 85mm | emotional close-ups, always shallow |
| macro | printing and ring-detail inserts |

**Height rule.** Kit is a giant here. The camera lives at **toy eye height — roughly 40mm
off the ground** — for all world coverage, so Kit is consistently looming and
foreshortened. Cut to his eye height only when he is emotionally isolated. This is the
film's core visual grammar; keep it consistent.

**Move vocabulary.** slow push in / slow pull out / lateral track / crane up reveal /
handheld follow / locked off. **One move per shot. Never two.**

---

## Spider-Verse accent — permitted uses only

| Device | Where | Prompt phrase |
|---|---|---|
| On-2s stepping | all toy movement, always | `toy characters move with slightly stepped, on-twos animation` |
| Impact frame | a hit lands, a thing breaks | `single-frame graphic impact burst, hard-edged shapes, chromatic offset` |
| Halftone | the pencil activating, Kit's panic | `Ben-Day halftone dot texture in the shadow areas` |
| Chromatic aberration | proximity to The Finisher | `heavy red/cyan chromatic offset at frame edges` |
| Comic panel split | reveals and montage only | `split into hard-edged comic panels within the frame` |

**Cap: no more than 12 shots** may use a device other than on-2s stepping. Overuse turns a
film into a filter.

---

## Aspect and delivery

- Generate at **21:9** (Seedance supports it — it is the closest available to scope) at
  **1080p**, **24fps**.
- Draft at 480p to test prompt behavior, final at 1080p.
- Never mix frame rates. One 30fps clip in the timeline is visible.

---

## Anti-drift rules

1. Never write a new style description. Paste the STYLE LOCK.
2. Never describe a character's appearance in a shot prompt. Paste their PROMPT BLOCK.
3. Never describe an environment freehand. Paste the PLATE BLOCK.
4. A shot prompt contains only: subject action, camera, emotion, and the pasted blocks. If
   you are writing adjectives about hair in a shot card, stop.
5. If a look must change, change it in the source file and re-render every affected shot.
   Never patch it in one prompt.
