import cv2
from grip import WhiteBall as WB
# NOTE: all references to "y" are in the z-direction
# All references to "z" are also in the z-direction
# Movements made are in the x-z plane; y is kept constant
class defense:
    def __init__(self):# Base initializations
        self.I = WB()
        self.font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.fontScale = 0.5
        self.color = (48,38,186)
        self.thickness = 3

        # Make equivalent to starting defense position
        self.x_prev = 0
        self.z_prev = 0
        self.x = 0
        self.z = 0

    def locate(self, frame):# Location establishing
        # Runs the image frame through grip.py
        self.I.process(frame)

        # Accessed if a "ball" is found
        if len(self.I.ball) > 0:
            # Making current position values
            x = self.I.ball[1] + self.I.startX
            z = self.I.ball[2] + self.I.startY

            # Image processing to frame the ball
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.drawMarker(frame, (x, z),  (0, 0, 255), cv2.MARKER_CROSS, 10, 1)
            txt = "{},{},{}".format(hsv[z,x,0], hsv[z,x,1], hsv[z,x,2])
            cv2.putText(frame, txt, (x,z), self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
            
            # Setting prior & current position values
            self.x_prev = self.x
            self.y_prev = self.y
            self.x = x
            self.y = z


    
    def move(self):

        # Initial values
        x0 = 1
        z0 = 1

        # Pixel-to-motion relation
        mX = 1
        mZ = 1

        # Linear relation between image pixels & meArm motion
        ballx = mX*self.x + x0
        ballz = mZ*self.z + z0

        return [ballx,ballz]