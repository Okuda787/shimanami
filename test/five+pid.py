# from __future__ import print_function 
# from __future__ import division       
import time     
import brickpi3 

BP = brickpi3.BrickPi3() 
BP.set_sensor_type(BP.PORT_3,  BP.SENSOR_TYPE.NXT_LIGHT_ON) #右
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON) #左
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右
time.sleep(1)

max = 50
med = 25
min = -max
lc_b = -5
hc_b = -15
max_v = 1000
min_v = -1000
goal = 50

try: 
    while True:

        sen_reading = int(BP.get_sensor(BP.PORT_4)) - int(BP.get_sensor(BP.PORT_3))
        nor_reading = 100 *(sen_reading - min_v)/(max_v - min_v)
        dif = nor_reading - goal

        print(dif)

        if dif > 30:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -min)
        elif dif > 10:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -med)
        elif dif < -30:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -max)
        elif dif < -10:
            BP.set_motor_power(BP.PORT_B, -med)
            BP.set_motor_power(BP.PORT_D, -max)
        
        else:
            pid()
        time.sleep(0.03)

except KeyboardInterrupt: 
    BP.reset_all()        
    print("Program Interrupted")

# python3 five_direction.py