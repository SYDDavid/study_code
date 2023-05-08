### 为了统一输出格式，python提供了字符串格式化方法

## printf风格（先用通配符%占用，后用元组中内容做代替）

# 举例如下：

salary = input('请输入薪资：')

tax = int(salary) *25/100

aftertax = int(salary) *75/100

print('税前薪资：%s元，缴税：%s元，税后薪资：%s元' %(salary,tax,aftertax))

print('*'*50)

## 这里的%s是一种格式化符号，解释器看到后先调用str()函数，再将对应对象传入，最后将返回结果填入占位中
# 占位符数量需与传参数一致，当只有一个时注意：(salary，)或者直接salary

## 指定宽度和对齐 %10s %-10s

print('税前薪资：%10s 元' % 100000)
print('税前薪资：%10s 元' % 10000)
print('税前薪资：%10s 元' % 1000)

print('税前薪资：%-10s 元' % 100000)
print('税前薪资：%-10s 元' % 10000)
print('税前薪资：%-10s 元' % 1000)

print('*'*50)

## %d和%f
# %d用于整数  %f用于小数 然而，%s同样可用于整数小数
# %010d 当我们希望指定宽度同时空位补0时可用

print('税前薪资：%010d 元' % 100000)
print('税前薪资：%010d 元' % 10000)
print('税前薪资：%010d 元' % 1000)

# 同样的：
# %010f 可以多小数指定宽度同时空位补0

print('税前薪资：%012f 元' % 1000.4522)
print('税前薪资：%012f 元' % 1008.6621)
print('税前薪资：%012f 元' % 1009.3351)

### 注意：小数用 %f 占位符时，小数点后必定为6位（且超过六位做舍弃处理）

print('*'*50)

# 小数当我们想至保留后两位时可以加 .2
# %010.2f  注意：这里是做四舍五入！！！

print('税前薪资：%010.2f 元' % 1000.4522)
print('税前薪资：%010.2f 元' % 1008.6621)
print('税前薪资：%010.2f 元' % 1009.3351)

## f-string 风格（字符串前加f，后用{}占位符占用，里面直接填写对象）
## 注意：py3.6后版本可用
## 举例如下：

salary = input('请输入薪资：')

tax = int(salary) *25/100

aftertax = int(salary) *75/100

print(f'税前薪资是：{salary}元， 缴税：{tax}元， 税后薪资是：{aftertax}元')

print('*'*50)

# {:10} 指定宽度(默认右对齐)

def calcTax(salary):
    tax = int(salary) *25/100
    aftertax = int(salary) *75/100
    print(f'税前薪资是：{salary:12}元， 缴税：{tax:12}元， 税后薪资是：{aftertax:12}元')

calcTax(8000)
calcTax(15000)
calcTax(100000)

print('*'*50)

# {:<10} 左对齐

def calcTax(salary):
    tax = int(salary) *25/100
    aftertax = int(salary) *75/100
    print(f'税前薪资是：{salary:<20d}元， 缴税：{tax:<20f}元， 税后薪资是：{aftertax:<20f}元')
# 使用f同样默认小数点后保留6位

calcTax(8320)
calcTax(15023)
calcTax(100030)

print('-'*50)

# {：20.1f} 小数点后保留至第几位

def calcTax(salary):
    tax = int(salary) *25/100
    aftertax = int(salary) *75/100
    print(f'税前薪资是：{salary:8.1f}元， 缴税：{tax:8.1f}元， 税后薪资是：{aftertax:8.1f}元')


calcTax(8320)
calcTax(15023)
calcTax(100030)

print('*'*50)

# {:010}{:010f} 对数字或者小数进行补0

def calcTax(salary):
    tax = int(salary) *25/100
    aftertax = int(salary) *75/100
    print(f'税前薪资是：{salary:08}元， 缴税：{tax:08.1f}元， 税后薪资是：{aftertax:08.1f}元')


calcTax(8320)
calcTax(15023)
calcTax(100030)

# {:<08}{:>08} 对字符串不足补零需说明左(右)对齐

var = '34324'
print(f'{var:<08}')
print(f'{var:>08}')