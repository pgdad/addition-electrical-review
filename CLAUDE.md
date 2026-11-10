# Laine addition: electrical, lighting and network review

You are reviewing a homeowner's electrical, lighting and low-voltage design for a three-story addition
(garage + enclosed hallway, second floor, third floor) and a separate sauna/shed outbuilding.

## Files
- plans/A2-garage-first-floor.pdf, A3-second-floor.pdf, A4-third-floor.pdf: the architect's sheets
  (dimensions, walls, windows, doors, stairs). Treat these as the geometry reference.
- drawings/*.svg: the device plans (one per level, north up, roughly to scale). Color key:
  green = switches (S#), pink = lights (L#), amber = power/panels/equipment (amber pills SD#/CO# = smoke and CO alarms),
  red = outlets (P#, O#, EV#), teal = blind outlets (H#), purple = network (numbers), blue = windows.
- drawings/*.legend.txt: every text label pulled out of each SVG (quick to grep).
- notes/design-decisions.md: the owner's decisions, what is only proposed, and open questions.

Use `pdftotext`/`pdftoppm` (poppler) to read the PDFs if available; otherwise read them directly.
Parse SVG coordinates for device positions; do not guess positions from the legends.

## Task 1: review
Write REVIEW.md. For each level, check and report:
1. Consistency: every device in a legend appears on the drawing and vice versa; IDs unique per level;
   cross-level pairs agree (2nd-floor S3/S4/S15/S16/S17 with garage S8/S9 and 3rd-floor S8/S9/S10).
2. Lighting control: every light has a switch; every 3-way pair has one switch at each end of the
   stair or room it serves; nothing is controlled from a spot you can't reach without crossing the dark area.
3. Code-oriented sanity checks (NEC 2023, Ohio residential): GFCI/AFCI where required, bathroom and
   kitchen circuits, garage receptacles, EV circuits (continuous load), sauna heater and light-driver
   placement, outdoor receptacles, panel working clearance, outbuilding feeder and grounding electrode.
   Flag these as "check with the electrician/inspector", not as rulings.
4. Network: PoE budget per switch (estimate per device type), fiber paths, surge protection on every
   outdoor copper run, AP coverage gaps.
5. The open questions in notes/design-decisions.md: give a recommendation for each.
Rank findings: must-fix, should-fix, nice-to-have. Cite device IDs and drawing names.
Do not change the drawings.

## Task 2: interactive 3D model of all lights
Build a single self-contained `lights-3d.html` (three.js from a pinned CDN version, no build step) that
opens by double-click in a browser:
- Model the addition as stacked levels using real dimensions from the plans: garage/hallway at ground
  level (9 ft ceiling), second floor above the garage, third floor above that, and the sauna/shed
  20 ft south of the garage SW corner (its east wall in line with the garage west wall).
  Exterior walls as translucent boxes, floor slabs as thin planes, stairs as simple stepped blocks.
- Place every light (L#) at its drawing position, at ceiling height for ceiling lights, ~6.5 ft for wall
  lights, at riser height for stair riser lights, under-cabinet height for L16. Convert SVG coordinates
  to feet using each drawing's own labeled dimensions; write the scale you derived in a comment.
- Place every switch (S#) at 4 ft, and draw a thin line from each switch to the lights it controls;
  3-way pairs share a color.
- UI: orbit/zoom; checkboxes to show/hide each level; click a light or switch to see its ID, room,
  controlling switches and circuit; a toggle that "turns on" lights (emissive + point light) per switch
  so the owner can test each switch; a list panel of all lights grouped by level and switch.
- Include a lights.json (or embedded data block) with id, level, room, x/y/z in feet, type
  (ceiling/wall/riser/under-cabinet/outdoor/low-voltage), switches[], circuit, source drawing.
Verify it loads without console errors before finishing.

## Ground rules
- Owner decisions in notes/design-decisions.md win over your suggestions; propose changes in REVIEW.md only.
- When the PDF and SVG disagree on geometry, use the PDF and list the mismatch in REVIEW.md.
