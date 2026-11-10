# Laine addition: electrical, lighting and network review

Reviewed Nov 9, 2026 against `plans/A2`, `A3`, `A4` (architect, geometry reference), the four device
drawings in `drawings/` and `notes/design-decisions.md`. The drawings were not changed during the review. Afterwards, at the
owner's request, smoke/CO alarms (SD#, CO#) and on/off notes for S6, S9, S11 were added to them.

How to read this:

- Positions are measured from the SVG coordinates and converted to feet with each drawing's own
  labeled dimensions (scales in the last section). "x" is feet east of the garage's NW outside corner,
  "z" is feet south of it.
- Code items are sanity checks against NEC 2023 as adopted in Ohio for dwellings. They are written as
  **"check with the electrician/inspector"**, not rulings. Ohio amends the NEC for residential work
  (AFCI/GFCI scope in particular), so the local building department has the last word.
- Owner decisions in the notes are left alone; anything below is a proposal.
- Ranking: **must-fix** = likely to fail inspection, be unbuildable as drawn, or be unsafe;
  **should-fix** = works but will annoy or cost money later; **nice-to-have** = drawing hygiene and comfort.

## Top 10 findings

| # | Rank | Finding | Where |
|---|------|---------|-------|
| 1 | must-fix | Main panel MP is drawn on the north wall inside the footprint of the garage stair (x 36.7 to 39.7 ft). The stair soffit there is roughly 5 to 6 ft above the slab, below the 6.5 ft headroom a panel's working space needs. A.2 also shows a wall along the south side of that stair, so MP, the WashTower, modem 1, switch 18 and P1/P2 would be inside a 3'4" wide enclosed under-stair space. | garage v20: MP, W/D, 1, 18, L14 |
| 2 | should-fix | Garage PoE switch 2 needs 6 PoE ports, about 75 W and a fiber port. The other switches are settled: garage 7 (8-port), garage 18 (8-port plus fiber), second-floor 8 (16-port) and the new second-floor 16 (8-port plus fiber). | garage v20: 2 |
| 3 | should-fix | Second-floor kitchen: island outlet P14 needs its position checked against the NEC 2023 island rule, and wall receptacle spacing runs long in a few places. (The counter south of the sink now has P25 and P26.) | second floor v20: P14 |
| 4 | should-fix | Third floor: ID 6 is used twice (network jack 6 and the empty rack opening), and ceiling outlet P21 only counts toward wall spacing if it is within 5.5 ft of the floor. | third floor v32: 6, P21 |
| 5 | nice-to-have | Garage labelling: MP has no text on the plan, device C reads like a circuit number, and switches E and F are drawn amber instead of green. | garage v20: MP, C, E, F |
| 6 | nice-to-have | Garage hallway: switch E is plotted in the hallway door opening at the stair foot, and nothing by the overhead doors controls L1 to L8. | garage v20: E, F |
| 7 | nice-to-have | Second floor: S17 and stair controller D need real locations, motorized screen B covers the balcony door when down, and the exterior stair is unlit at the bottom. | second floor v20: S17, D, B |
| 8 | nice-to-have | Third-floor sheet colors do not follow the key: blind outlets H1 to H5 are purple, network items are teal, blue and coral, and power items A to E are red. | third floor v32 |
| 9 | nice-to-have | Shed site sketch is labelled "East walls in line", but it is the shed's east wall in line with the garage's west wall. | shed v6 |
| 10 | nice-to-have | A 125 A subpanel on the second floor would replace about 24 home runs through the rated garage ceiling with one feeder. | second floor v20 |

## PDF vs drawing geometry mismatches

The PDF wins for geometry; these are the differences found.

| Item | Architect sheet | Device drawing / notes | Effect |
|------|-----------------|------------------------|--------|
| Garage ceiling | A.2: 9'5" | Notes and v20: "9 ft" | 5 in. The 3D model uses 9'5". |
| Hallway (breezeway) | A.2: 5'0" x 21'10", 8'4" ceiling, floor two risers above the garage slab | v20 draws it flush and about 5.5 ft wide | Hallway lights L9, L10 are on a lower ceiling than the garage lights. |
| Garage stair | A.2: enclosed by a wall on its south side with the tankless water heater on that wall | v20: no wall drawn; W/D, MP, 1, 18, P1, P2, L14, D inside the footprint | See finding 1. |
| Third-floor east room | A.4: "OFFICE/LOFT 14'0 x 12'7", guardrail, open to family room below | v32: one room 25 ft deep, "over the family room" | Owner decision: the area is floored over for more space, not left open, so v32 is correct. Sheet A.4 is out of date here; the architect needs to draw the added floor framing and drop the guardrail. |
| Family room ceiling | A.3: vaulted | v20: L17, L18 "family room ceiling" | With the third floor carried over the family room the ceiling is flat, not vaulted. The 3D model uses 9 ft. A.3 needs the same update as A.4. |
| Kitchen layout | A.3: pantry and fridge on the north wall, sink then range on the east wall | v20: fridge where the pantry is, range where the fridge is, sink and DW on the east wall | Recorded as an owner decision in the v20 legend. Range circuit E, hood N and DW circuit M follow the drawing. Confirm the architect knows. |
| Third-floor reading nook | A.4: the space south of the west office jog (about 5.6 x 4 ft) is unfinished attic behind the office's 5'0" wall, reached through a 22 x 30 attic access panel in that wall | v32 originally drew it outside the outline; it is now the children's reading nook with L10, S11 and a small door | Finishing it is a change for the architect: floor, insulation line and the low sloped ceiling. The nook door lands about where A.4 puts the attic access panel, so the attic beyond needs another way in. The 3D model places the nook's east wall at x 21.2 ft (A.4); the drawing has it at 21.9 ft. |
| Third-floor closet light | A.4 closet ends about z 14.4 ft | v32 had L7 plotted about 1.3 ft south of the closet's south wall line | Resolved: L7 is now drawn inside the closet. |
| Outbuilding site note | Task brief: shed east wall in line with the garage **west** wall | v6 sketch shows that, but its label reads "East walls in line" | Fix the label. |
| Exterior stair | A.2 plan: "UP 15R (verify)"; A.2 stair data: grade to balcony 16 risers | Not on device drawings | Architect's own inconsistency; affects stair light count only. |

