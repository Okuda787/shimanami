import numpy as np
import cv2
import time
import brickpi3  
from function.areadetection import *
from function.movement import *
from function.pid_g import *
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));

BP = brickpi3.BrickPi3() 
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B)) #左v
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D)) #右

# Orange
L = np.array([5,150, 0])
U = np.array([20,255,255])
T = 300000
wall = 0

def Wall():
    stay(1)
    r90(3)
    straight(3.5,30)
    for i in range(5):
        wall,dif,size = areaOrange()
    l90(3)
    # while True:
        # straight(4,40)
    straightwhileW(4.1,40)
    print("found black")
    r90cor()
    print("over")
    stay(1)
            


if __name__ == '__main__':
    try:
        wall()
    except KeyboardInterrupt:
        print("Ctrl+Cでmotorは停止しました")
        BP.reset_all()
