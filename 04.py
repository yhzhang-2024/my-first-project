text4 = "Python is great. Python is easy. Python is powerful. I love Python."
# 替换标点
for p in [".",",","!"]:
    text4 = text4.replace(p,"")
text4_low = text4.lower()
word_list4 = text4_low.split()
count4 = {}
for w in word_list4:
    count4[w] = count4.get(w,0)+1
for k,v in count4.items():
    print(f"{k}:{v}")
