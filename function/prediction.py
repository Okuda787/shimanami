import tensorflow as tf
import cv2
import keras
from datetime import datetime
import time
from cameraset import camA
import numpy as np

cam = camA()
start=time.time()
current_dir = "/home/pi/testphoto/"
model=tf.keras.models.load_model("/home/pi/model/model_2.h5")

def prediction():
    _,img2 = cam.read()
    #img_resize=cv2.resize(img,(480,640))
    img = np.expand_dims(img2,0)
    predictions_single = model.predict(img)
    reading_time=time.time()-start
    shoot_time = datetime.now()
    strf_time=shoot_time.strftime('%Y%m%d_%H%M%S%f')
    image_file = current_dir + strf_time +'.jpg'
    cv2.putText(img2,str(np.argmax(predictions_single)+1),(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    cv2.imwrite(image_file, img2)
    # print(image_file)
    print(np.argmax(predictions_single)+1)

   