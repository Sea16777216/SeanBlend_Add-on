#####################
#bl_info and imports#
#####################

bl_info = {
    "name":          "SeanBlend",
    "description":   "All add-ons made by SeanBlend",
    "author":        "Sean Huang, Patrick Huang",
    "version":       (1, 0, 3),
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

###########
#Operators#
###########

#Object Adder >> Mesh

class SEANBLEND_OT_Plane(Operator):
    bl_label = "Add Plane"
    bl_description = "Adds a plane"
    bl_idname = "seanblend.plane"

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add()
        return {'FINISHED'}

class SEANBLEND_OT_Cube(Operator):
    bl_label = "Add Cube"
    bl_description = "Adds a cube"
    bl_idname = "seanblend.cube"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}

class SEANBLEND_OT_UVSphere(Operator):
    bl_label = "Add UV Sphere"
    bl_description = "Adds a UV Sphere"
    bl_idname = "seanblend.uvsphere"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add()
        return {'FINISHED'}

class SEANBLEND_OT_IcoSphere(Operator):
    bl_label = "Add Ico Sphere"
    bl_description = "Adds a Ico Sphere"
    bl_idname = "seanblend.icosphere"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        return {'FINISHED'}

class SEANBLEND_OT_Circle(Operator):
    bl_label = "Add Circle"
    bl_description = "Adds a circle"
    bl_idname = "seanblend.circle"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_circle_add()
        return {'FINISHED'}

class SEANBLEND_OT_Cylinder(Operator):
    bl_label = "Add Cylinder"
    bl_description = "Adds a cylinder"
    bl_idname = "seanblend.cylinder"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cylinder_add()
        return {'FINISHED'}

class SEANBLEND_OT_Cone(Operator):
    bl_label = "Add Cone"
    bl_description = "Adds a cone"
    bl_idname = "seanblend.cone"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cone_add()
        return {'FINISHED'}

class SEANBLEND_OT_Torus(Operator):
    bl_label = "Add Torus"
    bl_description = "Adds a torus"
    bl_idname = "seanblend.torus"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_torus_add()
        return {'FINISHED'}

class SEANBLEND_OT_Grid(Operator):
    bl_label = "Add Grid"
    bl_description = "Adds a grid"
    bl_idname = "seanblend.grid"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_grid_add()
        return {'FINISHED'}

class SEANBLEND_OT_MonkeySuzzane(Operator):
    bl_label = "Add Monkey/Suzzane"
    bl_description = "Adds a Monkey/Suzzane"
    bl_idname = "seanblend.monkeysuzzane"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_monkey_add()
        return {'FINISHED'}

#Object Adder >> Curve

class SEANBLEND_OT_Bezier(Operator):
    bl_label = "Add Bezier"
    bl_description = "Adds a Bezier"
    bl_idname = "seanblend.bezier"

    def execute(self, context):
        bpy.ops.curve.primitive_bezier_curve_add()
        return {'FINISHED'}

class SEANBLEND_OT_CCircle(Operator):
    bl_label = "Add Circle (Curve)"
    bl_description = "Adds a Circle (Curve)"
    bl_idname = "seanblend.ccircle"

    def execute(self, context):
        bpy.ops.curve.primitive_bezier_circle_add()
        return {'FINISHED'}

class SEANBLEND_OT_Nurbs(Operator):
    bl_label = "Add Nurbs"
    bl_description = "Adds a Nurbs"
    bl_idname = "seanblend.nurbs"

    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_curve_add()
        return {'FINISHED'}

class SEANBLEND_OT_NurbsCircle(Operator):
    bl_label = "Add Nurbs Circle"
    bl_description = "Adds a Nurbs Circle"
    bl_idname = "seanblend.nurbscircle"

    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_circle_add()
        return {'FINISHED'}

class SEANBLEND_OT_Path(Operator):
    bl_label = "Add Path"
    bl_description = "Adds a Path"
    bl_idname = "seanblend.path"

    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_path_add()
        return {'FINISHED'}

#Object Adder >> Surface

class SEANBLEND_OT_NCSurface(Operator):
    bl_label = "Add Nurbs Curve (Surface)"
    bl_description = "Adds a Nurbs Curve (Surface)"
    bl_idname = "seanblend.ncsurface"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_curve_add()
        return {'FINISHED'}
        
class SEANBLEND_OT_NCCircle(Operator):
    bl_label = "Add Nurbs Curve (Surface: Circle)"
    bl_description = "Adds a Nurbs Curve (Surface: Circle)"
    bl_idname = "seanblend.nccircle"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_circle_add()
        return {'FINISHED'}

class SEANBLEND_OT_NSurface(Operator):
    bl_label = "Add Nurbs Surface"
    bl_description = "Adds a Nurbs Surface"
    bl_idname = "seanblend.nsurface"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_surface_add()
        return {'FINISHED'}

