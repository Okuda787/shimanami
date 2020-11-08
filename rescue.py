import numpy as np
import cv2
import time
import brickpi3  
import os
import shutil
from function.areaditection import *
from function.movement import *
from function.pid_g import *
from wall import *
from rescuekit import *

target_dir = '/home/pi/testphoto'
shutil.rmtree(target_dir)
os.mkdir(target_dir)

i = 1
try:
    while True:
        pid_g()
        if i % 200 == 0:
            wall = False
            print("1: "+str(wall))
            wall,dif,size = areaOrange()
            print("2: "+str(wall))
            if wall == True:
                Wall()
                Size=0
                Dif=0
        if i % 200 == 100:
            front,dif,size = areaBlue()
            print(front)
            if front == True:
                rescuekit()
                Size=0
                Dif=0
        if i == 1001:
            i = 1
        i = i + 1
        print("3: "+str(wall)) #Joe BIden for president
except KeyboardInterrupt: 
    BP.reset_all()
    print("Program Interrupted")

    
