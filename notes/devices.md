# Purchased devices

Specific products the owner has already bought (owner, Nov 15, 2026). Specifications are copied from the
product pages on Nov 15, 2026; where a page does not state something, the table says so. More devices will be
added to this section.

## Low-voltage lights (stair risers and island floor)

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Low-voltage light | [GekPower 4 inch Linear Step Light, white, 24V 0.6W, 3000K](https://gekpower.com/products/4-inch-linear-step-light-24v-0-6w-cct2-7k-3k-3-5k-4k-5k-white?variant=47782360154349) | Stair riser lights L7 and L8, island floor lights L36-L39, media room floor lights L44 and L45, hall floor lights L46-L51 | Model VBD-COB-24V-100L-xxxx-STP4-White; 24 V DC; 0.6 W; 100 lm; dimmable; IP20 (indoor); 94 x 22 x 9.7 mm; 2 ft lead; certification not stated |
| Matter controller | [MiBoxer SMZ2 Matter over Thread LED dimmer](https://www.ledbe.com/miboxer-smz2-matter-over-thread-led-dimmer.html) | Stair light controllers D, island controller T, media room controller U, hall controller V | 12-24 V DC in; 12 A max output; single-color or dual-white mode; Matter over Thread and 2.4 GHz remote; IP20; 74.5 x 36 x 17 mm; CE, EMC, RED; UL listing not stated |
| 24 V power supply | [Mean Well XLG-75-24-A LED power supply](https://www.amazon.com/dp/B07W93ZGWL) | Feeds the controllers (owner confirmed, Nov 16, 2026) | From the listing title, read Nov 16, 2026: 74.4 W; 24 V output (adjustable 16.8-24 V); 3.1 A; constant voltage and constant current; output current adjustable by a built-in potentiometer; metal case with wire leads; input 100-305 V AC. Listing marks and enclosure rating not read: check the label or the Mean Well datasheet |

The linked step-light variant is the 3000K one. The page also offers 2700K, 3500K, 4000K and 5000K.

## Control and power (owner, Nov 15, 2026)

- No wall switch is needed for the low-voltage lights. The Matter controllers that run them should not be
  powered off, so they stay powered all the time and the lights are controlled through Matter.
- Each stairway has two independently controlled segments of lights, so two controllers per stairway, four
  stair controllers in all (owner, Nov 16, 2026). On the drawings they are the two D symbols: garage sheet D for
  the east stair, second-floor D for the west stair.
- West stair split: the lower segment is every riser light east of the landing in the northwest corner (the
  north leg, 7 lights); the upper segment is the rest (the west leg, 9 lights).
- East stair split: the lowest 7 riser lights on one controller, the other 10 on the second.
- The second-floor hallway has one controller for all its low-voltage lights.
- The kitchen island lights all share a single controller.
- The two media room low-voltage lights L44 and L45 share one controller, U (owner, Nov 16, 2026; this replaces
  the earlier note of one controller per light).
- The power supplies can be arranged as the electrician decides (for example one supply per controller, or one
  supply shared by several controllers).

| Area | Controllers |
|------|-------------|
| East (garage) stair (risers L8) | 2 (D, garage sheet): lowest 7 lights; the other 10 |
| West stair (risers L7) | 2 (D, second-floor sheet): north leg 7 lights; west leg 9 lights |
| Second-floor hallway (L46-L51) | 1 (V) |
| Kitchen island (L36-L39) | 1 |
| Media room (L44, L45) | 1 (U) |

Placement notes:

- Placed on Nov 16, 2026: media room lights L44 and L45 on the south wall, about 6 in. above the floor, at about
  25% and 75% of the room width; hall lights L46-L51 on the hall north wall at the same height, about 4 ft apart.
  The six hall lights and the positions of controllers U and V were confirmed by the owner on Nov 16, 2026.
- East stair (Nov 16, 2026): switches S4 and garage S8 no longer run riser lights L8; they now run the new stair
  ceiling lights L52, L53. The west stair riser-light switches (second floor S3, third floor S8) were
  removed on Nov 16, 2026, and so was the island light switch S27. No low-voltage light has a wall switch now.
- The east stair "lowest 7" is read here as the 2 garage door steps, the 2 hallway steps and the first 3 risers
  of the flight. The owner should correct this if the 7 are counted differently.
- The second-floor sheet now shows all 16 west stair riser lights (it showed 14 before Nov 16, 2026).

## Load on each run

| Run | Lights | Load at 0.6 W each | Current at 24 V |
|-----|--------|--------------------|-----------------|
| East stair risers L8, lower segment | 7 | 4.2 W | 0.18 A |
| East stair risers L8, upper segment | 10 | 6.0 W | 0.25 A |
| West stair risers L7, north leg | 7 | 4.2 W | 0.18 A |
| West stair risers L7, west leg | 9 | 5.4 W | 0.23 A |
| Island floor lights L36-L39 | 4 | 2.4 W | 0.10 A |
| Media room floor lights L44, L45 | 2 | 1.2 W | 0.05 A |
| Hall floor lights L46-L51 | 6 | 3.6 W | 0.15 A |

Each run is far below the controller's 12 A limit. All seven runs together are 27 W (about 1.1 A at 24 V), so
any one 74.4 W Mean Well supply has room to spare for the runs it feeds. How many supplies there are and where
they sit is the electrician's decision.

## Low-voltage lights: check with the electrician/inspector

- The step-light page lists no safety certification and the controller page lists CE only (no UL or ETL listing
  stated). Ask whether the inspector accepts them, and whether the 24 V supply must be a listed Class 2 supply.
- The controllers and the step lights are IP20, for dry indoor places only. They are not assumed for the sauna
  lights (second floor L21, shed L1), which stay on control unit J.
- Each controller and its power supply must stay reachable after the walls and the island are closed.
- The Mean Well supply has a constant-current stage with an adjustable limit. For these lights it should run as
  a plain 24 V constant-voltage supply; ask the electrician to check the potentiometer setting.

## Inovelli White Series smart switches

The owner has the Smart Dimmer, the Smart On/Off and the Smart Fan switch from the
[Inovelli White Series](https://inovelli.com/collections/inovelli-white-series) (owner, Nov 15, 2026). All are
Thread / Matter, 120 V. Specifications are copied from the product pages on Nov 15, 2026.

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Smart dimmer | [White Series 2-in-1 Smart Dimmer, VTM31-SN](https://inovelli.com/products/thread-matter-white-series-smart-2-1-on-off-dimmer-switch) | The 27 dimmer positions (26 in smart-bulb mode, plus media fan switch S6 with no load) | Max 600 W incandescent, 300 W LED, 150 W CFL; lighting only, not for fans, outlets or other motor loads; smart-bulb mode; works with or without a neutral (no neutral: bypass needed, no energy monitoring); multi-way with the Aux switch; UL certified E528330 |
| Smart on/off | [White Series Smart On/Off Switch, VTM30-SN](https://inovelli.com/products/thread-matter-white-series-smart-on-off-switch-w-humidity) | The 4 on/off positions | Max 1500 W general purpose, 960 W incandescent, 300 W LED/CFL; may run any fan or outlet within the load limit; built-in temperature and humidity sensors; neutral wire required; ETL certified |
| Smart fan switch | [White Series Smart Fan Switch, VTM35-SN](https://inovelli.com/products/thread-matter-white-series-smart-fan-switch-3-speed-ceiling-on-off-exhaust) | Not assigned on the drawings; see the next part | Max 2.5 A, no more than 2 fans; AC motors only, DC motors not supported; not for lighting; no neutral: low and medium speed only and not usable on an exhaust fan; ETL certified 5027290 |
| Aux switch | [Inovelli Add-On (Aux) Switch](https://inovelli.com/products/white-series-add-on-aux-switch) | The 12 aux positions (owner to confirm these are bought) | Not a smart switch; needs a traveler to its main switch; works with or without a neutral; UL certified E528330 |

The switch counts are from the drawings (see the inventory). The two outdoor motion sensors are not Inovelli
switches.

## Smart Fan switch on the shower and bathroom exhaust fans (to be checked)

The owner expects that the Smart Fan switch can not be used for the shower and bathroom exhaust fans. The
product page does not rule it out completely, but it sets conditions that many bath fans do not meet:

- The fan must have an AC motor. DC motors are not supported, and many quiet bath fans have DC motors.
- The switch box must have a neutral wire. Without one, the page says the switch can not be used on an exhaust fan.
- The fan must draw no more than 2.5 A.
- The page lists a known incompatibility with the Broan / NuTone 696-R02 and 688-K fans.
- For an exhaust fan with a light on the same feed, and for DC-motor fans, Inovelli points to the Smart On/Off
  switch instead.

What to check, with the electrician:

- The make, model and motor type (AC or DC) of each exhaust fan, and its nameplate current.
- If a fan fails any condition above, use the Smart On/Off switch for it. Its humidity sensor can also turn the
  fan on by itself. The drawings already show the bath fan switch S18 as an on/off switch, so this needs no
  drawing change.
- There will be separate shower and bathroom fans (owner, Nov 16, 2026). The electrician decides the fans, their
  positions and their switches. The drawings still show one bath fan switch (second floor S18); the shower fan
  and its switch are not drawn until the electrician has decided.
- The media room fan L11 does not use the Smart Fan switch; see "Media room ceiling fan" below.

## Govee lights

Govee smart lights chosen by the owner (owner, Nov 15, 2026). Specifications are copied from the product pages on
Nov 15, 2026. The plan already puts Govee lights on Inovelli dimmers in smart-bulb mode, which keeps the lights
powered all the time.

### Indoor ceiling lights

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Ceiling light | [Govee 18-Inch Ceiling Light Pro, round, H1250](https://us.govee.com/products/govee-18-inch-ceiling-light-pro?variant=47293730095289) | Media room L9 and L10 (2 lights). Third-floor east office L3, L4, L5 (3 lights). 5 in all | 120 V; 55 W; 4800 lm; 2700K-6500K white plus color; 200 LEDs; Bluetooth, Wi-Fi and Matter; indoor; sized by Govee for rooms of 20 to 30 square metres (about 215 to 320 sq ft) |

Owner decisions (Nov 15, 2026):

- Media room: L9 and L10 are this Govee light. L11 is a ceiling fan and light combination (see "Media room ceiling fan").
- Third-floor east office: all three ceiling lights L3, L4, L5 are this Govee light.
- All five are the round model.

### Outdoor wall lights (candidates; the selection is left open)

The owner will use some combination of these three for the balcony, the stairs and the garage doors. Which
model goes where has not been decided and is left open (owner, Nov 16, 2026).

For the exterior stair lights L17, L18, which work from motion sensors, the owner notes (Nov 16, 2026) that two
of the three support motion sensors: the Outdoor Wall Light (H7075) and the Outdoor Wall Light Pro (H3751). The
stair lights will be one of these two.

| Device | Product | Specifications from the product page |
|--------|---------|--------------------------------------|
| Up/down wall light | [Govee Outdoor UpDown Wall Light, H7076](https://us.govee.com/products/govee-outdoor-up-down-wall-lights) | 24 V at the light; 24 W; 1200 lm; 2700K-6500K white plus color, up, down and side light; IP66; power source listed as AC; Matter support not stated |
| Wall light | [Govee Outdoor Wall Light, H7075](https://us.govee.com/products/govee-outdoor-wall-light) | 120 V, hardwired to a junction box; 24 W; 1500 lm; 2700K-6500K white plus color; IP65; -4 to 113 F; Wi-Fi; Matter support not stated |
| Wall light Pro | [Govee Outdoor Wall Light Pro, H3751](https://us.govee.com/products/govee-outdoor-wall-light-pro) | 24 V at the light, hardwired; 25 W; 2000 lm; tunable white plus color, 72 zones; IP67; -4 to 113 F; Bluetooth, Wi-Fi and Matter; the page sells a 2-pack with Govee motion sensor H5129 |

Outdoor light positions on the drawings that these could fill:

| Area | Lights on the drawings | Count |
|------|------------------------|-------|
| Garage overhead doors | Garage L11, L12, L15, L16 | 4 |
| Garage deck door | Garage L13 | 1 |
| Exterior stair | Garage L17, L18 | 2 |
| Balcony | Second floor L23, L24, L28, L29 | 4 |

Check with the electrician/inspector and the owner:

- The UpDown light and the Pro are listed at 24 V at the light. Find out from the manuals whether each has a
  built-in driver fed with 120 V at the junction box or a separate power adapter, and where an adapter would sit.
- Only the Pro lists Matter. If every light must be on Matter, the other two need to be confirmed with Govee.
- The exterior stair lights L17, L18 are drawn on motion sensors S10, S11 that cut their power. A smart light
  that loses power drops off the network and takes time to come back on. The H7075 and the H3751 support motion
  sensors (owner, Nov 16, 2026), so once the model is chosen, check how its motion sensor connects: if the light
  stays powered and the sensor only signals it, S10 and S11 on the garage sheet change from power-cutting sensors
  to that kind, and the drawing note should be updated then.
- The pages state no UL or ETL listing for these lights. Ask the electrician to confirm the listing mark on
  the units, and that each is rated for a wet location where it is exposed to rain.

## Media room ceiling fan (L11)

Owner decision, Nov 15, 2026. Specifications are copied from the Amazon listing on Nov 15, 2026.

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Ceiling fan with light | [Big Ass Fans Haiku L 52 in. Smart Ceiling Fan with LED Light, white](https://www.amazon.com/dp/B01DVSBQZA) | Media room L11 | 120 V; 20 W; brushless DC motor; 7 fan speeds; LED light with 16 dimming levels; built-in Wi-Fi, app, remote, Alexa and Google; for rooms up to 15 x 15 ft; universal mount with 5 in. downrod for 8 to 9 ft ceilings; indoor; cETLus (Intertek), Energy Star; Matter support not stated on the listing |

### How the switch is wired (important)

Switch S6 is an Inovelli Smart Dimmer, but **nothing is connected to its load terminal**.

- Line (with neutral and ground) goes to switch S6 **and** straight on to the fan/light. Both are powered from
  the line all the time.
- The load terminal of S6 is left empty and capped. The switch never cuts or dims the power to the fan.
- S6 only signals Home Assistant when it is pressed. Home Assistant then controls the fan and its light through
  the smart control built into the fan.
- Aux switch S23 keeps its traveler to S6, so both switches send the same signals.

Check with the electrician/inspector and the owner:

- The Inovelli page says the dimmer works without a neutral only with a bypass at the load. With no load at
  all, the switch needs the neutral wire in its box, so run a neutral to S6.
- The fan has a DC motor and its own electronics, so it must never be put on a dimmed or speed-controlled feed.
  Label the capped load terminal and the fan feed so nobody connects them later.
- The fan can not be switched off at the wall. Ask the electrician whether a means to cut its power for
  servicing other than the breaker is wanted (for example a plain switch out of the way).
- The listing states Wi-Fi, Alexa and Google control. It does not state Matter. The owner should confirm how
  Home Assistant reaches this fan (Matter or the fan's own Wi-Fi integration) before the walls are closed.
- With no load, S6 should be set so its paddle only sends button events (smart-bulb mode or the equivalent
  setting); the owner sets this when pairing.

## 15 A wall outlets

Owner decision, Nov 16, 2026. Specifications are copied from the Amazon listing on Nov 16, 2026.

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Smart wall outlet | [Eve Energy Outlet (Matter)](https://www.amazon.com/dp/B0CT62FC6W) | A selection of the 15 A wall outlets, to be chosen late in the job | In-wall duplex outlet; 15 A; 120 V; the two outlets are controlled separately; power meter (combined value for both outlets); Matter over Thread, needs a Thread border router; local control, no cloud; needs line, neutral and ground in the wall box; copper or copper-clad wire only; dry indoor locations only; UL certified; 3 wire nuts included |

To settle with the owner:

- The Eve outlets go on a selection of the 15 A outlets. The owner will pick them at the last minute (owner,
  Nov 16, 2026), so no positions or count are given and the drawings do not mark them.

Check with the electrician/inspector:

- The listing says dry indoor locations only. That rules it out for the outdoor outlets, and it should be
  checked for the garage, the bath, the sauna area and the shed before any are used there.
- It is not a GFCI outlet. Where GFCI protection is required (kitchen, bath, garage, laundry, outdoors) it has
  to come from the breaker or an upstream GFCI device.
- The listing does not say whether it is tamper-resistant. Ask whether the inspector requires tamper-resistant
  outlets at these positions (NEC 406.12) and whether this model qualifies.
- Many of the general outlet circuits on the plan are 20 A. A 15 A duplex outlet is normally allowed on a 20 A
  circuit, but ask the electrician to confirm, including whether this outlet may feed further outlets
  downstream. It has wire leads (wire nuts included), so box fill should be checked too.
- An outlet that can be switched off remotely should not feed equipment that must stay on: the network
  switches, the Matter controllers' power supplies, the fridge, and the smoke/CO alarms.
