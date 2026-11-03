# import sys
# sys.path.append( r" pythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\\Lib\\site-packages]")
# import requests
# from bs4 import BeautifulSoup
# url = "http://books.toscrape.com."
import csv
import re
with open("books.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    # 关键：只读取有书名，且价格不为空的行
    books = [row for row in reader if len(row) > 1 and row[1].strip() != ""]
    books.sort(key=lambda x: float(re.sub(r'[^0-9.]', '', x[1])), reverse=True)
print("抓取的书最贵的本是：")
for book in books[:5]:
    print(f"《{book[0]}》| 价格：{book[1]}")