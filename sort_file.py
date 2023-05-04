import os
import shutil

source_path = '/Users/gihan.buddhika/code_learn/mix_folder'

for i in os.listdir(source_path):
    file_path = os.path.join(source_path, i)
  #  print(file_path)
    file_ext = os.path.splitext(file_path)[1][1:]
   # ext = os.path.splitext(i)[1][1:]
    dest_folder = os.path.join(source_path,file_ext)

    os.makedirs(dest_folder,exist_ok=True)
    shutil.move(file_path, os.path.join(dest_folder,i))