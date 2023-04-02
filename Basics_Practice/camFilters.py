import cv2
import PencilSketch as ps
# Inversion of the original image
# inputs: 
#   image -> retrieved camera frame 
#   mask -> filter with 0 & non-0 values; all 0s set 0s in the output image
def burn(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)

# Pencil-like appearance of the image
def pencil(image,w,h):
    image = cv2.resize(image, (w,h))
    ps.PencilSketch.__init__(ps,w,h,image)
    return ps.PencilSketch.renderV2(ps,image)



cam = cv2.VideoCapture(0) # 0 = default camera

while(True):
    # ret: whether frames were grabbed 
    # frame: frame capture
    ret,frame = cam.read()

    # shows the frame
    # frame is modified by corresponding function used
    cv2.imshow('Pencil sketch (Exit with c)',pencil(frame,512,512))

    # change the character in ord() for a different exit key
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cam.release() # turns off the camera
cv2.destroyAllWindows() # closes out the video window