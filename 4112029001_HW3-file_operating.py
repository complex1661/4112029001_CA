# -*- coding: utf-8 -*-
"""HW4:file_operating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eNyZqsXLhsTWde2yHIU95aaLRgD9YyOa
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import time

os.makedirs('CS', exist_ok=True)

with open('CS/homework.txt', 'w') as file:
    student_info = '4112029001_陳彥碩'
    file.write(student_info)

with open('CS/homework.txt', 'r') as file:
    content = file.read()
    print(f'檔案內容：{content}')

file_info = os.stat('CS/homework.txt')
new_access_time = time.time()
new_modification_time = time.time()

os.utime('CS/homework.txt', (new_access_time, new_modification_time))
modified_time = os.path.getmtime('CS/homework.txt')
formatted_time = time.ctime(modified_time)

print(f'檔案大小：{file_info.st_size} bytes')
print(f'修改的最後時間: {formatted_time}')

os.remove('CS/homework.txt')
os.rmdir('CS')