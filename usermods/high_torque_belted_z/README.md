
### High Torque Belted Z

- @AgentL3r#0333

![Pic](https://github.com/AgentL3r/Tiny-M/blob/master/usermods/high_torque_belted_z/images/Fusion360_INQJiKzElE.png)

## Features and Rationale
- Allows for any size of NEMA17 motor to be used, increasing versatility and mitigates the need for slimline/pancake motors 
- Motors with higher detent torques can be used to prevent bed drop on power loss (after 4:1 gearing)
- Gearbox is mounted under the electronics enclosure leading to more space for electronics mounting
- Compatible with both 190mm³ and 150mm³ builds **MUST USE MODIFIED PARTS BY nehiLo#1732**
- Shoulder screw compatible upper z idler
- Arguably less Z artifacting due to no leadscrew
  
## Bill of Materials

Fasteners
- M3x5x4 mm threaded insert x5
- M3 washer (1mm) x3
- M3 shim (0.5mm) x3
- M3x6 BHCS x4
- M3x10 SHCS x4
- M3x20 SHCS x6
- M5 t-nut x7
- M5x10 BHCS x4
- M5x20 BHCS x2
- M5x28 BHCS OR M5x16 SHOULDER SCREW with 5mm shoulder x1
- M5x60 dowel pin

Motion
- F695-2RS bearing x2
- 20T 2GT pulley x2
- 80T 2GT pulley x1 (CAN ALSO USE PRINTED VORON M4 80T)
- 188mm 2GT 6mm belt loop
- some 2GT 6mm belt
- 20T 5mm bore idler

Electronics
- NEMA17 motor


## Assembly
It is best to refer to the CAD  model for guidance on how to build this system.

**Gearbox:**
Insert the four heatset inserts into the back of the shaft guide and press-fit the F695-2RS bearing as follows:
![Pic](https://github.com/AgentL3r/Tiny-M/blob/master/usermods/high_torque_belted_z/images/20210607_135443.jpg)
Press fit an F695-2RS bearing onto the motor plate.

Attach the motor plate to the bottom of the 2020 extrusion on your printer using two M5x10mm screws and two M5 t-nuts. Ensure you use the flat edge and a pair of calipers to correctly position the motor plate so that the pin is centered.

Attach the shaft guide using four M3x20 screws.

Insert the 5x60mm shaft through the motor plate and shaft guide, ensuring it spins freely in the bearings.

The pulleys can now be attached:

80T pulley --> printed spacer --> F695-2RS --> F695-2RS  --> 0.5mm shim --> 20T pulley

Tighten all grub screws.

Insert the remaining 20T pulley onto the shaft of the NEMA17 motor. Screw the motor to the motor plate using M3x10 screws (not fully tight as you'll need the motor to swivel for tension) and an M3 washer. During this, ensure the belt loop wraps around the 20T and 80T pulley. You can now tension the pulley and fully tighten all motor mounting screws. The gearbox is now complete.

**Idler:**
The upper idler is simple to assemble with a 20T idler sandwiched between two 0.5mm shims. Attach this to the top 2020 extrusion as per the CAD model.

**Tensioner:**
Insert the final heatset insert into the hole at the TOP of the tensioner.

Attach the tensioner to the back of the Z carriage using the M5x20mm screws and two M5 t-nuts. Positioning at this point isn't important.

Insert the two M3x20 screws into the tensioner. At this point, you can route the belt. 

The belt will wrap around the M3x20 screws so that the teeth indexes with itself, creating a very secure hold. Place the printed block in the center of the tensioner with the hole facing up.

Using the M3x6mm screws, secure the backplate.

Finally, use an M3x10 screw to tension the belt by pressing the printed block.

This assembly is fiddly and takes a while to get assembled - especially the belt tension. The system works very well and has given me excellent results.

Double check your spacing for everything prior to turning on the system - refer to the CAD if in doubt.

For any questions, feel free to get in touch with me on the TinyM Discord.
