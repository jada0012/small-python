import pyautogui as pag
import time
import random

screenWidth, screenHeight = pag.size()
pag.press("F6")

time.sleep(5)

# pag.click(669,443)

# pag.hotkey("Ctrl", "p")
# time.sleep(2)
pag.moveTo(676, 633)
time.sleep(2)
pag.mouseDown()
pag.drag( yOffset=-400, duration=2, button="left" )
pag.mouseUp()
time.sleep(2)

#click home button
pag.click(682, 698)

#click snapchat
pag.click(593, 548, duration=0.5)

#click camera
pag.click(680, 602, duration=1.5)
time.sleep(1.5)

#click crayon
pag.click(816,125, duration=1.98)

#pick colour
time.sleep(1)
pag.click(816, random.randint(120,225), duration=1.4)

#move to beginning of letter
time.sleep(1)
pag.moveTo(774, 157)

#drag
pag.dragTo(620,312,0.5,button="left")
pag.dragTo(745,420,0.5,button="left")
pag.dragTo(626,524,0.5,button="left")

#hit send button
pag.click(812,655, duration=0.6)

#hit recipients
pag.click(744,292, duration=0.5)
pag.click(595,331, duration=0.5)
pag.click(706,330, duration=0.5)
pag.click(616,291, duration=0.5)