"""
组合模式 (Composite Pattern) - 结构型模式

【解决的问题】
    1. 树形结构处理：需要统一处理单个对象和组合对象
    2. 部分 - 整体层次结构：客户端希望一致地对待单个对象和组合对象
    3. 递归组合：对象需要递归地包含其他对象

【应用场景】
    1. 树形结构：文件系统、组织架构、UI 组件树
    2. 部分 - 整体关系：菜单系统、XML/HTML 解析
    3. 需要递归操作的场景

【优缺点】
    优点：
        - 客户端代码可以一致地处理单个和组合对象
        - 易于添加新的组件类型
        - 自然地表达树形结构
    缺点：
        - 设计较复杂
        - 叶子节点和组合节点接口可能不一致

【UML 结构】
    Component(组件接口)
         ↑
    +----+----+
    |         |
Leaf(叶子)  Composite(组合，持有子 Component 列表)
"""

from abc import ABC, abstractmethod
from typing import List


# ===== 组件接口 =====
class FileSystemComponent(ABC):
    """文件系统组件接口"""
    @abstractmethod
    def show(self, indent: int = 0) -> str:
        """显示组件信息"""
        pass

    @abstractmethod
    def get_size(self) -> int:
        """获取大小"""
        pass


# ===== 叶子节点 =====
class File(FileSystemComponent):
    """文件 - 叶子节点"""
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def show(self, indent: int = 0) -> str:
        return " " * indent + f"[D] {self._name} ({self._size}KB)"

    def get_size(self) -> int:
        return self._size


# ===== 组合节点 =====
class Folder(FileSystemComponent):
    """文件夹 - 组合节点"""
    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def show(self, indent: int = 0) -> str:
        result = " " * indent + f"[F] {self._name}"
        for child in self._children:
            result += "\n" + child.show(indent + 2)
        return result

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("组合模式演示：文件系统")
    print("=" * 50)

    # 创建文件
    file1 = File("document.txt", 100)
    file2 = File("image.png", 500)
    file3 = File("video.mp4", 10240)
    file4 = File("readme.md", 20)

    # 创建文件夹
    folder1 = Folder("文档")
    folder1.add(file1)
    folder1.add(file4)

    folder2 = Folder("媒体")
    folder2.add(file2)
    folder2.add(file3)

    root = Folder("root")
    root.add(folder1)
    root.add(folder2)
    root.add(File("config.ini", 5))

    # 显示结构
    print("\n文件结构：")
    print(root.show())

    print(f"\n总大小：{root.get_size()}KB")
    print(f"文档文件夹大小：{folder1.get_size()}KB")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 文件系统：文件 + 文件夹")
    print("  - UI 框架：控件容器 + 原子控件")
    print("  - XML/HTML 解析：元素树")
    print("  - 组织架构：部门 + 员工")
    print("=" * 50)
