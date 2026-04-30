"""
状态模式 (State Pattern) - 行为型模式

【解决的问题】
    1. 对象状态相关行为：对象行为依赖于其状态，且状态会变化
    2. 大量条件分支：使用 if/elif/switch 导致代码臃肿
    3. 状态转换复杂：状态转换逻辑分散在各处

【应用场景】
    1. 工作流引擎：审批流程状态流转
    2. 游戏角色状态：站立、跑动、跳跃、受伤
    3. TCP 连接状态：建立、监听、关闭
    4. 订单状态：待支付、已支付、已发货、已完成

【优缺点】
    优点：
        - 消除大量条件分支
        - 状态转换集中管理
        - 符合开闭原则
        - 状态类职责单一
    缺点：
        - 增加类的数量
        - 状态类过多时维护困难

【UML 结构】
    Context(上下文，持有 State) --> State(状态接口)
                                      ↑
                               ConcreteStateA, ConcreteStateB, ...
"""

from abc import ABC, abstractmethod


# ===== 状态接口 =====
class OrderState(ABC):
    """订单状态接口"""
    @abstractmethod
    def pay(self, order: 'OrderContext'):
        pass

    @abstractmethod
    def ship(self, order: 'OrderContext'):
        pass

    @abstractmethod
    def deliver(self, order: 'OrderContext'):
        pass

    @abstractmethod
    def cancel(self, order: 'OrderContext'):
        pass

    @abstractmethod
    def __str__(self):
        pass


# ===== 上下文 =====
class OrderContext:
    """订单上下文 - 持有当前状态"""
    def __init__(self):
        self._state: OrderState = PendingState()

    def set_state(self, state: OrderState):
        self._state = state
        print(f"  订单状态变更 -> {state}")

    def pay(self):
        self._state.pay(self)

    def ship(self):
        self._state.ship(self)

    def deliver(self):
        self._state.deliver(self)

    def cancel(self):
        self._state.cancel(self)

    def __str__(self):
        return f"当前状态：{self._state}"


# ===== 具体状态 =====
class PendingState(OrderState):
    """待支付状态"""
    def pay(self, order: OrderContext):
        print("  支付成功！")
        order.set_state(PaidState())

    def ship(self, order: OrderContext):
        print("  [错误] 未支付，无法发货")

    def deliver(self, order: OrderContext):
        print("  [错误] 未支付，无法确认收货")

    def cancel(self, order: OrderContext):
        print("  订单已取消")
        order.set_state(CancelledState())

    def __str__(self):
        return "待支付"


class PaidState(OrderState):
    """已支付状态"""
    def pay(self, order: OrderContext):
        print("  [错误] 已支付，请勿重复支付")

    def ship(self, order: OrderContext):
        print("  已发货！")
        order.set_state(ShippedState())

    def deliver(self, order: OrderContext):
        print("  [错误] 未发货，无法确认收货")

    def cancel(self, order: OrderContext):
        print("  订单已取消（退款处理中）")
        order.set_state(CancelledState())

    def __str__(self):
        return "已支付"


class ShippedState(OrderState):
    """已发货状态"""
    def pay(self, order: OrderContext):
        print("  [错误] 已支付，请勿重复支付")

    def ship(self, order: OrderContext):
        print("  [错误] 已发货，请勿重复发货")

    def deliver(self, order: OrderContext):
        print("  确认收货！")
        order.set_state(CompletedState())

    def cancel(self, order: OrderContext):
        print("  [错误] 已发货，无法取消（请联系客服）")

    def __str__(self):
        return "已发货"


class CompletedState(OrderState):
    """已完成状态"""
    def pay(self, order: OrderContext):
        print("  [错误] 订单已完成")

    def ship(self, order: OrderContext):
        print("  [错误] 订单已完成")

    def deliver(self, order: OrderContext):
        print("  [错误] 订单已完成")

    def cancel(self, order: OrderContext):
        print("  [错误] 订单已完成，无法取消")

    def __str__(self):
        return "已完成"


class CancelledState(OrderState):
    """已取消状态"""
    def pay(self, order: OrderContext):
        print("  [错误] 订单已取消")

    def ship(self, order: OrderContext):
        print("  [错误] 订单已取消")

    def deliver(self, order: OrderContext):
        print("  [错误] 订单已取消")

    def cancel(self, order: OrderContext):
        print("  [错误] 订单已取消")

    def __str__(self):
        return "已取消"


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("状态模式演示：订单管理系统")
    print("=" * 50)

    order = OrderContext()
    print(f"\n初始状态：{order}")

    print("\n1. 正常流程：")
    order.pay()
    order.ship()
    order.deliver()

    print("\n2. 异常操作测试：")
    print("  [测试] 已完成订单再次支付：")
    order.pay()

    print("\n3. 取消流程：")
    order2 = OrderContext()
    order2.pay()
    print("  [测试] 已支付后取消：")
    order2.cancel()
    print("  [测试] 取消后发货：")
    order2.ship()

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - TCP 连接状态机")
    print("  - 工作流引擎")
    print("  - 游戏角色状态")
    print("  - 电梯控制系统")
    print("=" * 50)
