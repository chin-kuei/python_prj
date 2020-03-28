#  二分支 简写
print('true' if 6 > 5 else 'false')

x = 9
if x > 0:
    print('正数')
elif x == 0:
    print('0')
else:
    print('负数')

# for 循环
letter = 'abcdefghijklmn'
for l in letter:
    print(l, end=',')
print()

for i in range(0, 5):
    print(i)

print('#' * 20)

# while 循环
x = 3
while x > 0:
    print(x)
    x = x - 1

# 循环的else扩展 循环没有被break时，else能够被执行
for c in 'Python':
    if c == 't':
        continue
    print(c, end='')
else:
    print('正常退出')


for c in 'Python':
    if c == 't':
        break
    print(c, end='')
else:
    print('正常退出')