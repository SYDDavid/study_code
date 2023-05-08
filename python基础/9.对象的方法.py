# 对象通常有属于自己的方法(method)，对象的方法可以看作是对象的函数

### 字符串的方法
## count 方法 统计数量，返回出现的总次数

str = '我们今天不去上学，我们去踢足球'
print(str.count('我们'))

num1 = '我我我'.count('我我')
print(num1)

print('*' * 50)

## find 方法 查询子字符串，返回字符串第一次出现的索引值
# 若未找到该子字符串出现，返回值为：-1

# 用法一

print(str.find('我们'))

# 用法二 后面的参数表示从第几位开始再查询，并返回结果

print(str.find('我们', 5))

print('*' * 50)

## split 方法 以参数作为分隔，划分字符串；并返回列表，元素为每一段字符串

str2 = '小王 98|小胡 79|小吴 59'
element = str2.split('|')
print(element)

print('*' * 50)

## splitlines 方法 以回车作为分割，划分字符串；较多应用与文件传输场景下

str3 = '''
小王 98
小胡 79
小吴 59

'''
element1 = str3.splitlines()
print(element1)

print('*' * 50)

## join 方法 以参数作为拼接对象，将字符串接入

str4 = '|'.join(['小王 98', '小胡 79', '小李 59'])
print(str4)

print('*' * 50)

## strip/lstrip/rstrip 方法 删除左右/左/右所有空格

print('     good   night    '.strip())
print('     good   night    '.rstrip())
print('     good   night    '.lstrip())

print('*' * 50)

## replace 方法 替换字符串

str5 = str.replace('我们', '她们')
print(str5)

print('*' * 50)

## startswith/endswith 方法 校验是否以“XX”开头/结尾

print(str5.startswith('她们'))
print(str5.endswith('我们'))

print('*' * 50)

## isdigit 方法 校验字符串是否全为数字构成

str6 = '''
123'''
print(str6.isdigit())

print('-' * 50)

### 列表的方法

## append 方法 列表后添加一个列表/单个元素
## 注意：方法返回值为None

a = [1, 2, 3.14, 'hello']
a.append('bye')
print(a)

a.append(1)
print(a)

## insert 方法 插入某位置某元素进去
## 注意：方法返回值为None

a.insert(0, 'start')
print(a)

a.insert(2, 'third')
print(a)

## pop 方法 取出并删除某一元素(按照索引)

temp = a.pop(2)
print(temp)
print(a)

## remove 方法 取出并删除某一元素(按照元素值)，删除后不会向后遍历，仅删除第一个匹配的
## 注意：方法返回值为None

a.remove(1)
print(a)

## reverse 方法 将列表倒序
## 注意：方法返回值为None

a.reverse()
print(a)

## index 方法 查询某元素在列表中的位置,查询到后不会向后遍历，仅返回第一个匹配的

a.append(2)
print(a.index(2))

## sort 方法 重排序(全数字/字符串)
## 注意：方法返回值为None

b = [3, 4, 81, 32, 254352, 5]
c = ['as', 'werw', 'Dfafd', 'Had']

b.sort()
c.sort()

print(b)  # 默认从小到大
print(c)  # 默认A-Z,a-z

'''
请写一个程序：

首先提示用户输入年龄、身高、体重信息，格式如下如下

请输入您的性别：男
请输入您的身高（厘米）：175厘米
请输入您的体重（公斤）：80公斤
注意：

用户输入的内容，前后、中间都可能有空格，比如 175 厘米

然后根据如下的计算公式，计算出身高对应的标准体重。

标准体重(男)=(身高cm-100)x0.9(kg)
标准体重(女)=(身高cm-100)x0.9(kg)-2.5(kg)
如果体重在标准体重上下5公斤，都属于标准体重，提示用户体重标准。

否则提示用户高于标准还是低于标准
'''

"""
manul = input("请输入您的性别：").strip()
high = int(input("请输入您的身高（厘米）：").replace('厘米',' ').strip())
weigh = int(input("请输入您的体重（公斤）：").replace('公斤',' ').strip())

if manul == "男":
    temp = (high - 100) * 0.9
    if weigh >= temp - 5 and high <= temp + 5:
        print("您的体重标准")
    elif weigh > temp + 5:
        print("您已超重")
    else:
        print("你需增重")
else:
    temp = (high - 100) * 0.9 - 2.5
    if weigh >= temp - 5 and high <= temp + 5:
        print("您的体重标准")
    elif weigh > temp + 5:
        print("您已超重")
    else:
        print("你需增重")
"""