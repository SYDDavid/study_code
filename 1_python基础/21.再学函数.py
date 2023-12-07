### 局部变量和全局变量

var = '外面'  # 全局变量


def f():
    var = '里面'  # 局部变量
    print(f'函数内调用为：{var}')


f()
print(f'函数外调用为：{var}')

print('*' * 50)


## 若函数体内有申明变量，则调用他，若无则调用全局变量

def f1():
    print(f'内部若无则调用全局变量：{var}')


f1()

print('*' * 50)

## 在函数内部去改变外部全局变量 global

var = '外面'  # 全局变量


def f():
    global var  # 申明此处为全局变量
    var = '里面'
    print(f'函数内调用为：{var}')


f()
print(f'函数外调用为：{var}')

print('*' * 50)

### 可变参数 *
## 当调用该函数时，python解释器会创建一个tuple对象赋值给这个函数，并将需要传入的参数放入这个对象中

studentInfo = {
    '张飞': 18,
    '赵云': 17,
    '许褚': 16,
    '典韦': 18,
    '关羽': 19,
}


def printAge(students):
    for student in students:
        print(f'学生：{student} , 年龄 {studentInfo[student]}')


printAge(['张飞', '典韦', '关羽'])
printAge(['赵云'])

print('*' * 50)

# 我们对函数进行下优化，使用可变参数 *

studentInfo = {
    '张飞': 18,
    '赵云': 17,
    '许褚': 16,
    '典韦': 18,
    '关羽': 19,
}


def printAge(*students):  # 此处*表示可变参数，当不确定入参内容时，可以这么处理
    print(type(students))
    for student in students:
        print(f'学生：{student} , 年龄 {studentInfo[student]}')


tuple = ('张飞', '赵云', '典韦')
list = ['关羽', '典韦', '赵云']

printAge(*tuple)  # 此处的*表示展开，相当于tuple[0],tuple[1],tuple[2],tuple[3]
printAge(*list)  # 此处的*展开方式，不局限于元组中，列表中同样适用

print('*' * 50)


### 关键字可变参数 **
## 当调用该函数时，python解释器会创建一个dict对象赋值给这个函数，并将需要传入的参数放入这个对象中

def addStudents(table, **students):
    print(type(students))
    for name, age in students.items():
        table[name] = age


table1 = {}
table2 = {}

table3 = {
    'keqing': 30,
    'ganyu': 40
}

addStudents(table1, 李白=20, 杜甫=24)
addStudents(table2, **table3) # **在这里同样表示展开
print(table1)
print(table2)
