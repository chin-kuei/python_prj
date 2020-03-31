fi = open("cnmooc.txt", "r", encoding="UTF-8")
U = set()
for line in fi:
    if "大学" in line or "学院" in line:
        U.add(line.strip("\n "))
print(" ".join(U))
print(len(U))
fi.close()
