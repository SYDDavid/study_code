## 布尔表达式：返回结果为bool类型的表达式
# 是否相等 ==
# 是否不等 ！=
# 是否大于 >
# 是否大于等于 >=
# 是否小于 <
# 是否小于等于 <=

print('A' < 'B')

# 条件组合判断
# 与 and
# 或 or
# 非 not

# 当and遇到or时，优先计算and，其结果与or运算

print(True or True and False)

# 若想优先计算or，使用小括号

print((True or True) and False)

## 注意：not优先级高于and，and优先级高于or

# 判断语句 if 关键字
'''
#以下为格式

if *****:
    *******
elif *****:
    *******
elif *****:
    *******
else:
    *******

'''

# def 函数情况下 结合return可以提前结束

## 注意：条件哪里满足哪里执行缩进内容，执行完后跳出if

if 3<5:
    print(1)
elif 3<6:
    print(2)
else:
    print(3)