import time     
import brickpi3 
from .areaditection import *

BP = brickpi3.BrickPi3() 
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.NXT_LIGHT_ON) #右
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON) #左
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))  #真ん中

max_v_l = 2680 #センサー最大値
min_v_l = 1807 #センサー最小値
max_v_r = 2777 #センサー最大値
min_v_r = 1871 #センサー最小値

def r90(second):
    stay(0.5)
    start=time.time()
    cur=0
    target=540/second
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, target)
        BP.set_motor_dps(BP.PORT_D, -1*target)
        cur=time.time()-start

def l90(second):
    stay(0.5)
    start=time.time()
    cur=0
    target=540/second
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, -1*target)
        BP.set_motor_dps(BP.PORT_D, target)
        cur=time.time()-start

def straight(second,power):
    start=time.time()
    cur=0
    while(cur<=second):
        BP.set_motor_power(BP.PORT_B, power)
        BP.set_motor_power(BP.PORT_D, power)
        cur=time.time()-start

def straightwhileW(second,power):
    nor_reading_l=0 
    l=0 #時間で終わったのか線を読んで終わったのか
    while l==0:
        start=time.time()
        cur=0
        while(cur<=second):
            sen_reading_l = int(BP.get_sensor(BP.PORT_4)) #実測値
            nor_reading_l = 100 *(sen_reading_l - min_v_l)/(max_v_l - min_v_l) #実測値を標準化　0が最小値　100が最大値
            if nor_reading_l<=80:# 白　
                BP.set_motor_power(BP.PORT_B, power)
                BP.set_motor_power(BP.PORT_D, power)
                
            else:
                l=1
                print('fin')
                stay(0.5)
                break
            cur=time.time()-start
            # print(nor_reading_l)
        if l==0:
            stay(0.5)
            l90(3)
        
        

def stay(second):
    start=time.time()
    cur=0
    while(cur<=second):
        BP.set_motor_power(BP.PORT_B, 0)
        BP.set_motor_power(BP.PORT_D, 0)
        cur=time.time()-start
 
def r90cor():##
    stay(1)
    start=time.time()
    cur=0
    second=1.5
    power=30
    target=480/second
    nor_reading_l=0

    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, target)
        BP.set_motor_dps(BP.PORT_D, -1*target)
        cur=time.time()-start
    while(nor_reading_l<=80): #黒見つけるまで
        sen_reading_l = int(BP.get_sensor(BP.PORT_4)) #実測値
        nor_reading_l = 100 *(sen_reading_l - min_v_l)/(max_v_l - min_v_l) #実測値を標準化　0が最小値　100が最大値
        BP.set_motor_dps(BP.PORT_B, target)
        BP.set_motor_dps(BP.PORT_D, -1*target)
        cur=time.time()-start

    start=time.time()
    target=200/second
    cur=0
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, -1*target)
        BP.set_motor_dps(BP.PORT_D, target)
        cur=time.time()-start
        
def l90cor():##
    stay(1)
    start=time.time()
    cur=0
    second=1.5
    power=30
    target=480/second
    nor_reading_r=0

    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, -1*target)
        BP.set_motor_dps(BP.PORT_D, target)
        cur=time.time()-start
    while(nor_reading_r<=80): #黒見つけるまで
        sen_reading_r = int(BP.get_sensor(BP.PORT_3))
        nor_reading_r = 100 *(sen_reading_r - min_v_r)/(max_v_r - min_v_r) #実測値を標準化　0が最小値　100が最大値
        BP.set_motor_power(BP.PORT_B, power)
        BP.set_motor_power(BP.PORT_D, -1*power)
    
    start=time.time()
    target=200/second
    cur=0
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_B, -1*target)
        BP.set_motor_dps(BP.PORT_D, target)
        cur=time.time()-start

#案A　固定合わせ
# def curves(dif): #
#     k = 2 #比例定数
#     curve = k * dif 
#     for i in range(10):
#         BP.set_motor_power(BP.PORT_B,curve) 
#         BP.set_motor_power(BP.PORT_D,-curve) 
#     print("Checking whether or not this is run only once ")
#案B　ループ毎更新
def curves(dif): #
    k = 0.15 #比例定数
    curve = k * dif 
    while abs(dif) > 30 : 
        BP.set_motor_power(BP.PORT_B,-curve) 
        BP.set_motor_power(BP.PORT_D,curve) 
        front,dif,size=areaBlue() #
        stay(0.15)
        # print(dif)
        curve = k * dif
#案C　difからdegreesを出して角速度
# def curves(dif): #
#     k = 0.3 #比例定数s
#     deg = k * dif 
#     start=time.time()
#     cur=0
#     second=1.5
#     target=deg/second
#     while(cur<=second):
#         cur=time.time()-start
#         BP.set_motor_dps(BP.PORT_B, -1*target)
#         BP.set_motor_dps(BP.PORT_D, target)
        

def armUp():
    start=time.time()
    cur=0
    second=2
    target=320/second
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_C, -1*target)
        cur=time.time()-start
    BP.set_motor_power(BP.PORT_C, 0)

    start=time.time()
    cur=0
    second=2
    target=70/second
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_C, target)
        cur=time.time()-start
    BP.set_motor_power(BP.PORT_C, 0)

def armDown():
    start=time.time()
    cur=0
    second=2
    target=290/second
    while(cur<=second):
        BP.set_motor_dps(BP.PORT_C, target)
        cur=time.time()-start
    BP.set_motor_power(BP.PORT_C, 0)

if __name__ == '__main__':
    # armUp()
    # time.sleep(1)
    # armDown()
    straightwhileW(4,30)