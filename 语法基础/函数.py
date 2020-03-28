#  计算n!
def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fact(4))


# 位置传递 与 名称传递
def fact1(m, n):
    return m * n


print(fact1(3, 2))  # 位置传递
print(fact1(n=3, m=2))  # 名称传递

print("{:=^20}".format("可选参数"))


# 可选参数传递 ：函数为某些参数赋予了默认值，构成可选参数，可选参数必须在后面
def fact2(n, m=1):
    return n * m


print(fact2(3))
print(fact2(3, 2))

print("{:=^20}".format("可变参数"))


# 可变参数 函数可以接受不确定总数的参数变量 *b 元组 /  **d 字典

def fact3(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


print(fact3(10))
print(fact3(10, 3))
print(fact3(10, 3, 5, 8))  # (3,5,8) 传递了一个元组


def fact4(n, **d):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in d:
        s *= d[item]  # 注意此处取值方法
    return s


print(fact4(10))
print(fact4(10, a=3))
print(fact4(10, a=3, b=5, c=8))  # {a:3, b:5, c:8} 传递了一个字典

print("{:=^20}".format("多返回值"))


# 多返回值
def fact5(n, m):
    if n > m:
        return n, m
    else:
        return m, n


big, small = fact5(3, 6)  # 返回的是元组类型，可以拿多个参数接收
print(big, small)

print("{:=^20}".format("局部变量与全局变量"))

# 函数内为局部变量（函数执行完会销毁），，函数外为全局变量； 如果要在函数内部使用全局变量，要使用global关键字
s = 10


def fact6(n):
    global s
    s *= n
    return s


print(fact6(5), s)
# 如果局部变量为组合数据类型且未创建，等同于全局变量 例如：
ls = ['F', 'f']


def func(a):
    ls.append(a)  # 此处使用，未真实创建，所以其实是全局的ls
    return


func('C')
print(ls)

ls2 = ['F', 'f']


def func2(a):
    ls2 = []  # 此处使用，真实创建，所以其实是局部变量 ; 也可以使用global关键字，表示使用全局的ls2
    ls2.append(a)
    return


func2('C')
print(ls2)

print("{:=^20}".format("lambda函数"))
# lambda返回函数名字  <函数名> = lambda <参数> : <表达式>
fun_name = lambda x, y: x + y
print(fun_name(2, 5))


# 递归： 递归 = 基例 + 链条
def revs(s):
    if s == "":
        return s
    else:
        return revs(s[1:]) + s[0]


print(revs('abc'))
