#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author: jingmo
@file:   face_repson.py
@time:   2022/04/07 12:14:53
"""

"""
# 人像检测
    ok
# 检测响应
 # 1.设置超时！
     # demo 细化检测时间
        3-5 min 检测一次
        设置检测方式（存在于检测灵敏的优化，）
        / 人像检测的准确/（合格性）

 # 2.超时响应 （test）
    # 5 min 熄屏/ 锁屏   cmd 下输入 rundll32.exe user32.dll LockWorkStation，可以启动屏幕保护功能
    # 20 min 休眠       cmd  shutdown -h 这条指令让计算机休眠(未测试！)
    # ...
"""

from rec_face import Rec
import time
import os
import win32api


def post_config(sleep_min, sleep_sleep, sleep_hide, lm, out_key, out_time):
    # 暂停检测时间sleep_time(min)
    sleep_time = sleep_min * 60
    
    count_number = 0
    while True:
        # 灵敏度调节 lm人脸检测灵敏度， out_key人脸验证次数， out_time人脸检测超时（秒）
        key = Rec().rec_main(lm=lm, out_key=out_key, out_time=out_time)
        if key:
            # 重置检测计数
            count_number = 0
            print("已检测到用户！")
            
            # # 开始输入
            # # 关于锁屏
            # # 输入猜想
            # time.sleep(0.5)
            # # 回车
            # win32api.keybd_event(13, 0, 0, 0)
            # # 输入密码
            # time.sleep(1.5)
            # win32api.keybd_event(79, 0, 0, 0)
            # time.sleep(0.5)
            # win32api.keybd_event(80, 0, 0, 0)
            # time.sleep(0.5)
            # win32api.keybd_event(80, 0, 0, 0)
            # time.sleep(0.5)
            # win32api.keybd_event(79, 0, 0, 0)
            # # 回车
            # time.sleep(0.5)
            # win32api.keybd_event(13, 0, 0, 0)

        else:
            # 未检测计数，达到sleep_sleep 设定次数，执行睡眠
            # 未检测计数，达到sleep_hide 设定次数，执行休眠 / 否则锁屏
            count_number += 1
            print("检测计数：", count_number)
            if count_number >= sleep_sleep:
                print("执行睡眠")
                os.popen("psshutdown.exe -d -t 0")
                
            if count_number >= sleep_hide:
                print("执行休眠")
                # cmd的休眠指令：rundll32.exe powrProf.dll,SetSuspendState
                os.popen("rundll32.exe powrProf.dll,SetSuspendState")
            else:
                print("执行锁屏")
                # cmd的锁屏指令：rundll32.exe user32.dll LockWorkStation
                os.popen("rundll32.exe user32.dll LockWorkStation")
            
        for i in range(sleep_time, 0, -1):
            time.sleep(1)
            print(f"\r> 检测倒计时：{i} 秒！", end="")
        print("\n")


if __name__ == '__main__':
    # 设置一下命令窗的大小
    os.popen("mode con cols=50 lines=10")
    # sleep_min 循环检测次数，sleep_sleep 超时检测次数后睡眠，sleep_hide 超时检测次数后休眠
    # 灵敏度调节 lm人脸检测灵敏度， out_key人脸验证次数， out_time人脸检测超时（秒）
    post_config(sleep_min=3, sleep_sleep=2, sleep_hide=5, lm=1.5, out_key=5, out_time=6)

    