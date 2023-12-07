import traceback

## python中有很多异常类，继承自标准库的Exception类，表示各种不同类型的错误
## try: ... except: ...

try:
    miles = input('请输入英里数:')
    km = int(miles) * 1.609344
    print('一旦前面捕获到异常之后的命令将不会执行 代码逻辑直接跳转至except语句块中')
    print(f'等于{km}公里')
except ValueError:
    print('你输入了非数字字符')

## 可以使用多并行except来解决不同异常，进行精细化处理

try:
    choice = input('输入你的选择:')
    if choice == '1':
        100 / 0
    elif choice == '2':
        [][2]
except ZeroDivisionError:
    print('出现 ZeroDivisionError')
except IndexError:
    print('出现 IndexError')

### 获取异常对象 as

try:
    a = 100 / 0
except ZeroDivisionError as Z:  ## 使用as来获取具体异常信息
    print(f'异常信息如下：{Z}')

### 匹配所有异常并回溯

try:
    a = 100 / 0
except Exception:
    print('存在异常')

# 简单表述

try:
    a = 100 / 0
except:
    print('存在异常')

# 打印报错信息 traceback(先导入模块)

try:
    a = 100 / 0
except:
    print(traceback.format_exc())


## 自定义异常 第一步：定义Exception子类 第二步：raise异常 第三步：捕获并处理异常

class InvalidtelError(Exception):
    pass


class NotCHtelError(Exception):
    pass


def regedit():
    tel = input('请输入电话号码：')

    if not tel.isdigit():
        raise InvalidtelError

    if not tel.startswith('86'):
        raise NotCHtelError


try:
    regedit()
except InvalidtelError:
    print('非法电话')
except NotCHtelError:
    print('非中国地区电话')


## 函数调用栈中的异常
# 首先调用下函数，并打印异常

def f3():
    print('enter f3')
    100 / 0
    print('leave f3')


def f2():
    print('enter f2')
    f3()
    print('leave f2')


def f1():
    print('enter f1')
    f2()
    print('leave f1')


try:
    f1()
except:
    print(traceback.format_exc())

print('*' * 50)


## 打印发现函数报错被一层层上报。同样的，当异常产生时，解释器终止了代码执行，并会在本层搜索是否有对该异常的捕获煜处理，若没有则返回上一层寻找
## 直到最后均为发现处理，则终止代码执行
## 如果有处理则处理完后，继续执行之后的代码，如下：

def f3():
    print('enter f3')
    100 / 0
    print('leave f3')


def f2():
    print('enter f2')
    try:
        f3()
    except:
        print(f'未知异常{traceback.format_exc()}')
    print('leave f2')


def f1():
    print('enter f1')
    f2()
    print('leave f1')


f1()
