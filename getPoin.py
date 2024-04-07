
import os
try:
    import pyautogui as pag
except:
    os.sys("pip install pyautogui")
    os.sys("pip install pillow")
import pyautogui as pag
import time
time.sleep(5)
print("Move to X,Y want to click")
print(pag.displayMousePosition())
