import cv2
import numpy as np
import pyautogui
import keyboard
import time

# ----------------------------
GAME_REGION1 = (447, 650, 240, 70)
# GAME_REGION2 = (440, 530, 60, 40)
# Số lượng pixel đen để coi là có vật cản
PIXEL_THRESHOLD = 500           

def detect_obstacle1(frame):       
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    num_black = np.sum(binary == 0)   
    print(num_black)
    return num_black > PIXEL_THRESHOLD, binary

# def detect_obstacle2(frame):       
#     gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#     _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#     num_black = np.sum(binary == 0)   
#     print(num_black)
#     return num_black > PIXEL_THRESHOLD, binary

def grab_frame1():
    screenshot = pyautogui.screenshot(region=GAME_REGION1)
    frame1 = np.array(screenshot)
    return frame1

# def grab_frame2():
#     screenshot = pyautogui.screenshot(region=GAME_REGION2)
#     frame2 = np.array(screenshot)
#     return frame2
# -----------------------------
# Chạy AutoBot  
print("Bot khởi động... Mở game trong 3s")
time.sleep(3)

while True:
    frame1 = grab_frame1()
    # frame2 = grab_frame2()
    obstacle1, binary1 = detect_obstacle1(frame1)
    # obstacle2, binary2 = detect_obstacle2(frame2)
    if obstacle1:
        time.sleep(0.05)
        keyboard.press('up')
        time.sleep(0.1)
        keyboard.release('up')
    # elif obstacle2:
    #     keyboard.press('down')
    #     time.sleep(1)
    #     keyboard.release('down')
    # Hiển thị khung đang theo dõi
    cv2.imshow("View down", binary1)
    # cv2.imshow("View up", binary2)
    # Bấm ESC để thoát
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
