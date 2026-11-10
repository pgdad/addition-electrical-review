#!/usr/bin/env python3
"""Build lights.json and refresh the embedded data block in lights-3d.html.

Positions come from the SVG symbols (tools/svgdev.py); everything else (rooms, mounting type,
switching, circuits) is transcribed from the drawing legends and notes/design-decisions.md.

    python3 tools/build_lights.py
"""
import json, re
from svgdev import ROOT, SCALES, devices, to_ft

# ---- elevations (ft above the garage slab), from A.2 stair data and room labels -------------------
HALL_FLOOR = 1.08            # hallway is 2 risers up; 9'5" garage ceiling - 8'4" hallway ceiling
F2 = 10.46                   # hallway floor + 15 risers x 7.5" (9'4.5")
F3 = F2 + 10.15              # + 16 risers x 7-9/16" (10'1.75")
G_CEIL = 9.42                # A.2: garage 9'5" (notes say 9 ft)
FLOOR = {"G": 0.0, "2": F2, "3": F3, "S": 0.0}
LEVEL_NAME = {"G": "Garage and hallway", "2": "Second floor", "3": "Third floor", "S": "Sauna / shed"}
SOURCE = {k: "drawings/" + v[0] for k, v in SCALES.items()}

def east_stair_h(x):         # garage -> 2nd floor flight, rises going west from x=42.5 to x=32.4
    x = min(max(x, 32.4), 42.5)
    return 2.33 + (42.5 - x) / 10.1 * (F2 - 2.33)

def west_north_leg_h(x):     # 2nd -> 3rd, first leg rises going west from x=9.6 to x=4.2 (7 risers)
    x = min(max(x, 4.2), 9.6)
    return F2 + (9.6 - x) / 5.4 * 4.41

def west_leg_h(z):           # second leg rises going south from z=4.4 to z=10.2 (8 risers)
    z = min(max(z, 4.4), 10.2)
    return F2 + 4.41 + (z - 4.4) / 5.8 * 5.04

# ---- light metadata: id -> (room, type, height rule, circuit, note) --------------------------------
# height rule: number = ft above that level's floor; callable(x, z) = absolute ft.
G_LIGHT_CCT = "C10 garage lighting, 15A"
L2_CCT = "C15/C16 lighting, 15A (split not given on v20)"
LIGHTS = {
 "G": {
  **{f"L{i}": ("4-car garage", "ceiling", G_CEIL, G_LIGHT_CCT, "") for i in range(1, 9)},
  "L9":  ("Hallway", "ceiling", HALL_FLOOR + 8.33, G_LIGHT_CCT, "Hallway ceiling is 8'4\" above its own floor (A.2)"),
  "L10": ("Hallway", "ceiling", HALL_FLOOR + 8.33, G_LIGHT_CCT, ""),
  "L11": ("Outside, left (west) door", "outdoor", 6.5, G_LIGHT_CCT, "Mounted on the balcony pier"),
  "L15": ("Outside, left (west) door", "outdoor", 6.5, G_LIGHT_CCT, "Mounted on the balcony pier"),
  "L12": ("Outside, right (east) door", "outdoor", 6.5, G_LIGHT_CCT, ""),
  "L16": ("Outside, right (east) door", "outdoor", 6.5, G_LIGHT_CCT, ""),
  "L13": ("Outside, deck door", "outdoor", HALL_FLOOR + 6.5, G_LIGHT_CCT, ""),
  "L14": ("Under the garage stairs", "ceiling", lambda x, z: east_stair_h(x) - 1.0, G_LIGHT_CCT, "Mounted on the stair soffit; height follows the stair"),
 },
 "2": {
  **{f"L{i}": ("Hall", "wall", 6.5, L2_CCT, "North wall") for i in range(1, 7)},
  "L7":  ("West stair up to 3rd floor", "riser", None, L2_CCT, "Riser lights; 14 drawn for 16 risers"),
  "L8":  ("East stair down to garage", "riser", None, L2_CCT, "One light mid each riser from the garage floor up: 2 garage door steps, 2 hallway steps, 13-riser flight (17)"),
  "L9":  ("Media room", "ceiling", 9.0, L2_CCT, ""),
  "L10": ("Media room", "ceiling", 9.0, L2_CCT, ""),
  "L11": ("Media room", "ceiling", 8.2, L2_CCT, "Ceiling fan with light"),
  "L12": ("Media closet (under west stair)", "ceiling", 7.5, L2_CCT, ""),
  "L13": ("Kitchen", "ceiling", 9.0, L2_CCT, ""),
  "L14": ("Kitchen", "ceiling", 9.0, L2_CCT, ""),
  "L15": ("Kitchen island", "ceiling", 6.5, L2_CCT, "Pendant, hung to about 6.5 ft"),
  "L16": ("Kitchen, east counter", "under-cabinet", 4.5, L2_CCT, "Strip under the upper cabinets"),
  "L17": ("Family room", "ceiling", 9.0, L2_CCT, "Flat 9 ft ceiling under the third-floor east office"),
  "L18": ("Family room", "ceiling", 9.0, L2_CCT, "Flat 9 ft ceiling under the third-floor east office"),
  "L19": ("Bath", "ceiling", 9.0, L2_CCT, ""),
  "L20": ("Shower", "ceiling", 9.0, L2_CCT, "Wet rated"),
  "L21": ("Sauna", "low-voltage", 6.5, "C3 (driver J, 15A)", "Sauna rated, DC from driver J in the W/D closet"),
  "L22": ("W/D closet", "ceiling", 8.5, L2_CCT, ""),
  "L23": ("Balcony, by media door", "outdoor", 6.5, L2_CCT, ""),
  "L24": ("Balcony, by family door", "outdoor", 6.5, L2_CCT, ""),
  "L25": ("Under the west stair", "ceiling", lambda x, z: west_leg_h(z) - 1.0, L2_CCT, "On the stair soffit"),
  "L26": ("Under the west stair", "ceiling", lambda x, z: west_leg_h(z) - 1.0, L2_CCT, "On the stair soffit"),
  "L27": ("Under the west stair", "ceiling", lambda x, z: west_leg_h(z) - 1.0, L2_CCT, "On the stair soffit"),
  "L28": ("Balcony, west end", "outdoor", 8.0, L2_CCT, "High wall light"),
  "L29": ("Balcony, by family door", "outdoor", 8.0, L2_CCT, "High wall light"),
  "L30": ("East stair down to garage", "wall", lambda x, z: east_stair_h(x) + 6.5, L2_CCT, "6.5 ft above the tread below it"),
  "L31": ("East stair down to garage", "wall", lambda x, z: east_stair_h(x) + 6.5, L2_CCT, "6.5 ft above the tread below it"),
  "L32": ("East stair down to garage", "wall", lambda x, z: east_stair_h(x) + 6.5, L2_CCT, "6.5 ft above the tread below it"),
  "L33": ("West stair, north leg", "wall", lambda x, z: west_north_leg_h(x) + 6.5, L2_CCT, "6.5 ft above the tread below it"),
  "L34": ("West stair, west leg", "wall", lambda x, z: west_leg_h(z) + 6.5, L2_CCT, "6.5 ft above the tread below it"),
  "L35": ("West stair, west leg", "ceiling", lambda x, z: F3 + 7.8, L2_CCT, "Ceiling above the second leg (third-floor ceiling height)"),
 },
 "3": {
  "L1": ("West office", "ceiling", 8.0, "C7 lighting, 15A", ""),
  "L2": ("West office", "ceiling", 8.0, "C7 lighting, 15A", ""),
  "L3": ("East office", "ceiling", 8.0, "C7 lighting, 15A", ""),
  "L4": ("East office", "ceiling", 8.0, "C7 lighting, 15A", ""),
  "L5": ("East office (south)", "ceiling", 8.0, "C7 lighting, 15A", ""),
  "L6": ("Small attic", "ceiling", 6.5, "C7 lighting, 15A", ""),
  "L7": ("West office closet", "ceiling", 7.0, "C7 lighting, 15A", "Ordinary (non-smart) light, because S5 is a plain on/off switch"),
  "L8": ("Old house attic", "ceiling", 6.5, "C7 lighting, 15A", ""),
  "L9": ("East office sink nook", "ceiling", 7.0, "C7 lighting, 15A", "Short track light"),
  "L10": ("Children's reading nook", "wall", 4.5, "C7 lighting, 15A", "Wall-mounted, cool-to-the-touch LED on the nook's north wall (low sloped ceiling); smart fixture or smart lamp, since S11 is in smart-bulb mode; 4.5 ft height assumed"),
 },
 "S": {
  "L1": ("Sauna room, under the seating bench", "low-voltage", 1.5, "C3 (control unit J, 15A)", "Strip lights under the bench, heat rated; low-voltage wire runs low along the sauna north wall from control unit J"),
  "L2": ("Dressing room", "wall", 2.5, "C3, 15A", "Legend says 'low lights'; drawn low on the wall as an assumption"),
  "L3": ("Shed", "ceiling", 8.0, "C3, 15A", ""),
  "L4": ("Shed", "ceiling", 8.0, "C3, 15A", ""),
  "L5": ("Porch", "outdoor", 7.5, "C3, 15A", "Porch ceiling, centered over the porch door"),
 },
}

