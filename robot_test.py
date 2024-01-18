from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('com6',115200)

mc.send_angles([0.96, 86.22, -98.26, 10.54, 86.92, -2.37],60)
time.sleep(2)
for count in range(3):
  mc.send_angles([0.79,2.46,(-8.17),4.3,88.94,0.26],70)
  time.sleep(1)
  mc.send_angles([(-3.6),30.32,(-45.79),(-46.84),97.38,0.35],70)
  time.sleep(1)
mc.send_angles([0.79,2.46,(-8.17),4.3,88.94,0.26],70)