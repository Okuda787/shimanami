# -*- coding: utf-8 -*-
from datetime import datetime 
import cv2
import numpy as np
import time
from function.cameraset import *

current_dir = "/home/pi/testphoto/"
cam = camB()
print(cam)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
   
while(True):
    try:
        ret, frame = cam.read()
        shoot_time = datetime.now()
        strf_time=shoot_time.strftime('%Y%m%d_%H%M%S%f')
        image_file = current_dir + strf_time +'.jpg'
        cv2.imwrite(image_file, frame)    
    except KeyboardInterrupt:
        print("Ctrl+Cでcameraは停止しました")
        # save
        break

cam.release()
cv2.destroyAllWindows()
    