# ---- switches: (level, id) -> (room, [controlled light keys]) ---------------------------------------
def k(level, *ids): return [f"{level}:{i}" for i in ids]
def rng(level, a, b): return [f"{level}:L{i}" for i in range(a, b + 1)]
SWITCHES = {
 ("G", "S1"): ("Garage side of the hall door, at its south (latch) edge, two-gang with S3", rng("G", 1, 8)),
 ("G", "S2"): ("Garage west wall, near the SW corner", rng("G", 1, 8)),
 ("G", "S3"): ("Garage side of the hall door, at its south (latch) edge, two-gang with S1", k("G", "L11", "L12", "L15", "L16")),
 ("G", "S4"): ("Hallway east wall, south (latch) edge of the old-house door, two-gang with S5", k("G", "L9", "L10")),
 ("G", "S7"): ("Hallway, west wall by the garage door", k("G", "L9", "L10")),
 ("G", "S5"): ("Hallway east wall, south (latch) edge of the old-house door, two-gang with S4", k("G", "L13")),
 ("G", "S6"): ("Garage, at the under-stair space", k("G", "L14")),
 ("G", "E"):  ("Hallway, foot of the stairs", k("2", "L8")),
 ("G", "F"):  ("Hallway, foot of the stairs", k("2", "L30", "L31", "L32")),
 ("2", "S1"): ("Hall, south wall", rng("2", 1, 3)),
 ("2", "S2"): ("Hall, south wall", rng("2", 4, 6)),
 ("2", "S3"): ("Hall, foot of the west stair", k("2", "L7")),
 ("2", "S4"): ("Hall, head of the east stair", k("2", "L8")),
 ("2", "S5"): ("Media room, by the hall door", k("2", "L9")),
 ("2", "S24"): ("Media room, by the hall door, between S5 and S6", k("2", "L10")),
 ("2", "S6"): ("Media room, by the hall door", k("2", "L11")),
 ("2", "S7"): ("Media room, by the closet door", k("2", "L12")),
 ("2", "S8"): ("Kitchen, by the hall door", k("2", "L13", "L14", "L15")),
 ("2", "S9"): ("Kitchen, by the hall door", k("2", "L16")),
 ("2", "S10"): ("Family room, by the balcony door", k("2", "L17", "L18", "L24")),
 ("2", "S11"): ("Bath, by its door", k("2", "L19", "L20")),
 ("2", "S18"): ("Bath, by its door (fan only, no light)", []),
 ("2", "S19"): ("Hall, foot of the west stair (companion to S1)", rng("2", 1, 3)),
 ("2", "S20"): ("Hall, head of the east stair (companion to S2)", rng("2", 4, 6)),
 ("2", "S21"): ("Kitchen side of the media/kitchen door, latch edge (companion to S8)", k("2", "L13", "L14", "L15")),
 ("2", "S22"): ("Media room, east wall at the north edge of the kitchen door (companion to S5)", k("2", "L9")),
 ("2", "S25"): ("Media room, east wall at the north edge of the kitchen door (companion to S24)", k("2", "L10")),
 ("2", "S26"): ("Family room, north end of the wall shared with the bath (companion to S10)", k("2", "L17", "L18", "L24")),
 ("2", "S23"): ("Media room, east wall at the north edge of the kitchen door (companion to S6)", k("2", "L11")),
 ("2", "S12"): ("Kitchen side of the W/D closet", k("2", "L22")),
 ("2", "S13"): ("Media room, west (latch) side of the balcony door, below the window", k("2", "L23", "L28", "L29")),
 ("2", "S14"): ("Media room west wall, beside AP 9", rng("2", 25, 27)),
 ("2", "S15"): ("Hall, foot of the west stair", k("2", "L33", "L34")),
 ("2", "S16"): ("Hall, head of the east stair", k("2", "L30", "L31", "L32")),
 ("2", "S17"): ("Hall, foot of the west stair (above S15)", k("2", "L35")),
 ("3", "S1"): ("West office, top of the stairs", k("3", "L1", "L2")),
 ("3", "S2"): ("West office, by the shared door", k("3", "L1", "L2")),
 ("3", "S3"): ("East office, by the shared door", k("3", "L3", "L4", "L5")),
 ("3", "S4"): ("East office, north of the attic passage", k("3", "L6")),
 ("3", "S5"): ("Top stair landing, north edge of the closet by its door", k("3", "L7")),
 ("3", "S6"): ("Small attic, by the old-house entry", k("3", "L8")),
 ("3", "S7"): ("Sink nook, north end", k("3", "L9")),
 ("3", "S8"): ("West office, top of the stairs", k("2", "L7")),
 ("3", "S9"): ("West office, top of the stairs", k("2", "L33", "L34")),
 ("3", "S10"): ("West office, top of the stairs", k("2", "L35")),
 ("3", "S11"): ("West office, beside the reading nook door, mounted low at 3 ft", k("3", "L10")),
 ("S", "S1"): ("Dressing room, inside the porch door", k("S", "L2")),
 ("S", "S2"): ("Dressing room, inside the porch door", k("S", "L1")),
 ("S", "S4"): ("Dressing room, inside the porch door", k("S", "L5")),
 ("S", "S3"): ("Shed, inside the shed door", k("S", "L3", "L4")),
}
# 3-way pairs (one colour per pair in the model)
PAIRS = [
 (["G:S1", "G:S2"], "#ff8a3d"), (["G:S4", "G:S7"], "#4dd0e1"),
 (["G:E", "2:S4"], "#ffd54f"), (["G:F", "2:S16"], "#ba68c8"),
 (["2:S3", "3:S8"], "#81c784"), (["2:S15", "3:S9"], "#f06292"),
 (["2:S17", "3:S10"], "#64b5f6"), (["3:S1", "3:S2"], "#e57373"),
 (["2:S1", "2:S19"], "#aed581"), (["2:S2", "2:S20"], "#4db6ac"), (["2:S8", "2:S21"], "#ffb74d"),
 (["2:S5", "2:S22"], "#9575cd"), (["2:S6", "2:S23"], "#a1887f"), (["2:S24", "2:S25"], "#f48fb1"), (["2:S10", "2:S26"], "#90caf9"),
]
HALL_SWITCHES = {"G:S4", "G:S5", "G:S7", "G:E", "G:F"}   # stand on the raised hallway floor

