def first_unique_char(s):
    for idx, char in enumerate(s):
        if s.count(char) == 1:
            return idx
    return -1

test_str3 = "leetcode"
res3 = first_unique_char(test_str3)
print(f"输入:{test_str3},输出:{res3}")
