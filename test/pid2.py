import time     
import brickpi3 

BP = brickpi3.BrickPi3() 
BP.set_sensor_type(BP.PORT_3,  BP.SENSOR_TYPE.NXT_LIGHT_ON) #右
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON) #左
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右
time.sleep(1)

base_speed = 60
kp = 0.9
kd = 12 
ki = 0.02

max_v_l = 2680 #センサー最大値
min_v_l = 1807 #センサー最小値
max_v_r = 2777 #センサー最大値
min_v_r = 1871 #センサー最小値


goal_l = 0 #センサー目標値
goal_r = 0

isum_l = 0
dif_l = 0
isum_r = 0
dif_r = 0

try: 
    while True:

        sen_reading_l = int(BP.get_sensor(BP.PORT_4)) #実測値
        nor_reading_l = 100 *(sen_reading_l - min_v_l)/(max_v_l - min_v_l) #実測値を標準化　0が最小値　100が最大値
        
        pre_dif_l = dif_l #前回のずれを記録
        dif_l = goal_l - nor_reading_l #今回のずれを記録
        isum_l = isum_l/2 + dif_l #いままでのずれを足し合わせる
        ddif_l = dif_l - pre_dif_l #前回との差分を出す
        
        l_pow = (kp*dif_l + ki*isum_l*1.2 + kd*ddif_l + base_speed)

        sen_reading_r = int(BP.get_sensor(BP.PORT_3))
        nor_reading_r = 100 *(sen_reading_r - min_v_r)/(max_v_r - min_v_r)
        
        pre_dif_r = dif_r #前回のずれを記録
        dif_r = goal_r - nor_reading_r #今回のずれを記録
        isum_r = isum_r/2 + dif_r #いままでのずれを足し合わせる
        ddif_r = dif_r - pre_dif_r #前回との差分を出す
        
        r_pow = (kp*dif_r + ki*isum_r + kd*ddif_r + base_speed) 
        
        BP.set_motor_power(BP.PORT_B, l_pow)
        BP.set_motor_power(BP.PORT_D, r_pow)

        # print(nor_reading_l,nor_reading_r)
        # print(l_pow,r_pow)
        time.sleep(0.01)

except KeyboardInterrupt: 
    BP.reset_all()        
    print("Program Interrupted")