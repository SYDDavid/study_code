# python中调用外部程序通常有两种方式，os.system库或者subprocess模块

import os
from subprocess import PIPE, Popen

# os.system(cmd)

os.system('chcp 65001')  # 默认GBK编码(936) 切换为UTF-8编码(65001)

cmd = r'ping www.baidu.com'
result = os.system(cmd)

print('*' * 50)

print(result)

print('执行完成')  # os.system在执行时必须等调用程序执行完毕，代码才会继续执行下去，否则就会一直等待

## 局限性：无法获取被调用程序返回给终端窗口的信息，即函数返回信息为 0(可执行) 或 1(不可执行)

### 路径调用打开目录，或者打开程序

print('*' * 50)

# os.startfile(r'c:\Users\311004\Desktop\1.mp4') # 文件的话启动系统下对应程序打开
# os.startfile(r'c:\Users\311004\Desktop') # 目录的话打开文件管理器

print('*' * 50)

# subprocess可以让我们获取到其中返回给窗口的内容

# 返回的是 Popen 实例对象
proc = Popen(
    'fsutil volume diskfree c:',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True)

# communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# 标准输出设备和 标准错误设备 当前都是本终端设备
outinfo, errinfo = proc.communicate()

# 注意返回的内容是bytes 不是 str ，我的是中文windows，所以用gbk解码
outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')
print(outinfo)
print('-------------')
print(errinfo)

outputList = outinfo.splitlines()

# 剩余量
free = int(outputList[0].split(':')[1].replace(',', '').split('(')[0].strip())

# 总空间
total = int(outputList[1].split(':')[1].replace(',', '').split('(')[0].strip())

if (free / total < 0.1):
    print('!! 剩余空间告急！！')
else:
    print('剩余空间足够')

## popen执行的命令，程序不会等待其执行完成后后再执行其他内容

Popen(
    'ping www.baidu.com',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True
)

print('wait')
