"""
命令模式 (Command Pattern) - 行为型模式

【解决的问题】
    1. 请求封装：将请求封装为对象，支持参数化
    2. 请求排队/日志：支持请求排队、记录日志、撤销操作
    3. 解耦发送者和执行者：发送者无需知道谁执行了请求

【应用场景】
    1. 撤销/重做功能
    2. 事务操作
    3. 任务队列
    4. 菜单/按钮操作

【优缺点】
    优点：
        - 解耦发送者和接收者
        - 支持撤销/重做
        - 支持请求排队和日志
        - 可以组合命令
    缺点：
        - 增加类的数量
        - 每个命令都需要一个类

【UML 结构】
    Command(命令接口)
         ↑
    ConcreteCommand(具体命令，持有 Receiver)
         ↑
    Invoker(调用者，持有 Command)  -->  Receiver(接收者)
"""

from abc import ABC, abstractmethod
from typing import List


# ===== 接收者 =====
class Light:
    """灯 - 命令接收者"""
    def __init__(self, name: str):
        self._name = name
        self._is_on = False

    def on(self):
        self._is_on = True
        print(f"  {self._name} 灯亮了")

    def off(self):
        self._is_on = False
        print(f"  {self._name} 灯灭了")

    def status(self):
        return f"{self._name}: {'开' if self._is_on else '关'}"


# ===== 命令接口 =====
class Command(ABC):
    """命令接口"""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# ===== 具体命令 =====
class LightOnCommand(Command):
    """开灯命令"""
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(Command):
    """关灯命令"""
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


# ===== 宏命令（组合命令）=====
class MacroCommand(Command):
    """宏命令 - 批量执行多个命令"""
    def __init__(self, commands: List[Command]):
        self._commands = commands

    def execute(self):
        for cmd in self._commands:
            cmd.execute()

    def undo(self):
        for cmd in reversed(self._commands):
            cmd.undo()


# ===== 调用者 =====
class RemoteControl:
    """遥控器 - 命令调用者"""
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        """撤销上一次操作"""
        if self._history:
            cmd = self._history.pop()
            cmd.undo()
        else:
            print("  没有可撤销的操作")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("命令模式演示：智能家居遥控器")
    print("=" * 50)

    # 接收者
    living_light = Light("客厅")
    bedroom_light = Light("卧室")

    # 命令
    living_on = LightOnCommand(living_light)
    living_off = LightOffCommand(living_light)
    bedroom_on = LightOnCommand(bedroom_light)
    bedroom_off = LightOffCommand(bedroom_light)

    # 调用者（遥控器）
    remote = RemoteControl()

    print("\n1. 遥控客厅灯：")
    remote.execute_command(living_on)
    remote.execute_command(living_off)

    print("\n2. 撤销操作：")
    remote.undo()  # 客厅灯重新亮起
    remote.undo()  # 客厅灯熄灭

    print("\n3. 一键全开（宏命令）：")
    all_on = MacroCommand([living_on, bedroom_on])
    remote.execute_command(all_on)

    print("\n4. 一键全关：")
    all_off = MacroCommand([living_off, bedroom_off])
    remote.execute_command(all_off)

    print("\n5. 批量撤销：")
    remote.undo()  # 全关撤销 -> 全开
    remote.undo()  # 全开撤销 -> 全关

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 编辑器撤销/重做")
    print("  - 数据库事务")
    print("  - 任务调度队列")
    print("  - 图形界面按钮事件")
    print("=" * 50)
