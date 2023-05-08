## wb模式写入时即为二进制方式写入
### 注意：write()方法时，参数必须为字节串对象！！！

f = open('../utf8.txt', 'wb')
string = '传输时必须为字节串'
f.write(string.encode('utf8'))
f.close()

print('*' * 50)

## rb模式读取时即为以二进制方式读取

f = open('../utf8.txt', 'rb')
content = f.read()
f.close()
print(content)

print('*' * 50)

## with语句：为避免遗漏close方法造成意外，python会自己通过with调用close

with open('../utf8.txt', encoding='utf8') as f:
    content = f.read()
    print(content)

## 写入缓冲特性 flush()方法
# 当我们打开一个文件执行后并不会立刻执行之后的代码，当文件关闭或内存满时才会处理

with open('../utf8.txt', 'w', encoding='utf8') as f:
    f.write('传输时必须为字节串')
    f.flush()

    import time

    time.sleep(30)

print('*' * 50)

## 文件的复制

with open(r'C:\Users\311004\Desktop\1.mp4','rb') as f:
    content=f.read()

with open(r'C:\Users\311004\Desktop\2.mp4','wb') as f:
    f.write(content)

## 注意文件路径需要对转义字符串做处理方法有三：前加r，双反斜，正斜