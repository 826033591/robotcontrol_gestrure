from pymycobot.mycobot import MyCobot
import time

class RobotArmController:

    def __init__(self,port):
        #初始化链接
        self.mc = MyCobot(port, 115200)
        self.init_pose = [0.96, 86.22, -98.26, 10.54, 86.92, -2.37]
        self.coords = [-40, -92.5, 392.7, -92.19, -1.91, -94.14]
        self.speed = 60
        self.mode = 0

    def thum_up(self):
        self.mc.send_angles([0.96, 86.22, -98.26, 10.54, 86.92, -2.37], 60)
        time.sleep(1.5)
        for count in range(3):
            self.mc.send_angles([0.79, 2.46, (-8.17), 4.3, 88.94, 0.26], 70)
            time.sleep(1)
            self.mc.send_angles([(-3.6), 30.32, (-45.79), (-46.84), 97.38, 0.35], 70)
            time.sleep(1)
        self.mc.send_angles([0.79, 2.46, (-8.17), 4.3, 88.94, 0.26], 70)
        time.sleep(1)
        self.mc.send_angles([0.96, 86.22, -98.26, 10.54, 86.92, -2.37], 60)


    def increment_x_and_send(self, increment=20):
        # 增加x值并发送新坐标
        self.coords[0] += increment
        self.mc.send_coords(self.coords, self.speed, self.mode)

    def initial_position(self):
        self.mc.send_angles(self.init_pose,self.speed)


