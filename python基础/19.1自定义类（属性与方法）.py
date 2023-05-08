## 一步步来首先我们创建一个字典表示奔驰

benzCar = {
    'brand': '奔驰',
    'country': '德国',
    'price': 30000
}


## 然而现实中他还有许多行为动作，比如：鸣笛

def whistle():
    print('didididi')


benzCar = {
    'brand': '奔驰',
    'country': '德国',
    'price': 30000,
    'act': whistle  # 这里自定义函数作为对象被记录
}

benzCar['act']()  # 这里我们可以这样使用他的行为

print('*' * 50)


## 然而这里的benzCar更像是一个实例，我们可以将其写为类的形式

class BenzCar:  # 类的名称我们通常首字母大写
    brand = '奔驰'
    country = '德国'

    # 这里的brand与country叫做类的属性

    @staticmethod  # 该修饰器说明该方法为该类的静态方法(该方法不强制要求函数传递参数)
    def whistle():
        print('didididididi')


# 类外我们可以这样调用属性
print(BenzCar.brand)
# 类外我们可以这样调用他的静态方法
BenzCar.whistle()

print('*' * 50)

## 类的实例化

# 类的实例具有类的一切属性与方法
# type方法可以查看实例属于什么类

mycar = BenzCar()
print(type(mycar))
# 结果中的__main__说明该类为主模块下的

print('*' * 50)


### 类属性 与 类的实例属性
### 显然作为实例属性，每个实例其都有自己的差异点，而类属性为类下的共同特征

## 通常类的实例属性在 __init__ 中被定义

class BenzCar:
    brand = '奔驰'
    country = '德国'

    def __init__(self):  # 该方法在实例创建时立刻执行，故叫初始化方法
        self.color = 'white'
        self.ip = 12138

    @staticmethod
    def whistle():
        print('didididididi')


### 注意：__init__(self)，其中的self在实例被创建时，直接指向该实例
###      即可在后面将属性color和ip传给具体实例

### 类方法(静态方法) 和 类的实例方法
### 作为静态方法(@staticmethod)不可访问实例属性
### 显然作为实例方法，需要改变实例属性，否则一般的静态方法即可满足

# 当然实例属性允许从外界传入，代码修改如下：

class BenzCar:
    brand = '奔驰'
    country = '德国'

    def __init__(self, color, ip):  # 该方法在实例创建时立刻执行，故叫初始化方法
        self.color = color
        self.ip = ip

    @staticmethod
    def whistle():
        print('didididididi')


hiscar = BenzCar('yello', 12138)
hercar = BenzCar('white', 3111004)
print(hiscar.color)
print(hiscar.ip)
print(hercar.color)
print(hercar.ip)

print('*' * 50)


# 实例方法可以修改实例变量，代码如下：

class BenzCar:
    brand = '奔驰'
    country = '德国'

    def __init__(self, color, ip):  # 该方法在实例创建时立刻执行，故叫初始化方法
        self.color = color
        self.ip = ip

    @staticmethod
    def whistle():
        print('didididididi')

    def changeColor(self, color):
        self.color = color


hiscar = BenzCar('yello', 12138)
hiscar.changeColor('black')
print(hiscar.color)

print('*' * 50)


## 若你的实例属性与类属性重名了，通过实例访问到的是实例属性，通过类访问到的是类属性

class student:
    name = 'default'

    def __init__(self, name):
        self.name = name


syd = student('syd')
print(syd.name)
print(student.name)

print('*' * 50)