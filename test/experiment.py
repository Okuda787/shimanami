import numpy as np
import cv2
import time
import brickpi3  

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));

BP = brickpi3.BrickPi3() 
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  #左
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  #右

try:
    while(True):
        start=time.time()
        _,img = cam.read()
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # #Blue
        # lower = np.array([10, 150, 0])
        # upper = np.array([50,255,255])

        # Orange
        lower = np.array([10, 120, 0])
        upper = np.array([50,255,255])
        frame_mask = cv2.inRange(hsv,lower,upper)

        kernel=np.ones((5,5),dtype = np.uint8)
        opening=cv2.morphologyEx(frame_mask,cv2.MORPH_OPEN,kernel)

        contours, hierarchy  = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        rects = []
        for contour in contours:
            approx = cv2.convexHull(contour)
            rect = cv2.boundingRect(approx)
            rects.append(np.array(rect))

        if len(rects) > 0:
            rect = max(rects, key=(lambda x: x[2] * x[3]))
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 0 , 0), thickness=5)


        size=rect[2]*rect[3]
        dst1 = cv2.bitwise_and(img,img,mask = opening) 
        print(size)
        

        if size>200000:
            print("yes")
            BP.set_motor_power(BP.PORT_B, 30)
            BP.set_motor_power(BP.PORT_D, 30)
        else:
            BP.set_motor_power(BP.PORT_B, -30)
            BP.set_motor_power(BP.PORT_D, -30)
        finish=time.time()

except KeyboardInterrupt: 
    BP.reset_all()
    cam.release()        
    print("Program Interrupted")
   

 

