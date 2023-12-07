## 需要对文件写入时 要将字符串编码为字节串
## 需要对文本读取时 要将字节串解码为字符串

### 文件的打开分为：文本模式和二进制模式

# 内置函授 open 参数如下：
'''
open(
    file,
    mode='r',
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None
    )
'''

# file:文件所在路径，可以相对可以绝对
# mode: r只读文本；w只写文本；a追加文本 其中r为缺省值
# encoding: 字符编解码格式 缺省为gbk（cp936）

f = open('../test.txt', 'w', encoding='gbk')
f.write('这是一个测试文件')
f.close()  ## 记得操作完后关闭！！！！！

print('*' * 50)

## 注意：open路径下若无该文件，则创建
##      打开模式：w + write方法：覆盖文件！！！！
##      打开模式：a + write方法：正常追加

f = open('../test.txt', 'a', encoding='gbk')
f.write('不同编码下文件内容测试')
f.close()  ## 记得操作完后关闭！！！！！

print('*' * 50)

# 文件的只读模式

f = open('../test.txt', 'r', encoding='gbk')
content = f.read()
f.close()  ## 记得操作完后关闭！！！！！
name = content.split('内容')[-1]
print(name)

print('*' * 50)

## read函数的参数 size

f = open('../test.txt', 'r', encoding='gbk')
tmp = f.read(3)
print(tmp)  ## 读取前三个
tmp = f.read(3)
print(tmp)  ## 接着读三个
tmp = f.read()
print(tmp)  ## 读取剩余的所有
f.close()

print('*' * 50)

## readlines方法和splitlines方法
# readlines返回列表时会在每个列表最后带换行符
# 读取全部后splitlines方法返回的列表不带换行符

f = open('../readlines.txt')
lines = f.readlines()
f.close()
print(lines)

f = open('../readlines.txt')
lines = f.read()
f.close()
print(lines.splitlines())

print('*' * 50)
