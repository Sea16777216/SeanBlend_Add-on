bl_info = {
    "name":          "SeanBlend",
    "description":   "All add-ons made by SeanBlend",
    "author":        "Sean Huang, Patrick Huang",
    "version":       (1, 0, 1),
    "blender":       (2, 80, 0),
    "location":      "3D View >> Sidebar >> SeanBlend",
    "warning":       "",
    "wiki_url":      "https://github.com/Sea16777216/SeanBlend_Add-on",
    "tracker_url":    "https://github.com/Sea16777216/SeanBlend_Add-on",
    "category":      "SeanBlend"}

import bpy, math, time
from bpy.props import (StringProperty, 
                      BoolProperty,
                      IntProperty,
                      FloatProperty,
                      FloatVectorProperty,
                      EnumProperty,
                      PointerProperty)
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup)



class SeanBlendProperties(PropertyGroup):
    prop: BoolProperty(
        name = "Prop"
    )
    DisplaySize: EnumProperty(
        name = "Display Size (this doesn't do anything yet)",
        description = "Choosing your display size",
        items = [
            ('0', "Large", "Very big, don't recommend"),
            ('1', "Normal", "Normal size"),
            ('2', "Small", "Very compressed, saves space")
        ]
    )

class SEANBLEND_OT_Disable(Operator):
    bl_label = "Disable"
    bl_description = "Disables the add-on"
    bl_idname = "seanblend.disable"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module = "SeanBlend_Add-on")
        return {'FINISHED'}

class SEANBLEND_OT_Remove(Operator):
    bl_label = "Remove (Blender might crash)"
    bl_description = "Removes the add-on"
    bl_idname = "seanblend.remove"

    def execute(self, context):
        bpy.ops.preferences.addon_remove(module = "SeanBlend_Add-on")
        return {'FINISHED'}


class Panel():
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SeanBlend"
    bl_options = {'DEFAULT_CLOSED'}

class SEANBLEND_PT_Settings(Panel, bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SEANBLEND_PT_Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

class SEANBLEND_PT_QuickSettings(Panel, bpy.types.Panel):
    bl_label = "Quick Settings"
    bl_parent_id = "SEANBLEND_PT_Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

        layout.operator("seanblend.disable")
        layout.operator("seanblend.remove")
        layout.prop(prop, "DisplaySize")

class SEANBLEND_PT_OtherSettings(Panel, bpy.types.Panel):
    bl_label = "Other Settings"
    bl_parent_id = "SEANBLEND_PT_Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

classess = (SeanBlendProperties,                # Extra s in classess to keep letter count multiple of 4
            SEANBLEND_OT_Disable,
            SEANBLEND_OT_Remove,
            SEANBLEND_PT_Settings,
            SEANBLEND_PT_QuickSettings,
            SEANBLEND_PT_OtherSettings)


def register():
    from bpy.utils import register_class
    for cls in classess:
        register_class(cls)
    bpy.types.Scene.seanblend = PointerProperty(type = SeanBlendProperties)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classess):
        unregister_class(cls)
    del bpy.types.Scene.seanblend
    
if __name__ == "__main__":
    register()