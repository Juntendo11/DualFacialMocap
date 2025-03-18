import cv2

# Initialize camera capture objects
cap1 = cv2.VideoCapture(0)  # Camera 1
cap2 = cv2.VideoCapture(1)  # Camera 2

while True:
    # Read frames from the cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Display the frames
    cv2.imshow('Camera 1', frame1)
    cv2.imshow('Camera 2', frame2)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera capture objects
cap1.release()
cap2.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
