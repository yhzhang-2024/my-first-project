import re
log_text = """2026-01-15 10:23:45 192.168.1.1 INFO 用户登录成功
2026-01-15 10:24:12 192.168.1.2 ERROR 数据库连接失败
2026-01-15 10:25:33 192.168.1.1 WARNING 内存使用率过高
2026-01-15 10:26:01 192.168.1.3 ERROR 文件不存在"""
ip_result = re.findall(r"\d+\.\d+\.\d+\.\d+",log_text)
time_result = re.findall(r"\d{2}:\d{2}:\d{2}",log_text)
error_count = len(re.findall(r"ERROR",log_text))
print(f"IP地址：{ip_result}")
print(f"时间：{time_result}")
print(f"错误数量：{error_count}")