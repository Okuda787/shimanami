import cv2
import os

current_dir = "/home/pi/testphoto/"
cam = camB()
### size=0
### dif=0
start=time.time()
try:
    while True:
        _,img = cam.read()
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

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
            Size=rect[2]*rect[3]
            if Size>=10000:
                cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (0, 0 , 255), thickness=5)
                Dif=320-((rect[2]/2)+rect[0])
                Size = rect[2]*rect[3]
            else:
                Dif = 100
        else:  #
            print('rects empty')
            print(rects)
            Size = 0 #
            Dif = 0 #
        dst1 = cv2.bitwise_and(img,img,mask = opening) 
        reading_time=time.time()-start
        shoot_time = datetime.now()
        strf_time=shoot_time.strftime('%Y%m%d_%H%M%S%f')
        image_file = current_dir + strf_time +'.jpg'
        cv2.putText(dst1,str(Dif),(0,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)
        cv2.putText(dst1,str(Size),(0,150),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)
        cv2.imwrite(image_file, dst1)
        print("Size: "+str(Size),"target: "+str(target)) 