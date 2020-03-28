letter = "abcdefghijklmnopqrstuvwxyz"

# 索引
print(letter[1])

# 切片
print(letter[2:5])
print(letter[:])  # 全部
print(letter[::-1])  # 倒序

# 字符串运算
x, y = '123', '456'
print(x + y)  # 连接
print(x * 3)  # 复制n次
print('2' in x)  # 含有

# 星期判断
# weekStr = '一二三四五六日'
# weekPos = eval(input("请输入星期数字(1-7):"))
# print("星期" + weekStr[weekPos - 1:weekPos])


# 字符串操作函数及方法  不改变原来的字符串，只产生一个副本
print(len(letter))  # 字符串长度
print(str(365))  # str() 格式化为字符串
print(letter.upper())
splitStr = 'abcd,efg,hijk,lmn'
print(splitStr.split(','))  # 分割
print(','.join(letter))  # 插入到letter
print(splitStr.count(','))
print(splitStr.replace('hijk', '123'))

print('Python'.center(20, '#'))  # 居中，其他以#填充
print('python'.strip('pn'))  # 去除指定字符

# 格式化
print("{}:计算机{}的cpu占用率为:{}%".format('20200322', 'admin', 60))
print("{:=^20}".format("python"))
print("{:.2%}".format(3.14))

# 字节串
achar = b'abcd'
print(type(achar))
print(achar[::-1])
