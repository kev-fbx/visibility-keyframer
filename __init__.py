import bpy

bl_info = {
    "name": "Visibility Keyframer",
    "author": "kev-fbx",
    "description": "Keyframe the render visibility of objects",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "View3D > Properties > Tool",
    "category": "Animation",
}

class VISIBILITY_OT_keyframe_visibility(bpy.types.Operator):
    pass

class VISIBILITY_PT_keyframe_visibility_ui(bpy.types.Panel):
    pass

classes = [
    VISIBILITY_OT_keyframe_visibility,
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