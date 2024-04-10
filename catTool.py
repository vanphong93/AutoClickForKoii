
import pyautogui as py
import time

# for x in range(3):
#     print("Cat is running")
#     py.dragTo(212, 520, button='left')
#     py.dragTo(212, 521, 3, button='left')
#     try:
#         start = py.locateOnScreen('moveTo.png',confidence=0.8)
#         print(start)
#         py.moveTo(start)
#         py.dragTo(212, 520,1, button='left')
#         # py.dragTo(start,2, button='left')
      
#     except py.ImageNotFoundException:
#         pass


# x=132
# y=478


# color1=py.pixel(x,y)
# py.moveTo(x,478)
# color2=py.pixel(x+63,y)
# print(color1)
# print(color2)
# if color1==color2:
#     py.dragTo(x, y, button='left')
#     py.dragTo(x+63, y, 0.5, button='left')
# else:
#     print("no")

while True:
    for y in range(332,439,48):
        for x in range(171,361,63):
            py.click(x,y)
            time.sleep(0.3)
            try:
                start = py.locateOnScreen('freeCat.png',confidence=0.8)
                py.click(start)
                time.sleep(360)
                break
            except py.ImageNotFoundException:
                    pass
            try:
                start = py.locateOnScreen('1min.png',confidence=0.8)
                py.click(start)
                time.sleep(360)
                break
            except py.ImageNotFoundException:
                    pass
