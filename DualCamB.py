
"""
Blender import dual cam footage

1. Import video footages
2. hit run and shapekeys are imported :D

"""

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time

import bpy



# Create a VideoCapture object to capture video from the default webcam

# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='C:\\Users\\PC-kun\\Desktop\\Mocaps\\DualFacial\\face_landmarker_v2_with_blendshapes.task')
print("Model found!")
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       num_faces=1)
print("options set")
detector = vision.FaceLandmarker.create_from_options(options)
print("Mediapipe ready")

class FilepathAddonPanel(bpy.types.Panel):
    bl_idname = "FILEPATH_PT_filepath"
    bl_label = "Filepath"
    bl_category = "Object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label("Filepath")
        filepath = col.prop(context.scene, "filepath", text="")
        col.operator("filepath_operator.print_filepath")

class PrintFilepathOperator(bpy.types.Operator):
    bl_idname = "filepath_operator.print_filepath"
    bl_label = "Print Filepath"

    def execute(self, context):
        print(context.scene.filepath)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(FilepathAddonPanel)
    bpy.utils.register_class(PrintFilepathOperator)

def unregister():
    bpy.utils.unregister_class(FilepathAddonPanel)
    bpy.utils.unregister_class(PrintFilepathOperator)
    
    
"""
def run_mediapipe(path1):#, path2)
    cap1 = cv2.VideoCapture(path1)
    frameCount = bpy.data.scenes['Scene'].frame_current
    shape_keys = mesh_object.data.shape_keys

    while(cap1.isOpened()):
        ret1, frame1 = cap1.read()
        image1 = np.array(frame1)
        mp_image1 = mp.Image(image_format=mp.ImageFormat.SRGB, data = frame1)
        detection_result = detector.detect(mp_image1)
        if detection_result.face_blendshapes:
            print(detection_result.face_blendshapes[0])
        frameCount+=1
"""
    
if __name__ == "__main__":
    register()
    """
    cap.release()
    cv2.destroyAllWindows()
"""