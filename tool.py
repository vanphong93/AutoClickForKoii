
import pyautogui as pag
import time
#Number of task  you want to run
number=3
# Poin X (head)
x=326
# Poin Y (head)
y=275
# The distance between two points in the Y direction
distance=347-275
# Time per test
timeCheck=15
# Restart (True or False)
autoRestart=False
# If autoRestart=True, please input passWord when login and change IconApp.png
myPass='99999'
while True:
    windows = pag.getAllWindows()
    isDoing=False
    for window in windows:
        find=window.title
        if find == 'Koii Node':
            isDoing=True
            break
    if isDoing:
        print("Koii is running")
        for pointY in range(y, y + distance*number,distance):
                # pag.moveTo(x,pointY)
                time.sleep(6)
                try:
                    start = pag.locateOnScreen('play1.png',grayscale=True,confidence=0.8)
                    pag.click(start)
                    print("I see")
                except pag.ImageNotFoundException:
                     pass
                     
                # result=pag.pixelMatchesColor(x,pointY,(255,255,255))
                # if result:
                #     pag.leftClick(x,pointY)
    # else :
    #     if autoRestart:
    #         print("Some thing wrong, app is restarting")
    #         try:
    #             loc=pag.locateOnScreen("IconApp.png")
    #             pag.doubleClick(loc)
    #             time.sleep(25)
    #             pag.press(myPass[0])
    #             time.sleep(2)
    #             pag.press(myPass[1])
    #             time.sleep(2)
    #             pag.press(myPass[2])
    #             time.sleep(2)
    #             pag.press(myPass[3])
    #             time.sleep(2)
    #             pag.press(myPass[4])
    #             time.sleep(2)
    #             pag.press(myPass[5])
    #             time.sleep(20)
    #         except pag.ImageNotFoundException:
    #             print("Sorry, Image cannot be recognized")
    # time.sleep(timeCheck)
