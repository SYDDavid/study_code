'''
Python 设计模式学习

参考：
    - https://iowiki.com/python_design_patterns/python_design_patterns_factory.html
    - https://blog.csdn.net/lianghudream/article/details/146612129

创建型模式（5种）：
    1_Model_View_Controller pattern   - MVC 模式
    2_Singleton_单例模式               - 确保一个类只有一个实例
    3_Factory_工厂模式                 - 不暴露创建逻辑，使用公共接口创建对象
    4_Builder_构建器模式               - 分步构建复杂对象

结构型模式（7种）：
    5_Adapter_适配器模式               - 接口转换，使不兼容的类协同工作
    6_Bridge_桥接模式                  - 分离抽象与实现，使两者独立变化
    7_Composite_组合模式               - 统一处理单个对象和组合对象
    8_Decorator_装饰器模式             - 动态添加职责
    9_Facade_外观模式                  - 为子系统提供统一入口
    10_Flyweight_享元模式              - 共享对象减少内存占用
    11_Proxy_代理模式                  - 控制对象访问

行为型模式（10种）：
    12_ChainOfResponsibility_责任链模式 - 请求沿链传递直到被处理
    13_Command_命令模式                 - 将请求封装为对象
    14_Iterator_迭代器模式              - 顺序访问集合元素
    15_Mediator_中介者模式              - 集中管理对象间交互
    16_Memento_备忘录模式               - 保存和恢复对象状态
    17_Observer_观察者模式              - 一对多依赖通知
    18_State_状态模式                   - 对象行为随状态变化
    19_Strategy_策略模式                - 算法族可互相替换
    20_TemplateMethod_模板方法模式       - 定义算法骨架，子类实现细节
    21_Visitor_访问者模式               - 不修改类的情况下添加新操作
'''

'''
    python类实例化的步骤和过程
        - __new__
        - __init__
        - __call__
    
    __new__
        - 是一个天然的静态方法
        - 返回一个全新的实例对象
        - 首参为cls即类本身，意味着是创建一个类的实例
    
    __init__
        - 返回None
        - 首参为self即实例本身，意味着初始化一个实例
        
    __call__
        - call为元类方法，所有类的元类为type(这里需要区别于父类，父类和子类是集成关系，普通类是原类的实例是实现关系，元类的方法决定了类的实现形式)
            # 新定义一个元类
            class CallableMeta(type):
                def __call__(cls, name):
                    print(f"Hello, {name}!")
                    # 如果你想保留正常实例化功能，可以在这里继续调用 __new__ 和 __init__
                    # 不过这里我们只演示“让类可调用但不创建实例”
                    # 不返回实例也可以，但一般不这么玩
                    # return super().__call__()  # 这会继续正常实例化流程

            # 告诉编译器按照metaclass作为元类创建Dog类
            class Dog(metaclass=CallableMeta):
                pass

            Dog("Alice")   # 输出: Hello, Alice!  （然后还会得到一个 Dog 实例）
            
        - 当类对象被调用时，即调用了元类的__call__，在__call__中会依次先new后init，即：
            Dog("旺财")   →   type.__call__(Dog, "旺财")
            
            type伪代码如下：
            class type:
                def __call__(cls, *args, **kwargs):
                    # 1. 调用类的 __new__ 方法创建实例
                    instance = cls.__new__(cls, *args, **kwargs)
                    # 2. 如果返回的是该类实例，则调用 __init__ 初始化
                    if isinstance(instance, cls):
                        instance.__init__(*args, **kwargs)
                    return instance
        - call作为魔术方法，当其在类中被重写时，可以直接被当作方法使用
            Dog("旺财")   →   type.__call__(Dog, "旺财")
            
            class Dog():
                def __call__(cls, name):
                    print(f"Hello, {name}!")
            Dog("Alice") >>> Hello, Alice!
            

        
'''

# 新定义一个元类
class CallableMeta(type):
    def __call__(cls, name):
        print(f"Hello, {name}!")
        # 如果你想保留正常实例化功能，可以在这里继续调用 __new__ 和 __init__
        # 不过这里我们只演示“让类可调用但不创建实例”
        # 不返回实例也可以，但一般不这么玩
        # return super().__call__()  # 这会继续正常实例化流程

# 告诉编译器按照metaclass作为元类创建Dog类
class Dog(metaclass=CallableMeta):
    pass

Dog("Alice")   # 输出: Hello, Alice!  （然后还会得到一个 Dog 实例）
