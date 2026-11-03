import re
text = "这本书原价 99.5 元，打完折只要 49 元，太划算了！"
# \d+ 代表整数，\. 代表小数点，\d+ 代表小数部分，? 代表小数部分可有可无
prices = re.findall(r"\d+\.?\d*", text) 
print(prices)

