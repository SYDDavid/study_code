"""
桥接模式 (Bridge Pattern) - 结构型模式

【解决的问题】
    1. 多维度变化：类在多个维度上变化，导致类爆炸
    2. 抽象与实现耦合：抽象部分和实现部分绑定在一起，难以独立变化
    3. 运行时切换实现：需要在运行时动态切换不同的实现

【应用场景】
    1. 需要在多个维度上独立扩展的系统
    2. 抽象和实现需要独立变化的场景
    3. 需要在运行时动态组合不同实现的场景

【优缺点】
    优点：
        - 解耦抽象和实现，可以独立变化
        - 符合开闭原则，扩展无需修改源码
        - 避免类爆炸，减少类的数量
    缺点：
        - 增加了系统的理解难度
        - 需要正确识别多个维度

【UML 结构】
    Abstraction(抽象) --持有--> Implementor(实现接口)
         ↑                           ↑
    RefinedAbstraction         ConcreteImplementor
"""

from abc import ABC, abstractmethod


# ===== 实现接口维度：形状绘制方式 =====
class Renderer(ABC):
    """渲染器接口 - 实现维度"""
    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_square(self, side: float):
        pass


class VectorRenderer(Renderer):
    """矢量渲染器"""
    def render_circle(self, radius: float):
        return f"矢量绘制圆形，半径={radius}"

    def render_square(self, side: float):
        return f"矢量绘制正方形，边长={side}"


class RasterRenderer(Renderer):
    """光栅渲染器"""
    def render_circle(self, radius: float):
        return f"光栅绘制圆形，半径={radius}"

    def render_square(self, side: float):
        return f"光栅绘制正方形，边长={side}"


# ===== 抽象维度：形状类型 =====
class Shape(ABC):
    """形状抽象类 - 桥接实现"""
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    """圆形"""
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self._radius = radius

    def draw(self):
        return self._renderer.render_circle(self._radius)


class Square(Shape):
    """正方形"""
    def __init__(self, renderer: Renderer, side: float):
        super().__init__(renderer)
        self._side = side

    def draw(self):
        return self._renderer.render_square(self._side)


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("桥接模式演示：图形渲染系统")
    print("=" * 50)

    # 创建不同的渲染器
    vector = VectorRenderer()
    raster = RasterRenderer()

    # 组合：圆形 + 矢量渲染
    circle1 = Circle(vector, 5)
    print(f"\n{circle1.draw()}")

    # 组合：圆形 + 光栅渲染
    circle2 = Circle(raster, 5)
    print(f"{circle2.draw()}")

    # 组合：正方形 + 矢量渲染
    square1 = Square(vector, 10)
    print(f"{square1.draw()}")

    # 组合：正方形 + 光栅渲染
    square2 = Square(raster, 10)
    print(f"{square2.draw()}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - JDBC：Java 定义接口，各数据库厂商提供实现")
    print("  - 跨平台 UI：抽象组件 + 平台具体实现")
    print("  - 主题系统：组件 + 不同皮肤渲染")
    print("=" * 50)
