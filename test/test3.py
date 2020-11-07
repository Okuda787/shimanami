#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import time     # import the time library for the sleep function
import brickpi3
from builtins import input
import pandas as pd

BP=brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.NXT_LIGHT_ON) #?????????
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
time.sleep(1)

# df = pd.read_csv("/home/pi/sample2.csv",index_col=[0])
start=time.time()
i=0
try:
    while True:  
        #turn on the motors 
        v1 = int(BP.get_sensor(BP.PORT_4)) #left
        v2 = int(BP.get_sensor(BP.PORT_3)) #right
        # base speed
        s=30

        print(v1,v2)
        
        # k1=0.08#double sensors version
        # r = -1*(k1*(v1-v2)+s)   
        # l = -1*(k1*(v2-v1)+s)

        # #t=2100 #single sensor version
        # # k2=0.04#????
        # # l= -1*(k1*(s-k2*(value-t)))
        # # r=-1*(k1*(s+k2*(value-t)))
        # #BP.get_motocccr_encoder???????????????????????????????????????????
        
        # # 開始何秒か記録
        # reading_time=time.time()-start

        BP.set_motor_power(BP.PORT_D, s)
        BP.set_motor_power(BP.PORT_B, s)

        # BP.set_motor_power(BP.PORT_D, int(r))
        # BP.set_motor_power(BP.PORT_B, int(l))
        
        # df.loc[i]=[reading_time,r,l]
        # df.to_csv("/home/pi/sample2.csv")
        # i=1+i
        # time.sleep(0.038)
        time.sleep(0.02)

except KeyboardInterrupt:
    BP.reset_all()
    # save
    
    print("Ctrl+Cでmotorは停止しました")
    
# python3 test3.py&python3 test2.py