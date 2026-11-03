import sys
sys.path.append( r" pythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\\Lib\\site-packages]")
import requests
from bs4 import BeautifulSoup
import time #增加访问时间
import csv #将所得数据做成表格
import concurrent.futures #多线程工具箱
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive"}
session = requests.Session()
session.headers.update(headers)
def fetch_page(page):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    print(f"正在抓取第 {page} 页》...")
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    page_data = []
    for book in books:
        name = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").get_text()
        page_data.append([name, price])
    return page_data
if __name__== '__main__':
    start_time = time.time()
    all_books = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
         results = executor.map(fetch_page, range(1, 51))
         for page_data in results:
              all_books.extend(page_data)
with open("books_50.csv","w",newline="",encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["书名", "价格"])
        writer.writerows(all_books)
end_time = time.time()
print(f"抓取完毕！ 共 {len(all_books)} 本书。")
print(f"总耗时：{end_time - start_time:.2f}秒")