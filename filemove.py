from pathlib import Path
import shutil,  os
import schedule
import time


source = r'D:\downloads'
testi = 'this is called '
files = os.listdir(source)
source2 = r'D:\\Onedrive\\Pictures'

def filemover():


    for file in files:
        if file.endswith('.pdf'):
            shutil.move(f'{source}\{file}', f'{source}\pdfs')

        elif file.endswith('.exe'):
            shutil.move(f'{source}\{file}', f'{source}\exes')

        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            shutil.move(f'{source}\{file}', f'{source2}')
        
schedule.every(30).minutes.do(filemover)

while True:
    schedule.run_pending()
    time.sleep(1)