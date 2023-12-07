## 字典：以键值对方式进行数据的存储(key-value)
## 定义方式：用大括号包住，键值之间用冒号隔开，每个元素之间用逗号隔开

members = {
    'name': 'syd',
    'age': 11
}

### 注意：字典元素中的键必须是可进行哈希计算的，通常为：数字或者字符串
###      字典元素中的值可以为任意对象

role = {
    'ganyu': {
        'hp': 3000,
        'speed': 20
    },
    'keqing': {
        'hp': 2000,
        'speed': 30
    }
}

### 注意：字典书写隐规则：键值对后加逗号；键值对占单独一行

## 字典对象一大特点：可以通过键找到对应的值

print(members['name'])
print(role['ganyu']['speed'])

print('*' * 50)

## 字典优点：1、理论上内存足够大字典可以存储无限的数据
##         2、字典查询数据的效率非常高，非常适合存储查找数据

# 字典对象中键是唯一的，若重复后一个会替代前一个

student = {
    'class': 301,
    'class': 302
}

print(student['class'])

print('*' * 50)

# 字典的增、删、改操作
# 若字典中无该条则增加，若有则为修改

default = {}

# 增加

default['add'] = 'add'
default['add1'] = 'add1'
print(default)

print('*' * 50)

# 修改

default['add'] = 'change'
print(default)

print('*' * 50)

# 删除：1、pop方法(还会返回被删除的value)

print(default.pop('add'))
print(default)

print('*' * 50)

# 删除：2、del指令

del default['add1']
print(default)

print('*' * 50)

## 判断是否存在key(若没有直接去获取key的value会报错，故需要该判断)

if 'ip' in members:
    print('该元素存在于字典中')
if 'ip' not in members:
    print('该元素不存在于字典中')

print('*' * 50)

## 遍历访问所有字典中元素
# items方法，返回列表，其中每个元素作为列表中的元组元素返回

temp = members.items()
print(temp)

for key, value in members.items():
    print(f'key:{key},value:{value}')

print('*' * 50)

## 访问所有的key(keys方法)、访问所有的value(values方法)
## 返回的类似于列表的对象

print(members.keys())
print(members.values())

print('*' * 50)

## 清空字典(clear方法)

members.clear()
print(members)

print('*' * 50)

### 注意：区别于重新赋空值给字典对象，clear直接清除内存，赋值指是代替，合适时候解释器再清除原来对象在内存中的占用

## 合并字典(update方法)

role.update(student)
print(role)

print('*' * 50)

## 获取字典长度(length方法)

print(len(role))