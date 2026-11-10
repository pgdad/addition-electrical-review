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
| 2 | must-fix | Second-floor kitchen and laundry: NEC 2023 extends GFCI to all kitchen receptacles and to listed appliances, so C1 (range receptacle E), C6 (fridge K), C7 (DW/disposal M), C8 (microwave N) and C9 (WashTower W) need checking, not just counters C4/C5. No AFCI is noted anywhere on the second floor (the third floor notes it). | second floor v20 |
| 3 | must-fix | PoE doorbell 14 on the balcony is an outdoor copper run with no surge protector and no ground bar on that floor. Doorbell 16 (open question) is the same. PoE jacks 11 are plotted on the outside face of the jog wall; if they are outside they need protection too. | second floor v20: 14; garage v20: 16, 11 |
| 4 | should-fix | With 8 ft doors under a 9'5" ceiling, the open doors cover the south row of garage lights (L5 to L8) and both ceiling cord reels (P11, P12). | garage v20 |
| 5 | should-fix | Several lights can only be switched after crossing the dark: second-floor hall (S1/S2 mid-hall, 14 ft from the west stair and 8 ft from the east stair), family room (S10 only at the balcony door), media room (S5/S6 only at the hall door), third-floor east office (S3 only at the shared door, though the attic passage is a second entry), and attic lights L6 and L8. | second floor v20, third floor v32 |
| 6 | should-fix | The second-floor "small" PoE switch 8 has about 17 PoE drops and roughly 75 to 105 W. No 5/8-port switch covers that. Garage switch 2 needs 7 PoE ports and about 78 W plus a fiber cage; switch 18 needs 7 to 8 ports. | second floor v20: 8; garage v20: 2, 18 |
| 7 | should-fix | Hallway switches S4 and S5 are drawn on the east wall exactly across the east door opening, so there is no wall to mount them on. Move them to the wall beside the door. | garage v20: S4, S5 |
| 8 | should-fix | S10 runs the family room ceiling lights L17, L18 together with outdoor balcony light L24, and balcony light L29 is on the far door's switch S13. Put all four balcony lights (L23, L24, L28, L29) on one balcony control at each door. | second floor v20: S10, S13 |
| 9 | should-fix | Second-floor kitchen: the 1.8 ft of counter south of the sink has no receptacle, island outlet P14 needs its position checked against the NEC 2023 island rule, and wall receptacle spacing runs long in a few places. | second floor v20: P12 to P14 |
| 10 | should-fix | Blind outlet H4 is plotted on the balcony door opening and has no wall to sit on; put it above the window head. Sauna light driver J is in the W/D closet that the WashTower fills, so it cannot be reached. | second floor v20: H4, J |

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
| Third-floor closet light | A.4 closet ends about z 14.4 ft | v32: L7 plotted at z 15.7 ft, about 1.3 ft south of the closet's south wall line | L7 lands in the eave. Move the symbol into the closet. |
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
- L11 and L15 are plotted about 4.3 ft south of the west door wall, on the line of the balcony piers.
  Confirm whether they mount on the piers or on the wall. *nice-to-have*.

### Lighting control
- Every light has a switch: L1 to L8 on S1+S2, L9/L10 on S4+S7, L11/L12/L15/L16 on S3, L13 on S5, L14 on S6.
- 3-way ends: S1 is inside the hall door and S2 in the SW corner, so both entries used on foot are covered.
  S7 is on the hallway side of the garage door and S4 by the east door. The stair foot is 4 to 5 ft from S7. OK.
- **should-fix**: S4 and S5 are drawn on the east wall exactly across the east door opening
  (door z 17.8 to 20.7 ft, switches z 18.4 and 20.1 ft). Move them to the 2 ft of wall south of that door,
  or to the south wall beside the deck door.
- *nice-to-have*: E is plotted at z 6.3 ft, which is in the garage door opening (z 5.5 to 8.3 ft). A.2 leaves
  about 22 in of wall between the landing and that door, enough for a 2-gang with F above or beside E.
- *nice-to-have*: nothing by the overhead doors controls L1 to L8 except S2 in the far SW corner.
  A scene button at jack location 11 between the doors would cover both.
- **should-fix** (finding 4): the doors are 16080. An open 8 ft door sits about 8.5 ft up and reaches about
  9.5 ft back from its wall, so the west door covers z 12.5 to 22 ft and the east door z 15.8 to 25.3 ft.
  L5 to L8 (z 18.7 ft) end up above the open doors, P12 (z 20.1 ft) and P11 (z 14.8 ft) hang into the door path.
  O3 and O4 at 10.3 and 10.6 ft back are correctly clear. Options: shift the south light row and both reels
  north of the door travel, or add lights between and beside the tracks.

