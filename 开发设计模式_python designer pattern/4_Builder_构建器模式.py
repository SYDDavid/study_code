'''
构建者模式又称建造者模式
需求：
    1、目标类的属性过多       需要大量set，或者重构init函数
    2、目标类的属性结构复杂    使用过程需要不断考虑内部结构是否会被改变

一般是会设计两个类，一个类是目标类，也就是我们需要的类；另一个类就是构建器类，它是为了我们创建目标类时更加的方便。

注意：一旦目标类发生变动，构建器类也需要同步发生改变
'''


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()
        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)
        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)
        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car


# The whole product
class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def setBody(self, body):
        self.__body = body

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)

# 创建构建器类，定义函数组成，搭建构建框架
class Builder:
    def getWheel(self): pass

    def getEngine(self): pass

    def getBody(self): pass

# 实现具体Jeep构建类，重写方法，针对Jeep实现具体合理设计
class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


# Car parts
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None


def main():
    jeepBuilder = JeepBuilder()  # initializing the class
    director = Director()
    # Build Jeep
    print("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
    print("")


if __name__ == "__main__":
    main()