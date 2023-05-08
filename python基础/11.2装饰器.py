# 装饰器 实际是以一个函数作为参数，返回一个新的函数或方法
# 以下两种表述，实际效果一致

import time

def test(func):
    def wrapper():
        start = time.time()
        print("this is a order test, if you need not it, delete it")  # 用于测试执行顺序,可以跟着走一遍
        func()
        end = time.time()
        print("start:", start, " end:", end)
    return wrapper

def foo():
    print("this is a test")


foo = test(foo)
foo()

print('*'*50)

def test1(func):
    def wrapper():
        start1 = time.time()
        print("this is a order test, if you need not it, delete it") # 用于测试执行顺序,可以跟着走一遍
        a = func()
        end1 = time.time()
        print("start1:", start1, " end1:", end1)
        return a # 这种获得返回值的方法可能在多层修饰器的时候有矛盾,我先用!!!标记, 等理顺后再回来修改,如果我发布之后这里依然存在...说明我忘记了...
    return wrapper

@test1
def foo1():
    print("this is a test")
    return "this is a return value"

print(foo1())