class SEANBLEND_OT_NCCylinder(Operator):
    bl_label = "Add Nurbs Curve (Surface: Cylinder)"
    bl_description = "Adds a Nurbs Curve (Surface: Cylinder)"
    bl_idname = "seanblend.nccylinder"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_cylinder_add()
        return {'FINISHED'}

class SEANBLEND_OT_NCSphere(Operator):
    bl_label = "Add Nurbs Curve (Surface: Sphere)"
    bl_description = "Adds a Nurbs Curve (Surface: Sphere)"
    bl_idname = "seanblend.ncsphere"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_sphere_add()
        return {'FINISHED'}

class SEANBLEND_OT_NCTorus(Operator):
    bl_label = "Add Nurbs Curve (Surface: Torus)"
    bl_description = "Adds a Nurbs Curve (Surface: Torus)"
    bl_idname = "seanblend.nctorus"

    def execute(self, context):
        bpy.ops.surface.primitive_nurbs_surface_torus_add()
        return {'FINISHED'}

#Settings

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

########
#Panels#
########

class SeanBlendProperties(PropertyGroup):
    hi: BoolProperty(
        name = "hi",
        description = "hi"
    )

class Panel():
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SeanBlend"
    bl_options = {'DEFAULT_CLOSED'}

#Object Adder

class SEANBLEND_PT_Mesh(Panel, bpy.types.Panel):
    bl_label = "Mesh"
    bl_parent_id = "SEANBLEND_PT_ObjectAdder"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

        layout.operator("seanblend.plane")
        layout.operator("seanblend.cube")
        layout.operator("seanblend.circle")
        layout.operator("seanblend.uvsphere")
        layout.operator("seanblend.icosphere")
        layout.operator("seanblend.cylinder")
        layout.operator("seanblend.cone")
        layout.operator("seanblend.torus")
        layout.operator("seanblend.grid")
        layout.operator("seanblend.monkeysuzzane")

class SEANBLEND_PT_ObjectAdder(Panel, bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "SEANBLEND_PT_ObjectAdder"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

class SEANBLEND_PT_Curve(Panel, bpy.types.Panel):
    bl_label = "Curve"
    bl_parent_id = "SEANBLEND_PT_ObjectAdder"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

        layout.operator("seanblend.bezier")
        layout.operator("seanblend.ccircle")
        layout.operator("seanblend.nurbs")
        layout.operator("seanblend.nurbscircle")
        layout.operator("seanblend.path")

class SEANBLEND_PT_Surface(Panel, bpy.types.Panel):
    bl_label = "Surface"
    bl_parent_id = "SEANBLEND_PT_ObjectAdder"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

        layout.operator("seanblend.ncsurface")
        layout.operator("seanblend.nccircle")
        layout.operator("seanblend.nsurface")
        layout.operator("seanblend.nccylinder")
        layout.operator("seanblend.ncsphere")
        layout.operator("seanblend.nctorus")

#Settings

class SEANBLEND_PT_Settings(Panel, bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SEANBLEND_PT_Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        prop = scene.seanblend

        layout.operator("seanblend.disable")
        layout.operator("seanblend.remove")

#######
#Other#
#######

classess = (#Panels#
            #Settings
            SeanBlendProperties,                # Extra s in classess to keep letter count multiple of 4
            SEANBLEND_PT_Settings,
            #Object Adder
            SEANBLEND_PT_ObjectAdder,
            SEANBLEND_PT_Mesh,
            SEANBLEND_PT_Curve,
            SEANBLEND_PT_Surface,
            #Operators#
            #Settings
            SEANBLEND_OT_Disable,
            SEANBLEND_OT_Remove,
            #Object Adder >> Mesh
            SEANBLEND_OT_Plane,
            SEANBLEND_OT_Cube,
            SEANBLEND_OT_Circle,
            SEANBLEND_OT_UVSphere,
            SEANBLEND_OT_IcoSphere,
            SEANBLEND_OT_Cylinder,
            SEANBLEND_OT_Cone,
            SEANBLEND_OT_Torus,
            SEANBLEND_OT_Grid,
            SEANBLEND_OT_MonkeySuzzane,
            #Object Adder >> Curve
            SEANBLEND_OT_Bezier,
            SEANBLEND_OT_CCircle,
            SEANBLEND_OT_Nurbs,
            SEANBLEND_OT_NurbsCircle,
            SEANBLEND_OT_Path,
            #Object Adder >> Surface
            SEANBLEND_OT_NCSurface,
            SEANBLEND_OT_NCCircle,
            SEANBLEND_OT_NSurface,
            SEANBLEND_OT_NCCylinder,
            SEANBLEND_OT_NCSphere,
            SEANBLEND_OT_NCTorus,)

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