### Code-oriented checks (check with the electrician/inspector)
- **Panel location** (finding 1). NEC 110.26 working space is 30 in wide, 36 in deep and 6.5 ft high and has
  to stay clear; storage and a WashTower in the same under-stair space work against that. NEC 230.85 also
  requires an outdoor emergency disconnect for a dwelling service, which turns the indoor panels into
  feeder-supplied panels with separate neutrals and grounds. A 400 A service is normally two 200 A panels;
  the 2.9 ft red bar is barely two enclosures wide. Proposal: move MP out from under the stair, for example
  to the garage east wall south of S1/S3, where there is full headroom, and keep the
  under-stair space for the modem and switch only.
- **GFCI** (resolved on the drawing): C1 to C4, C8 and C9 are now all marked GFCI, which covers every garage
  receptacle including the ceiling ones (P11, P12, O3, O4) and outdoor outlet B. GFCI breakers keep the
  reset reachable. Two things to check: C2 carrying outdoor outlet B is allowed for a garage receptacle
  circuit, and a GFCI trip on C1 takes the modem and switches down, so consider a UPS or an alert.
  Hallway P14 to P17 (C7) are in a finished hallway, so AFCI is the question there rather than GFCI.
- **Garage receptacles**: one per vehicle bay and a 20 A garage circuit with no other outlets are satisfied
  by C2 and C3. Opener and cord-reel circuit C4 is separate, which is right.
- **EV circuits**: 60 A circuits at 48 A continuous are sized correctly (48 x 1.25 = 60). At that size the
  chargers are hardwired, and both count at full value in the service calculation unless a listed energy
  management system limits them. Location (resolved): EV1 is now at x 9.5 ft and EV2 at x 26.4 ft,
  both clear of the windows. EV2 sits between the boiler (ends about x 25.2 ft) and P5; confirm the boiler's
  service clearance with the installer.
- **Laundry under the stairs**: outlet A is now on laundry circuit C9 (20 A, 120 V, GFCI). See the WashTower open
  question for the 120 V vs 240 V conflict. A 74 in WashTower only fits under the west (high) end of the stair.
