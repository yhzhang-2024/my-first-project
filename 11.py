import re
text11 = "我有3个苹果，5个香蕉，还有12个橘子，总共20个水果。"
num_list = re.findall(r"\d+", text11)
print(num_list)