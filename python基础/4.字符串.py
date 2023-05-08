# 字符串中的引号，仅为了告诉解释器其中内容为对象，引号本身不作为对象一部分

var = "hello"  # 存储为 hello 而非 “hello”

# 字符串中有引号
# 1.单引号-->用双引号

var1 = "he said:'hello'"

# 2.双引号-->用单引号

var2 = 'he said:"hello"'

# 3.单双引号-->用三引号

var3 = '''syd's wife said:"hello"'''

# 字符串切片
# 缺省

print(var3[:4])
print(var3[4:])

# 切段 左闭右开

print(var3[0:3])

# 获取字符串长度 内置函数len()

length = len(var3)
print(length)

print('*' * 50)
# 题目：有如下的代码，定义了一个Python字符串
# str1 = '大家好，我的名字叫：黑羽白月'
# 请接下来写一行代码，使用字符串切片的方法 ，打印出 str1里面的人名字

str1 = '大家好，我的名字叫：黑羽白月'
print(str1[10:14])
print(str1[10:])
print(str1[len(str1) - 4:])   # sequence计数可以使用计算方式
print(str1[-4:])
