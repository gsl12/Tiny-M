### 190^3 Build volume which can use the Prusa Mini Bed Plate.

- @Ocho Camino & @AgentL3r
- Skirts by @AgentL3r

The changes for a 190^3 build volume are fairly simple.   
- All frame extrusions need to be 50mm longer
   * 11x 2020 310mm  (note one more than normal Tiny-M.  This is used as a cross brace about halfway up in the front to stiffen the frame)
   * 4x	2020 350mm
   * 2x	2020 300mm
- All bed extrusions need to be 40 mm longer
   * 3x	2020 170mm
- 1X 250mm MGN12H for X (RobotDigg SUS 440C highly recommended) 
- 2x 250mm MGN9H for Y 
- 2X 250mm MGN12H for Z
- 250mm TR8x4 leadscrew
- Mic6 bed should be 190x190x6mm.  Template for drilling are in the STLs subdir here.
- Bed heater should be 150x150mm.   [Keenovo or AliExpress](https://www.aliexpress.com/item/4000271859036.html?spm=a2g0s.9042311.0.0.27424c4dSLLDSs)
- Three parts need to be 40mm wider.  The front nosepiece and the upper and lower Z supports.  They are in the STLs subdir here
- Skirts are changed.  STLs and CAD by @AgentL3r are here

Note that the nosepiece is modded with proud text, so you can print it text up and do a filament swap for contrasting text.  The holes in the nosepiece have a membrane for printability that must be drilled out 5mm.

If you wish to use blind holes, the extrusion BOM:
- 2x HFSB5-2020-170-TPW		Z carriage.
- 1x HFSB5-2020-170-AH40-BH130	 Z carriage. 
- 2x HFSB5-2020-300-LCV-RCV		Vertical extrusions.
- 1x HFSB5-2020-310	X axis extrusion. 
- 3x HFSB5-2020-310-TPW	Lower front and upper left/right extrusions. 
- 4x HFSB5-2020-310-TPW-AH274		Left and right extrusions. 
- 2x HFSB5-2020-310-TPW-AH93.5-BH216.5	Horizontal Z extrusions.
- 2x HFSB5-2020-350-TPW-RCH-AP60		Front vertical extrusions. 
- 2x HFSB5-2020-350-TPW-RCH-AH60		Rear vertical extrusions.


![190^3 Z Assembly](https://github.com/gsl12/Tiny-M/blob/master/usermods/190mm_prusa_mini_mod/images/z.png)
