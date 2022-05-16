import sys
import time
import PySimpleGUI as sg 
import pyinputplus as pyin 
import requests


def seconds(hr,mins):
    sec = (hr*3600) + (mins*60)
    return sec

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        try:
            print(timer, end='\r')
            time.sleep(1)
            t-= 1
        except KeyboardInterrupt:
            input('press enter to continue')            
    
    sg.popup("time's up",auto_close=True, auto_close_duration=1,keep_on_top=True )
    
    

def pomotimer():
    default = pyin.inputYesNo('Do you want to use the default settings?\n Work:25mins \n Short break: 5mins \n Long Break: 15 mins\n')
    if default == 'yes':
        work = 25*60
        sbreak = 5*60
        lbreak = 15*60
        times = 100
        
        n=3
    else:
        s= pyin.inputYesNo('Do you know the time in seconds you want to work for.')
        if s == 'yes':
        
            work = pyin.inputNum('enter the time in seconds you want to work for.')
            sbreak =pyin.inputNum('enter the time in seconds you want to be on break for.')
            lbreak = pyin.inputNum('enter the time in seconds you want to be on a longer break for.')
        else:
            hours = pyin.inputInt('Enter the amount of hours you will be working for.')
            mins = pyin.inputInt('Enter the amount of minutes you will be working for.')
            work = seconds(hours, mins)

            hours = pyin.inputInt('Enter the amount of hours you will be on break for.')
            mins = pyin.inputInt('Enter the amount of minutes you will be on break for.')
            sbreak = seconds(hours, mins)

            hours = pyin.inputInt('Enter the amount of hours you will be on break for.')
            mins = pyin.inputInt('Enter the amount of minutes you will be on break for.')
            lbreak = seconds(hours, mins)


        times = pyin.inputNum('enter how many times you want to pomodoro for')
        n = pyin.inputNum('enter the amount of short breaks you want to have before a long break')

        
        
    
        

    completed = 0
    
    for i in range(1, times):
        if i != 0 and i % (n+1) == 0:
            print(f'Session number {i}')
            countdown(work  )

            print('long break!')
            countdown(lbreak)
            
        print(f'Session number {i}')
        print('work')
        countdown(work  )
        print('short break')
        countdown(sbreak  )
        completed +=1
def alt_pomodoro():
    
    
    work = 30*60
    sbreak = 5*60
    lbreak = 20*60
    times = 100
    mp3 = 'D:\\python\\small-python-projects\\takeabreak.mp3'
    n=2
    

    for i in range(1, times):

        print(f'Session number {i}')
        print('work')
        countdown(work  )
        print('short break')
        countdown(sbreak  )
        print('work')
        countdown(work  )
        print('long break!')
        countdown(lbreak  )

def timer():

    s= pyin.inputYesNo('Do you know the time in seconds you want to exercise for')
    if s == 'yes':
        t = pyin.inputNum('Enter the time in seconds you want the timer to go for')
    else:
        hours = pyin.inputInt('Enter the amount of hours you will be working for')
        mins = pyin.inputInt('Enter the amount of minutes you will be working for')
        t = seconds(hours, mins)
    countdown(t  )


def interval_timer():
    times = pyin.inputInt('How many sets do you want to do?')

    n = pyin.inputNum('after how many sets do you have to do this thing?')
    work3 = pyin.inputNum('Enter the time you will do this thing  for in seconds.') 

    work = pyin.inputNum('Enter the time you will work for in seconds.') 
    notwork = pyin.inputNum('Enter the time you will be on break for in seconds.')

    for i in range(1,times):
        if i % int(n+1) == 0:
            print('break but fin')
            countdown(work3  )
        else:
            print('work')
            countdown(work  )
            print('break')
            countdown(notwork  )


def stopwatch():
    t = 0
    while True:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        try:
            print(timer, end='\r')
            time.sleep(1)
            t += 1
        except KeyboardInterrupt:
            input('press enter to continue')

def exitconditions():
    choice = pyin.inputYesNo("would you like to go back to the main menu? ")
    if choice != "yes":
        sys.exit()
    else:
        return choice
    

def main():
    timer_choice = pyin.inputMenu(['timer/alarm', 'interval timer', 'pomodoro timer', 'stopwatch', 'alt pomodoro'], prompt='Choose which kind of timer you want \n', numbered=True)
    if timer_choice == 'timer/alarm':
        timer()
        exitconditions()
        main()
        


    elif timer_choice == 'interval timer':
        interval_timer()
        exitconditions()
        main()

    elif timer_choice == 'pomodoro timer':
        pomotimer()
        exitconditions()
        main()
    elif timer_choice == 'alt pomodoro':

        alt_pomodoro()
        exitconditions()
        main()
    else:
        stopwatch()
        exitconditions()
        main()


if __name__ == "__main__":
    main()
    


