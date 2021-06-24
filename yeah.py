import pyautogui, time
time.sleep(14)
f=open("scr.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('Enter') 