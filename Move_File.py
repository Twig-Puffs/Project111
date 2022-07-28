import os
import shutil

from_dir="C:/Users/devmo/Downloads"
tp_dir="C:/Users/devmo/Desktop/WhiteHat Jr/Projects/PRO-111"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)