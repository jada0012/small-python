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
        elif file.endswith('.docx') or file.endswith('.doc'):
            shutil.move(f'{source}\{file}',f'{source}\word_docs' )
        elif file.endswith('.pptx') or file.endswith('.ppt'):
            shutil.move(f'{source}\{file}',f'{source}\ppts' )
        
schedule.every(30).minutes.do(filemover)

while True:
    schedule.run_pending()
    time.sleep(1)