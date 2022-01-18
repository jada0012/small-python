from pathlib import Path
import shutil,  os
import schedule
import time


source = Path('D:\downloads')

files = os.listdir(source)
pic_folder = r'C:\\Users\\bobei\\OneDrive\\Pictures'
vid_folder = r'D:\\videos'
folder = 'folderFolder'



def filemover():


    for file in files:
        if file.endswith('.pdf'):
            if Path(source/"pdfs"/file).is_file():
                print(f'{file} already exists')
                os.remove(f'{source}\{file}')
            else:
                shutil.move(f'{source}\{file}', f'{source}\pdfs')

           
           

            # try:
            #     shutil.move(f'{source}\{file}', f'{source}\pdfs')
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass

        elif file.endswith('.exe') or file.endswith('.msi'):
            if Path(source/"exes"/file).is_file():
                print(f'{file} already exists')
                os.remove(f'{source}\{file}')

            else:
                shutil.move(f'{source}\{file}', f'{source}\exes')



            # try:
            #     shutil.move(f'{source}\{file}', f'{source}\exes')
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass


        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            if Path('{pic_folder}\\{file}').is_file():
                print(f'{file} already exists')
                os.remove(f'{source}\{file}')

            else:
                shutil.move(f'{source}\{file}', f'{pic_folder}')

                
            # try:
            #     shutil.move(f'{source}\{file}', f'{pic_folder}')
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass

        elif file.endswith('.docx') or file.endswith('.doc'):
            try:
                if Path(source/"word_docs"/file).is_file():
                    print(f'{file} already exists')
                    if not Path(source/"duplicates"/file).is_file():
                        os.remove(f'{source}\{file}')

                    else:
                        os.remove(Path(source/"duplicates"/file))

                    
                else:
                    shutil.move(f'{source}\{file}',f'{source}\word_docs' )
            except PermissionError:
                
                continue
            


                
            # try:
            #     shutil.move(f'{source}\{file}',f'{source}\word_docs' )
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass

            
        elif file.endswith('.pptx') or file.endswith('.ppt'):
            pass
            # try:
            #     shutil.move(f'{source}\{file}',f'{source}\ppts' )
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass
        elif file.endswith('.zip'):
            pass
            # try:
            #     shutil.move(f'{source}\{file}', f'{source}\{folder}')
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass

        elif file.endswith('.mp4'):
            pass
            # try:
            #     shutil.move(f'{source}\{file}', f'{vid_folder}')
            # except PermissionError:
            #     pass
            # except shutil.Error:
            #     pass
            

          
filemover()       
# schedule.every(30).minutes.do(filemover)
# g = source/"exes"/"AutoHotkey_1.1.33.02_setup.exe"
# if Path(source/"exes"/"AutoHotkey_1.1.33.02_setup.exe").is_file():
#     print('Fkdf')
# else:
#     print("ower")


# while True:
#     schedule.run_pending()
#     time.sleep(1)