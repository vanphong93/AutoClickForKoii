
import os
try:
    import pyautogui as pag
except:
    os.sys("pip install pyautogui")
    os.sys("pip install pillow")
    os.sys("pip install opencv-python")
import pyautogui as pag
import time
timeCheck=20
while True:

        print("Koii is running")
        try:
            start = pag.locateOnScreen('play1.png',grayscale=True,confidence=0.8)
            previous=pag.position()
            pag.click(start)
            pag.moveTo(previous)
            print("Click")
        except pag.ImageNotFoundException:
                     time.sleep(timeCheck)

