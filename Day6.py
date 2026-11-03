import sys
sys.path.append( r" pythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\\Lib\\site-packages]")
import requests
import requests
from bs4 import BeautifulSoup
import time #增加时间请求，防封IP
import csv #将爬得的电影做成表格
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive"
}
url = "https://douban.com/top250"
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")
movies = soup.find_all("div", class_="item")[:3] #只要前三部
print(f"抓到电影数量： {len(movies)}")
with open("test_3.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["电影名", "类型", "导演"])
    for movie in movies:
        name = movie.find("span", class_="title").get_text()
        detail_url = movie.find("div", class_="hd").a["hreef"]
        resp_detail = requests.get(detail_url, headers=headers)
        soup_detail = BeautifulSoup(resp_detail.text, "html.parser")
        genre_tags = soup_detail("span", property="v:genre")
        genre = " / ".join([tag.get_text() for tag in genre_tags])
        director_tag = soup_detail.find("a", rel="v:directedBy")
        diretor = director_tag.get_text() if director_tag else "未知"
        print(f"《{name}》 | 类型：{genre} | 导演: {diretor}")
        writer.writerow([name, genre, director_tag])
        time.sleep(5)
print("测试完成！ 已保存为 test_3.csv")