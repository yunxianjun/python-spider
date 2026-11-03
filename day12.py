import re
text = "这本书原价 99.5元， 现在只要49 元， 太划算了"
money = re.findall(r"1\.d{2}", text)
print("找到书的价格为：", money)
service = re.findall(r"\d{2}", text)
print("找到价格：", service)
