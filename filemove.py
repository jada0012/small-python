import os
import shutil

for root, subfolders, filenames in os.walk("C:\\Users\\bobei"):
    print("the current folder is " + root)
    print("the subfolders of " + root + "are" + subfolders)