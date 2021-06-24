import os, shutil
from pathlib import Path
sauce = r'D:\downloads'
ignore = ['exes', 'pdfs', 'word_docs', 'ppts']
folder = 'folderFolder'

p = Path(sauce)
for i in os.scandir(p):
    if  i.is_dir() or i.endswith('.zip')and i.name not in ignore:
        shutil.move(f'{sauce}\{i.name}', f'{sauce}\{folder}')

#todo tomorrow: strip the direntry off somehow???