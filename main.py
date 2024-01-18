import time
import mediapipe as mp
from gesture import handle_gesture_detection, is_palm_open, is_thump_up
from robot_control import RobotArmController


import cv2

# 初始化MediaPipe Hands模块
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# 初始化状态变量
gesture_detected = False
gesture_start_time = None
gesture_confirmation_time = 2
action_triggered = False
cooldown_start_time = None
cooldown_period = 2



if __name__ == '__main__':
    # 链接机械臂
    port = 'com6'
    mc = RobotArmController(port)
    mc.initial_position()

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("无法打开摄像头")
        exit()

    while cap.isOpened():
        # print("读取摄像头帧")
        ret, frame = cap.read()

        if not ret:
            continue

        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # 将BGR图像转换为RGB
        rgb_frame = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)
        # 处理图像并检测手部
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(rotated_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 获取手势
                current_gesture = handle_gesture_detection(hand_landmarks)

                # 处理手势
                current_time = time.time()
                if current_gesture:
                    if not gesture_detected:
                        gesture_detected = True
                        gesture_start_time = current_time
                    elif current_time - gesture_start_time > gesture_confirmation_time and not action_triggered:
                        # 根据手势执行相应动作
                        if current_gesture == "thumb_up":
                            print('good good')
                            mc.thum_up()
                        elif current_gesture == "palm_open":
                            print('forward')
                            mc.increment_x_and_send()
                        # 可以添加更多手势和对应动作的判断
                        action_triggered = True
                        cooldown_start_time = current_time
                else:
                    gesture_detected = False
                    gesture_start_time = None
                    if action_triggered and current_time - cooldown_start_time > cooldown_period:
                        print('can continue')
                        action_triggered = False
                        cooldown_start_time = None


        # 显示图像
        cv2.imshow('Hand Tracking', rotated_frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows() 
