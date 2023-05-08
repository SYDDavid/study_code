### 装饰器：修改其他函数功能的函数

## 第一步：一切皆对象
# 函数亦可作为对象被传递

def hi(name='default'):
    return 'hi ' + name


func = hi('em')  # 类似于变量的传递，函数也被传递了
print(func)

del hi  # 即使原函数被删除，被传递后的func依旧正确指出了hi
print(func)

# print(hi)  由于被删除直接报错

print('*' * 50)


## 第二步：函数中定义函数
#

def hi(name='default'):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi('emmmm')  # 这里可以看到函数被调用时，函数的函数也会一并调用

# greet() 然而函数内定义的函数只能在该函数内使用，在外不可调

print('*' * 50)


## 第三步：函数中返回函数

def hi(name='default'):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == 'default':
        return greet
    else:
        return welcome


a = hi()
print(a)
# 这里hi()被调用return了greet函数的位置，赋值给了a
print(a())
# 所以打印a时，打印的即为greet地址，打印a()时即为greet函数return的结果

print('*' * 50)


## 第四步：将函数作为参数传给另一个函数

def hi():
    return "hi"


def beforehi(func2):
    print("hello ",end='')
    print(func2())


a = beforehi(hi)

### 总结：要点在于函数名可视作变量，函数名后有括号，传递函数return值，且整个函数均会被调用

