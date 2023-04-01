import cv2
import PencilSketch as ps
# Inversion of the original image
# inputs: 
#   image -> retrieved camera frame 
#   mask -> filter with 0 & non-0 values; all 0s set 0s in the output image
def burnV2(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)




cam = cv2.VideoCapture(0) # 0 = default camera

while(True):
    # ret: whether frames were grabbed 
    # frame: frame capture
    ret,frame = cam.read()

    # filtering
    ps.__init__(512,512,frame)

    # shows the frame
    cv2.imshow('Exit with c',ps.renderV2(frame))

    # change the character in ord() for a different exit key
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cam.release() # turns off the camera
cv2.destroyAllWindows() # closes out the video window