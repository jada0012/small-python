import random
import pyinputplus as pyin
def roll():
    activities = ["exercise", "read", "watch netflix", "write", "listen to podcast", "watch video essay", "code", "go for a walk"]
    print("here are your options: ")
    for i in activities:
        print(i)
    print("\ni will make a choice for you! i hope you enjoy the next 15 mins!!!")
    print(activities[random.randint(0, len(activities)-1)])
    reroll = pyin.inputYesNo("reroll?")
    if reroll == "yes":
        roll()
    else:
        print("live long and prosper!")
        input()


roll()