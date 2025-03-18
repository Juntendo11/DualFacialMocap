import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

"""
Possible features
-adjustable smoothness from blender addon
-save the animation in SD carc
-

"""

# Create a VideoCapture object to capture video from the default webcam
cap0 = cv2.VideoCapture(0)
#cap1 = cv2.VideoCapture(1)

# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='face_landmarker_v2_with_blendshapes.task')
print("Model found!")
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       num_faces=1)

print("options set")
detector = vision.FaceLandmarker.create_from_options(options)
print("Mediapipe ready")

while True:
    ret0, frame0 = cap0.read()
    #ret1, frame1 = cap.read()
    
    if not ret0:
        print("Capture failed")
        break
    
    image0 = np.array(frame0)
    #image1 = np.array(frame1)
    
    mp_image0 = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame0)
    #mp_image1 = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame1)

    detection_result0 = detector.detect(mp_image0)
    #detection_result1 = detector.detect(mp_image1)

    #if both recognized
    if detection_result0.face_blendshapes: # and detection_result1.face_blendshapes:
        result = detection_result0.face_blendshapes[0] #+ detection_result1.face_blendshapes[0]
        print(result)
        
    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap0.release()
#cap1.release()
cv2.destroyAllWindows()
