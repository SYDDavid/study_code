# 自定义函数 关键字 def(define)
## 注意：函数需要先定义再使用，需养成习惯：定义放代码前

def interview():  # interview为函数类型对象
    print("把求职者带到3号会议室")
    print("请求职者 完成答卷")
    print("让测试经理来面试 求职者")
    print("让技术总监面试 求职者")  # 函数体缩进4


print('-' * 50)


# 函数返回值 关键字 return

def squarep(a, b):
    return a ** 2 + b ** 2
    print("return后代码不执行")  # return后函数体内代码不执行


print(squarep(3, 4))


# 函数缺省
# 1.参数缺省后，后面的函数均需缺省

def default(a, b, c=1, d=2):
    print(c, d)
    return


# 2.缺省调用，函数以默认参数执行，完全调用，参数设置将被覆盖

default(0, 0)
default(0, 0, 3, 4)

# 函数调用时入参设置

default(1, 2, 3, 4)  # 可以不写参
default(a=1, b=2, c=3, d=4)  # 可以写参
default(b=1, a=2, d=3, c=4)  # 可以写参，打乱顺序
default(1, 2, d=3, c=4)  # 可以参杂，但是一旦写参，后面都必须写参


# 范围覆盖 局部变量变全局变量 关键字 global

def default2(e=2):
    global f
    f = 5  # 需要分成两行写，不允许同行


default2()
print(f)

# 常用内置函数
# int() 字符串转整数，小数转整数（忽略小数部分）

print(int('123'))
print(int(1.23))
# print(int('9.23')) 报错，int转换字符串 条件为内部仅含数字

# float() 字符串转小数，整数转小数

print(float('100'))
print(float('1.23'))
print(float(100))

# str() 数字转字符串

print(str(314))
print(str(3.14))