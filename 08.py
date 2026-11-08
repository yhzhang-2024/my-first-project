def text_analyzer(txt):
    txt = txt.strip().lower()
    words = txt.split()
    total = len(words)
    #最长单词
    max_word = max(words, key=lambda x:len(x))
    #统计频次
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0)+1
    max_times = max(freq.values())
    most_word = [k for k,v in freq.items() if v==max_times][0]
    print(f"单词总数：{total}")
    print(f"最长单词：{max_word}")
    print(f"出现最多：{most_word}（{max_times}次）")

text8 = "  Python is great and Python is easy  "
text_analyzer(text8)