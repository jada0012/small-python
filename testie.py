import time




def wrapper():
    def stopwatch(begin=0):
        mins, secs = divmod(begin, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        begin += 1
    stopwatch()

while True:
    time.sleep(1)
    wrapper()