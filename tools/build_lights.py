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
  "L7": ("West office closet", "ceiling", 7.0, "C7 lighting, 15A", "Plotted 1.3 ft south of the closet outline"),
  "L8": ("Old house attic", "ceiling", 6.5, "C7 lighting, 15A", ""),
  "L9": ("East office sink nook", "ceiling", 7.0, "C7 lighting, 15A", "Short track light"),
  "L10": ("Children's reading nook", "ceiling", 6.0, "C7 lighting, 15A", "Low sloped ceiling behind the 5 ft office wall (A.4 shows attic here); 6 ft height assumed"),
 },
 "S": {
  "L1": ("Sauna room", "low-voltage", 6.5, "C3 (driver J, 15A)", "Heat rated, DC from driver J"),
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
 ("G", "S1"): ("Garage, inside the hall door", rng("G", 1, 8)),
 ("G", "S2"): ("Garage, SW corner", rng("G", 1, 8)),
 ("G", "S3"): ("Garage, inside the hall door", k("G", "L11", "L12", "L15", "L16")),
 ("G", "S4"): ("Hallway, east wall by the deck door", k("G", "L9", "L10")),
 ("G", "S7"): ("Hallway, west wall by the garage door", k("G", "L9", "L10")),
 ("G", "S5"): ("Hallway, east wall by the deck door", k("G", "L13")),
 ("G", "S6"): ("Garage, at the under-stair space", k("G", "L14")),
 ("G", "E"):  ("Hallway, foot of the stairs", k("2", "L8")),
 ("G", "F"):  ("Hallway, foot of the stairs", k("2", "L30", "L31", "L32")),
 ("2", "S1"): ("Hall, south wall", rng("2", 1, 3)),
 ("2", "S2"): ("Hall, south wall", rng("2", 4, 6)),
 ("2", "S3"): ("Hall, foot of the west stair", k("2", "L7")),
 ("2", "S4"): ("Hall, head of the east stair", k("2", "L8")),
 ("2", "S5"): ("Media room, by the hall door", k("2", "L9", "L10")),
 ("2", "S6"): ("Media room, by the hall door", k("2", "L11")),
 ("2", "S7"): ("Media room, by the closet door", k("2", "L12")),
 ("2", "S8"): ("Kitchen, by the hall door", k("2", "L13", "L14", "L15")),
 ("2", "S9"): ("Kitchen, by the hall door", k("2", "L16")),
 ("2", "S10"): ("Family room, by the balcony door", k("2", "L17", "L18", "L24")),
 ("2", "S11"): ("Bath, by its door", k("2", "L19", "L20")),
 ("2", "S18"): ("Bath, by its door (fan only, no light)", []),
 ("2", "S12"): ("Kitchen side of the W/D closet", k("2", "L22")),
 ("2", "S13"): ("Media room, by the balcony door", k("2", "L23", "L28", "L29")),
 ("2", "S14"): ("Media room west wall, beside AP 9", rng("2", 25, 27)),
 ("2", "S15"): ("Hall, foot of the west stair", k("2", "L33", "L34")),
 ("2", "S16"): ("Hall, head of the east stair", k("2", "L30", "L31", "L32")),
 ("2", "S17"): ("Hall, foot of the west stair (above S15)", k("2", "L35")),
 ("3", "S1"): ("West office, top of the stairs", k("3", "L1", "L2")),
 ("3", "S2"): ("West office, by the shared door", k("3", "L1", "L2")),
 ("3", "S3"): ("East office, by the shared door", k("3", "L3", "L4", "L5")),
 ("3", "S4"): ("East office, north of the attic passage", k("3", "L6")),
 ("3", "S5"): ("West office, beside the closet", k("3", "L7")),
 ("3", "S6"): ("Small attic, by the old-house entry", k("3", "L8")),
 ("3", "S7"): ("Sink nook, north end", k("3", "L9")),
 ("3", "S8"): ("West office, top of the stairs", k("2", "L7")),
 ("3", "S9"): ("West office, top of the stairs", k("2", "L33", "L34")),
 ("3", "S10"): ("West office, top of the stairs", k("2", "L35")),
 ("3", "S11"): ("West office, beside the reading nook door", k("3", "L10")),
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
]
HALL_SWITCHES = {"G:S4", "G:S5", "G:S7", "G:E", "G:F"}   # stand on the raised hallway floor