## Garage and hallway (`1-garage-and-hallway_v20.svg`)

### Consistency
- Every plotted ID has a legend row and every legend row has a symbol, with one exception: **MP** has a
  legend row but no "MP" text on the plan (it is the unlabeled red bar). *nice-to-have*: label it.
- IDs are unique. Two naming collisions are worth cleaning up (*nice-to-have*):
  device **C** ("20A circuit, computers, printers") reads like a circuit number next to C1 to C7, and
  switches **E** and **F** are drawn amber although the color key says switches are green.
  The second floor reuses the letters E (range) and F (bidet), so "garage E/F" needs the level every time.
- Cross-level pairs agree: E pairs with second-floor S4 (riser lights L8) and F with second-floor S16
  (wall lights L30 to L32) on both drawings and in the notes.
- Circuits (resolved): lighting is now C10 (15 A) and also feeds stair controllers D and alarms SD1/CO1;
  B is on C2, C on new dedicated C8, A on new laundry circuit C9.
- Windows are now drawn from A.2: two 2840 units on the north wall (x 12.3 to 15.0 ft and 28.3 to 31.0 ft)
  and one tempered 2840 on the west wall (z 1.7 to 4.4 ft).
- Blind outlets H1 to H3 (owner decision) are high beside the top of each window on its left seen from
  inside: H1 and H2 west of the north windows, H3 south of the west window, on C2 (GFCI). H2 is above P5 and
  beside EV2, and H3 shares its bit of wall with G2; they are at different heights, so this works.
- Resolved (Nov 10, 2026): ground bar G2 and surge protector SP2 were plotted on the west window; they are
  now just south of it (z 4.8 to 6.0 ft), about 5 ft from switch 7. G2 is the ground bar for any outdoor
  Ethernet cables added later at this corner. Switch 7 stays in the corner; mount it on the north wall, since
  the west wall has only about 1 ft between the corner and the window.
- L11 and L15 are plotted about 4.3 ft south of the west door wall because they mount on the balcony piers
  (owner decision).

### Lighting control
- Every light has a switch: L1 to L8 on S1+S2, L9/L10 on S4+S7, L11/L12/L15/L16 on S3, L13 on S5, L14 on S6.
- The door between the garage and the hallway is now drawn from A.2: a 2868 solid-core 30-minute door at
  z 5.8 to 8.7 ft, hinged on its north jamb and swinging into the garage, with two steps down on the garage
  side. S1 and S3 are a two-gang on the garage side at its south (latch) edge (owner decision, Nov 10, 2026).
  They sit beside the lower steps, so mount them at 4 ft above the hallway floor level, not the garage slab.
- 3-way ends: S1 is beside the hall door and S2 on the west wall near the SW corner (moved there Nov 10, 2026), so both entries used on foot are covered.
  S7 is on the hallway side of the garage door and S4 by the old-house door. The stair foot is 4 to 5 ft from S7. OK.
- Resolved (Nov 10, 2026): the door between the hallway and the old house is now drawn from A.2, a 3068 in
  the hallway east wall at z 16.6 to 19.6 ft, hinged on its north jamb and swinging into the hallway. (The
  earlier gap on the drawing was about 1 ft too far south.) S4 and S5, which were plotted in the opening, are
  now a two-gang on the east wall at the door's south (latch) edge. That spot is also beside the latch side
  of the deck door, so one box serves both doors.
- The front door from the hallway to the deck is now drawn from A.2: a 3068 in the hallway south wall,
  hinged on its west jamb and swinging into the hallway.
- Resolved (owner decision, Nov 10, 2026): doorbell 16 is on the east (latch) side of the front door, and
  L13 is centred over the door to make room for it.
- *nice-to-have*: E is plotted at z 6.3 ft, which is in the garage door opening (z 5.8 to 8.7 ft). A.2 leaves
  about 22 in of wall between the landing and that door, enough for a 2-gang with F above or beside E.
- *nice-to-have*: nothing by the overhead doors controls L1 to L8 except S2 on the west wall near the SW corner.
  A scene button at jack location 11 between the doors would cover both.
- Overhead doors: the doors are 16080. An open 8 ft door sits about 8.5 ft up and reaches about 9.5 ft back
  from its wall, so the west door covers z 12.5 to 22 ft and the east door z 15.8 to 25.3 ft.
  Both light rows were moved 2 ft north (owner decision, Nov 10, 2026): L1 to L4 are now at z 7.2 ft and
  L5 to L8 at z 16.7 ft. L5 to L8 are still above the open doors, which the owner accepts (they are for when
  the doors are closed). Ceiling cord reels P11 and P12, which hung in the door path, were dropped (owner
  decision, Nov 10, 2026). O3 and O4 at 10.3 and 10.6 ft back are clear.

### Code-oriented checks (check with the electrician/inspector)
- **Panel location** (finding 1). NEC 110.26 working space is 30 in wide, 36 in deep and 6.5 ft high and has
  to stay clear; storage and a WashTower in the same under-stair space work against that. NEC 230.85 also
  requires an outdoor emergency disconnect for a dwelling service, which turns the indoor panels into
  feeder-supplied panels with separate neutrals and grounds. A 400 A service is normally two 200 A panels;
  the 2.9 ft red bar is barely two enclosures wide. Proposal: move MP out from under the stair, for example
  to the garage east wall south of S1/S3, where there is full headroom, and keep the
  under-stair space for the modem and switch only.
