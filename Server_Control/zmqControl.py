#################################################
# ZMQ Server
#################################################

# To make this work
# pip3 install zmq

import time
import zmq
import pickle

# ZMQ
# ---

port = 5555

class Point(object):
    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y
        
ball_loc = Point()



# Open ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

# Main Loop
while True:
    # Here go your ball detection routines
    frame = socket.recv()
    ballx = 1
    bally = 1
    
    # Post zmq message if location request received
    try:
        message = socket.recv_string(flags=zmq.NOBLOCK)
        if message == "loc":
            ball_loc.x = -1
            ball_loc.y = -1
            if (len(ballx) > 0en(bally) > 0):
                ball_loc.x= ballx
                ball_loc.y= bally

            p = pickle.dumps(ball_loc) # serialize the ball_loc object
            socket.send(p)

    except zmq.Again as e:
        # print("No request received")
        pass