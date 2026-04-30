"""
策略模式 (Strategy Pattern) - 行为型模式

【解决的问题】
    1. 算法可替换：多种算法实现同一功能，可以互相替换
    2. 消除条件分支：大量 if/else 选择不同算法
    3. 算法独立变化：算法可以独立于使用它的客户端变化

【应用场景】
    1. 排序算法：多种排序策略可互换
    2. 支付方式：微信、支付宝、银行卡等
    3. 压缩算法：ZIP、RAR、GZIP 等
    4. 促销活动：满减、打折、返现等

【优缺点】
    优点：
        - 算法可以自由切换
        - 消除大量条件分支
        - 符合开闭原则
        - 算法可以复用
    缺点：
        - 客户端需要了解不同策略
        - 增加类的数量

【UML 结构】
    Context(上下文，持有 Strategy) --> Strategy(策略接口)
                                          ↑
                                   ConcreteStrategyA, ConcreteStrategyB, ...
"""

from abc import ABC, abstractmethod
from typing import List


# ===== 策略接口 =====
class PricingStrategy(ABC):
    """定价策略接口"""
    @abstractmethod
    def calculate(self, base_price: float) -> float:
        """计算最终价格"""
        pass


# ===== 具体策略 =====
class NormalPrice(PricingStrategy):
    """原价策略"""
    def calculate(self, base_price: float) -> float:
        return base_price


class DiscountPrice(PricingStrategy):
    """折扣策略 - 固定折扣"""
    def __init__(self, discount_rate: float):
        self._discount_rate = discount_rate

    def calculate(self, base_price: float) -> float:
        return base_price * (1 - self._discount_rate)


class FullReductionPrice(PricingStrategy):
    """满减策略"""
    def __init__(self, threshold: float, reduction: float):
        self._threshold = threshold
        self._reduction = reduction

    def calculate(self, base_price: float) -> float:
        if base_price >= self._threshold:
            return base_price - self._reduction
        return base_price


class MemberPrice(PricingStrategy):
    """会员价策略"""
    def __init__(self, level: str):
        self._level = level
        self._rates = {"普通会员": 0.95, "银卡会员": 0.9, "金卡会员": 0.8, "钻石会员": 0.7}

    def calculate(self, base_price: float) -> float:
        rate = self._rates.get(self._level, 1.0)
        return base_price * rate


# ===== 上下文 =====
class ShoppingCart:
    """购物车 - 上下文"""
    def __init__(self):
        self._items: List[tuple[str, float]] = []
        self._strategy: PricingStrategy = NormalPrice()

    def add_item(self, name: str, price: float):
        self._items.append((name, price))

    def set_strategy(self, strategy: PricingStrategy):
        """设置定价策略"""
        self._strategy = strategy

    def checkout(self) -> float:
        """结算"""
        total = sum(price for _, price in self._items)
        final_price = self._strategy.calculate(total)

        print(f"  商品：{[name for name, _ in self._items]}")
        print(f"  原价：RMB{total:.2f}")
        print(f"  策略：{self._strategy.__class__.__name__}")
        print(f"  实付：RMB{final_price:.2f}")
        return final_price


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("策略模式演示：电商促销系统")
    print("=" * 50)

    cart = ShoppingCart()
    cart.add_item("Python 编程书", 79.0)
    cart.add_item("机械键盘", 299.0)
    cart.add_item("显示器", 1299.0)

    print("\n1. 原价购买：")
    cart.set_strategy(NormalPrice())
    cart.checkout()

    print("\n2. 8折促销：")
    cart.set_strategy(DiscountPrice(0.2))
    cart.checkout()

    print("\n3. 满300减50：")
    cart.set_strategy(FullReductionPrice(300, 50))
    cart.checkout()

    print("\n4. 金卡会员价：")
    cart.set_strategy(MemberPrice("金卡会员"))
    cart.checkout()

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 支付方式选择（微信/支付宝/银行卡）")
    print("  - 排序算法切换")
    print("  - 数据压缩/加密算法")
    print("  - 验证规则（不同字段不同验证策略）")
    print("=" * 50)
