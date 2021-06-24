import pyautogui, time
for i in range(1, 15):
    print(i)
    time.sleep(1)

f=open("scr.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('Enter') 