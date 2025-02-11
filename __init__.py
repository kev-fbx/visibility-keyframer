# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import bpy

bl_info = {
    "name": "Visibility Keyframer",
    "author": "kev-fbx",
    "description": "Keyframe the render visibility of selected objects",
    "blender": (3, 6, 0),
    "version": (1, 0, 0),
    "location": "View3D > Properties > Animation",
    "category": "Animation",
}

class VISIBILITY_OT_keyframe_visibility_hide(bpy.types.Operator):
    """Hide and keyframe the render visibility of selected objects"""
    bl_idname = "view3d.keyframe_visibility_hide"
    bl_label = "Hide selected in render"
    bl_info = "Hides selected objects in render and keyframes the change"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = True
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

class VISIBILITY_OT_keyframe_visibility_show(bpy.types.Operator):
    """Show and keyframe the render visibility of selected objects"""
    bl_idname = "view3d.keyframe_visibility_show"
    bl_label = "Show selected in render"
    bl_info = "Shows selected objects in render and keyframes the change"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = False
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

class VISIBILITY_PT_keyframe_visibility_ui(bpy.types.Panel):
    """UI Panel for visibility keyframing"""
    bl_label = "Visibility Keyframer"
    bl_idname = "VISIBILITY_PT_Visibility_Keyframer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Animation"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()

        row = layout.row(align=True)
        layout.operator("view3d.keyframe_visibility_show", text="Show in render")
        layout.operator("view3d.keyframe_visibility_hide", text="Hide in render")

classes = [
    VISIBILITY_OT_keyframe_visibility_hide,
    VISIBILITY_OT_keyframe_visibility_show,
    VISIBILITY_PT_keyframe_visibility_ui
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()