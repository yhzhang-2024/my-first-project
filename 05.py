def judge_str(s):
    if s.startswith("www"):
        return "网址"
    elif s.endswith(".com"):
        return "商业域名"
    elif s.isalpha():
        return "纯字母"
    elif s.isdigit():
        return "纯数字"
    else:
        return "字母数字混合"

print(judge_str("hello"))
print(judge_str("12345"))
print(judge_str("abc123"))
print(judge_str("www.baidu.com"))
print(judge_str("example.com"))