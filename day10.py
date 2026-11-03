import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {"User-Agent": "Mozilla/5.0"}

print("正在向接口要数据...")
resp = requests.get(url, headers=headers)

# 核心绝招：用 .json() 替代 .text！
data = resp.json()

print(f"一共拿到了 {len(data)} 篇文章！\n")

for post in data[:3]:  # 只取前 3 篇看看
    print(f"文章ID: {post['id']}")
    print(f"标题: {post['title']}")
    print("-" * 30)