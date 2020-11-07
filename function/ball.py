import cv2
import time
from cameraset import camB
from datetime import datetime

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cam=camB()
current_dir = "/home/pi/testphoto/"
start=time.time()

def ball():
    _,img = cam.read()
    reading_time=time.time()-start
    shoot_time = datetime.now()
    strf_time=shoot_time.strftime('%Y%m%d_%H%M%S%f')
    image_file = current_dir + strf_time +'.jpg'
    cv2.imwrite(image_file, img)
    img_b=cv2.imread(image_file,1)
    # circles = cv2.HoughCircles(img_b,cv2.HOUGH_GRADIENT,dp =1,minDist = 10,param1 = 50,param2 = 45,minRadius = 1,maxRadius = 35)#円の検出　param1,2ともに下げるとゆるく、上げると厳しくなる
    # for i in circles[0]:
    #     cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),3)#線を書くだけなのでいらない
    #     print("X"+str(i[0]))
    #     print("Y"+str(i[1]))
    #     print("r"+str(i[2]))
    
    # cv2.putText(img,str(i[0]),(0,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)
    # cv2.putText(img,str(i[1]),(0,150),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)
    # cv2.putText(img,str(i[2]),(0,200),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)
    

if __name__=='__main__':
    try:
        while True:
            ball()
    except KeyboardInterrupt:
        print("Program Interrupted")