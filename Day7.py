import sys
sys.path.append( r" pythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\\Lib\\site-packages]")
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive"
}
import time
import csv

# requ = requests.get(url, headers=headers)
# beau = BeautifulSoup(requ.text, "html.parser")
# books = beau.find_all("article", class_="product_pod")
# print(f"抓到书数量：{len(books)}")
with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    wrier = csv.writer(f)
    wrier.writerow(["书名", "价格"])
    for page in range(1,51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        print(f"正在抓取第{page} 页...")
        requ = requests.get(url, headers=headers)
        beau = BeautifulSoup(requ.text, "html.parser")
        books = beau.find_all("article", class_="product_pod")
        for book in books:
            name = book.find("h3").find("a")["title"]
            price = book.find("p",class_="price_color").get_text()
            wrier.writerow([name, price])

        # for book in books:
        #     price = book.find("p", class_="price_color").get_text()
        #     print(f"《{name}》 | 价格：{price}")
        #     wrier.writerow([name, price])
    time.sleep(1)
print("成功！数据已保存为 books.csv")


