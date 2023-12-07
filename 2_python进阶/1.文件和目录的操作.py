import os
import shutil
import time
import glob

### 创建目录

# mkdir 与 makedirs
# 单级创建使用mkdir 多级目录创建使用makedirs

os.makedirs('syd1/syd2', exist_ok=True)  # exist_ok=True若目录存在也不会报错

## 对于路径的几点说明：
# 'syd1/syd2'      syd1与当前代码同级
# '/syd1/syd2'     syd1位于根目录下
# '../syd1/syd2'   syd1与当前代码上级目录同级

### 拷贝文件

shutil.copyfile('../test.txt', 'syd1/syd2/test.txt')

### 删除单个文件

os.remove('syd1/syd2/test.txt')

### 删除目录

## shutil.rmtree方法可以递归删除目录下子目录与其文件

shutil.rmtree('syd1', ignore_errors=True)  # ignore_errors=True若目录不存在也不会报错

### 拷贝目录 及其目录下子目录与文件

# shutil.copytree('e:\code\1_python基础', r'e:\code\tmp')  # 目标路径存在会报错，目标路径若不存在，先创建该路径，再复制目录
shutil.copytree(r'e:\code\1_python基础', r'e:\code\tmp', dirs_exist_ok=True)

### 修改文件名，目录名
## 注意：windows下目标路径存在会报错，Linux下直接覆盖

os.rename(r'e:\code\draft.py', r'e:\code\draft2.py')  # 修改文件名
os.rename(r'e:\code\draft2.py', r'e:\code\draft.py')

os.rename(r'e:\code\tmp', r'e:\code\tmp1')  # 修改目录名

shutil.rmtree(r'..\tmp1', ignore_errors=True)

### 对路径的处理
## windows使用\ Linux使用/ os.path模块可以兼容

path = 'e:\code\draft.py'

# 路径中文件名的获取

print(os.path.basename(path))

# 路径中目录的获取

print(os.path.dirname(path))

# 路径拼接

print(os.path.join(os.path.dirname(path), 'code', os.path.basename(path)))

print('*' * 50)

### 判断路径

# 是否存在路径

print(os.path.exists('e:\code\draft.py'))
print(os.path.exists('e:\code'))

# 路径下是否为文件

print(os.path.isfile('e:\code\draft.py'))

# 路径下是否为目录

print(os.path.isdir('e:\code'))

print('*' * 50)

### 文件的大小和日期信息

# 返回文件大小

os.path.getsize(r'..\draft.py')

# 返回文件时间（秒） 通过time。ctime转化为日期时间

print(time.ctime(os.path.getmtime(r'..\draft.py')))  # 修改时间
print(time.ctime(os.path.getatime(r'..\draft.py')))  # 访问时间
print(time.ctime(os.path.getctime(r'..\draft.py')))  # 创建时间

print('*' * 50)

### 修改文件工作目录

# 查询工作目录

cwd = os.getcwd()
print(cwd)

# 修改工作目录

os.chdir('e:\XMind')
os.chdir(cwd)

print('*' * 50)

### 递归遍历获取目录节点信息

targetdir = r'e:\code'

files = []  # 全文件名
dirs = []  # 全文件夹名
paths = []  # 全路径名 重点注意其使用方法

for (dirpath, dirsname, filesname) in os.walk(targetdir):  # dirpath为str filesname与dirsname为lsit
    files += filesname
    dirs += dirsname
    for file in filesname:
        abspath = os.path.join(dirpath, file)
        paths.append(abspath)

print(files)
print(dirs)
print(paths)

print('*' * 50)

### 得到目录下所有文件和子目录名

files = os.listdir(targetdir)
print(files)  # 仅得到该目录下文件及文件夹名，无法递归进入文件夹下

print([f for f in files if os.path.isfile(os.path.join(targetdir, f))])  # 筛选出文件

print([f for f in files if os.path.isdir(os.path.join(targetdir, f))])  # 筛选出文件名

print('*' * 50)

### 得到目录中指定扩展名的文件和子目录 需要导 glob

txts = glob.glob(r'e:\code\*.*')
print(txts)

## 当前认知为模糊匹配 很有用的样子

### 路径调用打开目录，或者打开程序

os.startfile(r'c:\Users\311004\Desktop\1.mp4') # 文件的话启动系统下对应程序打开
os.startfile(r'c:\Users\311004\Desktop') # 目录的话打开文件管理器
