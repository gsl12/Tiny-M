# KlipperSettingsPlugin

This plugin adds a Klipper setting named "K ..." to the Klipper Settings category in the Custom print setup of Cura.

add start G-code:
```
...
SET_GCODE_OFFSET Z={material_klipper_gcode_offset}
...
```

```
...
SET_GCODE_OFFSET Z={material_klipper_gcode_offset}
SET_PRESSURE_ADVANCE ADVANCE={material_klipper_pa} ADVANCE_LOOKAHEAD_TIME={material_klipper_pa_lookahead}
...
```
