# 浮点数存在范围，
import sys

print(sys.float_info)  # min max
print(0.1 + 0.2)  # 不确定尾数问题
print(round(0.1 + 0.2, 1))  # 消除不确定尾数
# 精确浮点数计算 可以转换为 整数 计算，，，0.0012 转换为 12 ， 4 两个数 （表示 12 和小数点后四位）


# 运算
print(10 // 3)  # 整数除，得到商
print(10 % 3)  # 取余
print(10 ** 3)  # 10的3次方
print(pow(10, 3))  # 等价于上面
#  python 没有 i++ 的操作


# 函数
print(divmod(10,3))  # 商余函数 同时得到商和余数
print(max(10,3))  # 最大值函数 还有最小值函数 min(10,3) 为 3

# 类型转换函数
print(int(10.3))
print(float(10))
