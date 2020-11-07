#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import time     # import the time library for the sleep function
import brickpi3
from builtins import input

BP=brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON)
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
time.sleep(1)
try:
    while True:
        value = int(BP.get_sensor(BP.PORT_4))
        #ただのライントレース 
        t=2100  #閾値を決める
        s=10
        k1=3
        k2=0.04#比例定数
        l= -1*(k1*(s-k2*(value-t)))
        r=-1*(k1*(s+k2*(value-t)))
        #BP.get_motocccr_encoderを使うのかな？うまく動かなかったら多分それが原因。必要かわからなかったから書いてない。
        BP.set_motor_power(BP.PORT_D, int(r))
        BP.set_motor_power(BP.PORT_B, int(l))
        time.sleep(0.02)
        print(value)

except KeyboardInterrupt:
    BP.reset_all()
    print("Ctrl+Cでmotorは停止しました")


