import numpy as np
import cv2

"""
The following code 
"""

vid = cv2.VideoCapture(0)  # Feeds stream of numpy-array images to variable 'vid'
if not vid.isOpened():
    print('Cannot open camera.')
    exit()

# Each iteration of the while loop uses .read() to determine
# whether the next frame in the video stream being captured can
# be read (stored as 'ret') and stores the numpy array containing
# the individual frame for that iteration of the loop in variable
# 'frame'.
while(True):
    # Capture the video frame-by-frame.
    # The following returns a boolean indicating whether
    ret, frame = vid.read()
    
    # If frame is read correctly, ret == True
    if not ret:
        print("Can't receive frames for some reason. Exiting...")
        break # Exit the otherwise infinite while loop b/c cant read video
    
    # Now can begin processing the frames...
    
    # Convert the color of the frame from RGB to grayscale. BGR == RGB
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    # Display the altered frame
    cv2.namedWindow("Gray Livestream", cv2.WINDOW_NORMAL) # Make window and constrain its shape
    cv2.imshow('Gray Livestream', gray_frame)
    
    # Break the infinite while loop by clicking in the display window
    # for the video feed and pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break
    
# When everything is done, release the capture
vid.release()
cv2.destroyAllWindows()