- **GFCI** (resolved on the drawing): C1 to C4, C8 and C9 are now all marked GFCI, which covers every garage
  receptacle including the ceiling ones (O3, O4) and outdoor outlet B. GFCI breakers keep the
  reset reachable. Two things to check: C2 carrying outdoor outlet B is allowed for a garage receptacle
  circuit, and a GFCI trip on C1 takes the modem and switches down, so consider a UPS or an alert.
  Hallway P14 to P17 (C7) are in a finished hallway, so AFCI is the question there rather than GFCI.
- **Garage receptacles**: one per vehicle bay and a 20 A garage circuit with no other outlets are satisfied
  by C2 and C3. Opener circuit C4 is separate, which is right.
- **EV circuits**: 60 A circuits at 48 A continuous are sized correctly (48 x 1.25 = 60). At that size the
  chargers are hardwired, and both count at full value in the service calculation unless a listed energy
  management system limits them. Location (resolved): EV1 is now at x 9.5 ft and EV2 at x 26.4 ft,
  both clear of the windows. EV2 sits between the boiler (ends about x 25.2 ft) and P5; confirm the boiler's
  service clearance with the installer.
- **Laundry under the stairs** (owner decision, Nov 10, 2026): location A gets both the 20 A, 120 V laundry
  circuit C9 (GFCI) and a new 30 A, 240 V dryer circuit C15, plus a gas stub, so either WashTower model fits.
  Check whether the 240 V dryer receptacle also needs GFCI under NEC 2023 in a garage. A 74 in WashTower only fits under the west (high) end of the stair.
- **Outdoor receptacles**: B (south), P18 (north) and P19 (west) are at grade; P18 and P19 also serve as
  the condensers' service receptacles. P21 (owner decision, Nov 10, 2026) is a GFCI weather-resistant
  outlet with an in-use cover on the deck, just west of the front door, on hallway circuit C7.
- **Mini-splits** are left off on purpose. Their power is now drawn at the four condenser positions on A.2:
  MS1 and MS2 outside the north wall (x about 24 and 27.5 ft) and MS3 and MS4 outside the west wall under
  the exterior stair (z about 12 and 15.5 ft), each a hardwired 240 V, 30 A connection on its own circuit
  (C11 to C14). Outdoor GFCI outlets P18 (north wall, x about 20.5 ft) and P19 (west wall, z about 17.5 ft),
  both 125 V, 20 A on C2, are the service receptacles, one beside each pair.
  The indoor units are fed from the condensers. Check with the electrician: confirm 30 A against each
  unit's nameplate maximum breaker size, put a disconnect within sight of each condenser, and add the four circuits (up to 120 A of breakers) to the load estimate.
- **Smoke/CO**: A.2 note 9 requires hardwired interconnected alarms and shows a smoke and a CO alarm in the
  hallway. Now drawn as SD1 and CO1 on the hallway ceiling (about 2.5 ft north of the A.2 spot to clear
  other symbols). Check with the inspector whether the garage itself needs a heat alarm.
- **Grounding**: G3 is a new ground bar under the stair by switch 18 for SP3 (doorbell 16); bond it to the
  service ground at MP with a short, straight conductor. G and G2 are noted as bonded to the addition ground. Check that this means the service
  grounding electrode system (intersystem bonding termination), and that the coax entry at device 1 has its
  ground block bonded to the same point.

## Second floor (`2-second-floor_v20.svg`)

### Consistency
- All plotted IDs have legend rows and the reverse; IDs are unique on this level.
- Cross-level pairs agree in both directions: S3 with third-floor S8 (L7), S4 with garage E (L8),
  S15 with third-floor S9 (L33, L34), S16 with garage F (L30 to L32), S17 with third-floor S10 (L35).
- *nice-to-have*: S17 is drawn mid-hall "above S15"; D (stair light controllers) is drawn in the stair run.
  Both need a real location. The under-stair space by P16 suits D.
- Resolved (Nov 10, 2026): H4 was plotted on the balcony door opening; it is now above the east end of the
  east 3020 window.
- *nice-to-have*: motorized screen B is plotted at the balcony door. When it is down it covers the door.

### Lighting control
- Every light has a control. L21 (sauna) has no wall switch by design; it is on the heater control.
- Stair pairs have a switch at each end: S3/S15/S17 at the foot of the west stair (x 10.6 to 12.1 ft, stair
  foot at x 9.6 ft) and S4/S16 at the head of the east stair (x 31.6 to 33.1 ft, first riser at x 33.8 ft).
- Companion switches (owner decision, Nov 10, 2026):
  - Hall: S19 pairs with S1 (L1 to L3) at the foot of the west stair, and S20 pairs with S2 (L4 to L6) at the
    head of the east stair. Each stair end lights its own half of the hall.
  - Kitchen: S21 pairs with S8 (L13 to L15) on the kitchen side of the media/kitchen door, at its latch edge.
  - Media: L9 and L10 are on separate switches (owner decision): S5 runs L9 and new S24 runs L10, both by
    the hall door with S6. Their companions S22 (L9), S25 (L10) and S23 (fan L11, on/off) are a three-gang
    on the media side of the media/kitchen wall at the door's north edge. That is the hinge side, but the
    door opens into the kitchen, so the switches stay clear.
  - S13 moved to the west (latch) side of the media/balcony door (owner decision). A.3 shows only about
    4 in of framing between the window and the door, so the box sits below the 3020 window, which is 2 ft
    tall and high on the wall. Check the sill height leaves room for a box at 4 ft.
- Family room (owner decision, Nov 10, 2026): S26 pairs with S10 for L17, L18 and L24, at the north end of
  the wall between the family room and the bath, which is the side you enter from the kitchen.
- Accepted (owner decision, Nov 10, 2026): S10 runs family ceiling lights L17, L18 together with balcony
  light L24, and L29 stays on S13.
