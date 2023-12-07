## 字符集 ASC GB2312 GBK unicode
## 编码规范           UTF-8 UTF-16


## 编码 encode

print('你好'.encode('utf8'))
print('你好'.encode('GBK'))

print('*'*50)

# b 开头表示，字节串对象bytes \x 用16进制表示一个字节

## 解码 decode

print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
print(b'\xc4\xe3\xba\xc3'.decode('GBK'))

print('*'*50)

## 编码 chr() unicode数字字符串转字符

print(chr(50))
print(chr(20013))
print(chr(0x4e2d))

print('*'*50)

## 解码 ord() 字符转unicode数字字符串

print(ord('2'))
print(ord('中'))

print('*'*50)


## 编码格式 unicode—escape 字符串转数字字符串

print('中中中'.encode('unicode-escape'))

print('*'*50)


## 用数字字符串直接输出字符串

print('\u4e2d\u4e2d\u4e2d\u4e2d')
print(hex(ord('中')))

