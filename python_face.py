#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author: jingmo
@file:   python_face.py
@time:   2022/04/06 20:28:05
"""

import cv2
import numpy as np

cv2.namedWindow("REC_face")  # Create a window
cap = cv2.VideoCapture(0)  # Open camera one
success, frame = cap.read()  # Read one frame

print("Camera open operation is: ", success)
color = (0, 69, 255)  # Config the color
classfier = cv2.CascadeClassifier(r".\haarcascades\haarcascade_frontalface_alt.xml")

a = 0
while success:
    success, frame = cap.read()
    size = frame.shape[:2]  #
    image1 = np.zeros(size, dtype=np.float16)  #
    image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #
    cv2.equalizeHist(image2, image2)  #
    divisor = 8
    h, w = size
    minSize = ((int)(w / divisor), (int)(h / divisor))
    
    # （大约灵敏度调节）
    # faceRects = classfier.detectMultiScale(image2, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)  # Face detect
    
    faceRects = classfier.detectMultiScale(image2, 1.5, 3, cv2.CASCADE_SCALE_IMAGE, minSize)  # Face detect
    if len(faceRects) > 0:  # If face array length > 0
        for faceRect in faceRects:  # Draw a rectangle for every face
            xf, yf, wf, hf = faceRect
            x = int((float)(xf))
            y = int((float)(yf))
            w = int((float)(wf))
            h = int((float)(hf))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 69, 255), 2)
            cv2.circle(frame, ((int)(x + 1.2 * w / 4), (int)(y + h / 3)), min((int)(w / 8), (int)(h / 8)), (0, 69, 255), 2)
            cv2.circle(frame, ((int)(x + 2.8 * w / 4), (int)(y + h / 3)), min((int)(w / 8), (int)(h / 8)), (0, 69, 255), 2)
        
        a += 1
        print(f"已检测！！{a}")
    
    cv2.imshow("REC_face", frame)  # Display image
    
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q', 'Q', chr(27)]:
        break
    if a >= 30:
        break

cv2.destroyWindow("REC_face")
