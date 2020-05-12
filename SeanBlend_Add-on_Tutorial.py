'''
Add-on Template
Written by Patrick Huang

This is a template for writing your add-on. Throughout the lesson, you will see many comments. There are two types. One is like this:
'''

'''
This is a comment
'''

'''
That is called a block comment. The block comments in this template are not important, and you can delete them after you read them (I advise you not to.)
The other type is a line comment:
# A comment
Those are important.
'''

bl_info = {
    "name":          "SeanBlend",             # Write add-on name between quotations.
    "description":   "All add-ons made by SeanBlend",             # Write description between quotations.
    "author":        "Sean Huang, Patrick Huang",
    "version":       (1, 0, 1),       # ex: (4, 2, 6) means 4.2.6
    "blender":       (2, 80, 0),      # Keep this as is.
    "location":      "3D View >> Sidebar >> SeanBlend",      # Keep as is
    "warning":       "",              # Only write if needed.
    "wiki_url":      "https://github.com/Sea16777216/SeanBlend_Add-on",              # GitHub website
    "tracker_url":    "https://github.com/Sea16777216/SeanBlend_Add-on",             # Website to report a bug
    "category":      "SeanBlend"}    # Change if you want

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
    '''
    This block contains all the properties of the add-on. A property is a input field, such as the amount of samples or Render Engine.
    Note: This block does not affect how the properties are put in the panel; that is reserved for later. This block only tells Blender
    about the properties and what they look like.
    To define a property, you type something like this:

    myProperty: FloatProperty(
        name = "Random Property",
        description = "A random thing I created",
        default = 4, min = -1.3, max = 1341135.151)
    
    Let's take a closer look:
        name: The name that shows up when someone sees it in the panel.
        description: what shows up when they hover over it.
        default: Default value
        min: Minimum value
        max: Maximum value
    Note: default, min, and max can be removed.

    There are a few types of properties:
    '''
    myFloat: FloatProperty(          # A float is a number that can be any real number. Ex: 2, 9.4, -12451.12412, pi
        name = "My Float Property",  # In this case, the user sees "My Float Property" as the label. myFloat is the name of the property, and can be edited.
        description = "A random property",
        default = 1.5, min = 0.1, max = 5.6
    )

    myInt: IntProperty(              # A int, or integer, is a number with only 0s after the decimal point. Ex: 2, 19235, -1240129
        name = "My Int Property",    # In this case, there is no maximum value for this property.
        description = "A random integer",
        default = 5, min = 1
    )

    Text: StringProperty(        # A string is any combination of letters, numbers, or symbols.
        name = "", # In this case, the default is set to "", or nothing.
        description = "Prints your typed text in the system console"
    )

    myColor: FloatVectorProperty(    # A Float Vector is 3 floats combined. They can also represent the R, G, and B for a color.
        name = "Colorful",           # If you leave the subtype = "COLOR", it is going to show up as a color picker. If you delete it, it will be 3 floats in a row.
        subtype = "COLOR",
        description = "A color",
        default = (0, 0, 0)
    )

    Render_Engine: BoolProperty(            # A Bool, or Boolean, is a True or False. If you are setting the default with True, the T must be capitalized. Same for False.
        name = "Set render engine",
        description = "Set your render engine",
        default = True
    )

    myEnum: EnumProperty(            # A Enum, or Enumeration, makes a dropdown list. The only 3 properties you need are Name, Description, and Items.
        name = "Which one?",          # Each member of the item property is a tuple with three items. A tuple is this: (1, 2, 3)
        description = "Pick",         # All three items of the tuple are strings. The first one is a number, like '0'.
        items = [                    # The second one is the name of the option, like Cycles or Eevee.
            ('0', "Cycles", "The Best Render Engine"),  # The third one is the description of the item, like Blender's raytraced engine.
            ('1', "Eevee", "The Realtime Render Engine"),
            ('2', "Workbench", "A Render Engine That Looks Like Solid View")
        ]
    )