- Doors are now drawn from A.3: hall to media and hall to kitchen (2668, hinged east, opening into the
  rooms), media to kitchen (2668, hinged north, opening into the kitchen; its gap was about 0.5 ft too far
  south and is corrected), media to balcony (3068, opening in), family to balcony (3068, opening out),
  closet, bath, sauna and the W/D closet bifold. What the doors show:
  - Resolved (owner decision, Nov 10, 2026): the hall/kitchen door is now hinged on its west jamb, the
    opposite of A.3, so S8 and S9 are on its latch side and no longer behind the open door.
  - Resolved (owner decision): doorbell 14 moved out of the family/balcony door's swing to the wall north
    of the door; L29 was nudged north to make room.
  - A.3 draws the sauna door opening into the sauna. Sauna doors normally open outward; check the heater
    manual and the inspector.
  - S5/S6 (latch side of the media door) and S11/S18 (latch side of the bath door) are well placed.
- *nice-to-have*: the exterior stair from grade to the balcony (16 risers) has only L28 at the top landing,
  which is what the residential code asks for, but the bottom is unlit. A step light or a light at the foot helps.
- Resolved (owner decision): S6 (media fan and its light), S9 (under-cabinet L16) and S11 (bath L19, L20, fan)
  are now plain on/off switches, not dimmers and not smart-bulb mode.
- Resolved (owner decision): the bath fan has its own on/off switch S18 below S11; S11 runs L19 and L20 only.
- *nice-to-have*: S6 and S11 are on/off switches that cut power to the L11 fan light, L19 and L20, so use
  ordinary (non-smart) lamps there. With the fan now on S18, S11 could go back to the standard smart-bulb
  dimmer if you prefer.

### Code-oriented checks (check with the electrician/inspector)
- **Bathroom**: C10 (bidet F, P15, P22) as a 20 A GFCI circuit for this one bathroom works. P15/P22 are
  within 3 ft of the vanity at the SW corner. L20 is noted wet rated. Confirm the exhaust fan circuit.
- **Kitchen circuits**: two small-appliance circuits exist (C4 counter, C5 P7 and island P14), fridge,
  microwave/hood and DW/disposal have their own. Check DW plus disposal on one 20 A against nameplates.
  GFCI/AFCI scope is now marked on the drawing (owner decision, Nov 10, 2026): GFCI on the range (C1),
  fridge (C6), DW/disposal (C7), microwave (C8) and WashTower (C9) as well as the counters; AFCI on every
  120 V, 15 and 20 A circuit except bath C10 and balcony C14; dual-function breakers where both apply.
  A fridge on GFCI can nuisance-trip; ask the electrician about a monitored or alarmed receptacle.
- **Counter receptacles**: the counter south of the sink (over the DW) now has P25 and P26 on counter
  circuit C4 (owner decision, Nov 10, 2026). Island P14: NEC 2023 no longer allows an island receptacle on the side below the
  countertop; it must be on or above the top or a listed pop-up. *should-fix*.
- **Wall receptacle spacing** (6 ft from a door edge, 12 ft apart) measures long in a few places: kitchen north
  wall west of the hall door (7.8 ft of wall, none), family room stub south of the balcony door (7 ft to P9),
  media north wall between P3 and A (13 ft), and 6.5 ft from door edges to P6 and P7. *should-fix* at rough-in.
- **Sauna heater G**: 50 A, 240 V "per its manual" is the right approach; the manual also sets wire
  temperature rating, control location, GFCI or no GFCI and clearances. G is 1.5 ft from the door, as A.3
  shows; check the heater's door-side clearance. A disconnect within sight or a lockable breaker is the usual ask.
- **Sauna light and driver** (owner decision, Nov 10, 2026): driver J moved from the W/D closet to the bath
  north wall, east of the door, where it can be reached. The low-voltage run to L21 goes up through the W/D
  closet wall into the sauna. Check with the electrician: a bathroom is a damp location, so J needs a
  suitable enclosure or rating and should sit high, away from the shower opening.
- **Balcony**: P11, P23, P24 on GFCI circuit C14 satisfy the balcony receptacle rule.
- **AFCI**: now noted on C3 to C8, C11 to C13, C15 and C16 (dual-function breakers cover the GFCI ones).
- **Smoke/CO**: A.3 shows both in the hall. Now drawn as SD1 and CO1 on the hall ceiling.
- **Panel**: about 16 second-floor and 8 third-floor home runs go down through the rated garage ceiling to MP.
  A 125 A subpanel on this floor would cut that to one feeder. *nice-to-have*; not in a clothes closet or bathroom.

## Third floor (`3-third-floor_v32.svg`)

### Consistency
- **should-fix**: ID **6** is used twice: network item 6 (wall Ethernet jack, south wall) and the empty
  rack opening labeled "6". Rename the opening (R6 or "spare").
- *nice-to-have*: colors do not follow the key on this sheet. Blind outlets H1 to H5 are purple, network
  items are teal, blue and coral, and power items A to E are red.
- Cross-level pairs agree: S8 with second-floor S3, S9 with S15, S10 with S17.
- L7: see the mismatch table.

### Lighting control
- Every light has a switch: L1/L2 on S1+S2, L3 to L5 on S3, L6 on S4, L7 on S5, L8 on S6, L9 on S7, and
  reading-nook light L10 on S11, which is on the office side beside the nook door.
- S1 (top of stairs) and S2 (by the shared door) are at the two ends of the west office. Good.
- Accepted (owner decision, Nov 10, 2026): the east office keeps one switch, S3 at the shared door, although
  the attic passage is a second entry; L6 stays on S4 (office side) and L8 on S6 (small attic side).
- Accepted (owner decision): the four switches at the top of the stairs (S1, S8, S9, S10) stay separate.
- S5 is on the closet's north edge by its door and is a plain on/off switch, and L7 is marked on the drawing
  as an ordinary, non-smart light (owner decision).
- Reading nook (owner decision): L10 is a wall-mounted, cool-to-the-touch LED on the nook's north wall,
  because the ceiling is low, and S11 is mounted low (3 ft) so children can reach it.
