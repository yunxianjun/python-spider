import sys
sys.path.append( r" pythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\\Lib\\site-packages]")
import requests
from bs4 import BeautifulSoup
import time #用来减少网页请求，增加网页请求时间
import csv #将爬得的电影做成表格
headers = {"User-Agent": "Mozilla/5.0 (Winsow NT 10.0; Win64; x64)"} #User-Agent"告诉使用什么浏览器" header“伪装浏览器 ”
with open("doban_250.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "电影名", "评分"])
# start 从 0 到 225 ，每次加 25
    for start in range(0 , 250 , 25):
        url = f"https://movie.douban.com/top250?satrt = {start}" #f"..."的意思是：引号里的{satrt}会被替换成实际数字
        print(f"正在抓取第 {start//25 + 1} 页...")
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        movies = soup.find_all("div", class_="item")
        for movie in movies:
            rank = movie.find("em").get_text()                  #排名
            name = movie.find("span", class_="title").get_text() #名字
            score = movie.find("span", class_="rating_num").get_text() #评分
            writer.writerow([rank, name, score])
    time.sleep(2) #爬完一页，休息两秒，防封IP
print("全部 250 部电影已保存 douban_250.csv")




                
