"""
中介者模式 (Mediator Pattern) - 行为型模式

【解决的问题】
    1. 对象间多对多通信：多个对象互相引用，形成网状结构
    2. 降低耦合度：对象间直接通信导致高度耦合
    3. 集中控制交互：需要集中管理对象间的交互逻辑

【应用场景】
    1. 聊天室：多个用户通过聊天室通信
    2. 机场塔台：飞机通过塔台协调
    3. 对话框组件：组件通过中介者交互
    4. MVC 中的 Controller

【优缺点】
    优点：
        - 降低对象间耦合度
        - 将多对多通信转为一对多
        - 集中管理交互逻辑
    缺点：
        - 中介者可能变得庞大复杂
        - 增加系统复杂性

【UML 结构】
    Mediator(中介者接口) <-- ConcreteMediator(具体中介者，持有所有 Colleague)
    Colleague(同事接口) <-- ConcreteColleague(具体同事，持有 Mediator)
"""

from abc import ABC, abstractmethod
from typing import Dict, List


# ===== 中介者接口 =====
class ChatMediator(ABC):
    """聊天中介者接口"""
    @abstractmethod
    def send_message(self, message: str, sender: 'User'):
        pass

    @abstractmethod
    def add_user(self, user: 'User'):
        pass


# ===== 具体中介者 =====
class ChatRoom(ChatMediator):
    """聊天室 - 具体中介者"""
    def __init__(self, name: str):
        self._name = name
        self._users: List['User'] = []

    def add_user(self, user: 'User'):
        self._users.append(user)

    def send_message(self, message: str, sender: 'User'):
        """将消息广播给所有其他用户"""
        for user in self._users:
            if user != sender:
                user.receive(message, sender.name)


# ===== 同事类 =====
class User:
    """用户 - 同事类"""
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        self._mediator.add_user(self)

    def send(self, message: str):
        print(f"[{self.name} 发送]: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender_name: str):
        print(f"[{self.name} 收到来自 {sender_name}]: {message}")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("中介者模式演示：聊天室")
    print("=" * 50)

    # 创建聊天室（中介者）
    chat_room = ChatRoom("技术交流群")

    # 创建用户（同事）
    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)

    print("\n1. Alice 发消息：")
    alice.send("大家好！今天讨论设计模式？")

    print("\n2. Bob 回复：")
    bob.send("好呀，我先讲中介者模式！")

    print("\n3. Charlie 加入讨论：")
    charlie.send("我在用着呢！")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - MVC 中的 Controller")
    print("  - 聊天室系统")
    print("  - 机场调度系统")
    print("  - 对话框组件协调")
    print("=" * 50)
