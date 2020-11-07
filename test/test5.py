#!/usr/local/bin/python3
import time     # import the time library for the sleep function
import brickpi3
import time 
import cv2
import picamera
from builtins import input

BP=brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON)
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
time.sleep(1)
main_dir="/home/pi/testphoto/"  
# カメラ初期化
camera=picamera.PiCamera()
# 解像度の設定
camera.resolution = (512, 384)


i=0

try:
    while True:
        i+=1
        value = int(BP.get_sensor(BP.PORT_4))
        #ただのライントレース 
        t=2200  #閾値を決める
        s=20
        k1=3
        k2=0.05#比例定数
        l= k1*(s-k2*(value-t))
        r=k1*(s+k2*(value-t))
        #BP.get_motor_encoderを使うのかな？うまく動かなかったら多分それが原因。必要かわからなかったから書いてない。
        BP.set_motor_power(BP.PORT_D, int(r))
        BP.set_motor_power(BP.PORT_B, int(l))
        time.sleep(0.2)
        # 撮影して指定したファイル名で保存する
        camera.capture(main_dir+"photo"+str(i)+".jpg")
        print(value)

except KeyboardInterrupt:
    BP.reset_all()



