import cv2

def camA(): #下向き
    camA = cv2.VideoCapture(0)
    # camA.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'));
    camA.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camA.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return camA

def camB(): #前面
    camB = cv2.VideoCapture(1)
    camB.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'));
    camB.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camB.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return camB

