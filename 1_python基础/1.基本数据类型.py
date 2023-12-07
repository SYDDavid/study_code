# python中，变量在赋值后才会被创建
# 数据类型是指，存储在变量中内容的类型，与变量无关
# 变量的多赋值

a = b = c = 1
c, d, e = 1, 1.01, '你好'

# python3中六种标准数据类型为：number string(str) tuple list set dictionary(dict)
#                          不可变     不可变    不可变 可变  可变      可变
# number 类型又分为 int float complex bool

# 内置type() isinstance()可查询变量类型

print(type(e))
print(type(e) == str)
print(isinstance(e, str))
print('-----------------------------')


# type()      不会认为子类与父类同类
# isinstance()会认为子类与父类同类

class A:
    pass


class B(A):
    pass


print(type(A()) == A)
print(type(B()) == A)
print(isinstance(A(), A))
print(isinstance(B(), A))
print("---------------------------")

# 注意：python中 bool 为 int 子类，True == 1, False == 0，二者可以相加
# 内置issubclass(x,y)可校验 x 是否为 y 子类

print(issubclass(bool, int))
print(type(False + 1))  # bool经过运算得到的是int类型
print('---------------------------')

# is 与 == 的区别
# is 来判断双方对象ID是否一致

