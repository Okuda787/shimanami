# -*- coding: utf-8 -*-
from datetime import datetime 
import cv2
import numpy as np
import time
import os
import shutil
from function.cameraset import *
from function.movement import *

target_dir = '/home/pi/testphoto'
shutil.rmtree(target_dir)
os.mkdir(target_dir)
cam = camB()
print(cam)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
   
while(True):
    try:
        for i in range(10):
            front,dif,size = areaBlue()
        print("10")
        
        for i in range(10):
            front,dif,size = areaBlue()
        print("20")

    except KeyboardInterrupt:
        print("Ctrl+Cでcameraは停止しました")
        # save
        break

cam.release()
cv2.destroyAllWindows()
    