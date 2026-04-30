"""
享元模式 (Flyweight Pattern) - 结构型模式

【解决的问题】
    1. 大量细粒度对象：系统需要创建大量相似对象
    2. 内存占用过高：对象数量过多导致内存消耗大
    3. 对象共享：多个对象可以共享部分状态

【应用场景】
    1. 需要创建大量相似对象的场景
    2. 对象的大部分状态可以共享
    3. 内存成为瓶颈的场景

【优缺点】
    优点：
        - 大幅减少内存占用
        - 提高系统性能
        - 共享对象可以复用
    缺点：
        - 增加了系统的复杂性
        - 需要分离内部状态和外部状态
        - 线程安全问题

【UML 结构】
    Flyweight(享元接口)
         ↑
    +----+----+
    |         |
ConcreteFlyweight(具体享元)   FlyweightFactory(享元工厂，管理共享池)
"""

from typing import Dict, List


# ===== 享元类：文字样式 =====
class FontStyle:
    """文字样式 - 享元类（内部状态：可共享）"""
    def __init__(self, font_family: str, font_size: int, color: str):
        self.font_family = font_family
        self.font_size = font_size
        self.color = color

    def __repr__(self):
        return f"FontStyle({self.font_family}, {self.font_size}, {self.color})"


# ===== 享元工厂 =====
class FontStyleFactory:
    """字体样式工厂 - 管理共享的样式对象"""
    def __init__(self):
        self._styles: Dict[str, FontStyle] = {}

    def get_style(self, font_family: str, font_size: int, color: str) -> FontStyle:
        """获取或创建样式（共享相同样式）"""
        key = f"{font_family}-{font_size}-{color}"
        if key not in self._styles:
            print(f"  [创建新样式] {key}")
            self._styles[key] = FontStyle(font_family, font_size, color)
        else:
            print(f"  [复用样式] {key}")
        return self._styles[key]

    def get_cache_count(self) -> int:
        return len(self._styles)


# ===== 使用享元的类：文字对象 =====
class Text:
    """文字对象 - 持有享元样式（外部状态：位置）"""
    def __init__(self, content: str, x: int, y: int, style: FontStyle):
        self.content = content      # 外部状态
        self.x = x                  # 外部状态
        self.y = y                  # 外部状态
        self.style = style          # 内部状态（共享）

    def render(self):
        return f"'{self.content}' @ ({self.x},{self.y}) - {self.style}"


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("享元模式演示：文本编辑器")
    print("=" * 50)

    factory = FontStyleFactory()

    # 创建大量文字对象，但样式可以共享
    texts: List[Text] = []

    # 标题样式（复用）
    title_style = factory.get_style("微软雅黑", 24, "黑色")
    # 正文样式（复用）
    body_style = factory.get_style("宋体", 12, "灰色")
    # 强调样式（复用）
    highlight_style = factory.get_style("黑体", 14, "红色")

    # 创建 1000 个文字对象
    for i in range(1000):
        if i % 3 == 0:
            style = title_style
        elif i % 3 == 1:
            style = body_style
        else:
            style = highlight_style
        texts.append(Text(f"文字{i}", i % 100, i // 100, style))

    print(f"\n创建了 {len(texts)} 个文字对象")
    print(f"但只使用了 {factory.get_cache_count()} 种样式")
    print(f"节省内存：约 {(1000 - 3) * 100} 字节（假设每个样式 100 字节）")

    print("\n部分文字渲染结果：")
    for text in texts[:5]:
        print(f"  {text.render()}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 文本编辑器：字符样式共享")
    print("  - 游戏开发：子弹、粒子效果共享")
    print("  - 图形界面：图标、按钮样式")
    print("  - 数据库连接池")
    print("=" * 50)
