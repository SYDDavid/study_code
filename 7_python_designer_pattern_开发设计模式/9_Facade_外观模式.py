"""
外观模式 (Facade Pattern) - 结构型模式

【解决的问题】
    1. 复杂系统简化：子系统复杂，客户端使用困难
    2. 降低耦合：客户端与多个子系统类直接耦合
    3. 提供统一入口：需要为子系统提供统一的访问入口

【应用场景】
    1. 复杂系统的简化访问
    2. 需要为子系统提供统一入口
    3. 层次化系统的入口点

【优缺点】
    优点：
        - 简化客户端使用，降低学习成本
        - 解耦客户端和子系统
        - 符合迪米特法则（最少知道原则）
    缺点：
        - 不符合开闭原则，修改外观需要改内部
        - 可能成为"上帝类"，承担过多职责

【UML 结构】
    Client --> Facade(外观类，持有多个子系统引用) --> SubSystem1, SubSystem2, ...
"""


# ===== 子系统 =====
class CPU:
    """CPU 子系统"""
    def freeze(self):
        return "CPU: 冻结"

    def jump(self, position: str):
        return f"CPU: 跳转到 {position}"

    def execute(self):
        return "CPU: 执行指令"


class Memory:
    """内存子系统"""
    def load(self, position: str, data: str):
        return f"内存：在 {position} 加载数据 {data}"


class HardDrive:
    """硬盘子系统"""
    def read(self, lba: str, size: int) -> str:
        return f"硬盘：从 {lba} 读取 {size} 字节"


class GPU:
    """显卡子系统"""
    def render(self):
        return "显卡：渲染画面"


class Audio:
    """音频子系统"""
    def play(self):
        return "音频：播放声音"


# ===== 外观类 =====
class ComputerFacade:
    """电脑外观 - 提供一键开机接口"""
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hd = HardDrive()
        self._gpu = GPU()
        self._audio = Audio()

    def start(self):
        """一键开机"""
        print("=== 电脑启动 ===")
        print(self._cpu.freeze())
        print(self._memory.load("0x00", self._hd.read("MBR", 512)))
        print(self._cpu.jump("0x00"))
        print(self._cpu.execute())
        print(self._gpu.render())
        print(self._audio.play())
        print("=== 启动完成 ===\n")

    def shutdown(self):
        """一键关机"""
        print("=== 电脑关机 ===")
        print("音频：停止播放")
        print("显卡：停止渲染")
        print("CPU: 停止执行")
        print("=== 关机完成 ===\n")


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("外观模式演示：电脑启动系统")
    print("=" * 50)

    # 客户端只需要调用外观类
    computer = ComputerFacade()
    computer.start()
    computer.shutdown()

    print("=" * 50)
    print("实际工程应用：")
    print("  - 框架入口：如 requests.get() 封装 HTTP 细节")
    print("  - 服务层接口：Service 层封装多个 DAO 操作")
    print("  - SDK 封装：将复杂 API 简化为简单接口")
    print("  - 启动器：Spring Boot 的@SpringBootApplication")
    print("=" * 50)
