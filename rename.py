import re
import os

dir_path = 'E:/poo/lpw13/v1/'
out_path = 'E:/poo/lpw13/v1'

files = os.listdir(dir_path)
total = 1
for n, i in enumerate(files):
  full_path = os.path.join(dir_path,i)
  base, ext = os.path.splitext(i)
  print(full_path)
  os.rename(full_path, f'{out_path}/rena{n}{ext}')
  total += 1



#   print(clean_filename)
print(total)
# Output: 6Yo_Mini_2_Suck_Asian_Girl_Kleuterkutje.mp4