- S11 stays a dimmer in smart-bulb mode (owner decision, Nov 10, 2026), so L10 stays powered and must be a
  smart fixture or take a smart lamp.

### Code-oriented checks (check with the electrician/inspector)
- **Racks in the eave** (R1 to R5): behind a 5 ft knee wall in a strip about 2.8 ft deep. Confirm the roofline
  is the insulation line so the racks are inside conditioned space. See rack cooling under open questions.
- **AFCI** is noted on C3 to C8 and "confirm" on rack circuits C1 and C2. Agree; ask the inspector.
- **Sink SK**: P16 and P17 are GFCI. A sink beside network and office gear is fine with the leak sensor shown.
- **Receptacle spacing** in the west office, measured along the walls from the drawing (the usual rule: no
  point on a wall more than 6 ft from a receptacle, so about 12 ft apart, with doorways breaking the run).
  With P18 to P21 added and P5 moved east, every run now measures inside that: P1 to P21 is about 11.8 ft,
  P21 to P20 7.8 ft, P18 to P19 7.7 ft, P19 to P4 7.4 ft, and the wall end by the shared door is 5.6 ft from P5.
- **P21 on the sloped ceiling** (*should-fix*, check with the electrician/inspector): a receptacle more than
  5.5 ft above the floor does not count toward wall spacing. A.4 gives the north wall as 5'0" high, so P21
  has to sit on the slope right above the wall, within 5.5 ft of the floor, or the north wall has a 19.5 ft
  gap again. P1 to P21 is also close to the 12 ft limit, so hold P21's position at rough-in.
- **Attics**: lights with a switch at the entry are there (S4, S6). P13 to P15 are on dual AFCI/GFCI C6.
- **Smoke alarm**: A.4 shows one in the west office. Now drawn as SD1. A.4 has none in the east office;
  now that it is a full floored room, ask the inspector whether it needs its own.

## Sauna / shed outbuilding (`4-sauna-shed_v6.svg`)

### Consistency
- All IDs match between plan and legend and are unique. Switch mapping reads S1 dressing (L2), S2 sauna (L1),
  S4 porch (L5), S3 shed (L3, L4).
- Site label: see the mismatch table.

