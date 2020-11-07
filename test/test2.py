# -*- coding: utf-8 -*-
from datetime import datetime
import cv2, os
import time
import brickpi3
import pandas as pd

def main():
    # パス
    current_dir = "/home/pi/testphoto/"
    cam = cv2.VideoCapture(0)
    # cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'));
    # [[]]であることに注意、index_colで一列目をインデックス（一番左）にしてる
    # df = pd.read_csv("/home/pi/sample1.csv",index_col=[0])
    BP=brickpi3.BrickPi3()

    if cam == None:
        return False

    time.sleep(1)
    # スタート時間
    start=time.time()
    i=0
    while True:
        try:
            _, img = cam.read()
            # 開始何秒か記録
            reading_time=time.time()-start
            
            shoot_time = datetime.now()
            strf_time=shoot_time.strftime('%Y%m%d_%H%M%S%f')
            image_file = current_dir + strf_time +'.jpg'
            
            # df.loc[i]=[reading_time,strf_time]

            cv2.imwrite(image_file, img)

            print(reading_time,strf_time)

            # On python,"i=i+1" is faster than "i+=1"
            i=i+1

            time.sleep(0.02)

        except KeyboardInterrupt:
            print("Ctrl+Cでcameraは停止しました")
            # save
            # df.to_csv("/home/pi/sample1.csv")
            BP.reset_all()
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()