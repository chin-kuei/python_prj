# SensorReader.py
try:
    f = open("sensor-data.txt", "r")  # "r" 表示只读模式打开
    avg, cnt = 0, 0
    for line in f:
        ls = line.split()  # split() 按空格分割
        cnt += 1
        avg += eval(ls[2])
    print("平均温度为：{:.2f}".format(avg / cnt))
    f.close()
except:
    print("文件打开错误")
