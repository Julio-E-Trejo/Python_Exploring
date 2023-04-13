import cv2
from grip import WhiteBall as WB

class defense:
    def __init__(self):# Base initializations
        self.I = WB()
        self.font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.fontScale = 0.5
        self.color = (48,38,186)
        self.thickness = 3

        # Make equivalent to starting defense position
        self.x_prev = 0
        self.y_prev = 0

    def locate(self, frame):
        self.I.process(frame)
        if len(self.I.ball) > 0:
            x = self.I.ball[1] + self.I.startX
            y = self.I.ball[2] + self.I.startY
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.drawMarker(frame, (x, y),  (0, 0, 255), cv2.MARKER_CROSS, 10, 1)
            txt = "{},{},{}".format(hsv[y,x,0], hsv[y,x,1], hsv[y,x,2])
            cv2.putText(frame, txt, (x,y), self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)

    # mX represents linear gain in 
    def move(self,mX,mZ):
        
        return ballx,bally