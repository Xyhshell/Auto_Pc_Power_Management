#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author: jingmo
@file:   rec_face.py
@time:   2022/04/07 12:44:43
"""
import os
import time
import cv2


class Rec(object):
    def rec_main(self, lm, out_key, out_time):
        cap = cv2.VideoCapture(0)  # Open camera one
        success, frame = cap.read()  # Read one frame
        print("Camera open operation is: ", success)
        classfier = cv2.CascadeClassifier(r".\haarcascades\haarcascade_frontalface_alt.xml")
        
        # 计数检测
        count_number = 0
        time_start = time.time()
        while success:
            success, frame = cap.read()
            size = frame.shape[:2]  #
            image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #
            cv2.equalizeHist(image2, image2)  #
            divisor = 8
            h, w = size
            minSize = ((int)(w / divisor), (int)(h / divisor))
            
            faceRects = classfier.detectMultiScale(image2, lm, 3, cv2.CASCADE_SCALE_IMAGE, minSize)  # Face detect
            if len(faceRects) > 0:  # If face array length > 0
                count_number += 1
                # print(f"已检测！！{count_number}")
            
            time_out = time.time()
            # 时间取整
            sleep_time = int(time_out - time_start)
            # print(sleep_time)
            
            if sleep_time >= out_time:
                return False
            if count_number >= out_key:
                return True


if __name__ == '__main__':
    rec = Rec().rec_main(lm=1.5, out_key=4, out_time=5)
    print(rec)
    print(type(rec))
