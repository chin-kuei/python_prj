try:
    1 / 0
except ZeroDivisionError:
    print('除数不能为0')

print('{:=^20}'.format('分割线'))

try:
    2 / 1
except ZeroDivisionError:
    print('除数不能为0')
else:
    print('try块无异常')
finally:
    print('finally一定会被执行')

print('{:=^20}'.format('分割线'))

# 函数中使用

def f(x):
    try:
        print(1 / x)
        return True
    except:
        print('except')
    else:
        print('else')
    finally:
        print('finally')
        return False


print(f(1)) # try有return else不执行
