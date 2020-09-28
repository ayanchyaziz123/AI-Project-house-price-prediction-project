import pyautogui
import time
message  = 200

while message > 0:
    time.sleep(2)
    pyautogui.typewrite("I love uuuu so muchh")
    time.sleep(2)
    pyautogui.press('enter')
    message -= 1