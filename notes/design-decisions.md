# Design decisions (Laine addition), as of Nov 9, 2026

Source of truth: the owner's own decisions, captured while drawing the plans.
Items marked (proposed) were the designer's suggestion and are not yet confirmed.
The drawing legends in ../drawings/*.legend.txt are the device-by-device detail.

## Whole building
- Service: 400A, entering at main panel MP on the garage north wall, just east of the W/D under the stairs.
- Lighting standard: dimmable Govee ceiling lights; Inovelli White Series wall switches in smart-bulb mode
  (switches send scene/automation commands; the bulbs stay powered).
  Exception (owner decision, Nov 9, 2026): switches on non-smart loads are plain on/off, not dimmers and not
  smart-bulb mode: second-floor S6 (media fan and its light), S9 (under-cabinet L16), S11 (bath L19, L20) and S18 (bath fan, its own switch below S11),
  and third-floor S5 (closet light L7).
- Smoke/CO alarms: hardwired, interconnected, battery backup (A.2 note 9), drawn at the architect's
  locations as SD#/CO#: garage hallway SD1 + CO1, second-floor hall SD1 + CO1, third-floor west office SD1.
- Presence sensors are mostly PoE ESP32 units; normally they drive the lights, wall switches are the fallback.
- Blinds: powered smart blinds on every window, outlets high near window tops (H# items); double windows get one
  each side. No blinds on the second-floor sauna window or the balcony doors.
- Network: cable modem under the garage stairs -> media converter -> fiber up to rack R1 on the third floor.
  Two fiber runs share one smurf tube up the riser (item 1 converter, item 18 under-stair switch).
  Fiber from R1 out to small 5/8-port PoE switches near APs, cameras and computers.
  Every network switch (garage 2, 7, 18, second-floor 8, shed 1) uplinks by fiber to the aggregation switch
  that sits with the main switch in R1 (owner decision, Nov 10, 2026).
- Mini-splits shown on the architect sheets are intentionally left off the drawings.
  Their power is drawn (owner decision, Nov 10, 2026) at the four condenser positions on sheet A.2: two
  outside the garage north wall (MS1, MS2) and two outside the west wall under the exterior stair (MS3, MS4),
  each a hardwired 240V 30A connection on its own circuit (C11-C14), plus one outdoor-rated 125V 20A GFCI
  service outlet per wall on C2: P18 on the north wall, P19 on the west wall. The indoor units need no outlets.
- Rough load estimate (proposed, not a code calc): 2nd floor ~115A, 3rd ~30-40A, ~150A combined;
  two 60A EV circuits ~96A continuous; fits in 400A.

## Garage and enclosed hallway (sheet A.2, drawing v20)
- 41'6" x 24'4", 9 ft ceiling, two 16x8 doors on the south wall; balcony above west door, pergola above east door.
- "Breezeway" on the plan is an enclosed hallway ending at the stairs up to the 2nd floor over the garage.
- Under the stairs (west end): LG WashTower, electric washer + GAS dryer (builder notes say all-electric
  WKEX200HBA). Owner decision, Nov 10, 2026: run both the 20A 120V laundry circuit C9 and a 30A 240V dryer
  circuit C15, plus the gas stub, so either model fits. Cable ingress, modem and converter behind it.
- Door between the garage and the hallway (A.2), drawn Nov 10, 2026: 2868, hinged north, swings into the
  garage. S1 and S3 are a two-gang on the garage side at the door's south (latch) edge (owner decision).
- Door between the hallway and the old house (A.2), drawn Nov 10, 2026: 3068 in the hallway east wall,
  hinged north, swings into the hallway. S4 and S5 are a two-gang on the east wall at its south (latch)
  edge (owner decision).
- Front door from the hallway to the deck (A.2), drawn Nov 10, 2026: 3068 in the hallway south wall, hinged
  west, swings into the hallway.
- Outdoor outlet P21 (owner decision, Nov 10, 2026): GFCI weather-resistant, on the deck just west of the
  front door, on hallway circuit C7.
- Switch 18 is an 8-port PoE switch with a fiber port (owner decision, Nov 10, 2026).
- S2 is on the west wall near the SW corner, directly west of where it was first drawn (owner decision, Nov 10, 2026).
- Ethernet jacks 21 (owner decision, Nov 10, 2026): four data-only jacks on the north wall near switch 7, by
  outlet C. Switch 7 is an 8-port PoE switch with high outlet P20 beside it on C1. Ground bar G2 (with SP2) sits just south of the west window, about 5 ft from switch 7, and is the
  bar for surge protectors on outdoor Ethernet cables added later.
- PoE jacks 11 are inside the garage, on the east face of the short north-south wall between the overhead
  doors (owner decision, Nov 10, 2026).
- Garage Ethernet (proposed, Nov 10, 2026, not yet confirmed): sensor 12 on switch 7; APs 5, 6 and jacks 11 on
  switch 2; AP 17 and sensors 13, 14, 15, 19, 20 on switch 18. Details in REVIEW.md ("Garage Ethernet plan").
- Lights: L1-L8 garage ceiling on S1+S2 3-way; L9, L10 hallway on S4+S7 3-way; L13 deck door on S5;
  L14 under-stair on S6; outside L11/L15 flank the left door on the balcony piers, L12/L16 the right door, all on S3 (proposed).
  Garage lights are on switches only, not tied to the overhead doors.
  South row L5-L8 stays under the open doors: it is for when the doors are closed (owner decision,
  Nov 10, 2026). Both rows L1-L8 were then moved 2 ft north, away from the garage doors: now 7.2 and 16.7 ft
  from the north wall.
- Blind outlets H1-H3 (owner decision, Nov 10, 2026): one high beside the top of each garage window, on its
  left seen from inside (H1, H2 west of the north windows, H3 south of the west window), on C2.
- Stairs garage -> 2nd floor: riser lights (L8 on the 2nd-floor drawing) on 3-way E (bottom) + 2nd-floor S4 (top).
  One light in every riser from the garage floor up (owner decision, Nov 9, 2026): 2 garage door steps,
  2 hallway steps and the 13-riser flight, 17 in all, as one run.
  Stair wall lights L30-L32 on 3-way F (bottom, just north of E) + 2nd-floor S16 (top).
- Power: P1, P2, P13, P20 on C1 20A (network); P3-P7 C2 GFCI; P8-P10 C3 GFCI; ceiling cord reels P11, P12 dropped (owner decision, Nov 10, 2026); wall jackshaft
  openers O1, O2 and ceiling trolley-opener outlets O3, O4 on C4; EV1, EV2 60A 240V (C5, C6),
  moved off the north windows Nov 9, 2026: EV1 at 9.5 ft and EV2 at 26.4 ft from the west wall;
  hallway P14-P17 east wall on C7.
  Added Nov 9, 2026 (owner decision): every garage receptacle circuit is GFCI (C1-C4 and the new C8, C9).
  Outdoor outlets B, P18 and P19 on C2; outlet C (computers, printers) on new dedicated C8 20A; W/D outlet A on new
  laundry circuit C9 20A 120V; lighting is C10 15A and also feeds stair controllers D and alarms SD1, CO1.
- Grounding: G by switch 2 (SW), G2 by switch 7 (NW), bonded to the addition ground; Ethernet surge
  protectors SP1 (items 3, 4, 5) on G and SP2 (item 8) on G2.
  PoE doorbell 16 has surge protector SP3 at the switch 18 end of its cable, on ground bar G3 under the
  stair, bonded to the service ground at MP (owner decision, Nov 10, 2026). The doorbell is on the east
  (latch) side of the front door and is wired to switch 18; L13 is centred over the door.
- Windows (A.2), drawn Nov 10, 2026: two 2840 on the north wall, centred 13'8" and 29'8" from the west
  corner; one 2840 tempered on the west wall, centred 3'0" from the north corner.

## Second floor (sheet A.3, drawing v20) -- owner review in progress
- Lights: L1-L6 hall (S1, S2); L7 stair-up risers (S3 bottom + 3rd-floor S8 top); L8 stair-down risers
  (S4 + garage E); L9-L11 media (S5, S6); L12 media closet (S7); L13-L15 kitchen (S8); L16 under-cabinet (S9);
  L17, L18, L24 family/balcony (S10); L19, L20 bath (S11), bath fan on its own switch S18; L21 sauna on the heater control (DC from
  driver J); L22 W/D closet (S12); L23 balcony (S13); L25-L29 per legend.
- West stair to the 3rd floor: wall lights L33 (north leg) and L34 (west leg) on S15 (bottom) + 3rd-floor S9 (top);
  L35 ceiling light over the west (second) leg on S17 (bottom, above S15) + 3rd-floor S10 (top).
  Stair wall lights are separate from the riser lights, with switches at both ends.
- East stair wall lights L30-L32 on S16 (top, by S4) + garage F (bottom).
- Big loads: range 50A, sauna heater 50A, WashTower WKE100HVA 30A 240V, hood/microwave 20A.
- Unplanned yet: family room devices, balcony network.

## Third floor (sheet A.4, drawing v32) -- owner said "looks good" at v30
- West office 18'11" x 12'4" with the stairs and a closet; east office 14'0" wide over the family room.
- East office is fully floored over the family room for more space; the "open to family room below" on
  sheet A.4 is superseded (owner decision, Nov 9, 2026).
- Racks R1-R5 (20U) in the west clipped-ceiling strip, 6th opening empty; bookshelves B1-B5 opposite.
- Children's reading nook (owner decision, Nov 10, 2026): the low space south of the west office, between the
  P4 wall and the rack strip, is sectioned off from the racks by a thin wall on the line of the rack-strip
  west wall. Small door in its north wall from the west office; light L10 inside, switch S11 on the office
  side by the door. P5 moved east of the door; P4 moved to the office side of its wall.
- West office outlets (owner decision, Nov 10, 2026): P1 moved to the east wall near S2; P2 and P3 removed
  as not needed; P18 added on the wall below the S1/S8/S9/S10 switch stack. Then P5 moved further east; P19 added mid south
  wall under the windows, P20 at the northwest corner, and P21 near the middle of the north wall but on the
  sloped ceiling above it, because that wall is very low. Now: P1, P4, P5, P18-P21.
- Closet at the top of the stairs (owner decision, Nov 10, 2026): its door is on its north edge, off the
  top landing; L7 is inside it and is an ordinary (non-smart) light; S5 moved to that north edge by the
  door and is on/off, not a dimmer.
- Lighting review answers (owner decision, Nov 10, 2026): east office keeps the single switch S3; attic
  lights L6 (S4) and L8 (S6) stay switched from one side; the four switches at the top of the stairs stay
  separate. Reading nook light L10 is wall-mounted and cool to the touch (low ceiling), on the nook's north
  wall east of the door; S11 is mounted low (3 ft) for children and stays a
  dimmer in smart-bulb mode, so L10 must be a smart fixture or take a smart lamp. Attic outlet P15 is on the old house attic
  side of the wall.
- Lights L1-L9 on S1-S7, L10 on S11; stair risers S8; stair wall lights S9; L35 (2nd-floor stair ceiling) S10.

- Ethernet (proposed, Nov 10, 2026, not yet confirmed): APs 2, 3 and presence sensors 7 to 13 are home runs
  from one PoE switch in rack R1: Cat6A to the APs, Cat6 to the sensors, plus data-only (non-PoE) Cat6A runs to
  Ethernet jacks 4, 5 and 6; about 360 ft in all. Routes and
  lengths are in REVIEW.md ("Third-floor Ethernet plan") and drawn on lights-3d.html.

## Sauna / shed outbuilding (drawing v6)
- 12 x 24 ft south of the garage: north half porch (12x3) + dressing room (west) + wood-burning sauna (east);
  south half shed, no door between. Fed 60A 240V and fiber from the garage SW corner.
- Sauna lights (owner decision, Nov 10, 2026): L1 is strip lighting under the seating bench, like kitchen
  under-cabinet lights. Its control unit J fits a 15 x 11 in space, low on the dressing room north wall by
  the sauna door; the low-voltage wire runs low along the sauna north wall to the bench.
- Doors drawn Nov 10, 2026 (owner request): porch door from the dressing room; sauna door at the north end
  of the wall between the dressing room and the sauna. Widths (2'8" and 2'0") and swings (porch door out
  onto the porch, sauna door out into the dressing room) are the designer's assumptions.
- Ground bar G is bonded to subpanel A's grounding bar and to the shed ground rods (Nov 10, 2026).
- Lights: L1 sauna low-voltage (via control unit J), L2 dressing, L3, L4 shed, L5 porch (centered over the porch door). Switches S1, S2, S4 inside
  the porch door (currently drawn east of it; side not confirmed), S3 by the shed door.

## Open questions (not yet answered by the owner)
- Sauna/shed switches S1, S2, S4: east or west of the porch door?
- Do wall jackshaft openers O1, O2 come off now that ceiling trolley outlets O3, O4 exist?
- Which switch feeds hallway AP 17 (probably the new under-stair switch 18)?
- Are all four outside garage lights OK on one switch S3?
- Blind outlets in the gaps between the west-office south windows?
- Riser fiber path, edge switch locations, rack cooling, which switch feeds the 2nd-floor hall sensors.
