import pyautogui
import time
import random
time.sleep(3)
movement = ['up', 'down', 'left', 'right']

while True:
    pyautogui.press('down')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('up')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press(movement[random.randint(0, 3)])
    


  