import requests
import os
url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=5"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive"}
print("正在向必应要数据...")
resq = requests.get(url , headers=headers)
data = resq.json()
if not os.path.exists("wallpaper"):
    os.mkdir("wallpaper")
images = data["images"]
for index, img in enumerate(images):
    img_url = img["url"]
    full_url = "https://cn.bing.com" + img_url
    print(f"正在下载第{index+1} 张图...")
    img_resq = requests.get(full_url, headers=headers)
    file_name = f"wallpaper/bing_{index+1}.jpg"
    with open(file_name, "wb") as f:
        f.write(img_resq.content)
print("搞定!壁纸已保存在 wallpaper 文件夹里!")