"""
观察者模式 (Observer Pattern) - 行为型模式

【解决的问题】
    1. 一对多依赖：一个对象状态变化，多个对象需要同步更新
    2. 解耦发布者和订阅者：发布者无需知道订阅者是谁
    3. 广播通信：需要向多个对象广播状态变化

【应用场景】
    1. 事件驱动系统
    2. 消息推送/通知
    3. 数据变化实时更新 UI
    4. 日志监控

【优缺点】
    优点：
        - 解耦发布者和订阅者
        - 支持广播通信
        - 符合开闭原则
    缺点：
        - 订阅者收到通知的顺序不确定
        - 可能引发循环依赖
        - 如果订阅者过多，通知可能耗时

【UML 结构】
    Subject(主题接口，持有 Observer 列表) <-- ConcreteSubject(具体主题)
    Observer(观察者接口) <-- ConcreteObserver(具体观察者)
"""

from abc import ABC, abstractmethod
from typing import List


# ===== 观察者接口 =====
class Observer(ABC):
    """观察者接口"""
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


# ===== 主题 =====
class WeatherStation:
    """气象站 - 主题"""
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def attach(self, observer: Observer):
        """注册观察者"""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """移除观察者"""
        self._observers.remove(observer)

    def _notify_all(self):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        """更新气象数据"""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        print(f"\n[气象站] 新数据：温度={temperature}C, 湿度={humidity}%, 气压={pressure}hPa")
        self._notify_all()


# ===== 具体观察者 =====
class PhoneDisplay(Observer):
    """手机显示 - 观察者"""
    def __init__(self, name: str):
        self._name = name

    def update(self, temperature: float, humidity: float, pressure: float):
        print(f"  [手机-{self._name}] 当前温度：{temperature}C")


class TVDisplay(Observer):
    """电视屏显 - 观察者"""
    def update(self, temperature: float, humidity: float, pressure: float):
        print(f"  [电视屏显] 天气简报：{temperature}C | 湿度 {humidity}% | 气压 {pressure}hPa")


class AlarmSystem(Observer):
    """报警系统 - 观察者"""
    def __init__(self):
        self._last_temp = 0.0

    def update(self, temperature: float, humidity: float, pressure: float):
        if temperature > 40:
            print(f"  [!!高温警报!!] 温度 {temperature}C 超过警戒线！")
        if humidity > 90:
            print(f"  [!!湿度警报!!] 湿度 {humidity}% 超过警戒线！")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("观察者模式演示：气象站系统")
    print("=" * 50)

    # 创建气象站
    station = WeatherStation()

    # 创建观察者
    phone = PhoneDisplay("Alice")
    tv = TVDisplay()
    alarm = AlarmSystem()

    # 注册观察者
    station.attach(phone)
    station.attach(tv)
    station.attach(alarm)

    # 更新气象数据（所有观察者自动收到通知）
    station.set_measurements(25.0, 65.0, 1013.0)
    station.set_measurements(35.0, 70.0, 1008.0)
    station.set_measurements(42.0, 95.0, 1002.0)

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 事件监听系统（鼠标点击、键盘输入）")
    print("  - 消息队列（Kafka、RabbitMQ）")
    print("  - Vue/React 响应式数据")
    print("  - 日志框架的 Handler 链")
    print("=" * 50)
