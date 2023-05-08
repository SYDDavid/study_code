# 关键字 input
## 注意：用户input内容均作为 字符串 返回

# 实例：计算员工税后薪资

salary=input("please input employee's salary:")
print('realsalary:'+str(int(salary)*0.75))

# 具体使用时灵活使用 str() int() float()

print('-'*50)

# 实例：
# 请定义一个函数printlen, 该函数中让用户输入一个字符串， 该函数打印出用户输入的这个字符串的 长度
# 比如 用户输入 123456789， 该函数应该打印出：长度为9

def stringlen():
    str1 = input('please input your string:')
    return '长度为：'+str1(len(str1))

print(stringlen())

## 注意
# 1、函数变量命名同为str时，会报错
# 2、'len(str1)' 这样的表达，解释器默认引号内为字符串，故输出：len(str1)