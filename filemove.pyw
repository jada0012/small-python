from pathlib import Path
import shutil,  os
import schedule
import time


source = r'D:\downloads'
testi = 'this is called '
files = os.listdir(source)
source2 = r'D:\\Onedrive\\Pictures'
folder = 'folderFolder'

def filemover():


    for file in files:
        if file.endswith('.pdf'):
            try:
                shutil.move(f'{source}\{file}', f'{source}\pdfs')
            except shutil.Error:
                pass

        elif file.endswith('.exe'):
            try:
                shutil.move(f'{source}\{file}', f'{source}\exes')
            except shutil.Error:
                pass

        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            try:
                shutil.move(f'{source}\{file}', f'{source2}')
            except shutil.Error:
                pass
        elif file.endswith('.docx') or file.endswith('.doc'):
            try:
                shutil.move(f'{source}\{file}',f'{source}\word_docs' )
            except shutil.Error:
                pass

            
        elif file.endswith('.pptx') or file.endswith('.ppt'):
            try:
                shutil.move(f'{source}\{file}',f'{source}\ppts' )
            except shutil.Error:
                pass
        elif file.endswith('.zip'):
            try:
                shutil.move(f'{source}\{file}', f'{source}\{folder}')
            except shutil.Error:
                pass

            
        
schedule.every(1).seconds.do(filemover)

while True:
    schedule.run_pending()
    time.sleep(1)