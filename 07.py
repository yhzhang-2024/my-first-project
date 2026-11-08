s7 = "Hello World 123 Python 456"
upper_cnt = 0
lower_cnt = 0
digit_cnt = 0
for ch in s7:
    if ch.isupper():
        upper_cnt +=1
    elif ch.islower():
        lower_cnt +=1
    elif ch.isdigit():
        digit_cnt +=1
print(f"大写字母：{upper_cnt}")
print(f"小写字母：{lower_cnt}")
print(f"数字：{digit_cnt}")