- **Outdoor receptacles**: B (south) and now P18 (north wall at the NW corner, which also serves as
  the condensers' service receptacle) are at grade. Nothing serves the deck side.
  Proposal: add a GFCI weather-resistant outlet by the deck door. *should-fix*.
- **Mini-splits** are left off on purpose. Their power is now drawn at the four condenser positions on A.2:
  MS1 and MS2 outside the north wall (x about 24 and 27.5 ft) and MS3 and MS4 outside the west wall under
  the exterior stair (z about 12 and 15.5 ft), each a hardwired 240 V, 30 A connection on its own circuit
  (C11 to C14). Outdoor GFCI outlet P18 (125 V, 20 A, on C2) at the NW corner is the service receptacle.
  The indoor units are fed from the condensers. Check with the electrician: confirm 30 A against each
  unit's nameplate maximum breaker size, put a disconnect within sight of each condenser, confirm P18 is
  within 25 ft of all four, and add the four circuits (up to 120 A of breakers) to the load estimate.
- **Smoke/CO**: A.2 note 9 requires hardwired interconnected alarms and shows a smoke and a CO alarm in the
  hallway. Now drawn as SD1 and CO1 on the hallway ceiling (about 2.5 ft north of the A.2 spot to clear
  other symbols). Check with the inspector whether the garage itself needs a heat alarm.
- **Grounding**: G and G2 are noted as bonded to the addition ground. Check that this means the service
  grounding electrode system (intersystem bonding termination), and that the coax entry at device 1 has its
  ground block bonded to the same point.

## Second floor (`2-second-floor_v20.svg`)

### Consistency
- All plotted IDs have legend rows and the reverse; IDs are unique on this level.
- Cross-level pairs agree in both directions: S3 with third-floor S8 (L7), S4 with garage E (L8),
  S15 with third-floor S9 (L33, L34), S16 with garage F (L30 to L32), S17 with third-floor S10 (L35).
- *nice-to-have*: S17 is drawn mid-hall "above S15"; D (stair light controllers) is drawn in the stair run.
  Both need a real location. The under-stair space by P16 suits D.
- *should-fix*: H4 has no wall to sit on. The east 3020 window ends 2 in from the balcony door, so H4 is
  plotted on the door opening. Put it above the window head.
- *nice-to-have*: motorized screen B is plotted at the balcony door. When it is down it covers the door.

### Lighting control
- Every light has a control. L21 (sauna) has no wall switch by design; it is on the heater control.
- Stair pairs have a switch at each end: S3/S15/S17 at the foot of the west stair (x 10.6 to 12.1 ft, stair
  foot at x 9.6 ft) and S4/S16 at the head of the east stair (x 31.6 to 33.1 ft, first riser at x 33.8 ft).
- **should-fix** (finding 5):
  - Hall L1 to L6: S1/S2 are mid-hall at x 23.9 and 25.4 ft. Add hall control at both stairs. With Inovelli
    switches this can be a multi-tap scene on S3 and S4 instead of more boxes.
  - Family L17/L18: only S10 at the balcony door. Coming from the kitchen or the media door you cross the room.
  - Kitchen L13 to L15: only S8 at the hall door, nothing at the media door.
  - Media L9/L10 and fan L11: only S5/S6 at the hall door, nothing at the balcony door or the family door.
- **should-fix**: S10 runs family ceiling lights L17, L18 and outdoor balcony light L24 together. The balcony
  light cannot be on without the room lights on the fallback switch. L29 is beside the family door but is on
  S13 at the media door. Proposal: all four balcony lights (L23, L24, L28, L29) on one balcony control at each door.
- *nice-to-have*: the exterior stair from grade to the balcony (16 risers) has only L28 at the top landing,
  which is what the residential code asks for, but the bottom is unlit. A step light or a light at the foot helps.
- Resolved (owner decision): S6 (media fan and its light), S9 (under-cabinet L16) and S11 (bath L19, L20, fan)
  are now plain on/off switches, not dimmers and not smart-bulb mode.
- *nice-to-have*: S11 still switches the bath lights and the fan together, and an on/off switch cuts power
  to L19, L20 and the L11 fan light, so use ordinary (non-smart) lamps there. A separate fan switch or a
  humidity control would let the fan run on after the lights are off.

### Code-oriented checks (check with the electrician/inspector)
- **Bathroom**: C10 (bidet F, P15, P22) as a 20 A GFCI circuit for this one bathroom works. P15/P22 are
  within 3 ft of the vanity at the SW corner. L20 is noted wet rated. Confirm the exhaust fan circuit.
- **Kitchen circuits**: two small-appliance circuits exist (C4 counter, C5 P7 and island P14), fridge,
  microwave/hood and DW/disposal have their own. Check DW plus disposal on one 20 A against nameplates.
  GFCI/AFCI scope: finding 2.
- **Counter receptacles**: the 1.8 ft of counter south of the sink (over the DW) has no receptacle; a counter
  12 in or wider needs one. Island P14: NEC 2023 no longer allows an island receptacle on the side below the
  countertop; it must be on or above the top or a listed pop-up. *should-fix*.
- **Wall receptacle spacing** (6 ft from a door edge, 12 ft apart) measures long in a few places: kitchen north
  wall west of the hall door (7.8 ft of wall, none), family room stub south of the balcony door (7 ft to P9),
  media north wall between P3 and A (13 ft), and 6.5 ft from door edges to P6 and P7. *should-fix* at rough-in.
- **Sauna heater G**: 50 A, 240 V "per its manual" is the right approach; the manual also sets wire
  temperature rating, control location, GFCI or no GFCI and clearances. G is 1.5 ft from the door, as A.3
  shows; check the heater's door-side clearance. A disconnect within sight or a lockable breaker is the usual ask.
- **Sauna light and driver**: L21 is 4.6 ft from the heater and fed at low voltage from driver J outside the
  hot room, which is good. J sits in a W/D closet about 2.9 x 3.2 ft that the WashTower fills; it has to be
  reachable without pulling the appliance. Proposal: mount J high on the closet side wall by the door, or
  outside the closet. *should-fix*.
- **Balcony**: P11, P23, P24 on GFCI circuit C14 satisfy the balcony receptacle rule.
- **AFCI**: note it on C4 to C8 and C11 to C16 (dual-function breakers cover the GFCI ones).
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
- Every light has a switch: L1/L2 on S1+S2, L3 to L5 on S3, L6 on S4, L7 on S5, L8 on S6, L9 on S7.
- S1 (top of stairs) and S2 (by the shared door) are at the two ends of the west office. Good.
- **should-fix** (finding 5): the east office has two entries, the shared door and the attic passage, but only
  S3 at the door. L6 (small attic) is switched from the office side only (S4) and L8 (old house attic) from the
  small attic side only (S6), so walking in from the old house means crossing both in the dark.
  Proposal: a second control for L3 to L5 at the passage, and make S4 and S6 two-ended.
- *nice-to-have*: five switches (S1, S8, S9, S10, S5) stack at the top of the stairs. Inovelli scenes could
  fold S9 and S10 into one device.

### Code-oriented checks (check with the electrician/inspector)
- **Racks in the eave** (R1 to R5): behind a 5 ft knee wall in a strip about 2.8 ft deep. Confirm the roofline
  is the insulation line so the racks are inside conditioned space. See rack cooling under open questions.
- **AFCI** is noted on C3 to C8 and "confirm" on rack circuits C1 and C2. Agree; ask the inspector.
- **Sink SK**: P16 and P17 are GFCI. A sink beside network and office gear is fine with the leak sensor shown.
- **Receptacle spacing**: the west office south wall under the three windows (10.3 ft) has no receptacle, and
  Ethernet jack 6 there has no power beside it. Add one. *should-fix*.
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
- *nice-to-have*: L5 is at the east end of the porch, 6.7 ft from the porch door. Center it on the door.
- *nice-to-have*: no light on the 20 ft walk from the garage, and the shed door is on the far (south) side.

### Code-oriented checks (check with the electrician/inspector)
- **Feeder**: 60 A, 240 V is ample for a 20 A heater, one 20 A receptacle circuit and a lighting circuit.
  It needs four wires (separate neutral and ground), a disconnect at the building (a main breaker in A),
  and burial depth per the wiring method (18 in for PVC conduit).
- **Grounding electrode**: a detached building with a feeder needs its own electrode (normally two rods)
  connected to the subpanel's grounding bar. G is on the south wall and A on the north wall of the shed.
  The drawing should show G bonded to A's grounding bar, not just to a rod. **should-fix**.
- **Working clearance** at A: keep 30 in x 36 in clear in the shed. Switch 1 and P2 beside it are fine.
- **GFCI**: P1 to P6 on GFCI C2 covers the accessory-building rule. If heater B is cord-connected, its
  receptacle needs GFCI too.
- **Driver J**: "high, outside sauna" on the partition beside the sauna door is the warmest spot in the
  dressing room. Mount it low or mid-height and check its ambient rating. The low-voltage run to L1 passes
  through the hot room; use wire rated for sauna temperatures and keep it low and away from the stove.
- **Network**: the link from the garage is fiber, so there is no copper between buildings. Camera 2 has SP
  on G. AP 3 is inside. A switch in an unheated shed needs a cold-rated model. Fiber and power can share a
  trench; give the fiber its own conduit with a pull string.

## Network

### PoE budget (estimates, per device type)

Assumed draw: outdoor camera 8 W, indoor ceiling camera 5 W, outdoor AP 15 W, wall AP 13.5 W,
ceiling AP 21 W (PoE+), PoE doorbell 10 W, ESP32 presence sensor 3 W, spare PoE jack 15 W.

| Switch | Devices assumed on it | PoE ports | Estimated W | Comment |
|--------|-----------------------|-----------|-------------|---------|
| Garage 2 (SW) | cameras 3, 4; outdoor AP 5; AP 6; jacks 11 (2); sensor 12 | 7 | 78 | Needs 8 PoE ports, about 100 W and an SFP cage. |
| Garage 7 (NW) | camera 8; camera 9; outlet C computers (no PoE) | 2 | 13 | Fine for a small switch. How is 7 uplinked: fiber or copper from 2? |
| Garage 18 (under stair) | camera 10; sensors 13, 14, 15, 19, 20; AP 17; doorbell 16 | 8 | 44 | 8 PoE ports plus SFP. Too many ports for a 5-port. |
| Second floor 8 (SW closet) | sensors 1 to 6, 10 to 13; AP 9; AP 15; doorbell 14; jacks 7 (4) | 17 | 75 (105 if two jacks at 7 draw PoE) | Not a small switch. See below. |
| Third floor R1 | AP 2; AP 3; sensors 7 to 13; jacks 4, 5, 6 | 12 | 56 | Also needs fiber ports for 1, 18, 2, 8 and the shed: at least 5 SFP. |
| Shed 1 | camera 2; AP 3 | 2 | 23 | Fine. Cold-rated. |

Total is about 290 to 320 W. Budgets are fine if each switch is picked for port count, not just watts.

### Fiber paths
- Two runs (1 and 18) share one smurf tube up the riser. That is a single point of damage but acceptable;
  pull two spare strands and leave a pull string.
- The riser starts on the north wall under the garage stair (x 37 to 41 ft). Directly above is the east
  stairwell and then the east office north wall. R1 is at x 24 ft, z 14 ft on the third floor, so the run
  needs about 20 ft of horizontal travel on the third floor. See the open question for a route.
- Not shown anywhere: fiber to garage switches 2 and 7, to second-floor switch 8, and the garage end of the
  shed fiber. *should-fix*: draw them.

### Surge protection on outdoor copper
| Run | Protected? |
|-----|-----------|
| Garage cameras 3, 4, AP 5 | Yes, SP1 on G |
| Garage camera 8 | Yes, SP2 on G2 |
| Garage doorbell 16 | **No** (open question) |
| Garage jacks 11 | Plotted outdoors under the balcony; **no**, if they really are outside |
| Second-floor doorbell 14 | **No**, and no ground bar on that floor |
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
   Before deleting them, decide the opener type with finding 4 in mind. A jackshaft opener with high-lift
   track keeps the ceiling clear for lights and cord reels under a 9'5" ceiling; a trolley opener does not.
   If trolley openers stay, keep O1/O2 as ordinary GFCI wall receptacles at the jambs.
3. **Which switch feeds hallway AP 17?** Switch 18, about 6 ft away. That brings 18 to 8 PoE devices, so it
   must be an 8-port PoE+ switch with a fiber uplink.
4. **Does doorbell 16 get a surge protector?** Yes, at the switch 18 end, bonded to the service ground at MP.
   Give second-floor doorbell 14 one as well.
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
8. **WashTower model conflict.** WKEX200HBA is LG's all-electric model and needs a 30 A, 240 V receptacle;
   outlet A as drawn ("washer; gas dryer") is 120 V and suits only a gas model. Confirm the model with the
   builder. If it stays undecided at rough-in, run both the 30 A, 240 V circuit and the 20 A, 120 V laundry
   circuit plus the gas stub; the extra cable is cheap. Either way it needs a dryer exhaust to the north wall.

## All findings by rank

**Must-fix**
1. MP under the garage stair: headroom and working space (garage).
2. GFCI/AFCI scope on second-floor kitchen, laundry and living circuits (second floor).
3. Surge protection for doorbell 14, doorbell 16 and jacks 11 if outdoors (network).

**Should-fix**
4. Open doors over L5 to L8, P11, P12 (garage).
5. Lights switched from the far side: hall, family, kitchen, media, east office, attics (floors 2 and 3).
6. PoE switch sizing: 8, 2, 18; undrawn fiber links (network).
7. S4/S5 drawn in the hallway's east door opening (garage).
8. S10 mixes family lights with balcony L24; L29 on the far door's switch (second floor).
9. No counter receptacle south of the sink; island P14 position; wall spacing gaps (second floor).
10. H4 has no wall; driver J behind the WashTower (second floor).
11. Duplicate ID 6; no receptacle on the west office south wall (third floor).
12. Shed ground bar G to subpanel A bond not shown; driver J mounted high (shed).
13. Outdoor receptacles: none by the deck door (garage).

**Nice-to-have**
14. Label MP; rename device C; draw E/F green (garage).
15. E in the door opening; scene button between the overhead doors; L11/L15 mounting (garage).
16. S17 and D need real locations; screen B over the balcony door; light at the foot of the exterior stair (second floor).
17. Color key on the third-floor sheet; L7 symbol; five-gang at the top of the stairs (third floor).
18. Porch light L5 centered on the door; path light to the sauna; "East walls in line" label (shed).
19. A second-floor subpanel instead of about 24 home runs through the garage ceiling.
20. One AP too many in the middle of the building; outdoor coverage north and east.

## Scales used

| Drawing | Basis | Scale |
|---------|-------|-------|
| Garage v20 | Outline 492.0 px wide = 42'6" outside (41'6" label plus two 6 in walls); 292.9 px deep = 25'4" | 11.58 px/ft (x), 11.56 px/ft (z) |
| Second floor v20 | Outline 510.3 px = 42'6"; 303.8 px = 25'4" | 12.01 px/ft (x), 11.99 px/ft (z) |
| Third floor v32 | "Overall 42'6" wide" = 607.8 px; 361.7 px = 25'4" | 14.30 px/ft (x), 14.28 px/ft (z) |
| Sauna/shed v6 | "12 ft x 24 ft": 300 px = 12 ft | 25 px/ft |

Room labels inside each drawing (media 17'1", family 14'2" x 20'8", east office 14'0") agree with these
scales to within about 3%, so positions are good to roughly half a foot.
