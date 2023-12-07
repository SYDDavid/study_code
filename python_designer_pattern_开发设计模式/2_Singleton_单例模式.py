'''
需求：一个类只能有一个实例，并提供对该实例的全局访问点。
实例：整个系统只有一个文件管理器，不需要创建很多实例去访问同一个东西
UML类图：
    class：        Singleton
    attribute：  - static instance：Singleton
    function：   + static getInstance：Singleton()
                 -  Singleton()
'''


class Singleton:
    __instance = None

    # 提供方法去获取到这个单例，即使例未被创建也会调用到constructor function
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
# s2=Singleton()
print(s)
s1 = Singleton.getInstance()
print(s)
s2 = Singleton.getInstance()
print(s)
