### All Metal Bed Undercarriage

- @Ocho Camino

![Pic](https://github.com/gsl12/Tiny-M/blob/master/usermods/all_metal_bed_undercarriage/images/150.png)

## Rationale
The existing bed mounts are made of ABS and flex somewhat.   Making the entire bed undercarriage out of metal greatly reduces this flex.

## Status

  Alpha.  Still testing.  There could be some changes.
  
## BOM

150mm Bed:
- 1x HFSB5-2020-160-AH80-AV10-BV150
- 1x HFSB5-2020-160 (with 4 3mm clearance holes drilled for the MGN12 mount screws. Use MGN12_drill_jig.stl)
- 1x HFSB5-2020-133-RTP-AV10 (Misumi). 

190mm Bed:
- 1x HFSB5-2040-200-AH100-AV10-BV190 
- 1x HSFB5-2020-200 (with 4 3mm clearance holes drilled for the MGN12 mount screws.  Use MGN12_drill_jig.stl)
- 1x HFSB5-2020-173-RTP-AV10

Common:
- 6x Openbuilds Angle Brackets [Openbuilds](https://openbuildspartstore.com/black-angle-corner-connector/) [Ali Express](https://www.aliexpress.com/item/32899575950.html)
- 3x 16mm long silicone bed mounts [Amazon](https://smile.amazon.com/dp/B07RZKF8MB?psc=1&ref=ppx_yo2_dt_b_product_details)
- 3x Bed Adjusters (reuse existing) [Ali Experss Style B or D](https://www.aliexpress.com/item/4000421280308.html)
- 3x 45mm (or 50mm) FHCS screws.  45s protrude only 2.3 mm below the extrusion, so 50 is probably better.
- 4x M3 washers (at least 6mm OD)
- 4x M3x8 SHCS
- 11x M5x6 BHCS
- 1x M5x12 SHCS
- 1x M5x16 SHCS

## Assembly

Print the parts (ok, it's not all metal, but the load bearing parts are). The nosepiece can be printed with a filament swap for a contrasting color for the logo.  

Note the rear two holes on the bed are in slightly different positions than on stock Tiny-M.  They are 12mm from the rear.
Use the template (TBD) to drill the two countersunk M3 holes.   

The underbed assembly is made of 3 pieces of 2020.  The rear piece attaches to the MGN12 cars.  The middle piece sisters to the rear piece and also supports the bed at each end in the rear.  The front piece is the forward pointing spar that supports the bed at the middle in the front.

The rear 2020 piece will need to be drilled with 4 3mm clearance holes to attach it to the MGN12 car.  Use the MGN12_drill_jig.stl to drill these holes, from each side of the 2020.

If you ordered the other 2020 parts without Misumi drilling for you, you will need to use the drill guide. The middle 2020 that is is sistered to the rear 2020 piece needs a 3mm vertical clearance hole 10mm from each end, and a 5mm horizontal clearance hole 30mm from each end (middle_front_drill_jig.stl).   Additionally that piece needs a 5mm horiztonal clearance hole centered on the extrusion - use middle_jig.stl centered on the extrusion.

The front piece is tapped M5 at the rear and has a 3mm clearance hole drilled vertically 10mm from the front of it (middle_front_drill_jig.stl).

Assemble the middle and front spar 2020 pieces to form a tee.   The two angle brackets that support the forward spar can be any type of angle bracket. Make sure this connection is solid and doesn't twist or flex.   Attach the spar to the tapped hole with a M3x8 BHCS for more rigidity. 

The Openbuilds corner brackts screw into the top screw holes of the MGN12H cars. Attach them to the rear 2020 piece.  The rear 2020 is attached to the lower screw holes of the MGN12H car via M3x16 SHCS.

Attach the tee piece to the rear piece with 2 M5x6 BHCS

The rest of the parts assembly should be straightforward.
