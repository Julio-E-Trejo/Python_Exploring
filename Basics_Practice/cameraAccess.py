import cv2

cam = cv2.VideoCapture(0) # 0 = default camera

while(True):
    # ret: whether frames were grabbed 
    # frame: frame capture
    ret,frame = cam.read()

    # shows the frame
    cv2.imshow('Exit with c',frame)

    # change the character in ord() for a different exit key
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cam.release() # turns off the camera
cv2.destroyAllWindows() # closes out the video window