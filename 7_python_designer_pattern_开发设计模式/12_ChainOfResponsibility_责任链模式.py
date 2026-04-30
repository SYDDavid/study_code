"""
责任链模式 (Chain of Responsibility Pattern) - 行为型模式

【解决的问题】
    1. 请求多级处理：请求需要经过多个处理者逐级处理
    2. 解耦发送者和接收者：发送者无需知道谁最终处理了请求
    3. 动态组合处理链：处理链可以灵活配置

【应用场景】
    1. 审批流程：逐级审批
    2. 日志记录：不同级别日志不同处理
    3. 中间件链：Web 框架的中间件管道
    4. 异常处理：逐级向上抛出

【优缺点】
    优点：
        - 降低耦合：发送者和接收者解耦
        - 灵活性强：可以动态调整处理链
        - 符合单一职责：每个处理者只做一件事
    缺点：
        - 请求可能不被处理
        - 调试困难：链路过长时难以追踪

【UML 结构】
    Handler(处理者接口，持有下一个 Handler)
         ↑
    ConcreteHandler1 --> ConcreteHandler2 --> ConcreteHandler3
"""

from abc import ABC, abstractmethod
from typing import Optional


# ===== 请求对象 =====
class PurchaseRequest:
    """采购请求"""
    def __init__(self, amount: float, purpose: str):
        self.amount = amount
        self.purpose = purpose


# ===== 处理者接口 =====
class Approver(ABC):
    """审批者抽象类"""
    def __init__(self, name: str):
        self._name = name
        self._next: Optional[Approver] = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        """设置下一个审批者（链式调用）"""
        self._next = approver
        return approver

    @abstractmethod
    def approve(self, request: PurchaseRequest):
        """审批请求"""
        pass

    def _next_approve(self, request: PurchaseRequest):
        """交给下一个审批者"""
        if self._next:
            self._next.approve(request)
        else:
            print(f"  [无人审批] 金额 RMB{request.amount} 的 '{request.purpose}' 请求被搁置")


# ===== 具体处理者 =====
class TeamLeader(Approver):
    """团队组长：可审批 1000 元以下"""
    def approve(self, request: PurchaseRequest):
        if request.amount <= 1000:
            print(f"  [组长 {self._name}] 批准 RMB{request.amount} 用于 '{request.purpose}'")
        else:
            print(f"  [组长 {self._name}] 超出权限，转交上级")
            self._next_approve(request)


class Manager(Approver):
    """经理：可审批 5000 元以下"""
    def approve(self, request: PurchaseRequest):
        if request.amount <= 5000:
            print(f"  [经理 {self._name}] 批准 RMB{request.amount} 用于 '{request.purpose}'")
        else:
            print(f"  [经理 {self._name}] 超出权限，转交上级")
            self._next_approve(request)


class Director(Approver):
    """总监：可审批 20000 元以下"""
    def approve(self, request: PurchaseRequest):
        if request.amount <= 20000:
            print(f"  [总监 {self._name}] 批准 RMB{request.amount} 用于 '{request.purpose}'")
        else:
            print(f"  [总监 {self._name}] 超出权限，转交上级")
            self._next_approve(request)


class CEO(Approver):
    """CEO：可审批任意金额"""
    def approve(self, request: PurchaseRequest):
        print(f"  [CEO {self._name}] 批准 RMB{request.amount} 用于 '{request.purpose}'")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("责任链模式演示：采购审批系统")
    print("=" * 50)

    # 构建审批链：组长 -> 经理 -> 总监 -> CEO
    leader = TeamLeader("张三")
    manager = Manager("李四")
    director = Director("王五")
    ceo = CEO("赵六")

    leader.set_next(manager).set_next(director).set_next(ceo)

    # 发起各种金额的采购请求
    requests = [
        PurchaseRequest(500, "办公文具"),
        PurchaseRequest(3000, "显示器"),
        PurchaseRequest(15000, "服务器"),
        PurchaseRequest(100000, "ERP 系统"),
    ]

    for req in requests:
        print(f"\n采购请求：RMB{req.amount} - {req.purpose}")
        print("-" * 30)
        leader.approve(req)

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - Django 中间件链")
    print("  - Java Servlet Filter")
    print("  - 日志框架：Logger -> Handler 链")
    print("  - 游戏事件传播")
    print("=" * 50)
