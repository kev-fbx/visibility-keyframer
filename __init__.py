import bpy

bl_info = {
    "name": "Visibility Keyframer",
    "author": "kev-fbx",
    "description": "Keyframe the render visibility of selected objects",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "View3D > Properties > Tool",
    "category": "Animation",
}

class VISIBILITY_OT_keyframe_visibility_hide(bpy.types.Operator):
    "Hide and keyframe the render visibility of selected objects"
    bl_idname = "view3d.keyframe_visibility_hide"
    bl_label = "Hide selected in render"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = True
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

class VISIBILITY_OT_keyframe_visibility_show(bpy.types.Operator):
    "Show and keyframe the render visibility of selected objects"
    bl_idname = "view3d.keyframe_visibility_show"
    bl_label = "Show selected in render"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = False
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

class VISIBILITY_PT_keyframe_visibility_ui(bpy.types.Panel):
    "UI Panel for visibility keyframing"
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
        layout.operator("view3d.keyframe_visibility")

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