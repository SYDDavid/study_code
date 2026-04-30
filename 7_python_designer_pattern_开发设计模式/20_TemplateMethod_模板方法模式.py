"""
模板方法模式 (Template Method Pattern) - 行为型模式

【解决的问题】
    1. 复用算法骨架：多个类有相同的算法步骤，但细节不同
    2. 控制子类扩展：父类定义框架，子类实现细节
    3. 避免代码重复：提取公共代码到父类

【应用场景】
    1. 框架设计：Spring 的 JdbcTemplate
    2. 构建流程：编译、测试、打包
    3. 数据迁移：提取、转换、加载（ETL）
    4. 游戏 AI：不同角色有相同的决策框架

【优缺点】
    优点：
        - 复用代码，避免重复
        - 框架控制反转：父类调用子类方法
        - 符合开闭原则
    缺点：
        - 子类限制了父类骨架的灵活性
        - 可能违反里氏替换原则

【UML 结构】
    AbstractClass(抽象类，定义 template_method，声明 abstract 步骤)
         ↑
    ConcreteClass(具体类，实现具体步骤)
"""

from abc import ABC, abstractmethod


# ===== 抽象类 =====
class DataMiner(ABC):
    """数据挖掘器 - 模板方法类"""
    def mine(self):
        """模板方法：定义数据挖掘的骨架"""
        print("\n=== 开始数据挖掘 ===")
        data = self.load_data()
        parsed = self.parse_data(data)
        result = self.analyze(parsed)
        self.output_result(result)
        print("=== 数据挖掘完成 ===\n")

    @abstractmethod
    def load_data(self) -> str:
        """加载数据"""
        pass

    @abstractmethod
    def parse_data(self, data: str):
        """解析数据"""
        pass

    def analyze(self, parsed_data) -> str:
        """分析数据（通用实现，子类可覆盖）"""
        return f"分析结果：{parsed_data}"

    def output_result(self, result: str):
        """输出结果（通用实现）"""
        print(f"输出：{result}")


# ===== 具体类 =====
class PDFMiner(DataMiner):
    """PDF 数据挖掘器"""
    def load_data(self) -> str:
        print("  [PDF] 从文件加载 PDF 数据...")
        return "PDF:raw_data"

    def parse_data(self, data: str):
        print("  [PDF] 解析 PDF 格式...")
        return f"parsed_{data}"


class CSVDataMiner(DataMiner):
    """CSV 数据挖掘器"""
    def load_data(self) -> str:
        print("  [CSV] 从数据库加载 CSV 数据...")
        return "CSV:raw_data"

    def parse_data(self, data: str):
        print("  [CSV] 解析 CSV 格式...")
        return f"parsed_{data}"


class WebScraperMiner(DataMiner):
    """网页数据挖掘器"""
    def load_data(self) -> str:
        print("  [Web] 从网页抓取数据...")
        return "HTML:raw_data"

    def parse_data(self, data: str):
        print("  [Web] 解析 HTML...")
        return f"parsed_{data}"

    def analyze(self, parsed_data) -> str:
        """覆盖分析逻辑"""
        return f"网页分析结果（含 NLP）：{parsed_data}"


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("模板方法模式演示：数据挖掘系统")
    print("=" * 50)

    print("\n1. PDF 数据挖掘：")
    PDFMiner().mine()

    print("2. CSV 数据挖掘：")
    CSVDataMiner().mine()

    print("3. 网页数据挖掘：")
    WebScraperMiner().mine()

    print("=" * 50)
    print("实际工程应用：")
    print("  - Spring JdbcTemplate / RedisTemplate")
    print("  - Servlet 的 doGet/doPost")
    print("  - 单元测试框架（setUp -> test -> tearDown）")
    print("  - 构建工具（compile -> test -> package）")
    print("=" * 50)
