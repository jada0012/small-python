import pyautogui as pag
import time

screenWidth, screenHeight = pag.size()
pag.hotkey("Ctrl", "p")
time.sleep(2)
pag.moveTo(676, 633)
pag.drag(yOffset=300)