# 变量命名规则：
#    1.数字 字母 下划线 中文（不建议这么做）
#    2.字母 下划线开头
#    3.不可包含空格
#    4.关键字 内置函数 不可同名
#    5.大小写敏感

# 变量重新引用新对象
# 1.对象不可变 string number tuple

age = 11
age = "年龄"  # 没有被引用的对象，解释器随后会将其从内存中删除

num = 10
num += 1  # 等价于 num = num + 1

# 2.对象可变 dictionary list cet 自定义实例对象

info = {'name': 'george', 'age': 11}
info['age'] = 12
print(info)