### Lighting control
- Every light has a switch and each is at the door of the space it serves.
- L5 is now centered over the porch door (moved from the east end of the porch).
- Doors are now drawn (Nov 10, 2026): the porch door from the dressing room, 2'8" wide, hinged west and
  opening out onto the porch (designer's assumption); and the sauna door at the north end of the wall
  between the dressing room and the sauna, 2'0" wide, hinged north and opening out into the dressing room
  (owner decision).
- *should-fix*: hinged north, the open sauna door lies along the short north wall east of the porch door,
  about 7 in off it, and covers S1, S2 and S4 (control unit J is low and only needs occasional access).
  Move the three switches to the north wall west of the porch door (open question 1), or to the dressing
  room west wall beside that door.

### Code-oriented checks (check with the electrician/inspector)
- **Feeder**: 60 A, 240 V is ample for a 20 A heater, one 20 A receptacle circuit and a lighting circuit.
  It needs four wires (separate neutral and ground), a disconnect at the building (a main breaker in A),
  and burial depth per the wiring method (18 in for PVC conduit).
- **Grounding electrode**: a detached building with a feeder needs its own electrode (normally two rods)
  connected to the subpanel's grounding bar. G is on the south wall and A on the north wall of the shed.
  Resolved on the drawing (Nov 10, 2026): G is now shown bonded to A's grounding bar as well as to the rods.
- **Working clearance** at A: keep 30 in x 36 in clear in the shed. Shed outlets P2, P3 and P5 were removed and P6 moved north to
  where P2 was (owner decision, Nov 10, 2026), so switch 1 has an outlet about 4 ft away. P6 is south of A's
  working space; keep it that way.
- **GFCI**: P1, P4 and P6 on GFCI C2 covers the accessory-building rule. If heater B is cord-connected, its
  receptacle needs GFCI too.
- **Sauna lights and control unit J** (owner decision, Nov 10, 2026): L1 is strip lighting under the seating
  bench, like under-cabinet lights. Control unit J sits in a 15 x 11 in space low on the dressing room north
  wall by the sauna door, and the low-voltage wire runs low along the sauna north wall to the bench, away
  from the wood stove. Low on the wall is the coolest part of both rooms. Still check J's ambient rating and
  use wire and fixtures rated for sauna temperatures.
- **Network**: the link from the garage is fiber, so there is no copper between buildings. Camera 2 has SP
  on G. AP 3 is inside. A switch in an unheated shed needs a cold-rated model. Fiber and power can share a
  trench; give the fiber its own conduit with a pull string.

## Network

### PoE budget (estimates, per device type)

Assumed draw: outdoor camera 8 W, indoor ceiling camera 5 W, outdoor AP 15 W, wall AP 13.5 W,
ceiling AP 21 W (PoE+), PoE doorbell 10 W, ESP32 presence sensor 3 W, spare PoE jack 15 W.

| Switch | Devices assumed on it | PoE ports | Estimated W | Comment |
|--------|-----------------------|-----------|-------------|---------|
| Garage 2 (SW) | cameras 3, 4; outdoor AP 5; AP 6; jacks 11 (2) | 6 | 75 | Needs 8 PoE ports, about 100 W and a fiber (SFP) port. |
| Garage 7 (NW) | camera 8; camera 9; sensor 12; jacks 21 (4, no PoE) | 3 (7 ports in all) | 16 | 8-port PoE switch (owner decision); the fiber uplink needs an SFP port besides the 8. |
| Garage 18 (under stair) | camera 10; sensors 13, 14, 15, 19, 20; AP 17; doorbell 16 | 8 | 44 | 8 PoE ports plus SFP. Too many ports for a 5-port. |
| Second floor 8 (SW closet) | sensors 1, 3, 5, 6; AP 9; doorbell 14; jacks 7 (4) | 10 | 95 (35 if the jacks draw no PoE) | 16-port PoE switch with a fiber port (owner decision). Six ports spare. |
| Second floor 16 (family SE corner) | sensors 2, 4, 10, 11, 12, 13; AP 15 | 7 | 39 | New (owner decision): 8-port PoE switch with a fiber port. One port spare. |
| Third floor R1 | AP 2; AP 3; sensors 7 to 13; jacks 4, 5, 6 | 12 | 56 | The aggregation switch beside it takes the six fiber uplinks (garage 2, 7, 18, second-floor 8 and 16, shed 1) plus the modem converter fiber: at least 7 SFP ports. |
| Shed 1 | camera 2; AP 3 | 2 | 23 | Fine. Cold-rated. |

Total is about 290 to 320 W. Budgets are fine if each switch is picked for port count, not just watts.

### Third-floor Ethernet plan (proposed, Nov 10, 2026)
Every third-floor AP, presence sensor and Ethernet jack (jacks are data only, no PoE) is a home run from one PoE switch in rack R1 (network item 1).
All twelve drops are within about 25 ft of R1 in plan, so no edge switch is needed on this floor. The runs
are drawn on `lights-3d.html` (3D and the third-floor 2D map, "Ethernet runs" filter) and listed in
`lights.json` under `cables`.

| Port | Device | Cable | Length | PoE | Route from R1 |
|------|--------|-------|--------|-----|---------------|
| 1 | AP 2, east office ceiling | Cat6A | 25 ft | 21 W | Straight east above the east office ceiling |
| 2 | AP 3, west office east wall | Cat6A | 20 ft | 13 W | North bundle, drop to the AP |
| 3 | Sensor 7, west face of the shared wall | Cat6 | 25 ft | 3 W | North bundle, over the door header |
| 4 | Sensor 8, east face of the shared wall | Cat6 | 25 ft | 3 W | North bundle, over the door header |
| 5 | Sensor 9, east office north wall | Cat6 | 35 ft | 3 W | North bundle to the north wall, then east |
| 6 | Sensor 10, east office north wall | Cat6 | 40 ft | 3 W | North bundle, then east past the windows |
| 7 | Sensor 11, east office south wall | Cat6 | 30 ft | 3 W | South bundle, then east |
| 8 | Sensor 12, east office south wall | Cat6 | 35 ft | 3 W | South bundle, then east past the window |
| 9 | Sensor 13, top of the west stair | Cat6 | 40 ft | 3 W | West above the nook wall and west office ceiling to the closet |
| 10 | Jack 4, floor box across from R2 | Cat6A | 20 ft | none | Floor run: down from R1 into the floor framing, south then east |
| 11 | Jack 5, floor box across from B1 | Cat6A | 30 ft | none | Floor run, continuing east under the east office floor |
| 12 | Jack 6, west office south wall | Cat6A | 35 ft | none | West bundle with sensor 13, then south and down inside the wall |

- Three bundles leave R1: north above the wall between the offices (6 cables), south above the rack strip
  (2 cables) and west above the west office ceiling (2 cables: sensor 13 and jack 6). AP 2 goes straight
  east on its own. Floor jacks 4 and 5 run in the floor framing under the east office; check which way the
  joists run before settling that route.
- Lengths are estimates: the path above the ceiling at about 7 ft plus the drops and 8 ft of service loop
  (5 ft at the rack, 3 ft at the device), rounded up to 5 ft. Total about 360 ft: about 230 ft of Cat6 and 130 ft of Cat6A. Every run is far under the 328 ft limit.
- Switch in R1: 9 PoE ports and about 55 W for these devices, 12 ports and about 56 W with jacks 4, 5 and 6.
  A 16-port PoE+ switch with a budget of 100 W or more leaves spare ports; the fiber uplinks need their own
  SFP ports (see the PoE table).
- Cat6A for the two APs and the three jacks allows multi-gigabit later; the sensors only need Cat6. Pull one spare cable to each
  AP while the ceiling is open.
- Check with the electrician/inspector: keep the data cables out of the holes and boxes used for power
  cable, keep them a few inches away from parallel power runs, and firestop the top-plate holes.
- The ceiling route assumes there is a reachable space above the third-floor ceiling. If the roof framing
  leaves none, run the bundles inside the knee-wall and eave spaces instead; lengths grow by a few feet.

### Fiber paths
- Two runs (1 and 18) share one smurf tube up the riser. That is a single point of damage but acceptable;
  pull two spare strands and leave a pull string.
- The riser starts on the north wall under the garage stair (x 37 to 41 ft). Directly above is the east
  stairwell and then the east office north wall. R1 is at x 24 ft, z 14 ft on the third floor, so the run
  needs about 20 ft of horizontal travel on the third floor. See the open question for a route.
- Owner decision (Nov 10, 2026): every network switch uplinks by fiber to the aggregation switch that sits
  with the main switch in R1. The six uplinks are now drawn on `lights-3d.html` (orange lines) and listed
  in `lights.json` under `fibers`; they are not yet on the SVG drawings. Estimated lengths with 15 ft of
  slack: garage 18 about 75 ft, garage 7 about 110 ft, garage 2 about 130 ft, shed 1 about 185 ft (buried
  conduit to the garage SW corner, then with the switch 2 fiber), second-floor 16 about 45 ft (up the family room southeast corner into the third-floor floor framing, then
  west and north to R1), second-floor 8 about 50 ft (straight up
  into R1 from below the rack strip). Pre-terminated duplex single-mode (OS2) LC works for all of them.
- The riser now carries four garage-side fibers (2, 7, 18, shed) plus the converter fiber, so size the
  conduit for five duplex cables and a pull string.

### Second-floor Ethernet plan (proposed, Nov 10, 2026)
Two switches split the floor: switch 8 (16-port, SW closet) takes the west half, the projector jacks and the
doorbell; new switch 16 (8-port, family room southeast corner) takes the east half. Runs are drawn on
`lights-3d.html` and listed in `lights.json` under `cables`.

| Switch | Port | Device | Cable | Length | PoE |
|--------|------|--------|-------|--------|-----|
| 8 (SW closet) | 1 | AP 9, media west wall | Cat6A | 25 ft | 13 W |
| 8 | 2 | Sensor 1, west stair landing | Cat6 | 30 ft | 3 W |
| 8 | 3 | Sensor 5, media ceiling | Cat6 | 25 ft | 3 W |
| 8 | 4 | Sensor 6, media ceiling | Cat6 | 35 ft | 3 W |
| 8 | 5 | Sensor 3, hall ceiling at the media door | Cat6 | 45 ft | 3 W |
| 8 | 6-9 | Jacks 7 (four), projector wall | 4 x Cat6A | 4 x 45 ft | 60 W |
| 8 | 10 | Doorbell 14, balcony (via SP1 on GB1) | Cat6 | 40 ft | 10 W |
| 16 (family SE) | 1 | AP 15, kitchen/family ceiling | Cat6A | 25 ft | 21 W |
| 16 | 2 | Sensor 12, near the balcony door | Cat6 | 25 ft | 3 W |
| 16 | 3 | Sensor 13, bath ceiling | Cat6 | 15 ft | 3 W |
| 16 | 4 | Sensor 10, kitchen sink | Cat6 | 30 ft | 3 W |
| 16 | 5 | Sensor 11, kitchen by the hall door | Cat6 | 40 ft | 3 W |
| 16 | 6 | Sensor 4, hall ceiling at the kitchen door | Cat6 | 40 ft | 3 W |
| 16 | 7 | Sensor 2, hall northeast corner | Cat6 | 40 ft | 3 W |

- Totals: about 590 ft of copper; switch 8 about 95 W (35 W if the projector jacks draw no PoE), switch 16
  about 39 W.
- Switch 16 has no outlet of its own. It is drawn high in the corner by blind outlet H6; make that box a
  duplex so it feeds both the blind and the switch. *should-fix* until confirmed.
- The family room ceiling is vaulted and the third-floor east office is floored over it, so the runs from
  switch 16 go in whatever framing space that leaves; lengths are estimates.
- Sensor 2 in the hall's northeast corner is the longest reach from either switch. Garage switch 18 is
  directly below it and full, so it stays on switch 16.

### Garage Ethernet plan (proposed, Nov 10, 2026)
Each garage and hallway AP, presence sensor and jack goes to the nearest of the three switches. The runs
are drawn on `lights-3d.html` and listed in `lights.json` under `cables`.

| Switch | Port | Device | Cable | Length | PoE |
|--------|------|--------|-------|--------|-----|
| 2 (SW corner) | 1 | Outdoor AP 5 (via SP1) | Cat6A | 20 ft | 13 W |
| 2 | 2 | AP 6, west wall | Cat6A | 25 ft | 13 W |
| 2 | 3-4 | Jacks 11 (two), between the doors | 2 x Cat6A | 2 x 35 ft | 30 W |
| 7 (NW corner) | 1 | Sensor 12, ceiling west half | Cat6 | 25 ft | 3 W |
| 7 | 2-5 | Jacks 21 (four), north wall by outlet C | 4 x Cat6A | 4 x 25 ft | none |
| 18 (under stair) | 1 | AP 17, hallway north wall | Cat6A | 25 ft | 13 W |
| 18 | 2 | Sensor 13, ceiling east half | Cat6 | 30 ft | 3 W |
| 18 | 3 | Sensor 14, hallway north wall | Cat6 | 20 ft | 3 W |
| 18 | 4 | Sensor 20, hallway landing | Cat6 | 25 ft | 3 W |
| 18 | 5 | Sensor 19, hallway east wall | Cat6 | 30 ft | 3 W |
| 18 | 6 | Sensor 15, over the doorway | Cat6 | 45 ft | 3 W |
| 18 | 7 | Doorbell 16, front door east side (via SP3 on G3) | Cat6 | 50 ft | 10 W |

- Sensor 12 moved from switch 2 to switch 7: it is 11 ft from 7 and 19 ft from 2, and 7 has spare ports.
- Cameras 3, 4, 8, 9 and 10 also land on these switches (see the PoE table) but are not drawn on the page.
- Jacks 21 (owner decision) are four data-only jacks on the north wall by computer outlet C. Switch 7 is
  an 8-port PoE switch (owner decision) with its own high outlet P20 beside it on network circuit C1.
  With cameras 8 and 9 it uses 7 of the 8 ports, so the fiber uplink needs a separate SFP port. Jacks 11 are
  the other jacks on this level. The drawing calls those PoE jacks, so 15 W each is
  allowed for. They are inside the garage, on the east face of the short wall between the doors (owner
  decision, Nov 10, 2026), so they need no surge protector.
- The hallway runs from switch 18 cross the stairwell at the hallway's north end; route them in the wall
  and under the landing rather than across the open stair.

### Surge protection on outdoor copper
| Run | Protected? |
|-----|-----------|
| Garage cameras 3, 4, AP 5 | Yes, SP1 on G |
| Garage camera 8 | Yes, SP2 on G2 |
| Garage doorbell 16 | Yes, SP3 at the switch 18 end, on ground bar G3 (bonded to the service ground at MP) |
| Garage jacks 11 | Indoor (east face of the wall between the doors), not needed |
| Second-floor doorbell 14 | Yes, SP1 at the switch 8 end on ground bar GB1, bonded to garage ground bar G below |
| Shed camera 2 | Yes, SP on G |
| Shed AP 3 | Indoor, not needed |

### AP coverage
- Third-floor AP 2 (x 31.9, z 13.6), second-floor AP 15 (x 28.8, z 16.6) and third-floor AP 3 (x 23.4, z 11.4)
  are within about 8 ft of each other in plan. With a floor between them AP 2 and AP 15
  still overlap heavily. One of them can go, or AP 2 can move to the NE of the east office.
- Likely weak spots: the north yard and the deck/pergola side (no outdoor AP faces either), the east end of
  the garage (AP 6 is on the west wall 40 ft away, AP 17 is behind the hallway wall), and the second-floor
  bath/sauna corner behind tile and foil.
- Balcony and family-room network are still unplanned (notes). The balcony is covered by AP 9 and AP 15
  through one wall each, which is usually enough.

## Open questions: recommendations

1. **Sauna/shed switches S1, S2, S4, east or west of the porch door?** West. The east side is a 2.2 ft
   corner shared with the sauna door, which has to swing out into that corner and brings heat and steam
   with it. Use the latch side of the porch door if that also turns out to be the west side; if the door
   is hinged west, keep them west anyway and hinge the door east.
2. **Do O1/O2 come off now that O3/O4 exist?** As opener outlets, yes: one opener type per door.
   Before deleting them, decide the opener type. A jackshaft opener with high-lift
   track keeps the ceiling clear for the lights under a 9'5" ceiling; a trolley opener does not.
   If trolley openers stay, keep O1/O2 as ordinary GFCI wall receptacles at the jambs.
3. **Which switch feeds hallway AP 17?** Switch 18, about 6 ft away. That brings 18 to 8 PoE devices, so it
   must be an 8-port PoE+ switch with a fiber uplink.
4. **Does doorbell 16 get a surge protector?** Resolved (owner decision, Nov 10, 2026): SP3 is drawn at the
   switch 18 end, bonded to the service ground at MP. Second-floor doorbell 14 now has SP1 on ground bar GB1 as well.
5. **Are all four outside garage lights OK on S3?** Yes. They work as one scene and smart fixtures can still
   be grouped or scheduled. Add the same scene to S7 so they can be controlled from the hallway side.
6. **Blind outlets in the gaps between the west-office south windows?** Not in the gaps: A.4 shows about
   6 in of framing between the 2846 units, which is solid studs with no room for a box. Put one high outlet
   above the head of each gap instead, so each of the three blinds has an outlet within reach
   (H1 and H2 alone leave the middle blind without one).
7. **Riser fiber path, edge switches, rack cooling, second-floor hall sensors.**
   - *Riser*: a dedicated 1-1/4 in conduit from under the garage stair up the north wall beside the east
     stairwell to the third-floor north eave, then through the eave space to R1. Firestop each floor and
     seal the garage ceiling penetration. Simpler alternative: run the coax up the same tube and put the
     modem in R1, which removes the converter.
   - *Edge switches*: 2, 7 and 18 as drawn, sized per the PoE table. On the second floor, replace "small
     switch 8" with one 24-port PoE switch in R1 and home-run the second-floor drops up through the riser
     (the longest is under 80 ft), or use a 16-port in the SW closet and send the east-end devices
     (2, 4, 10, 11, 13, 15) to R1.
   - *Rack cooling*: add up the expected watts first. Below about 300 to 500 W, open rack fronts to the
     office and a thermostat fan exhausting the eave space are enough. Rack circuits A and B allow up to
     about 3.8 kW, and at that level the eave needs its own mini-split head or a ducted return.
     Add a temperature sensor with an alert either way.
   - *Second-floor hall sensors* (1 to 4): 1 and 3 to the SW closet switch, 2 and 4 to R1 or to garage
     switch 18 directly below; or all four to R1 if the 24-port option is chosen.
8. **WashTower model conflict.** Resolved for rough-in (owner decision, Nov 10, 2026): both circuits and
   the gas stub are run. Background: WKEX200HBA is LG's all-electric model and needs a 30 A, 240 V receptacle;
   outlet A as drawn ("washer; gas dryer") is 120 V and suits only a gas model. Confirm the model with the
   builder. If it stays undecided at rough-in, run both the 30 A, 240 V circuit and the 20 A, 120 V laundry
   circuit plus the gas stub; the extra cable is cheap. Either way it needs a dryer exhaust to the north wall.

## All findings by rank

**Must-fix**
1. MP under the garage stair: headroom and working space (garage).

**Should-fix**
2. PoE switch sizing: garage switch 2 (network).
3. Island P14 position; wall spacing gaps (second floor).
4. Duplicate ID 6; ceiling outlet P21 must stay within 5.5 ft of the floor to count (third floor).

**Nice-to-have**
5. Label MP; rename device C; draw E/F green (garage).
6. E in the door opening; scene button between the overhead doors (garage).
7. S17 and D need real locations; screen B over the balcony door; light at the foot of the exterior stair (second floor).
8. Color key on the third-floor sheet (third floor).
9. "East walls in line" label (shed).
10. A second-floor subpanel instead of about 24 home runs through the garage ceiling.
11. One AP too many in the middle of the building; outdoor coverage north and east.

## Scales used

| Drawing | Basis | Scale |
|---------|-------|-------|
| Garage v20 | Outline 492.0 px wide = 42'6" outside (41'6" label plus two 6 in walls); 292.9 px deep = 25'4" | 11.58 px/ft (x), 11.56 px/ft (z) |
| Second floor v20 | Outline 510.3 px = 42'6"; 303.8 px = 25'4" | 12.01 px/ft (x), 11.99 px/ft (z) |
| Third floor v32 | "Overall 42'6" wide" = 607.8 px; 361.7 px = 25'4" | 14.30 px/ft (x), 14.28 px/ft (z) |
| Sauna/shed v6 | "12 ft x 24 ft": 300 px = 12 ft | 25 px/ft |

Room labels inside each drawing (media 17'1", family 14'2" x 20'8", east office 14'0") agree with these
scales to within about 3%, so positions are good to roughly half a foot.
