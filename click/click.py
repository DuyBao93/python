import pyautogui as pag
import sys
import time

time.sleep(10)
# print (pag.position())

count = 1
while (True):
    try:
        c = pag.locateOnScreen('cal.png', grayscale=True, confidence=.5)
        print ("in screen")
        if (count == 2):
            pag.press("1")
            count = 1
        else:
            pag.press("9")
            count += 1
    except:
        print ("exit program")
        sys.exit()