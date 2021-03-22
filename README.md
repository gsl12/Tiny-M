# Tiny-M

<img src="images/build_p1.jpg" width="200">

A compact printer with build volume: 150x150x150 mm

This is a Corona project.  
It is based on [Voron V0](https://github.com/VoronDesign/Voron-0) .  
As extruder I used [Voron Jetpack](https://github.com/VoronDesign/Jetpack-Extruder).
or my new [Nema17 Pocketwatch](https://github.com/gsl12/VoronUsers/tree/master/printer_mods/GSL12/pocketwatch_nema17)
A direct drive extruder using [Annex Engineering's Sherpa Mini](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder) is now available.

Source is available at [Tiny-M Onshape](https://cad.onshape.com/documents/d2a24a4147c3d522115f6ea5/w/d8f44be5c0a081fbf527e154/e/debb6c2779e27f86389232d5).

This is my first project of this kind. Maybe something will be missing, is not well documented, or just messy. I apologize for that.

## Why the whole thing?

I had many 3D printer parts in my pocket from my old no longer used printer. 
I cleared out my pocket and took what I had in the box without buying anything new.
After checking all parts, I recognize, that I could build a converted Voron V0 with this parts.

### Hardware

    - 2020 Nut 5 I-Typ alu profiles (6mm wide slot Misumi 2020 will work)
    - Nema 17 stepper motors
    - 3x 200mm MGN9H for XY
    - 2x 200mm MGN12H for Z
    - FYSETC Cheetah V1.1b (TMC2209) or SKR Mini E3 with TMC2209
    - 24V everywhere

### BOM
DRAFT BOM is available now. Thanks to CookieSN !

### Build Tips
There are 3 versions of the XY-Joins.

- V2 - use 2GT 20T pulleys - No Set Screw Hub
    - The outer diameter of the flanges from the pulleys for XY Joins will not fit.
    - You will need to grind the flanges to fit.
- V3 - use 2GT 20T toothed idler and no M5 Nuts
- V4 - split into 3 parts
    - removed one M5 screw for better alignment
    - optimized belt path to use E3D idler (10mm high) or chinese (9mm high)
    - some design changes
    - more rigid

[Mark Hoy's Excellent Build Log](https://github.com/mark-hoy/tiny-m-build)

### User Mods
There are several user mod STLs in the usermods directory.

[190^3 Mod which uses Prusa mini bed plates]()

[Xile's Sherpa Direct Drive Toolhead](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder/tree/master/Toolheads/Xile_Tiny_M)

[Ocho Camino's Sailfin Direct Drive Toolhead](https://github.com/CroXY3D/Sailfin-Extruder)

[Schlank's Fysetc 12864 mod](https://github.com/VoronDesign/VoronUsers/tree/master/legacy_printers/printer_mods/schlank/minima)


### Discord

The [CroXY Discord](https://discord.gg/tmZkjWs) has a tiny-m channel where several Tiny-M builders hang out.


# Images

V4  

<img src="images/cad_v4.jpg" width="400"> 

old  

<img src="images/build_p2.jpg" width="200"> <img src="images/build_p3.jpg" width="200">


