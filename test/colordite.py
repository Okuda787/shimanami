from areaditection import areaditection
import numpy as np
import time

# # Orange
# OrangeL = np.array([10, 120, 0])
# OrangeU = np.array([50,255,255])

# Blue
BlueL = np.array([100,120,0])
BlueU = np.array([150,255,255])

while(True):
    # orange=areaditection(OrangeL,OrangeU)
    blue=areaditection(BlueL,BlueU)
   
    # print("Orange is "+str(orange),"Blue is "+str(blue))
    # time.sleep(0.2)
    