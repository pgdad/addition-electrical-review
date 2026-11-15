# Purchased devices

Specific products the owner has already bought (owner, Nov 15, 2026). Specifications are copied from the
product pages on Nov 15, 2026; where a page does not state something, the table says so. More devices will be
added to this section.

## Low-voltage lights (stair risers and island floor)

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Low-voltage light | [GekPower 4 inch Linear Step Light, white, 24V 0.6W, 3000K](https://gekpower.com/products/4-inch-linear-step-light-24v-0-6w-cct2-7k-3k-3-5k-4k-5k-white?variant=47782360154349) | Stair riser lights L7 and L8, island floor lights L36-L39 | Model VBD-COB-24V-100L-xxxx-STP4-White; 24 V DC; 0.6 W; 100 lm; dimmable; IP20 (indoor); 94 x 22 x 9.7 mm; 2 ft lead; certification not stated |
| Matter controller | [MiBoxer SMZ2 Matter over Thread LED dimmer](https://www.ledbe.com/miboxer-smz2-matter-over-thread-led-dimmer.html) | Stair light controllers D, island controller T | 12-24 V DC in; 12 A max output; single-color or dual-white mode; Matter over Thread and 2.4 GHz remote; IP20; 74.5 x 36 x 17 mm; CE, EMC, RED; UL listing not stated |
| 24 V power supply | [Amazon item B07W93ZGWL](https://www.amazon.com/dp/B07W93ZGWL) | Feeds each controller | Not read: the Amazon page could not be opened from here. Owner to give the brand, model and wattage |

The linked step-light variant is the 3000K one. The page also offers 2700K, 3500K, 4000K and 5000K.

## Control and power (owner, Nov 15, 2026)

- No wall switch is needed for the low-voltage lights. The Matter controllers that run them should not be
  powered off, so they stay powered all the time and the lights are controlled through Matter.
- Each stairway has two independently controlled segments of lights, so two controllers per stairway.
- The second-floor hallway has one controller for all its low-voltage lights.
- The kitchen island lights all share a single controller.
- Each media room low-voltage light has its own controller.
- The power supplies can be arranged as the electrician decides (for example one supply per controller, or one
  supply shared by several controllers).

| Area | Controllers |
|------|-------------|
| Garage stair (risers L8) | 2, one per segment |
| West stair (risers L7) | 2, one per segment |
| Second-floor hallway | 1 |
| Kitchen island (L36-L39) | 1 |
| Media room | 1 per light |

Not yet on the drawings (to settle with the owner):

- The drawings show no low-voltage lights in the second-floor hallway or the media room, so their number and
  positions, and the number of media room controllers, are not known yet.
- The drawings still show wall switches for the riser lights (second floor S3 and S4, garage S8, third floor S8)
  and for the island lights (S27). With this note those switches are no longer needed to power the lights; whether
  to remove them or keep them as Matter scene buttons is the owner's call.
- Where each stairway is split into its two segments is not set.

## Load on each run

| Run | Lights | Load at 0.6 W each | Current at 24 V |
|-----|--------|--------------------|-----------------|
| Garage stair risers L8 | 17 | 10.2 W | 0.43 A |
| West stair risers L7 | 16 | 9.6 W | 0.40 A |
| Island floor lights L36-L39 | 4 | 2.4 W | 0.10 A |

Each run is far below the controller's 12 A limit, and each stair run will be split over two controllers.
The power supply size and arrangement are the electrician's decision; the size is still to be checked against these
loads once its model is known.

## Low-voltage lights: check with the electrician/inspector

- The step-light page lists no safety certification and the controller page lists CE only (no UL or ETL listing
  stated). Ask whether the inspector accepts them, and whether the 24 V supply must be a listed Class 2 supply.
- The controllers and the step lights are IP20, for dry indoor places only. They are not assumed for the sauna
  lights (second floor L21, shed L1), which stay on control unit J.
- Each controller and its power supply must stay reachable after the walls and the island are closed.
- That these products serve the riser lights and the island floor lights is taken from the earlier notes
  (controllers D and T are "Matter" controllers); the owner should confirm.

## Inovelli White Series smart switches

The owner has the Smart Dimmer, the Smart On/Off and the Smart Fan switch from the
[Inovelli White Series](https://inovelli.com/collections/inovelli-white-series) (owner, Nov 15, 2026). All are
Thread / Matter, 120 V. Specifications are copied from the product pages on Nov 15, 2026.

| Device | Product | Used for | Specifications from the product page |
|--------|---------|----------|--------------------------------------|
| Smart dimmer | [White Series 2-in-1 Smart Dimmer, VTM31-SN](https://inovelli.com/products/thread-matter-white-series-smart-2-1-on-off-dimmer-switch) | The 28 dimmer positions (smart-bulb mode) | Max 600 W incandescent, 300 W LED, 150 W CFL; lighting only, not for fans, outlets or other motor loads; smart-bulb mode; works with or without a neutral (no neutral: bypass needed, no energy monitoring); multi-way with the Aux switch; UL certified E528330 |
| Smart on/off | [White Series Smart On/Off Switch, VTM30-SN](https://inovelli.com/products/thread-matter-white-series-smart-on-off-switch-w-humidity) | The 5 on/off positions | Max 1500 W general purpose, 960 W incandescent, 300 W LED/CFL; may run any fan or outlet within the load limit; built-in temperature and humidity sensors; neutral wire required; ETL certified |
| Smart fan switch | [White Series Smart Fan Switch, VTM35-SN](https://inovelli.com/products/thread-matter-white-series-smart-fan-switch-3-speed-ceiling-on-off-exhaust) | Not assigned on the drawings; see the next part | Max 2.5 A, no more than 2 fans; AC motors only, DC motors not supported; not for lighting; no neutral: low and medium speed only and not usable on an exhaust fan; ETL certified 5027290 |
| Aux switch | [Inovelli Add-On (Aux) Switch](https://inovelli.com/products/white-series-add-on-aux-switch) | The 13 aux positions (owner to confirm these are bought) | Not a smart switch; needs a traveler to its main switch; works with or without a neutral; UL certified E528330 |

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
- The drawings show one bath fan (second floor, switch S18). A separate shower fan is not on the drawings; the
  owner should say whether there is one and where its switch goes.
- The media room fan (second floor S6 with aux S23) is drawn as one on/off switch for the fan and its light.
  The Smart Fan switch can not run a light, so it fits there only if the fan has no light on that feed.
