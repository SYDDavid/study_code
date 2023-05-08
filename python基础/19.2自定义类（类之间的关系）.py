## 继承关系  class son(father):

# 被继承的类叫做 子类，派生类
# 继承类称为     父类，基类

class BenzCar:
    brand = '奔驰'
    country = '德国'

    def __init__(self, color, ip=111):
        self.color = color
        self.ip = ip

    @staticmethod
    def whistle():
        print('didididididi')

    def changeColor(self, color):
        self.color = color


class BenzCar2016(BenzCar):
    price = 30000


class BenzCar2018(BenzCar):
    price = 20000


### 注意：子类自动拥有父类的一切属性与方法

car1 = BenzCar2016('blue')
print(car1.color)
car1.changeColor('yellow')
print(car1.color)

print('*' * 50)


## 子类在继承父类方法和属性基础上可以拥有自己的方法和属性

class BenzCar2016(BenzCar):
    price = 30000

    def __init__(self, color, ip, weight, oil):
        BenzCar.__init__(self, color, ip)  # 子类初始化函数也需要初始换父类函数
        self.weight = weight
        self.oil = oil

    def addoil(self, addedoil):
        self.oil += addedoil
        return self


car3 = BenzCar2016('white', weight=10000, ip=111, oil=200)
print(car3.addoil(50).oil)

print('*' * 50)


## 若子类没有自己的初始化方法，子类在实例化时会自动调用父类的初始化方法

class father:
    def __init__(self):
        print('若子类没有自己的初始化方法，子类在实例化时会自动调用父类的初始化方法')


class son(father):
    pass


s = son()

print('*' * 50)


## 若子类有自己的初始化方法，则不会调用父类的

class father:
    def __init__(self):
        print('father')


class son(father):
    def __init__(self):
        print('son')


s = son()

print('*' * 50)


## super方法
# 1、初始化时可不写父类名，切使用后不用写self参数

class BenzCar2016(BenzCar):
    price = 30000

    def __init__(self, color, ip, weight, oil):
        super().__init__(color, ip)  # super()可使链路更完整，且不用self参数
        self.weight = weight
        self.oil = oil

    def addoil(self, addedoil):
        self.oil += addedoil
        return self


car3 = BenzCar2016('white', weight=10000, ip=111, oil=200)
print(car3.addoil(50).oil)

print('*' * 50)


# 2、多继承下的初始方法也可用super()

class BenzCar2016Hybird(BenzCar2016):
    def __init__(self, color, ip, weight, oil, name):
        super().__init__(color, ip, weight, oil)
        self.name = name


car4 = BenzCar2016Hybird('white', weight=10000, ip=111, oil=200, name='hello')
print(car4.addoil(50).oil)

print('*' * 50)


## 类之间的组合(另一个类作为该类的属性)

class Tire:
    def __init__(self, size, createDate):
        self.size = size  # 尺寸
        self.createDate = createDate  # 出厂日期


class BenzCar:
    brand = '奔驰'
    country = '德国'

    def __init__(self, color, engineSN, tires):
        self.color = color  # 颜色
        self.engineSN = engineSN  # 发动机编号
        self.tires = tires


# 创建4个轮胎实例对象
tires = [Tire(20, '20160808') for i in range(4)]
tires.append(Tire(20, '20160909'))
car = BenzCar('red', '234342342342566', tires)

print(car.tires[-1].createDate)
# 我们可以通过BenzCar对象进一步访问到Tires对象
