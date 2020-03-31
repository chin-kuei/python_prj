fi = open("icourses.txt", "r", encoding="UTF-8")
ls = []
for line in fi:
    if "alt" in line:
        tokens = line.split('"');
        uname = tokens[-2]
        if "大学生" in uname:
            continue
        if "大学" in uname or "学院" in uname:
            ls.append(uname)

print(" ".join(ls))
print(len(ls))
fi.close()
