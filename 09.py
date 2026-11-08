def check_pwd(pwd):
    if len(pwd) <6:
        return "弱"
    has_alpha = any(c.isalpha() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    if has_alpha and has_digit and has_special:
        return "非常强"
    elif has_alpha and has_digit:
        return "强"
    elif (has_alpha and not has_digit) or (has_digit and not has_alpha):
        return "中"
    else:
        return "弱"

print(check_pwd("1234"))
print(check_pwd("abcdef"))
print(check_pwd("abc123"))
print(check_pwd("abc123!"))