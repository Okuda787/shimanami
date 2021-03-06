import numpy as np
import cv2
import time
import brickpi3  
import os
import shutil
from function.areadetection import *
from function.movement import *
from function.pid_g import *

BP = brickpi3.BrickPi3() 
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B)) #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D)) #右

# ifの後を書く

T2 = 140000

powerForward=30
### dif=20
true=[]
def rescuekit():
    while True:
        front,dif,size=areaBlue() #
        if front == True: #
            print("dif:"+str(dif))
            if abs(dif) <= 50: 
                print("Found")
                if len(true) > 3:
                    stay(1)
                    armUp()
                    time.sleep(1)
                    armDown()
                    for i in range(10):
                        front,dif,size=areaBlue() #
                    straightwhileW(5,-40)
                    stay(1)
        
                else:
                    if size >= T2: #キット取りますの
                        true.append(0)
                        print(true)
                    else: #まだ進みますの
                        print("forward")
                        while size <= T2:
                            BP.set_motor_power(BP.PORT_B, powerForward)
                            BP.set_motor_power(BP.PORT_D, powerForward)
                            front,dif,size=areaBlue() #
            else:
                print("I'll rotate")
                front,dif,size=areaBlue() #
                curves(dif) #
                armDown()
                stay(2)
                # front,dif,size=area(L,U,T) 
        else:
            pid_g()


if __name__ == '__main__':
    try:
        target_dir = '/home/pi/testphoto'
        shutil.rmtree(target_dir)
        os.mkdir(target_dir)
        rescuekit()
    except KeyboardInterrupt: 
        BP.reset_all()        
        print("Program Interrupted")
    