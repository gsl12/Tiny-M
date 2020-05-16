### Slicer Information

## Start and End Gcode for specific slicer i used.

# ------ CURA ---------
Values "material_klipper_pa" , "material_klipper_pa_smooth_time"  and "material_klipper_gcode_offset" 
are only available with my CURA Klipper settings plugin.

Start GCODE:
;#================ STARTCODE ====================
PRINT_START E_T={material_print_temperature_layer_0} B_T={material_bed_temperature_layer_0}
SET_GCODE_OFFSET Z={material_klipper_gcode_offset}
SET_PRESSURE_ADVANCE ADVANCE={material_klipper_pa} SMOOTH_TIME={material_klipper_pa_smooth_time}
;#---------------- HEATTOWER --------------------
;   Only enable it , if needed by removing ";"
;   Extruder temp decreased 5 degree every 5 mm.
;TUNING_TOWER COMMAND=M104 PARAMETER=S START={material_print_temperature_layer_0} FACTOR=-1 BAND=5
;#---------------- PA Tuning --------------------
;   Only enable it , if needed by removing ";"
;SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
;TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.01