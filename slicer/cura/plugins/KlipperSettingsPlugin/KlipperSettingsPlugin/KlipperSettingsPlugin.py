# The KlipperSettingsPlugin .


import os, json, re
from collections import OrderedDict

from UM.Extension import Extension
from UM.Application import Application
from UM.Logger import Logger
from UM.Settings.SettingDefinition import SettingDefinition
from UM.Settings.DefinitionContainer import DefinitionContainer
from UM.Settings.ContainerRegistry import ContainerRegistry

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("KlipperSettingsPlugin")

class KlipperSettingsPlugin(Extension):
    def __init__(self):
        super().__init__()

        self._i18n_catalog = None
        self._application = Application.getInstance()

        self._category_key = "klipper_settings"
        self._category_dict = {
            "label": "Klipper Settings",
            "description": "Klipper firmware specific settings.",
            "type": "category",
            "icon": "category_machine"
        }
        self._setting_k_g_offset_key = "material_klipper_gcode_offset"
        self._setting_k_g_offset_dict = {
            "label": "K - GCODE Offset",
            "description": "material_klipper_gcode_offset : Sets the GCODE Offset for Klipper. Note that unless this setting is used in a start gcode snippet, it has no effect!",
            "type": "float",
            "unit": "mm",
            "default_value": 0,
			"minimum_value": "-layer_height_0",
            "maximum_value_warning": "layer_height_0",
            "settable_per_mesh": False,
            "settable_per_extruder": True,
            "settable_per_meshgroup": False
        }

        self._setting_k_pa_key = "material_klipper_pa"
        self._setting_k_pa_dict = {
            "label": "K - Pressure Advance",
            "description": "material_klipper_pa : 0.0 disable. Sets the Pressure Advance for Klipper. Note that unless this setting is used in a start gcode snippet, it has no effect!",
            "type": "float",
            "default_value": 0.0,
			"minimum_value": 0.0,
            "settable_per_mesh": False,
            "settable_per_extruder": True,
            "settable_per_meshgroup": False
        }

        self._setting_k_pa_l_key = "material_klipper_pa_smooth_time"
        self._setting_k_pa_l_dict = {
            "label": "K - PA Smooth Time",
            "description": "material_klipper_pa_smooth_time : 0.04. Sets the Pressure Advance smooth time for Klipper. Note that unless this setting is used in a start gcode snippet, it has no effect!",
            "type": "float",
            "default_value": 0.040,
            "settable_per_mesh": False,
            "settable_per_extruder": True,
            "settable_per_meshgroup": False
        }

        self._application.engineCreatedSignal.connect(self._fixSettingVisibility)
        self._application.getPreferences().preferenceChanged.connect(self._onPreferencesChanged)
        ContainerRegistry.getInstance().containerLoadComplete.connect(self._onContainerLoadComplete)
		
        # running through the generate GCODE if needed
        self._application.getOutputDeviceManager().writeStarted.connect(self._filterGcode)

    def _onContainerLoadComplete(self, container_id):
        container = ContainerRegistry.getInstance().findContainers(id = container_id)[0]
        if not isinstance(container, DefinitionContainer):
            # skip containers that are not definitions
            return
        if container.getMetaDataEntry("type") == "extruder":
            # skip extruder definitions
            return

        material_settings_category = container.findDefinitions(key="material")
        klipper_settings_category = container.findDefinitions(key=self._category_key)
        if material_settings_category and not klipper_settings_category:
            # this machine doesn't have a GCODE Offset setting yet
            material_settings_category = material_settings_category[0]
            klipper_settings_category = SettingDefinition(self._category_key, container, None, self._i18n_catalog)

            category_dict = self._category_dict
            category_dict["children"] = OrderedDict()

            klipper_gcode_offset_definition = SettingDefinition(self._setting_k_g_offset_key, container, klipper_settings_category, self._i18n_catalog)
            klipper_gcode_offset_definition.deserialize(self._setting_k_g_offset_dict)
            
            klipper_pa_definition = SettingDefinition(self._setting_k_pa_key, container, klipper_settings_category, self._i18n_catalog)
            klipper_pa_definition.deserialize(self._setting_k_pa_dict)

            klipper_pa_l_definition = SettingDefinition(self._setting_k_pa_l_key, container, klipper_settings_category, self._i18n_catalog)
            klipper_pa_l_definition.deserialize(self._setting_k_pa_l_dict)

            category_dict["children"][self._setting_k_g_offset_key] = self._setting_k_g_offset_dict
            category_dict["children"][self._setting_k_pa_key] = self._setting_k_pa_dict
            category_dict["children"][self._setting_k_pa_l_key] = self._setting_k_pa_l_dict
            
            klipper_settings_category.deserialize(category_dict)
            container.addDefinition(klipper_settings_category)

            container._updateRelations(klipper_settings_category)

    def _onGlobalContainerStackChanged(self):
        self._global_container_stack = self._application.getGlobalContainerStack()

    def _onPreferencesChanged(self, preference):
        if preference == "general/visible_settings":
            self._fixSettingVisibility()

    def _fixSettingVisibility(self):
        # Fix preferences
        preferences = self._application.getPreferences()
        visible_settings = preferences.getValue("general/visible_settings")
        if not visible_settings:
            # Wait until the default visible settings have been set
            return

        visible_settings_changed = False
        if self._category_key not in visible_settings:
            visible_settings += ";%s" % self._category_key
            visible_settings_changed = True

        if not visible_settings_changed:
            return

        preferences.setValue("general/visible_settings", visible_settings)

    def _filterGcode(self, output_device):
        scene = self._application.getController().getScene()

        global_container_stack = self._application.getGlobalContainerStack()
        if not global_container_stack:
            return

        gcode_dict = getattr(scene, "gcode_dict", {})
        if not gcode_dict: # this also checks for an empty dict
            Logger.log("w", "Scene has no gcode to process")
            return

        dict_changed = False

        for plate_id in gcode_dict:
            gcode_list = gcode_dict[plate_id]
            if len(gcode_list) < 2:
                Logger.log("w", "Plate %s does not contain any layers", plate_id)
                continue

            for layer_number, layer in enumerate(gcode_list):
                lines = layer.split("\n")
                for (line_nr, line) in enumerate(lines):
                    if "M204 P" in line:
                        ACC = line.replace("M204 P","")
                        DCC = int(ACC)/2
                        lines[line_nr] = "SET_VELOCITY_LIMIT ACCEL={0} ACCEL_TO_DECEL={1}".format(ACC,DCC)
                    if "M204 S" in line:
                        ACC = line.replace("M204 S","")
                        DCC = int(ACC)/2
                        lines[line_nr] = "SET_VELOCITY_LIMIT ACCEL={0} ACCEL_TO_DECEL={1}".format(ACC,DCC)
                    if "M204 T" in line:
                        ACC = line.replace("M204 T","")
                        DCC = int(ACC)/2
                        lines[line_nr] = "SET_VELOCITY_LIMIT ACCEL={0} ACCEL_TO_DECEL={1}".format(ACC,DCC)
                    gcode_list[layer_number] = "\n".join(lines)
            
            gcode_dict[plate_id] = gcode_list
            dict_changed = True
            #if ";KLIPPERPLUGINPROCESSED\n" not in gcode_list[0]:
            #    gcode_list[1] = ("SET_GCODE_OFFSET Z=%f ;added by KlipperGcodeOffsetPlugin\n" % klipper_gcode_offset) + gcode_list[1]
            #    gcode_list[0] += ";KLIPPERPLUGINPROCESSED\n"
            #    gcode_dict[plate_id] = gcode_list
            #    dict_changed = True
            #else:
            #    Logger.log("d", "Plate %s has already been processed", plate_id)
            #    continue

        if dict_changed:
            setattr(scene, "gcode_dict", gcode_dict)