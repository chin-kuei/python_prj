# WordsCount.py
import jieba

f = open("2018年一号文件.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
ls = jieba.lcut(txt)
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1  # get(w,0) 0 表示默认值，如果键w不存在，则返回0
for k in d:
    if d[k] >= 50 and k != "\n":
        print('"{}"出现{}次'.format(k, d[k]))
