import time     
import brickpi3 

BP = brickpi3.BrickPi3() 
BP.set_sensor_type(BP.PORT_3,  BP.SENSOR_TYPE.NXT_LIGHT_ON) #右
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.NXT_LIGHT_ON) #左
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右
time.sleep(1)

max = 60
med = 40
min = 10 
# max = 35
# med = 20
# min = -10 歯車とりver.
lc_b = -5
hc_b = -15
max_v = 1000
min_v = -1000

goal = 50

try: 
    while True:

        sen_reading = int(BP.get_sensor(BP.PORT_4)) - int(BP.get_sensor(BP.PORT_3))
        nor_reading = 100 *(sen_reading - min_v)/(max_v - min_v)
        dif = -(nor_reading - goal)

        # print(dif)

        # BP.set_motor_power(BP.PORT_B, -med*1.7)
        # BP.set_motor_power(BP.PORT_D, -med)

        if dif > 30:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -min)
            print(1)
        elif dif > 15:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -med)
            print(2)
        elif dif < -30:
            BP.set_motor_power(BP.PORT_B, -min)
            BP.set_motor_power(BP.PORT_D, -max)
            print(3)
        elif dif < -15:
            BP.set_motor_power(BP.PORT_B, -med)
            BP.set_motor_power(BP.PORT_D, -max)
            print(4)
        else:
            BP.set_motor_power(BP.PORT_B, -max)
            BP.set_motor_power(BP.PORT_D, -max)
            print(5)

        # BP.set_motor_power(BP.PORT_B, -max*1.3)
        # BP.set_motor_power(BP.PORT_D, -med)
        # print(2)
        time.sleep(0.03)

except KeyboardInterrupt: 
    BP.reset_all()        
    print("Program Interrupted")

# python3 five_direction.py