class SEANBLEND_OT_Button(Operator):
    ''' This is a button, which is a clickable item that performs an action when clicked. Some examples are "Setup Eevee", or "Search".
    Two lines above, it says 
    class SEANBLEND_OT_Button(Operator)
    For each button you create, you need to create a new class.
    Each name must start with 
    SEANBLEND_OT_
    After that, you can put whatever you want like EeveeSetup. After that, you must put (Operator).
    Within the class of every button, there are three elements needed:
    bl_label: the words that show up
    bl_idname: Unique identifier for the button. Must start with wm.seanblend_ Every idname must be different.
    def execute: What happens when the button is pressed.
    '''
    bl_label = "Press to print Hi."   # User will see "Press for fat" on the button.
    bl_idname = "wm.seanblend_hi"   # Identifier
    
    def execute(self, context):        # This is what happens when the button is pressed.
        prop = context.scene.seanblend    # Sets up variables. Needed for every button.
        print("Hi.")             # This line and the next just print words       # This line prints whatever the myFloat value is set to above. If you want to print the string, put prop.myString.

        return {'FINISHED'}       # Needed at the end of every def execute. Tells Blender finished successfully.

class SEANBLEND_OT_Button2(Operator):
    bl_label = "Press to print Bye."
    bl_idname = "wm.seanblend_bye"

    def execute(self, context):
        print("Bye.")          # This button doesn't do anything...yet. Customize it to do whatever you want.
        return {'FINISHED'}

#### Panel time: The "HTML and CSS of Blender".
class Panel:            # This panel is the main panel. It's what you find when you press 'n'. It is the vertical words.
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SeanBlend"     # Name of the panel
    bl_options = {"DEFAULT_CLOSED"} # Note: IMPORTANT: DO NOT PUT THIS CLASS IN classes. YOU WILL READ MORE LATER.

class SEANBLEND_PT_HI(Panel, bpy.types.Panel):
    ''' This is a Panel like the Add-on Settings in PatBlend. Every panel name must start with SEANBLEND_PT_
    The name after that is the name. And, you need (Panel, bpy.types.Panel) after that.
    The elements of a panel are:
    bl_idname: Unique identifier, must begin with SEANBLEND_PT_
    bl_label: What people see the title is
    def draw: The HTML and CSS, where you decide how properties and buttons look like on your panel.

    Note: This panel mainly focuses on how to put those things in. The next panel focuses more on style. (HTML and CSS).
    '''
    bl_idname = "SEANBLEND_PT_For_Fun"
    bl_label = "For Fun"

    def draw(self, context):   # This is where you do HTML and CSS. There must be (self, context) after def draw.
        layout = self.layout   # This and the next line are inits NEEDED for every panel.
        prop = context.scene.seanblend

        layout.prop(prop, "Text")     # layout.prop adds a property. Remember: Properties were defined at the beginning, but I mentioned
        layout.prop(prop, "Render_Engine")       # that the beginning doesn't define the order. Here, you can define the order. Right now, I am putting      # Float, Int, and Enum. That is not the same order as the beginning, but it still works. To add a prop, put
                                         # layout.prop( and then put the word "prop", then comma, then the EXACT name of the property.

class SEANBLEND_PT_BYE(Panel, bpy.types.Panel):
    # In this panel, I will be focusing on styling and making things look cool.
    bl_idname = "SEAMBLEND_PT_Panel2"
    bl_label = "Bye."

    def draw(self, context):
        layout = self.layout
        prop = context.scene.seanblend

        # Remember, in the previous panel, we did layout.prop. That adds a row. Now, I am going to split the row and put two properties in a row.
        row = layout.row()    # Tells Blender I am focusing on one row  Optional: put "align = True" in the parenthesis (DON't PUT THE QUOTATIONS.)
        row.prop(prop, "myString")   # I am putting two operators in the same row.
        row.prop(prop, "myBull")    

        row = layout.row()   # Moving on to the next row
        row.scale_y = 2      # The vertical scale is 7 times
        row.operator("wm.seanblend_bye.")       # I put a button. The things in the parenthisis is the bl_idname of the button.

classes = (SeanBlendProperties,      # Here, wherever in the script you see the word class, type the word in front of it.
           SEANBLEND_OT_Button,      # The only exception is class Panel, as mentioned above.
           SEANBLEND_OT_Button2,
           SEANBLEND_PT_HI,
           SEANBLEND_PT_BYE)

def register():                     # Leave as is
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.seanblend = PointerProperty(type = SeanBlendProperties)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.seanblend
    
if __name__ == "__main__":
    register()