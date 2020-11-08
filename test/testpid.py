import numpy as np
import cv2
import time
import brickpi3  
from function.areadetection import area
from function.movement import r90,l90,straight,stay
from function.pid import *

# BP = brickpi3.BrickPi3() 
# BP.set_sensor_type(BP.PORT_3,  BP.SENSOR_TYPE.NXT_LIGHT_ON) #右
# BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON) #左
# BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
# BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右
# time.sleep(1)

# base_speed = 60
# kp = 0.9
# kd = 12 
# ki = 0.02

# max_v_l = 2680 #センサー最大値
# min_v_l = 1807 #センサー最小値
# max_v_r = 2777 #センサー最大値
# min_v_r = 1871 #センサー最小値

# goal_l = 0 #センサー目標値
# goal_r = 0

# isum_l = 0
# dif_l = 0
# isum_r = 0
# dif_r = 0

L = np.array([100,120,0])
U = np.array([150,255,255])
T = 300000


def returnTrue():
    wall=area(L,U,T)
    print(1)
    return True

pid(returnTrue)