import numpy as np
import cv2
import time
import brickpi3  
import os
import shutil
from function.areadetection import *
from function.movement import *
from function.pid_g import *
from learningmovement import *
from wall import *
from rescuekit import *
from prediction import *
target_dir = '/home/pi/testphoto'
shutil.rmtree(target_dir)
os.mkdir(target_dir)

i = 1
try:
    while True:
        if i % 300 == 0:
            front,dif,size = areaBlue()
            print(front)
            if front == True:
                rescuekit()
                Size=0
                Dif=0
        elif i % 300 == 100:
            wall = False
            print("1: "+str(wall))
            wall,dif,size = areaOrange()
            print("2: "+str(wall))
            if wall == True:
                Wall()
                Size=0
                Dif=0
        elif i % 300 == 200:
            ##
            learningmovement()
        else:
            pid_g()
        if i == 1001: 
            i = 1
        i = i + 1
        print("3: "+str(wall))
except KeyboardInterrupt: 
    BP.reset_all()
    print("Program Interrupted")

    
