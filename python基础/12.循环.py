### 循环 py中含有两种循环方式：while循环和for循环

command = input("请输入命令:")
while command != 'exit':
    print(f'输入的命令是{command}')
    command = input("请输入命令:")

# while后语句只要是true就会一直循环（死循环）

## for循环 通常是从一个sequence类型出发（字符串，列表，元组）依次取元素执行操作

studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']

for student in studentAges:
    print(student)

print('*' * 50)

# 注：此处student变量即表示，studentAges下的每个元素
# 可以将其理解为依次遍历

## 循环n次
# 引入新函数：range()

a = range(5)  # 默认从 0 开始, 在 5 以内, 到不了 5
print(list(a))  # [0, 1, 2, 3, 4]

a = range(1, 5)  # 给出起点, 终点(到不了的)
print(list(a))  # [1, 2, 3, 4]

a = range(1, 11, 2)  # 给出起点, 终点(到不了的), 步长(正整数,负整数)
print(list(a))  # [1, 3, 5, 7, 9]

a = range(2, 2468, 2)  # 最大下标这样获得:len(a)-1
print(a[0], a[1], a[2], a[len(a) - 1])  # 2 4 6 2466

### 这里可以得知：range()[]索引方式可以访问到该对象下的具体元素

a = range(100, 80, -2)  # 前大后小的,步长应该是负数
print(list(a))  # [100, 98, 96, 94, 92, 90, 88, 86, 84, 82]

### 结合for循环

for i in range(10, 1, -1):
    print(i)

# enumerate函数
# enumerate函数 对sequence对象处理，得到indix与content可迭代元组对象

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, 3)))  # 小标从3开始

### 结合for循环

studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']

for idx, student in enumerate(studentAges):
    if int(student.split(':')[-1]) > 16:
        print(f"年龄超过17的为第{idx + 1}位")

# return与break与contunie的区别

# 首先：return不可用于定义函数外的地方
# 其次：若在函数体内循环：
#      1、执行到return直接结束，并返回函数结果
#      2、执行到break仅退出循环
#      3、执行到continue仅结束该次，继续下次循环内容

## 列表推导式

list1 = [1, 2, 3, 4, 5, 6]
list2 = []

for num in list1:
    list2.append(num**2)

# 以上通过一个列表推导另一个列表的方式叫做，列表推导式
## 注意：除此以外还有种简便写法

list3=[num**3 for num in list1]

print(list1)
print(list2)
print(list3)

print('*'*50)