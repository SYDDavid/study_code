"""
访问者模式 (Visitor Pattern) - 行为型模式

【解决的问题】
    1. 数据结构稳定，操作多变：对象结构稳定（如文件树），但需要不断添加新操作
    2. 操作分散在各处：对同一组对象的操作分散在多个类中
    3. 违反开闭原则：给对象添加新操作需要修改对象类

【应用场景】
    1. 编译器 AST 处理：语法树结构稳定，需要多种操作（类型检查、优化、代码生成）
    2. 文件系统扫描：文件结构稳定，需要不同操作（搜索、统计、备份）
    3. 报表系统：数据结构固定，需要多种报表格式
    4. 图形编辑器：图形元素固定，需要多种操作（渲染、导出、碰撞检测）

【优缺点】
    优点：
        - 符合开闭原则：新增操作无需修改现有类
        - 操作集中管理：相关操作集中在访问者中
        - 累积状态：访问者可以在遍历时累积状态
    缺点：
        - 增加新元素困难：新增元素需要修改所有访问者
        - 破坏封装：访问者需要了解元素内部细节

【UML 结构】
    Element(元素接口，声明 accept) <-- ConcreteElement(具体元素)
    Visitor(访问者接口，为每个元素定义 visit) <-- ConcreteVisitor(具体访问者)
"""

from abc import ABC, abstractmethod
from typing import List


# ===== 元素接口 =====
class FileElement(ABC):
    """文件元素接口"""
    @abstractmethod
    def accept(self, visitor: 'FileVisitor'):
        pass


# ===== 具体元素 =====
class TextFile(FileElement):
    """文本文件"""
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.size = len(content)

    def accept(self, visitor: 'FileVisitor'):
        visitor.visit_text(self)


class ImageFile(FileElement):
    """图片文件"""
    def __init__(self, name: str, width: int, height: int):
        self.name = name
        self.width = width
        self.height = height
        self.size = width * height // 1000  # 模拟大小

    def accept(self, visitor: 'FileVisitor'):
        visitor.visit_image(self)


class VideoFile(FileElement):
    """视频文件"""
    def __init__(self, name: str, duration: int, resolution: str):
        self.name = name
        self.duration = duration
        self.resolution = resolution
        self.size = duration * 10  # 模拟大小

    def accept(self, visitor: 'FileVisitor'):
        visitor.visit_video(self)


# ===== 访问者接口 =====
class FileVisitor(ABC):
    """文件访问者接口"""
    @abstractmethod
    def visit_text(self, file: TextFile):
        pass

    @abstractmethod
    def visit_image(self, file: ImageFile):
        pass

    @abstractmethod
    def visit_video(self, file: VideoFile):
        pass


# ===== 具体访问者 =====
class FileSizeCalculator(FileVisitor):
    """文件大小计算器 - 访问者"""
    def __init__(self):
        self.total_size = 0

    def visit_text(self, file: TextFile):
        self.total_size += file.size
        print(f"  [TXT] {file.name}: {file.size}KB")

    def visit_image(self, file: ImageFile):
        self.total_size += file.size
        print(f"  [IMG] {file.name}: {file.size}KB ({file.width}x{file.height})")

    def visit_video(self, file: VideoFile):
        self.total_size += file.size
        print(f"  [VID] {file.name}: {file.size}KB ({file.duration}s, {file.resolution})")


class FileSearchVisitor(FileVisitor):
    """文件搜索器 - 访问者"""
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.results: List[str] = []

    def visit_text(self, file: TextFile):
        if self.keyword in file.content or self.keyword in file.name:
            self.results.append(file.name)

    def visit_image(self, file: ImageFile):
        if self.keyword in file.name:
            self.results.append(file.name)

    def visit_video(self, file: VideoFile):
        if self.keyword in file.name:
            self.results.append(file.name)


class FileReportGenerator(FileVisitor):
    """文件报告生成器 - 访问者"""
    def __init__(self):
        self._report_lines: List[str] = []

    def visit_text(self, file: TextFile):
        self._report_lines.append(f"| 文本 | {file.name} | {file.size}KB | 内容预览: {file.content[:20]}... |")

    def visit_image(self, file: ImageFile):
        self._report_lines.append(f"| 图片 | {file.name} | {file.size}KB | 分辨率: {file.width}x{file.height} |")

    def visit_video(self, file: VideoFile):
        self._report_lines.append(f"| 视频 | {file.name} | {file.size}KB | 时长: {file.duration}s |")

    def get_report(self) -> str:
        header = "| 类型 | 文件名 | 大小 | 详情 |\n|------|--------|------|------|"
        return header + "\n" + "\n".join(self._report_lines)


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("访问者模式演示：文件系统扫描")
    print("=" * 50)

    # 创建文件列表
    files: List[FileElement] = [
        TextFile("readme.txt", "Welcome to the Visitor Pattern demo!"),
        TextFile("notes.txt", "Design patterns are useful"),
        ImageFile("photo.jpg", 1920, 1080),
        ImageFile("logo.png", 200, 200),
        VideoFile("tutorial.mp4", 600, "1080p"),
        VideoFile("demo.mov", 120, "4K"),
    ]

    print("\n1. 计算所有文件大小：")
    size_calc = FileSizeCalculator()
    for f in files:
        f.accept(size_calc)
    print(f"  总大小：{size_calc.total_size}KB")

    print("\n2. 搜索包含 'tutorial' 的文件：")
    searcher = FileSearchVisitor("tutorial")
    for f in files:
        f.accept(searcher)
    print(f"  找到：{searcher.results}")

    print("\n3. 生成文件报告：")
    reporter = FileReportGenerator()
    for f in files:
        f.accept(reporter)
    print(reporter.get_report())

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - 编译器 AST 处理")
    print("  - 文件系统扫描/搜索")
    print("  - 报表生成")
    print("  - 代码分析工具（如 pylint）")
    print("=" * 50)
