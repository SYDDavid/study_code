"""
装饰器模式 (Decorator Pattern) - 结构型模式

【解决的问题】
    1. 动态添加职责：需要在运行时动态给对象添加功能
    2. 避免类爆炸：使用继承会导致子类数量爆炸
    3. 灵活组合功能：需要灵活地组合多个功能

【应用场景】
    1. 需要动态添加/撤销职责的场景
    2. 功能可以灵活组合的场景
    3. 继承方案不灵活或不可行的场景

【优缺点】
    优点：
        - 比继承更灵活，可以动态组合功能
        - 避免类爆炸
        - 符合开闭原则
    缺点：
        - 增加了系统的复杂性
        - 多层装饰难以调试

【UML 结构】
    Component(组件接口)
         ↑
    +----+----+
    |         |
ConcreteComponent  Decorator(装饰基类，持有 Component)
                         ↑
                    ConcreteDecorator
"""

from abc import ABC, abstractmethod


# ===== 组件接口 =====
class Coffee(ABC):
    """咖啡接口"""
    @abstractmethod
    def cost(self) -> float:
        """价格"""
        pass

    @abstractmethod
    def description(self) -> str:
        """描述"""
        pass


# ===== 具体组件 =====
class SimpleCoffee(Coffee):
    """基础咖啡"""
    def cost(self) -> float:
        return 10.0

    def description(self) -> str:
        return "基础咖啡"


# ===== 装饰基类 =====
class CoffeeDecorator(Coffee):
    """咖啡装饰器基类"""
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


# ===== 具体装饰器 =====
class MilkDecorator(CoffeeDecorator):
    """牛奶装饰器"""
    def cost(self) -> float:
        return self._coffee.cost() + 3.0

    def description(self) -> str:
        return self._coffee.description() + " + 牛奶"


class SugarDecorator(CoffeeDecorator):
    """糖装饰器"""
    def cost(self) -> float:
        return self._coffee.cost() + 1.0

    def description(self) -> str:
        return self._coffee.description() + " + 糖"


class CreamDecorator(CoffeeDecorator):
    """奶油装饰器"""
    def cost(self) -> float:
        return self._coffee.cost() + 5.0

    def description(self) -> str:
        return self._coffee.description() + " + 奶油"


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("装饰器模式演示：咖啡订单系统")
    print("=" * 50)

    # 基础咖啡
    coffee1 = SimpleCoffee()
    print(f"\n{coffee1.description()}: RMB{coffee1.cost()}")

    # 咖啡 + 牛奶
    coffee2 = MilkDecorator(SimpleCoffee())
    print(f"{coffee2.description()}: RMB{coffee2.cost()}")

    # 咖啡 + 牛奶 + 糖
    coffee3 = SugarDecorator(MilkDecorator(SimpleCoffee()))
    print(f"{coffee3.description()}: RMB{coffee3.cost()}")

    # 咖啡 + 牛奶 + 糖 + 奶油
    coffee4 = CreamDecorator(SugarDecorator(MilkDecorator(SimpleCoffee())))
    print(f"{coffee4.description()}: RMB{coffee4.cost()}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - Java I/O 流：BufferedInputStream(FileInputStream)")
    print("  - Python 装饰器语法：@decorator")
    print("  - 中间件系统：多层请求处理")
    print("  - GUI 组件：边框、滚动条装饰")
    print("=" * 50)
