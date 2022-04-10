#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: jingmo
@file:   face_v2.py
@time:   2022/04/10 11:55:16
"""

from rec_face import Rec
import time
import os
import argparse
import win32api


def post_config(sleep_min, sleep_sleep, sleep_hide, lm, out_key, out_time):
    # 设置一下命令窗的大小
    os.popen("mode con cols=50 lines=10")
    
    # 暂停检测时间sleep_time(s)
    sleep_time = int(sleep_min * 60)
    
    count_number = 0
    while True:
        # 灵敏度调节 lm人脸检测灵敏度， out_key人脸验证次数， out_time人脸检测超时（秒）
        key = Rec().rec_main(lm=lm, out_key=out_key, out_time=out_time)
        if key:
            # 使用 Scrlk键 阻止熄屏
            win32api.keybd_event(145, 0, 0, 0)
            print("已检测到用户！")
            # 重置检测计数
            print("重置检测计数")
            count_number = 0
        else:
            print("未检测到用户！")
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
            print(f"\r> 下一次检测倒计时：{i} 秒！", end="")
        print("\n")


def main():
    face_info = argparse.ArgumentParser(description="空置参数 - 暂无默认配置 — 请按要求完成设置")
    face_info.add_argument('-m', '--sleep_min', help='* 循环检测倒计时(分钟)_建议值：3', required=True)
    face_info.add_argument('-s', '--sleep_sleep', help='* 超时检测次数后睡眠(整数)_建议值：2', required=True)
    face_info.add_argument('-e', '--sleep_hide', help='* 超时检测次数后休眠(整数)_建议值：5', required=True)
    face_info.add_argument('-l', '--lm', help='* 人脸检测灵敏度1.4~1.6(小数)_建议值：1.5', required=True)
    face_info.add_argument('-o', '--out_key', help='* 人脸验证次数(整数)_建议值：3', required=True)
    face_info.add_argument('-p', '--out_time', help='* 人脸检测超时（秒）_建议值：6', required=True)
    info = face_info.parse_args()

    print("传入的所有信息(命名空间)如下:", info)
    sleep_min = float(info.sleep_min)
    sleep_sleep = int(info.sleep_sleep)
    sleep_hide = int(info.sleep_hide)
    lm = float(info.lm)
    out_key = int(info.out_key)
    out_time = int(info.out_time)
    
    # print(type(sleep_min), type(sleep_sleep), type(sleep_hide), type(lm), type(out_key), type(out_time))
    # python face_v2.py -m 3 -s 2 -e 5 -l 1.5 -o 4 -p 6
    # sleep_min 循环检测倒计时(分钟)，sleep_sleep 超时检测次数后睡眠，sleep_hide 超时检测次数后休眠
    # 灵敏度调节 lm人脸检测灵敏度， out_key人脸验证次数， out_time人脸检测超时（秒）
    # post_config(sleep_min=3, sleep_sleep=2, sleep_hide=5, lm=1.5, out_key=4, out_time=6)
    post_config(sleep_min=sleep_min, sleep_sleep=sleep_sleep, sleep_hide=sleep_hide, lm=lm, out_key=out_key, out_time=out_time)


if __name__ == '__main__':
    try:
        main()
    except:
        os.popen("mode con cols=90 lines=20")
        help_txt = """
        配置参考：
        形如： face_v2.exe -m 3 -s 2 -e 5 -l 1.5 -o 4 -p 6

          '-m' -  '* 循环检测倒计时(分钟)_建议值：3
          '-s' -  '* 超时检测次数后睡眠(整数)_建议值：2
          '-e' -  '* 超时检测次数后休眠(整数)_建议值：5
          '-l' -  '* 人脸检测灵敏度1.4~1.6(小数)_建议值：1.5
          '-o' -  '* 人脸验证次数(整数)_建议值：3
          '-p' -  '* 人脸检测超时（秒）_建议值：6

        """
        print("空置参数 - 暂无默认配置 — 请按要求完成设置\n", help_txt)