# ---- outlets: (ids, description, kind, height above the floor in ft, circuit). Heights are assumptions:
# 1.5 ft wall, 3.7 ft counter, ceiling height for ceiling outlets, 7 ft or so for blind outlets.
# kind: wall | counter | ceiling | floor | outdoor | blind | appliance | hardwired
GC = 9.42
OUTLETS = {
 "G": [
  ("A", "W/D outlet under the stairs (washer; gas dryer), GFCI", "appliance", 3.0, "C9 laundry, 20A 120V GFCI"),
  ("B", "Outdoor outlet, AirGradient, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
  ("C", "Computers and printers outlet, GFCI", "wall", 1.5, "C8 dedicated, 20A GFCI"),
  ("P1 P2", "Under the stairs, network gear, GFCI", "wall", 1.5, "C1 dedicated, 20A GFCI"),
  ("P13", "High outlet beside network switch 2, GFCI", "wall", 7.0, "C1 dedicated, 20A GFCI"),
  ("P3 P4 P5", "Garage north wall, GFCI", "wall", 1.5, "C2, 20A GFCI"),
  ("P6 P7", "Garage west wall, GFCI", "wall", 1.5, "C2, 20A GFCI"),
  ("P8 P9 P10", "Garage east wall, GFCI", "wall", 1.5, "C3, 20A GFCI"),
  ("P11 P12", "Garage ceiling, cord reel, GFCI", "ceiling", GC, "C4, 20A GFCI"),
  ("O1 O2", "Wall (jackshaft) opener outlet, GFCI", "wall", 8.0, "C4, 20A GFCI"),
  ("O3 O4", "Ceiling outlet for a trolley opener, GFCI", "ceiling", GC, "C4, 20A GFCI"),
  ("EV1", "EV charger, hardwired", "hardwired", 4.0, "C5, 60A 240V"),
  ("EV2", "EV charger, hardwired", "hardwired", 4.0, "C6, 60A 240V"),
  ("P14 P15 P16 P17", "Hallway east wall", "wall", 1.5, "C7, 20A"),
  ("MS1", "Mini-split condenser, hardwired, north wall", "hardwired", 2.0, "C11, 30A 240V"),
  ("MS2", "Mini-split condenser, hardwired, north wall", "hardwired", 2.0, "C12, 30A 240V"),
  ("MS3", "Mini-split condenser, hardwired, west wall", "hardwired", 2.0, "C13, 30A 240V"),
  ("MS4", "Mini-split condenser, hardwired, west wall", "hardwired", 2.0, "C14, 30A 240V"),
  ("P18", "Outdoor service outlet, north wall, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
  ("P19", "Outdoor service outlet, west wall, GFCI weather-resistant", "outdoor", 1.5, "C2, 20A GFCI"),
 ],
 "2": [
  ("A", "Projector wall, 4 outlets", "wall", 1.5, "C11 media, 20A"),
  ("B", "Motorized screen, smart control", "appliance", 8.0, "C11 media, 20A"),
  ("C", "Media closet outlet", "wall", 1.5, "C11 media, 20A"),
  ("E", "Range receptacle", "appliance", 0.5, "C1, 50A 240V"),
  ("F", "Bidet outlet, GFCI", "wall", 1.5, "C10 bath, 20A GFCI"),
  ("G", "Sauna heater, hardwired per its manual", "hardwired", 1.0, "C2, 50A 240V"),
  ("K", "Fridge", "appliance", 3.5, "C6, 20A"),
  ("M", "Dishwasher and disposal", "appliance", 1.5, "C7, 20A"),
  ("N", "Microwave/hood above the range", "appliance", 6.0, "C8, 20A"),
  ("W", "WashTower WKE100HVA", "appliance", 3.0, "C9, 30A 240V"),
  ("P1 P2", "Hall, south wall", "wall", 1.5, "C12, 20A"),
  ("P3 P4 P5 P6", "Media room", "wall", 1.5, "C11 media, 20A"),
  ("P7", "Kitchen, west wall, GFCI", "wall", 1.5, "C5 kitchen, 20A GFCI"),
  ("P8 P9 P10 P21", "Family room", "wall", 1.5, "C12, 20A"),
  ("P11 P23 P24", "Balcony, weatherproof GFCI", "outdoor", 1.5, "C14 balcony, 20A GFCI"),
  ("P12 P13", "Kitchen counter, GFCI", "counter", 3.7, "C4 counter, 20A GFCI"),
  ("P14", "Kitchen island, GFCI", "counter", 3.0, "C5 kitchen, 20A GFCI"),
  ("P15 P22", "Bath west wall, GFCI", "counter", 3.5, "C10 bath, 20A GFCI"),
  ("P16 P17 P18", "Under the stairs up", "wall", 1.5, "C13, 20A"),
  ("P19 P20", "Media room, by S7", "wall", 1.5, "C13, 20A"),
  ("H1 H2", "Blind outlet, hall window, high", "blind", 7.5, "C12, 20A"),
  ("H3 H4", "Blind outlet, media windows, high", "blind", 7.5, "C12, 20A"),
  ("H5 H6", "Blind outlet, family windows, high", "blind", 7.5, "C12, 20A"),
 ],
 "3": [
  ("A", "Duplex outlet inside rack R2", "wall", 1.5, "C1 dedicated, 20A"),
  ("B", "Duplex outlet inside rack R4", "wall", 1.5, "C2 dedicated, 20A"),
  ("E", "Spare home run, boxed in rack R3", "wall", 1.5, "C8 spare, 20A"),
  ("C D", "Floor power outlet, east office", "floor", 0.1, "C4 east office desks, 20A"),
  ("P18", "West office, below the switch stack at the top of the stairs", "wall", 1.5, "C3 west office, 20A"),
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
  ("P2 P3 P4 P5 P6", "Shed outlet, GFCI", "wall", 1.5, "C2, 20A GFCI"),
 ],
}
HALL_OUTLETS = {"P14", "P15", "P16", "P17"}

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
        y = base + (4.7 if key == "2:S17" else 4.0)
        rec = dict(key=key, id=sid, level=lv, levelName=LEVEL_NAME[lv], room=room, x=x, y=round(y, 2), z=z,
                   controls=ctl, source=SOURCE[lv])
        if key in pair_of: rec["pairWith"], rec["pairColor"] = pair_of[key]
        rec["mode"] = "on/off" if key in ("2:S6", "2:S9", "2:S11", "2:S18") else "smart-bulb dimmer"
        switches.append(rec)
    outlets = []
    for lv, rows in OUTLETS.items():
        for ids, desc, kind, h, cct in rows:
            for oid in ids.split():
                src = {"3:P18": "S9"}.get(f"{lv}:{oid}", oid)      # P18 is drawn off the wall with a leader; it sits under the switches
                x, z = to_ft(lv, *dev[lv][src]["pts"][0])
                base = 0.0 if kind in ("outdoor",) and lv == "G" or oid.startswith("MS") else (HALL_FLOOR if (lv == "G" and oid in HALL_OUTLETS) else FLOOR[lv])
                outlets.append(dict(key=f"{lv}:{oid}", id=oid, level=lv, levelName=LEVEL_NAME[lv], room=desc, kind=kind,
                                    x=x, y=round(base + h, 2), z=z, circuit=cct, source=SOURCE[lv]))
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
        lights=lights, switches=switches, outlets=outlets)

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
