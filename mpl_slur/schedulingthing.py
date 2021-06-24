import schedule
import time
import csv

def write_to_csv():
    pass

schedule.every().day.at("11:56").do(write_to_csv)


while True:
    schedule.run_pending()
    time.sleep(1)
