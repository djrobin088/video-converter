import os
from moviepy.editor import *
import magic
import shutil
import time

def is_mp3_file(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    print(file_type)
    return file_type == 'video/mp4'

out_path = 'E:/poo/lpw13/f_v/'

dir_path = 'E:/poo/lpw13/v1/'
files = os.listdir(dir_path)

for n,i in enumerate(files):
  
  print(f'{n:4}: {i}')
  full_path = os.path.join(dir_path,i)
  print(full_path)
  base, ext = os.path.splitext(i)
  # print(full_path)
  # print(is_mp3_file(full_path))
  

  if is_mp3_file(full_path):
    print(full_path,"it is copy")
    shutil.copyfile(full_path, f'E:/poo/lpw13/f_v/{i}')
    print(full_path,"it is copy")
    # time.sleep(10)

  else:
    print(full_path, "command")
    os.system(f'cmd /c "ffmpeg -i lpw13/v1/{i} -qscale 0 lpw13/f_v/{n}.mp4"')
    
    # time.sleep(10)