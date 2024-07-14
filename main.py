import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time
import psutil

# Camera Setup
cap = cv2.VideoCapture(2)  # Change the index to 0 if you have only one camera
detector = HandDetector(detectionCon=0.8, maxHands=1)

# VLC Media Player Hotkeys
gesture_actions = {
    "play_pause": "space",
    "volume_up": "up",  # Increase volume by 2%
    "volume_down": "down",  # Decrease volume by 2%
    "next_track": "n",
    "previous_track": "p"
}

# Function to detect gestures and perform actions
def process_gesture(lmList, detector, hand):
    fingers = detector.fingersUp(hand)
    print(fingers)

    # Determine Hand Type (Left or Right)
    if lmList[17][0] < lmList[5][0]:
        hand_type = "Right"
    else:
        hand_type = "Left"

    # Play/Pause Gesture (Index Finger)
    if fingers == [1, 0, 0, 0, 0]:
        pyautogui.press(gesture_actions["play_pause"])
        time.sleep(0.3)  # Prevent accidental multiple presses

    # Volume Up Gesture (Index & Middle Fingers)
    elif fingers == [0, 1, 1, 0, 0]:
        for _ in range(5):  # Press volumeup key 5 times for a bigger change
            pyautogui.press(gesture_actions["volume_up"])

    # Volume Down Gesture (Middle Finger)
    elif fingers == [0, 1, 0, 0, 0]:
        for _ in range(5):
            pyautogui.press(gesture_actions["volume_down"])
  

    # Next Track Gesture (Four fingers of right hand)
    elif fingers == [0, 1, 1, 1, 1] and hand_type == "Right":
        pyautogui.press(gesture_actions["next_track"])
        time.sleep(0.5)

    # Previous Track Gesture (four fingers of left hand)
    elif fingers == [0, 1, 1, 1, 1] and hand_type == "Left":
        pyautogui.press(gesture_actions["previous_track"])
        time.sleep(0.5)

# Activate VLC Media Player
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == "vlc":  # or "vlc.exe" for Windows
        pyautogui.press("alt")
        pyautogui.press("tab")
        break  # Exit loop after VLC is found and activated                                                                           

# Main Loop
while True:
    success, img = cap.read()

    if not success:
        print("Ignoring empty camera frame.")
        continue

    hands, img = detector.findHands(img)  # With draw


    if hands:
        lmList = hands[0]['lmList']
        hand = hands[0]
        process_gesture(lmList, detector, hand)

    cv2.imshow("Gesture Controlled Media Player", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
