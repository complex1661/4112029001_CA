# -*- coding: utf-8 -*-
"""HW2:Physical_Address.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-LE0amkJO9xP1DbjO1orYNK2Ixw0782v
"""

def memory_addressing(page_table, page_size, logical_address):
    page_number, offset = divmod(logical_address, page_size)

    if page_number in page_table:
        frame_number = page_table[page_number]
        physical_address = frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")

page_size = 4096
element_count = int(input("請輸入page table的資料數量: "))
page_table = {}

for i in range(element_count):
    index = int(input("請輸入頁號: "))
    value = int(input("請輸入框架號: "))
    page_table[index] = value

logical_address = int(input("請輸入logical address: "))
memory_addressing(page_table, page_size, logical_address)