# ---- outlets: (ids, description, kind, height above the floor in ft, circuit). Heights are assumptions:
# 1.5 ft wall, 3.7 ft counter, ceiling height for ceiling outlets, 7 ft or so for blind outlets.
# kind: wall | counter | ceiling | floor | outdoor | blind | appliance | hardwired
GC = 9.42
OUTLETS = {
 "G": [
  ("A", "W/D outlets under the stairs: 120V 20A and 240V 30A, plus a gas stub, so either WashTower model fits", "appliance", 3.0, "C9 laundry 20A 120V GFCI and C15 dryer 30A 240V"),
  ("B", "Outdoor outlet, AirGradient, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
  ("C", "Computers and printers outlet, GFCI", "wall", 1.5, "C8 dedicated, 20A GFCI"),
  ("P1 P2", "Under the stairs, network gear, GFCI", "wall", 1.5, "C1 dedicated, 20A GFCI"),
  ("P13", "High outlet beside network switch 2, GFCI", "wall", 7.0, "C1 dedicated, 20A GFCI"),
  ("P20", "High outlet on the north wall beside network switch 7, GFCI", "wall", 7.0, "C1 dedicated, 20A GFCI"),
  ("P3 P4 P5", "Garage north wall, GFCI", "wall", 1.5, "C2, 20A GFCI"),
  ("H1 H2", "Blind outlet, high on the west side of a north window", "blind", 7.0, "C2, 20A GFCI"),
  ("H3", "Blind outlet, high on the south side of the west window", "blind", 7.0, "C2, 20A GFCI"),
  ("P6 P7", "Garage west wall, GFCI", "wall", 1.5, "C2, 20A GFCI"),
  ("P8 P9 P10", "Garage east wall, GFCI", "wall", 1.5, "C3, 20A GFCI"),
  ("O1 O2", "Wall (jackshaft) opener outlet, GFCI", "wall", 8.0, "C4, 20A GFCI"),
  ("O3 O4", "Ceiling outlet for a trolley opener, GFCI", "ceiling", GC, "C4, 20A GFCI"),
  ("EV1", "EV charger, hardwired", "hardwired", 4.0, "C5, 60A 240V"),
  ("EV2", "EV charger, hardwired", "hardwired", 4.0, "C6, 60A 240V"),
  ("P14 P15 P16 P17", "Hallway east wall", "wall", 1.5, "C7, 20A GFCI + AFCI"),
  ("P21", "Outdoor outlet on the deck, west of the front door, GFCI weather-resistant", "outdoor", 2.6, "C7, 20A; GFCI receptacle"),
  ("MS1", "Mini-split condenser, hardwired, north wall", "hardwired", 2.0, "C11, 30A 240V"),
  ("MS2", "Mini-split condenser, hardwired, north wall", "hardwired", 2.0, "C12, 30A 240V"),
  ("MS3", "Mini-split condenser, hardwired, west wall", "hardwired", 2.0, "C13, 30A 240V"),
  ("MS4", "Mini-split condenser, hardwired, west wall", "hardwired", 2.0, "C14, 30A 240V"),
  ("P18", "Outdoor service outlet, north wall, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
  ("P19", "Outdoor service outlet, west wall, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
 ],
 "2": [
  ("A", "Projector wall, 4 outlets", "wall", 1.5, "C11 media, 20A AFCI"),
  ("B", "Motorized screen, smart control", "appliance", 8.0, "C11 media, 20A AFCI"),
  ("C", "Media closet outlet", "wall", 1.5, "C11 media, 20A AFCI"),
  ("E", "Range receptacle", "appliance", 0.5, "C1, 50A 240V GFCI"),
  ("F", "Bidet outlet, GFCI", "wall", 1.5, "C10 bath, 20A GFCI"),
  ("G", "Sauna heater, hardwired per its manual", "hardwired", 1.0, "C2, 50A 240V"),
  ("K", "Fridge", "appliance", 3.5, "C6, 20A GFCI + AFCI"),
  ("M", "Dishwasher and disposal", "appliance", 1.5, "C7, 20A GFCI + AFCI"),
  ("N", "Microwave/hood above the range", "appliance", 6.0, "C8, 20A GFCI + AFCI"),
  ("W", "WashTower WKE100HVA", "appliance", 3.0, "C9, 30A 240V GFCI"),
  ("P1 P2", "Hall, south wall", "wall", 1.5, "C12, 20A AFCI"),
  ("P3 P4 P5 P6", "Media room", "wall", 1.5, "C11 media, 20A AFCI"),
  ("P7", "Kitchen, west wall, GFCI", "wall", 1.5, "C5 kitchen, 20A GFCI + AFCI"),
  ("P8 P9 P10 P21", "Family room", "wall", 1.5, "C12, 20A AFCI"),
  ("P11 P23 P24", "Balcony, weatherproof GFCI", "outdoor", 1.5, "C14 balcony, 20A GFCI"),
  ("P12 P13", "Kitchen counter, GFCI", "counter", 3.7, "C4 counter, 20A GFCI + AFCI"),
  ("P25 P26", "Kitchen counter south of the sink, GFCI", "counter", 3.7, "C4 counter, 20A GFCI + AFCI"),
  ("P14", "Kitchen island, GFCI", "counter", 3.0, "C5 kitchen, 20A GFCI + AFCI"),
  ("P15 P22", "Bath west wall, GFCI", "counter", 3.5, "C10 bath, 20A GFCI"),
  ("P16 P17 P18", "Under the stairs up", "wall", 1.5, "C13, 20A AFCI"),
  ("P19 P20", "Media room, by S7", "wall", 1.5, "C13, 20A AFCI"),
  ("H1 H2", "Blind outlet, hall window, high", "blind", 7.5, "C12, 20A AFCI"),
  ("H3 H4", "Blind outlet, media windows, high", "blind", 7.5, "C12, 20A AFCI"),
  ("H5 H6", "Blind outlet, family windows, high", "blind", 7.5, "C12, 20A AFCI"),
 ],
 "3": [
  ("A", "Duplex outlet inside rack R2", "wall", 1.5, "C1 dedicated, 20A"),
  ("B", "Duplex outlet inside rack R4", "wall", 1.5, "C2 dedicated, 20A"),
  ("E", "Spare home run, boxed in rack R3", "wall", 1.5, "C8 spare, 20A"),
  ("C D", "Floor power outlet, east office", "floor", 0.1, "C4 east office desks, 20A"),
  ("P18", "West office, below the switch stack at the top of the stairs", "wall", 1.5, "C3 west office, 20A"),
  ("P19", "West office south wall, mid-wall under the windows", "wall", 1.5, "C3 west office, 20A"),
  ("P20", "West office north wall, northwest corner", "wall", 1.5, "C3 west office, 20A"),
  ("P21", "West office, on the sloped ceiling just above the low north wall, mid-wall", "ceiling", 5.5, "C3 west office, 20A"),
  ("P1 P4 P5", "West office wall outlet", "wall", 1.5, "C3 west office, 20A"),
  ("P6 P7 P11 P12", "East office wall outlet", "wall", 1.5, "C5 east office perimeter, 20A"),
  ("P8 P9 P10", "East office wall outlet", "wall", 1.5, "C4 east office desks, 20A"),
  ("P13 P14", "Small attic", "wall", 1.5, "C6 sink and attics, 20A AFCI/GFCI"),
  ("P15", "Old house attic side of the wall", "wall", 1.5, "C6 sink and attics, 20A AFCI/GFCI"),
  ("P16 P17", "Near the sink, GFCI", "counter", 3.7, "C6 sink and attics, 20A AFCI/GFCI"),
  ("H1 H2", "Blind outlet, west office south windows, high", "blind", 6.5, "C3 west office, 20A"),
  ("H3 H4 H5", "Blind outlet, east office windows, high", "blind", 6.5, "C5 east office perimeter, 20A"),
 ],
 "S": [
  ("B", "Space heater outlet, dressing room", "appliance", 1.5, "C1 heater, 20A"),
  ("P1", "Dressing room outlet, GFCI", "wall", 1.5, "C2, 20A GFCI"),
  ("P4 P6", "Shed outlet, GFCI", "wall", 1.5, "C2, 20A GFCI"),
 ],
}
HALL_OUTLETS = {"P14", "P15", "P16", "P17"}

# ---- network: Wi-Fi access points and network switches (the numbered network items on each sheet).
# level -> [(item number, kind ap|switch, name, where, height above the floor in ft (assumed), note)]
NETWORK = {
 "G": [
  ("2", "switch", "PoE switch", "Garage southwest corner, high beside outlet P13", 7.0, "Feeds cameras 3 and 4, outdoor AP 5, AP 6 and jacks 11"),
  ("7", "switch", "8-port PoE switch", "Garage northwest corner, north wall, beside outlet P20", 7.0, "Feeds cameras 8 and 9, sensor 12 and jacks 21"),
  ("18", "switch", "8-port PoE switch with a fiber port", "Under the garage stairs", 3.0, "Fiber to the third-floor rack R1"),
  ("5", "ap", "Outdoor AP", "Outside the garage south wall, facing south", 9.0, "Outdoor copper run; surge protector SP1"),
  ("6", "ap", "UniFi wall AP", "Garage, mid west wall", 7.0, ""),
  ("16", "doorbell", "PoE video doorbell", "Outside the front door, on its east (latch) side", 4.0, "Outdoor copper run: surge protector SP3 on ground bar G3 at switch 18"),
  ("17", "ap", "UniFi wall AP", "Hallway north wall", 7.0, "Feeding switch not confirmed (probably 18)"),
 ],
 "2": [
  ("8", "switch", "16-port PoE switch with a fiber port", "Media closet, southwest", 5.0, "West half of the floor, the projector jacks and doorbell 14 (via SP1 on GB1)"),
  ("16", "switch", "8-port PoE switch with a fiber port", "Family room, southeast corner, high by blind outlet H6", 7.0, "East half of the floor; powered from the H6 box (make it a duplex)"),
  ("14", "doorbell", "PoE video doorbell", "Balcony, on the wall north of the family room door", 4.0, "Outdoor copper run: surge protector SP1 on ground bar GB1 at switch 8"),
  ("9", "ap", "UniFi wall AP", "Media room west wall", 7.0, ""),
  ("15", "ap", "UniFi ceiling AP", "Kitchen / family room border", 8.9, ""),
 ],
 "3": [
  ("1", "switch", "Rack R1: main switch and fiber aggregation switch", "West clipped strip, rack R1", 3.0, "Every other network switch uplinks here by fiber; fiber in from the garage modem"),
  ("2", "ap", "UniFi ceiling AP", "East office ceiling", 6.4, ""),
  ("3", "ap", "UniFi wall AP", "West office east wall, south of the door", 6.0, ""),
 ],
 "S": [
  ("1", "switch", "PoE switch", "Shed north wall", 5.0, "Fiber in from the garage"),
  ("3", "ap", "Outdoor PoE AP", "Inside the shed north wall", 7.0, ""),
 ],
}
# ---- Ethernet runs (proposed, third floor only so far): level -> (switch item, [(device item, cable, PoE W (0 = data only),
# plan waypoints, route, optional route height in ft above the floor; negative = in the floor framing)])
ROUTE_H, CABLE_SLACK = {"3": 7.0, "G": 8.8, "2": 8.6}, 8.0     # per level: ft above the floor for the horizontal run; ft of service loop (5 at the rack, 3 at the device)
_N = "North bundle: up from R1, north above the wall between the offices"
_S = "South bundle: up from R1, south above the rack strip to the south wall"
CABLES = {
 "3": [("1", [
  ("2",  "Cat6A", 21, [(24.05, 13.59)], "Straight east above the east office ceiling"),
  ("3",  "Cat6A", 13, [(24.6, 14.16), (24.6, 11.35)], _N + ", drop to the AP"),
  ("7",  "Cat6", 3, [(24.6, 14.16), (24.6, 5.4)], _N + ", over the door header, drop on the west face"),
  ("8",  "Cat6", 3, [(24.6, 14.16), (24.6, 5.4)], _N + ", over the door header, drop on the east face"),
  ("9",  "Cat6", 3, [(24.6, 14.16), (24.6, 1.06)], _N + " to the north wall, then east"),
  ("10", "Cat6", 3, [(24.6, 14.16), (24.6, 1.06)], _N + " to the north wall, then east past the windows"),
  ("11", "Cat6", 3, [(24.6, 14.16), (24.6, 24.17)], _S + ", then east"),
  ("12", "Cat6", 3, [(24.6, 14.16), (24.6, 24.17)], _S + ", then east past the window"),
  ("13", "Cat6", 3, [(24.05, 12.7), (3.84, 12.7)], "West above the nook wall and the west office ceiling to the closet, then north to the stair wall"),
 ])],
 # Garage: each device goes to the nearest of the three switches. Cameras 3, 4, 8, 9, 10 and doorbell 16 also land on
 # these switches (see the PoE table in REVIEW.md) but are not drawn on the page.
 "G": [
  ("2", [
   ("5",  "Cat6A", 13, [(4.18, 20.75)], "Up from switch 2, east along the south wall, out through the wall to the AP (surge protector SP1)"),
   ("6",  "Cat6A", 13, [], "Up from switch 2, north along the west wall, drop to the AP"),
   ("11", "Cat6A", 15, [(1.2, 21.6), (21.6, 21.6)], "Up from switch 2, east along the south wall above the west door, through to the east face of the wall between the doors", None, 2),
  ]),
  ("7", [
   ("12", "Cat6", 3, [(11.81, 1.2)], "Up from switch 7, east along the north wall, then out across the ceiling"),
   ("21", "Cat6A", 0, [(1.2, 0.3)], "Up from switch 7, a few feet east inside the north wall, down to the jack plates", None, 4),
  ]),
  ("18", [
   ("17", "Cat6A", 13, [(41.15, 1.12)], "Up from switch 18, east through the stair wall into the hallway north wall"),
   ("13", "Cat6", 3, [(41.15, 4.26)], "Up from switch 18, out of the under-stair space, west across the garage ceiling"),
   ("14", "Cat6", 3, [(41.15, 1.12)], "Up from switch 18, east through the stair wall to the hallway north wall"),
   ("20", "Cat6", 3, [(41.15, 3.28)], "Up from switch 18, east across the landing to the hallway east wall"),
   ("19", "Cat6", 3, [(41.15, 2.2), (47.4, 2.2)], "Hallway bundle: east to the hallway east wall, then south along it"),
   ("15", "Cat6", 3, [(41.15, 2.2), (47.4, 2.2), (47.4, 21.55)], "Hallway bundle: east to the hallway east wall, south along it, then west to the doorway"),
   ("16", "Cat6", 10, [(41.15, 2.2), (47.4, 2.2), (47.4, 22.5)], "From SP3 at switch 18 with the hallway bundle down the east wall, out through the south wall beside the front door"),
  ]),
 ],
}
# Second floor (proposed): west half on switch 8 in the SW closet, east half on switch 16 in the family room SE corner.
_W8 = "Up from switch 8 in the closet, "
_E16 = "Up from switch 16, "
CABLES["2"] = [
  ("8", [
   ("9",  "Cat6A", 13, [(2.19, 10.82)], _W8 + "north in the closet wall, drop to the AP on the media west wall"),
   ("1",  "Cat6", 3, [(1.0, 15.71)], _W8 + "north along the west wall of the stairwell to the landing"),
   ("5",  "Cat6", 3, [(8.1, 15.71)], _W8 + "east above the media ceiling, then north"),
   ("6",  "Cat6", 3, [(16.86, 15.71)], _W8 + "east above the media ceiling, then north"),
   ("3",  "Cat6", 3, [(19.96, 15.71)], _W8 + "east above the media ceiling, then north into the hall ceiling"),
   ("7",  "Cat6A", 15, [(13.49, 15.71)], _W8 + "east above the media ceiling, north to the projector wall, down inside it", None, 4),
   ("14", "Cat6", 10, [(2.19, 16.5), (20.9, 16.5)], "From SP1 at switch 8 east along the media south wall, out to the balcony, along the wall to the doorbell"),
  ]),
  ("16", [
   ("15", "Cat6A", 21, [(28.75, 23.2)], _E16 + "west above the family room ceiling, then north to the AP"),
   ("12", "Cat6", 3, [(26.23, 23.2)], _E16 + "west along the south wall, then north"),
   ("13", "Cat6", 3, [(38.45, 23.2)], _E16 + "east through the wall into the bath ceiling"),
   ("10", "Cat6", 3, [(35.3, 10.14)], _E16 + "north above the family room and kitchen ceilings, then east"),
   ("11", "Cat6", 3, [(35.3, 6.09)], _E16 + "north above the kitchen ceiling, then west"),
   ("4",  "Cat6", 3, [(35.3, 2.2)], _E16 + "north to the hall ceiling, then west to the kitchen door"),
   ("2",  "Cat6", 3, [(35.3, 0.85)], _E16 + "north to the hall north wall, then east above the stair to the corner"),
  ]),
]
# ---- fiber uplinks (owner decision): every network switch runs fiber to the aggregation switch in rack R1 on the third floor.
# (switch level, switch item, [(level, x, height above that level's floor (None = switch height), z), ...] ending at R1, route)
RISER = (39.5, 0.6)              # under the garage stair, up the north wall beside the east stairwell
_UP = [("G", *RISER[:1], 8.8, RISER[1]), ("3", RISER[0], 7.0, RISER[1]), ("3", 24.6, 7.0, 0.6), ("3", 24.6, 7.0, 14.16)]
FIBER = [
 ("G", "18", [("G", 41.15, 8.8, 1.46)] + _UP, "Up from switch 18 to the riser beside it, up the north wall to the third-floor north eave, west, then south above the office wall to R1"),
 ("G", "7",  [("G", 1.2, 8.8, 1.2), ("G", 1.2, 8.8, 0.6)] + _UP, "East along the garage north wall to the riser, then up and across the third floor to R1"),
 ("G", "2",  [("G", 1.2, 8.8, 20.75), ("G", 0.6, 8.8, 20.75), ("G", 0.6, 8.8, 0.6)] + _UP, "North along the garage west wall, east along the north wall to the riser, then up to R1"),
 ("S", "1",  [("S", -0.5, 5.0, 54.64), ("S", -0.5, -2.0, 54.64), ("G", -0.5, -2.0, 21.4), ("G", 0.6, -2.0, 21.4), ("G", 0.6, 8.8, 21.4), ("G", 0.6, 8.8, 0.6)] + _UP,
  "Buried conduit from the shed to the garage SW corner, up inside, then with the switch 2 fiber to the riser and R1"),
 ("2", "16", [("2", 35.3, 8.6, 23.2), ("3", 35.3, -0.6, 24.8), ("3", 24.6, -0.6, 24.8), ("3", 24.6, -0.6, 14.16)],
  "Up the family room southeast corner into the third-floor floor framing, west along the south wall, north under the rack strip, up into R1"),
 ("2", "8",  [("2", 2.19, 8.6, 15.71), ("2", 24.05, 8.6, 15.71), ("2", 24.05, 8.6, 14.16)], "East above the second-floor ceiling to below the rack strip, then straight up through the floor into R1"),
]
FIBER_SLACK = 15.0
# Ethernet jacks (non-PoE data drops): level -> [(item, where, height above the floor in ft)]
JACKS = {
 "3": [("4", "Floor jack, east edge of the west clipped strip, across from R2", 0.1),
       ("5", "Floor jack, west edge of the east clipped strip, across from B1", 0.1),
       ("6", "Wall jack, west office south wall, east of the windows", 1.5)],
}
JACKS["2"] = [("7", "Four PoE jacks on the projector wall (media north wall)", 1.5, "Four jacks, PoE available (15 W each assumed)")]
JACKS["G"] = [("21", "Four Ethernet jacks on the north wall by outlet C, near switch 7", 1.5, "Four jacks, data only, no PoE"),
              ("11", "Two PoE jacks at 7 ft, inside the garage on the east face of the short wall between the overhead doors", 7.0, "Two jacks, PoE available (15 W each assumed); indoors, so no surge protector needed")]
for _lv, _rows in JACKS.items():
    for _i, _where, _h, *_note in _rows: NETWORK[_lv].append((_i, "jack", "Ethernet jack", _where, _h, _note[0] if _note else "Data only, no PoE"))
_F = "Floor run: down from R1 into the floor framing, south then east under the east office floor"
CABLES["3"][0][1].extend([
  ("4",  "Cat6A", 0, [(24.05, 16.12)], _F + ", up into the floor box", -0.6),
  ("5",  "Cat6A", 0, [(24.05, 16.12)], _F + " to the far floor box", -0.6),
  ("6",  "Cat6A", 0, [(24.05, 12.7), (14.12, 12.7)], "West bundle with sensor 13 above the west office ceiling, then south and down inside the south wall"),
])
HALL_NET = {"17", "14", "15", "16", "19", "20"}
# presence sensors (PoE ESP32 units): level -> [(item numbers, where, height above the floor in ft, assumed)]
SENSORS = {
 "G": [("12", "Garage ceiling, west half", 9.3), ("13", "Garage ceiling, east half", 9.3),
       ("14", "Hallway north wall, faces south", 7.0), ("15", "Hallway, over the garage doorway", 7.0),
       ("19", "Hallway east wall, watches the garage doorway", 7.0), ("20", "Hallway east wall at the landing, sees up the stairs", 7.0)],
 "2": [("1", "Hall, above the west stair landing", 7.0), ("2", "Hall, high northeast corner, faces west", 8.0),
       ("3", "Hall ceiling, media door", 8.9), ("4", "Hall ceiling, kitchen door", 8.9), ("5 6", "Media room ceiling", 8.9),
       ("10", "Kitchen, sink and dishwasher", 8.9), ("11", "Near the hallway entry door", 7.0), ("12", "Near the balcony door", 7.0),
       ("13", "Bath ceiling", 8.9)],
 "3": [("7", "West office east wall, north of the door, facing west", 6.0), ("8", "East office side of the same wall, facing east", 6.0),
       ("9 10", "East office north wall, beside the windows", 6.0), ("11 12", "East office south wall, beside the window", 6.0),
       ("13", "South wall at the top of the stairs, facing north down the stairs", 6.0)],
}
for _lv, _rows in SENSORS.items():
    for _ids, _where, _h in _rows:
        for _i in _ids.split(): NETWORK[_lv].append((_i, "sensor", "PoE presence sensor", _where, _h, ""))

def east_riser_points():     # one light mid each riser, garage slab -> 2nd floor (17 risers)
    rise, run = (F2 - 2.33) / 13, 10.1 / 13
    pts = [[40.83 - 0.04, 0.27, 6.91], [41.67 - 0.04, 0.81, 6.91]]                   # garage door steps (DN 2R on A.2)
    pts += [[44.85, HALL_FLOOR + 0.31, 5.23 + 0.04], [44.85, HALL_FLOOR + 0.94, 4.4 + 0.04]]   # hallway steps to the landing
    pts += [[42.5 - i * run + 0.04, 2.33 + (i + 0.5) * rise, 2.17] for i in range(13)]   # flight west along the north wall
    return [[round(v, 2) for v in p] for p in pts]

def build():
    lights, switches = [], []
    dev = {lv: devices(lv) for lv in SCALES}
    controlled_by = {}
    for (lv, sid), (_, ctl) in SWITCHES.items():
        for lk in ctl: controlled_by.setdefault(lk, []).append(f"{lv}:{sid}")
    for lv, table in LIGHTS.items():
        for lid, (room, typ, h, cct, note) in table.items():
            d = dev[lv][lid]
            pts_ft = [to_ft(lv, *p) for p in d["pts"]]
            points = None
            if lid == "L8" and lv == "2":
                points = east_riser_points()
            elif typ == "riser":
                points = []
                for (x, z) in pts_ft:
                    if lid == "L8": y = east_stair_h(x) - 0.3
                    elif abs(z - pts_ft[0][1]) < 0.01: y = west_north_leg_h(x) + 0.33     # north leg dots
                    else: y = west_leg_h(z) + 0.33                                       # west leg dots
                    points.append([x, round(y, 2), z])
            elif d["shape"] == "rect":                      # strips: L16 (2nd floor), L9 (3rd floor)
                (cx, cz), (w, hh) = d["pts"][0], d["size"]
                y = FLOOR[lv] + h
                a = to_ft(lv, cx, cz - hh / 2); b = to_ft(lv, cx, cz + hh / 2)
                points = [[a[0], round(y, 2), a[1]], [b[0], round(y, 2), b[1]]]
            if points:
                x = round(sum(p[0] for p in points) / len(points), 2)
                y = round(sum(p[1] for p in points) / len(points), 2)
                z = round(sum(p[2] for p in points) / len(points), 2)
            else:
                x, z = pts_ft[0]
                y = round(h(x, z) if callable(h) else FLOOR[lv] + h, 2)
            key = f"{lv}:{lid}"
            rec = dict(key=key, id=lid, level=lv, levelName=LEVEL_NAME[lv], room=room, x=x, y=y, z=z,
                       type=typ, switches=controlled_by.get(key, []), circuit=cct, source=SOURCE[lv])
            if key == "2:L21": rec["control"] = "Sauna heater control (no wall switch)"
            if note: rec["note"] = note
            if points: rec["points"] = points
            lights.append(rec)
    pair_of = {}
    for members, color in PAIRS:
        for m in members: pair_of[m] = ([x for x in members if x != m][0], color)
    for (lv, sid), (room, ctl) in SWITCHES.items():
        key = f"{lv}:{sid}"
        src = "S15" if key == "2:S17" else sid            # S17 is "above S15": same box position
        x, z = to_ft(lv, *dev[lv][src]["pts"][0])
        base = HALL_FLOOR if key in HALL_SWITCHES else FLOOR[lv]
        y = base + {"2:S17": 4.7, "3:S11": 3.0}.get(key, 4.0)    # S11 is low so children can reach it
        if key in ("G:S4", "G:S5"): x, z = 47.4, (20.0 if sid == "S4" else 20.5)  # two-gang on the east wall, just south of the door jamb at 19.6 ft
        if key in ("G:S1", "G:S3"): x, z = 42.2, (9.1 if sid == "S1" else 9.6)   # two-gang on the wall, just south of the door jamb at 8.7 ft
        if key == "3:S6": x = 47.4                      # sheet draws the small attic narrower than A.4; keep S6 on its east wall
        rec = dict(key=key, id=sid, level=lv, levelName=LEVEL_NAME[lv], room=room, x=x, y=round(y, 2), z=z,
                   controls=ctl, source=SOURCE[lv])
        if key in pair_of: rec["pairWith"], rec["pairColor"] = pair_of[key]
        rec["mode"] = "on/off" if key in ("2:S6", "2:S9", "2:S11", "2:S18", "2:S23", "3:S5") else "smart-bulb dimmer"
        switches.append(rec)
    outlets = []
    for lv, rows in OUTLETS.items():
        for ids, desc, kind, h, cct in rows:
            for oid in ids.split():
                src = {"3:P18": "S9"}.get(f"{lv}:{oid}", oid)      # P18 is drawn off the wall with a leader; it sits under the switches
                x, z = to_ft(lv, *dev[lv][src]["pts"][0])
                if f"{lv}:{oid}" == "3:P15": x = 48.0     # old house attic side of the wall (A.4 wall at 47.67 ft)
                if lv == "2" and oid in ("P25", "P26"): x = 42.2   # drawn on the wall line; they are on the counter backsplash
                if (lv, oid) == ("G", "P21"): x, z = 43.3, 23.1  # outside face of the hallway south wall, west of the front door
                if (lv, oid) == ("G", "P20"): x, z = 2.0, 0.3   # drawn below switch 7; it is on the north wall beside it
                if lv == "G" and oid in ("H1", "H2"): z = 0.3   # drawn on the wall line; inside face of the north wall
                if lv == "G" and oid == "H3": x = 0.3           # drawn outside the wall line to clear G2; inside face of the west wall
                base = 0.0 if kind in ("outdoor",) and lv == "G" or oid.startswith("MS") else (HALL_FLOOR if (lv == "G" and oid in HALL_OUTLETS) else FLOOR[lv])
                outlets.append(dict(key=f"{lv}:{oid}", id=oid, level=lv, levelName=LEVEL_NAME[lv], room=desc, kind=kind,
                                    x=x, y=round(base + h, 2), z=z, circuit=cct, source=SOURCE[lv]))
    network = []
    for lv, rows in NETWORK.items():
        for nid, kind, name, where, h, note in rows:
            x, z = to_ft(lv, *dev[lv][nid]["pts"][0])
            if (lv, nid) == ("G", "21"): z = 0.3            # drawn below C to clear it; it is on the north wall
            base = HALL_FLOOR if (lv == "G" and nid in HALL_NET) else FLOOR[lv]
            rec = dict(key=f"{lv}:N{nid}", id=nid, level=lv, levelName=LEVEL_NAME[lv], kind=kind, name=name, room=where,
                       x=x, y=round(base + h, 2), z=z, source=SOURCE[lv])
            if note: rec["note"] = note
            network.append(rec)
    # Ethernet runs (proposed): home runs from the level's switch, routed above the ceiling at ROUTE_H, with
    # plan waypoints (x, z) between the two ends. Length = 3D path + CABLE_SLACK, rounded up to 5 ft.
    net_by = {n["key"]: n for n in network}
    cables = []
    for lv, sw, rows in [(lv, sw, rows) for lv, groups in CABLES.items() for sw, rows in groups]:
        a = net_by[f"{lv}:N{sw}"]
        port = 0
        for nid, cat, watts, via, route, *opt in rows:
            d = net_by[f"{lv}:N{nid}"]
            count = opt[1] if len(opt) > 1 else 1
            port += 1
            h = FLOOR[lv] + (opt[0] if opt and opt[0] is not None else ROUTE_H[lv])
            pts = [(a["x"], a["y"], a["z"]), (a["x"], h, a["z"])] + [(x, h, z) for x, z in via] + [(d["x"], h, d["z"]), (d["x"], d["y"], d["z"])]
            run = sum(sum((p[i] - q[i]) ** 2 for i in range(3)) ** 0.5 for p, q in zip(pts, pts[1:]))
            length = int(-(-(run + CABLE_SLACK) // 5) * 5)
            cables.append(dict(key=f"{lv}:C{nid}", level=lv, **{"from": a["key"], "to": d["key"]}, cable=cat, poeW=watts * count, count=count,
                               port=str(port) if count == 1 else f"{port}-{port + count - 1}",
                               lengthFt=length, route=route, points=[[round(v, 2) for v in p] for p in pts]))
            port += count - 1
            d["cable"] = cables[-1]["key"]
    # fiber uplinks: explicit path, each point tagged with the level whose map it is drawn on
    agg = net_by["3:N1"]
    fibers = []
    for lv, sw, path, route in FIBER:
        a = net_by[f"{lv}:N{sw}"]
        tagged = [(lv, a["x"], a["y"], a["z"])] + [(l, x, FLOOR[l] + h, z) for l, x, h, z in path] + [("3", agg["x"], agg["y"], agg["z"])]
        pts = [t[1:] for t in tagged]
        run = sum(sum((p[i] - q[i]) ** 2 for i in range(3)) ** 0.5 for p, q in zip(pts, pts[1:]))
        plan = {}
        for l, x, y, z in tagged: plan.setdefault(l, []).append([round(x, 2), round(z, 2)])
        fibers.append(dict(key=f"{lv}:F{sw}", **{"from": a["key"], "to": agg["key"]}, cable="Fiber, duplex single-mode (OS2), LC",
                           lengthFt=int(-(-(run + FIBER_SLACK) // 5) * 5), route=route, levels=sorted(plan), plan=plan,
                           points=[[round(v, 2) for v in p] for p in pts]))
        a["fiber"] = fibers[-1]["key"]
    for lv in SCALES:                                   # every plotted P#, O#, EV#, H#, MS# is in the outlet table
        plotted = {n for n in dev[lv] if re.fullmatch(r"(P|O|EV|H|MS)\d+", n)}
        have = {o["id"] for o in outlets if o["level"] == lv}
        assert plotted <= have, (lv, plotted - have)
    # sanity: every plotted L# is in the data and vice versa
    for lv in SCALES:
        plotted = {n for n in dev[lv] if re.fullmatch(r"L\d+", n)}
        assert plotted == set(LIGHTS[lv]), (lv, plotted ^ set(LIGHTS[lv]))
        sw = {n for n, d in dev[lv].items() if re.fullmatch(r"S\d+", n)} | ({"E", "F"} if lv == "G" else set())
        assert sw == {s for (l, s) in SWITCHES if l == lv}, (lv, sw ^ {s for (l, s) in SWITCHES if l == lv})
    return dict(
        units="feet",
        axes="x = east, z = south, y = up; origin = garage NW exterior corner at the garage slab",
        scales={lv: dict(drawing=SOURCE[lv], px_per_ft_x=round(v[2], 3), px_per_ft_y=round(v[3], 3)) for lv, v in SCALES.items()},
        floors=dict(garage=0.0, hallway=HALL_FLOOR, second=F2, third=round(F3, 2), shed=0.0),
        lights=lights, switches=switches, outlets=outlets, network=network, cables=cables, fibers=fibers)

if __name__ == "__main__":
    data = build()
    (ROOT / "lights.json").write_text(json.dumps(data, indent=1) + "\n")
    html = ROOT / "lights-3d.html"
    if html.exists():
        s = html.read_text()
        block = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
        s2, n = re.subn(r'(<script id="lights-data" type="application/json">).*?(</script>)',
                        lambda m: m.group(1) + "\n" + block + "\n" + m.group(2), s, flags=re.S)
        assert n == 1, "data block not found in lights-3d.html"
        html.write_text(s2)
    print(len(data["lights"]), "lights,", len(data["switches"]), "switches")
