# Copyright (c) 2019 GSL12
# The KlipperSettingsPlugin is released 

from . import KlipperSettingsPlugin


def getMetaData():
    return {}

def register(app):
    return {"extension": KlipperSettingsPlugin.KlipperSettingsPlugin()}
