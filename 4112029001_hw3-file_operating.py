import os
import time

os.makedirs('CS', exist_ok=True)

with open('CS/homework.txt', 'w') as file:
    student_info = '4112029001_陳彥碩'
    file.write(student_info)

with open('CS/homework.txt', 'r') as file:
    content = file.read()
    print(f'檔案內容：{content}')

file_size = os.path.getsize('CS/homework.txt')
print(f'文件大小：{file_size} 字節')

modification_time = os.path.getmtime('CS/homework.txt')
print(f'最後修改時間: {modification_time}')

formatted_time = time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式): {formatted_time}')

os.remove('CS/homework.txt')
os.rmdir('CS')
