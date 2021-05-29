import schedule
import datetime
import math


def update_status():
    today = datetime.datetime.now()
    csec = datetime.datetime(2021,6,14)
    freedom = datetime.datetime(2021, 7, 14)

    p = csec-today
    pain =math.ceil(p.total_seconds()/86400) 
    f = freedom-today
    free =math.ceil(f.total_seconds()/86400) 

    print(f"{pain} days till pain; {free} days till freedom.")

update_status()