import sqlite3

# 連接到 SQLite 資料庫（若不存在，將創建一個新的資料庫文件）
conn = sqlite3.connect('BBQ.db')

# 創建一個游標對象，用於執行SQL查詢
cursor = conn.cursor()

# 創建名為'meat'的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )''')

# 插入資料
cursor.execute(
    "INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)")
cursor.execute(
    "INSERT INTO meat (name, price, quantity) VALUES ('beaf', 55, 10)")
cursor.execute(
    "INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)")

# 提交事務
conn.commit()

cursor.execute("SELECT * FROM meat")
meat_list = cursor.fetchall()

print("\n表格內容 (修改資料後):")
for item in meat_list:
    print(item)

# 更新資料
cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")

conn.commit()

cursor.execute("SELECT * FROM meat")
meat_list = cursor.fetchall()

print("\n表格內容 (修改資料後):")
for item in meat_list:
    print(item)

cursor.execute("DELETE FROM meat WHERE price = '40'")
conn.commit()

cursor.execute("SELECT * FROM meat")
meat_list = cursor.fetchall()

print("\n表格內容 (修改資料後):")
for item in meat_list:
    print(item)

cursor.execute("DROP TABLE meat")
cursor.close()
conn.close()
