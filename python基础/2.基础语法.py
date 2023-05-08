# 变量定义直接赋值，可多个变量同时赋值

a = 1;
b = 1.0;
c = '字符串';
a = b = c = "字符串";
a, b, c = 2, 3.1, '任意文字';

# Number四种类型 :int float bool complex

a = 1
b = 1.1
c = True  # 区分大小写
d = 1.1 + 2.2j

# python中单双引号完全相同 “ ‘

a = '字符串'
b = "字符串"

# ’‘’或者”“”可以指定多行字符串

c = """三双引号或者单引号
可以指定多行的字符串"""

# 反斜杠表转义，字符前加r可以不发生转义

print("反斜杠表转义\n字符前加r可以不发生转义");
print(r"反斜杠表转义\n字符前加r可以不发生转义");

# 字符串可用：+连接 用*重复
# 字符串索引：从左到右 0 1 2 3 从右到左 -1 -2 -3 -4
# 截取语法如下 变量[头标：尾标：步长]  注：左闭右开区间

str = '123456789'
str2 = '添加字符'

print(str + str2)
print(str * 2)

print('--------------------------------')

print(str[3])
print(str[3:])
print(str[0:3])  # 右不取到
print(str[0:3:2])
print(str[0:3:3])  # 超出步长，可显示
print(str[0:-1])  # 右不取到

# print默认换行，若不需要则在末尾添加 ,end=''

print(str[3],end='')
print(str[3:])

# 等待用户输入

x = input('按下enter后退出')  # ''内内容为默认提示，总会显示，函数输出以用户最终回车前前内容为准
print(x)

# 复合语句如if，while，def，class，首行关键字开始，冒号：结尾，该行后一行或多行组成一个代码组

if a == 1:
    a = 2
elif a != 1:
    a = 1
else:
    a = 3

# import 与 from import
# 导入整个模块：import somemodule
# 导入模块中某函数：from somemodule import somefunction
# 导入模块中某些函数：from somemodule import firstfunc,secondfunc,thirdfunc
# 导入模块中所有函数：from somemodule import *

