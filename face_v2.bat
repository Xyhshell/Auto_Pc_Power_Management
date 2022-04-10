@ECHO OFF&PUSHD %~DP0 &TITLE   face_v2 By：jingmo
mode con cols=90 lines=20
@rem color 9F

@echo
@echo  配置参考(按格式填写！)：
@echo  形如： face_v2.exe -m 3 -s 2 -e 5 -l 1.5 -o 4 -p 6  
@echo  --
@echo    '-m' -  '* 循环检测倒计时(分钟)_建议值：3
@echo    '-s' -  '* 超时检测次数后睡眠(整数)_建议值：2
@echo    '-e' -  '* 超时检测次数后休眠(整数)_建议值：5
@echo    '-l' -  '* 人脸检测灵敏度1.4~1.6(小数)_建议值：1.5
@echo    '-o' -  '* 人脸验证次数(整数)_建议值：3
@echo    '-p' -  '* 人脸检测超时（秒）_建议值：6
pause
face_v2.exe -m 3 -s 2 -e 5 -l 1.5 -o 4 -p 6

