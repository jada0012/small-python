import schedule 
import playsound
import time
import PySimpleGUI as sg 

def timer():
    mp3="takeabreak.mp3"
    playsound.playsound(mp3)
    sg.popup("Look 20 feet away for 20 seconds.")
  

schedule.every(20).minutes.do(timer)
while True:
    schedule.run_pending()
    time.sleep(1)