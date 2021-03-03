import numpy as np
import cv2

# this can capture video OR pictures
capture_device = cv2.VideoCapture(0)

while True:
    ret, frame = capture_device.read()

    # this will take one of my frames and make it gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.imshow("frame1", gray)

    # if i hit 'q' on my keyboard while in the frame, it will close:
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break