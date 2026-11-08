import re
text13 = "Hello 你好 World 世界 Python 编程 123 数字"
chinese_list = re.findall(r'[\u4e00-\u9fa5]+',text13)
print(chinese_list)