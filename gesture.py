import mediapipe as mp
import time
import cv2



# # 初始化MediaPipe Hands模块
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


def handle_gesture_detection(hand_landmarks):
    # 判断是否是竖大拇指手势
    if is_thump_up(hand_landmarks):
        return "thumb_up"
    if is_palm_open(hand_landmarks):
        return "palm_open"
    return None

def is_palm_open(hand_landmarks):
    """
    检测是否是手掌打开手势
    """
    # 获取所有指尖和第二个关节的坐标
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
    middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]

    # 检查所有指尖是否都高于对应的关节
    if (thumb_tip.y < thumb_mcp.y and
        index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y):
        return True
    return False

#检测手势是否在画面内
def is_thump_up(hand_landmarks):

    """
    检测特定的手势是否在里面
    """

    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    
    #比较大拇指和食指的Y值那个大
    if thumb_tip.y < index_tip.y:
        return True
    
    return False

