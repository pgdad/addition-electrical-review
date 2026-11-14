# Inventory (Nov 14, 2026)

Counted from `lights.json` (built from the drawings). Quantities only; models are the owner's standards
(Inovelli White Series switches, Govee dimmable lights, UniFi network gear).

## Network switches (9 devices)

| Level | Switch | Ports | Where |
|-------|--------|-------|-------|
| Garage | 2 | 8-port PoE + fiber | Southwest corner |
| Garage | 7 | 16-port PoE + fiber | Northwest corner |
| Garage | 18 | 8-port PoE + fiber | Under the stair |
| Second floor | 8 | 16-port PoE + fiber | Media closet |
| Second floor | 16 | 8-port PoE + fiber | Family room southeast corner |
| Third floor | Main switch in R1 | Not set; 15 copper ports are used by the plan, so 24-port PoE | Rack R1 |
| Third floor | Fiber aggregation switch in R1 | Not set; at least 7 fiber (SFP) ports | Rack R1 |
| Shed | 1 | Not set; feeds AP 3 and camera 2, plus fiber in (5-port PoE is enough) | North wall |

Totals by size: four 8-port, two 16-port, three not yet sized.

## Light switches (43)

| Level | Dimmer (smart-bulb mode) | On/off | Aux | Total |
|-------|--------------------------|--------|-----|-------|
| Garage / hallway | 5 | 0 | 3 | 8 |
| Second floor | 12 | 4 | 5 | 21 |
| Third floor | 6 | 1 | 3 | 10 |
| Shed | 4 | 0 | 0 | 4 |
| **Total** | **27** | **5** | **11** | **43** |

The 11 aux switches each need a traveler to their main switch (11 three-way pairs).
The hall and stair wall lights and their 8 switches were removed on Nov 14, 2026.

## Light fixtures (60 entries)

| Level | Ceiling | Wall | Outdoor | Stair riser runs | Under-cabinet | Low-voltage | Total |
|-------|---------|------|---------|------------------|---------------|---------------------|-------|
| Garage / hallway | 11 | 0 | 5 | 0 | 0 | 0 | 16 |
| Second floor | 17 | 0 | 4 | 2 | 1 | 5 | 29 |
| Third floor | 9 | 1 | 0 | 0 | 0 | 0 | 10 |
| Shed | 2 | 1 | 1 | 0 | 0 | 1 | 5 |
| **Total** | **39** | **2** | **10** | **2** | **1** | **6** | **60** |

The two riser runs are counted as one entry each (one light per riser: 17 risers on the garage stair,
16 on the west stair). They are listed on the second-floor sheet.
Low-voltage: the two sauna lights (second floor L21, shed L1) and the four island floor lights L36-L39 (Nov 12, 2026).

## Presence sensors (23)

| Level | Ceiling | Wall | Total |
|-------|---------|------|-------|
| Garage / hallway | 2 | 4 | 6 |
| Second floor | 6 | 4 | 10 |
| Third floor | 0 | 7 | 7 |
| Shed | 0 | 0 | 0 |
| **Total** | **8** | **15** | **23** |

## Cameras (6)

| Level | Outdoor | Indoor | Total |
|-------|---------|--------|-------|
| Garage / hallway | 3 | 2 | 5 |
| Sauna / shed | 1 | 0 | 1 |
| **Total** | **4** | **2** | **6** |

The same counts are shown live in the "Inventory" section at the bottom of `lights-3d.html`.

## Fiber segments (7)

Six switch uplinks to the aggregation switch in R1 (garage 2, 7, 18; second floor 8, 16; shed 1), plus the
fiber from the garage modem to R1.

## Ethernet jack locations (8 locations, 20 jacks)

| Level | Location | Jacks |
|-------|----------|-------|
| Garage | 11, wall between the overhead doors | 2 |
| Garage | 21, north wall by outlet P22 | 4 |
| Garage | 22, north wall between EV1 and EV2 | 2 |
| Second floor | 7, projector wall | 4 |
| Second floor | 17, media room south wall, high by H3 | 2 |
| Third floor | 4, floor box by R2 | 2 |
| Third floor | 5, floor box by B1 | 2 |
| Third floor | 14, west office south wall | 2 |
