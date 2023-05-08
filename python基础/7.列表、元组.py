# 列表和元组均有 序列 性质

# 列表用于存储对象 且对象任意 甚至可以为另一列表

datalist = []
datalist = [1, 2, 3.14, '列表使用方括号表示']  # 对象间用逗号隔开，每个对象称为元素

### 列表的sequence操作

# 元素操作
listToList = [1, 2, 3.14, '任意', [7, 8, 9]]
# 单元素指引

print(listToList[0])
print(listToList[4])
print(listToList[-1])
print(listToList[-1][2])

print('-' * 50)

# 多元素切片

print(listToList[0:3])
print(listToList[:3])
print(listToList[3:])
print(listToList[-1][:2])

print('-' * 50)

### 列表的可变换特性

# 单元素变换

listToChange = [1, 2, 1.414, '列表支持变化', [9, 8, 7]]
listToChange[-2] = '元组不可变'
print(listToChange)
listToChange[-1][-1] = 10
print(listToChange)

var = '元素可以为变量'
listToVar = [1, 2, var]  # 元素可以是变量

print('-' * 50)

## 注意：通过变量赋值，列表内以赋值时的变量对象创建列表对象，之后变量改变不会影响到已被创建好的对象，需重新赋值

# 切片赋值

list1 = [0, 1, 2, 3, 4, 5]
a = ['a', 'b', 'c']
list1[1:4] = a
print(list1)

print('-' * 50)

# 合并列表 加号即可

a = [1, 2, 3]
a += [4, 5, 6]
print(a)

print('*' * 50)

# 元组
# 元组同列表非常相似，可以sequence存储多类型对象，唯一不同的是 元组不可变

tuple1 = (1, 2, 3.14, '元组使用小括号来表示')

# 同样的元组中的元素，也可以为元组或者列表

tuple2 = (1, 3.14, (2, 1.41), [3, 1.77])

tuple3 = (1,)  # 注意：当元组中元素仅为一个时，后面必须加逗号

### 元组的sequence操作

# 元素操作
tuple4 = (1, 2, 3.14, '任意', [7, 8, 9])
# 单元素指引

print(tuple4[0])
print(tuple4[4])
print(tuple4[-1])
print(tuple4[-1][2])

print('*' * 50)

# 多元素切片

print(tuple4[0:3])
print(tuple4[:3])
print(tuple4[3:])
print(tuple4[-1][:2])

print('*' * 50)

### 元组的不可变换特性

## 然而元组中的列表可变

tuple4[-1][2] = 100
print(tuple4)

# 判断元素是否在莫元组中 in 关键字（not in）

list=[1,2,'hello']
tuple=(1,2,'bye')

if 'hello' in list:
    print("list with 'hello'")
if 'hello' not in tuple:
    print("tuple without 'hello'")

print('*' * 50)

# 多变量赋值 元组列表方式
## 注意：长度必须保持一致

a,b=(1,2)
x,y=['hello','bye']

print(a,b)
print(x,y)

print('*' * 50)

# 函数返回值以元组或者列表做结果
# 当返回值有多个时可以使用

def func1():
    age=input('please input your age:')
    name=input('please input your name:')
    return [age,name]

def func2():
    age=input('please input your age:')
    name=input('please input your name:')
    return age,name                   # 元组可以忽略小括号
