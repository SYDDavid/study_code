"""
适配器模式 (Adapter Pattern) - 结构型模式

【解决的问题】
    1. 接口不兼容：两个类接口不匹配，无法协同工作
    2. 复用现有类：想复用已有类，但其接口不符合需求
    3. 统一多个接口：多个子类接口不同，需要统一对外接口

【应用场景】
    1. 系统需要使用现有的类，而这些类的接口不符合要求
    2. 想要创建一个可以复用的类，用于与其他不兼容的类合作
    3. 需要统一多个不同接口的子类

【优缺点】
    优点：
        - 让不兼容的类可以一起工作
        - 提高了类的复用性
        - 目标类和适配器类可以独立扩展
    缺点：
        - 过多使用适配器会让系统变得混乱
        - 增加了系统的复杂性

【UML 结构】
    Target(目标接口) <-- Adapter(适配器，继承/实现 Target，持有 Adaptee) <-- Adaptee(被适配者)
"""

from abc import ABC, abstractmethod


# ===== 被适配者：已有的类 =====
class EuropeanSocket:
    """欧式插座（两孔圆插）- 已有的类"""
    def voltage(self):
        return 220

    def plug_in_round(self):
        return "插入欧式圆插头"


# ===== 目标接口：我们需要的接口 =====
class USASocket(ABC):
    """美式插座接口（两孔扁插）- 目标接口"""
    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def plug_in_flat(self):
        pass


# ===== 适配器 =====
class SocketAdapter(USASocket):
    """电源适配器 - 将欧式插座适配为美式插座"""
    def __init__(self, european_socket: EuropeanSocket):
        self._european_socket = european_socket

    def voltage(self):
        # 电压转换：220V -> 110V
        return self._european_socket.voltage() // 2

    def plug_in_flat(self):
        return "通过适配器插入美式扁插头"


# ===== 客户端 =====
class AmericanDevice:
    """美式电器 - 只能使用美式插座"""
    def __init__(self, socket: USASocket):
        self._socket = socket

    def power_on(self):
        print(f"电压：{self._socket.voltage()}V")
        print(self._socket.plug_in_flat())
        print("设备正常工作！")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("适配器模式演示：电源转换器")
    print("=" * 50)

    # 创建欧式插座（现有类）
    european = EuropeanSocket()
    print(f"\n欧式插座：{european.plug_in_round()}，电压：{european.voltage()}V")

    # 创建适配器
    adapter = SocketAdapter(european)

    # 美式电器通过适配器使用欧式插座
    device = AmericanDevice(adapter)
    print("\n美式电器通过适配器连接：")
    device.power_on()

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - JSON/XML 数据格式转换")
    print("  - 第三方库接口封装")
    print("  - 遗留系统接口适配")
    print("=" * 50)
