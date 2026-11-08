import re
text12 = "Python is great. Python is easy. Python is powerful."
words12 = re.findall(r'[a-zA-Z]+',text12.lower())
freq12 = {}
for w in words12:
    freq12[w] = freq12.get(w,0)+1
for k,v in freq12.items():
    print(f"{k}: {v}")