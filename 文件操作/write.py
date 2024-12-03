fo = open("out.txt", "w+",encoding='utf-8')
ls = ["中国", "法国", "英国"]
fo.writelines(ls)
fo.seek(0)  # 指针移到开头
for line in fo:
    print(line)
fo.close()
