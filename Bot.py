import pyautogui
import pydirectinput
import time
import keyboard
import random
import win32api, win32con

while 1:
    time.sleep(0.5)
    if pyautogui.locateOnScreen('1time.png', confidence=0.85) != None:
        print("1 time")
        pydirectinput.press('space')
        time.sleep(5)
        pydirectinput.press('z')
    elif pyautogui.locateOnScreen('2times.png', confidence=0.85) != None:
        print("2 times")
        pydirectinput.press('space')
        pydirectinput.press('space')
        time.sleep(5)
        pydirectinput.press('z')
    elif pyautogui.locateOnScreen('3times.png', confidence=0.85) != None:
        print("3 times")
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        time.sleep(5)
        pydirectinput.press('z')
    elif pyautogui.locateOnScreen('4times.png', confidence=0.85) != None:
        print("4 times")
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        time.sleep(5)
        pydirectinput.press('z')
    elif pyautogui.locateOnScreen('5times.png', confidence=0.85) != None:
        print("5 times")
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.press('space')
        time.sleep(5)
        pydirectinput.press('z')
