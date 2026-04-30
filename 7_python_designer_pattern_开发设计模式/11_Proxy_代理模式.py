"""
代理模式 (Proxy Pattern) - 结构型模式

【解决的问题】
    1. 访问控制：需要控制对对象的访问
    2. 延迟加载：大对象需要延迟初始化
    3. 增强功能：需要在访问对象前后添加额外操作

【应用场景】
    1. 远程代理：为远程对象提供本地代表
    2. 虚拟代理：延迟加载大对象
    3. 保护代理：控制访问权限
    4. 智能代理：访问前后执行额外操作

【优缺点】
    优点：
        - 客户端无需知道代理的存在
        - 可以灵活地添加额外功能
        - 支持开闭原则
    缺点：
        - 增加了系统的复杂性
        - 可能降低请求速度

【UML 结构】
    Subject(主题接口)
         ↑
    +----+----+
    |         |
RealSubject(真实主题)  Proxy(代理，持有 RealSubject)
"""

from abc import ABC, abstractmethod
import time


# ===== 主题接口 =====
class Image(ABC):
    """图片接口"""
    @abstractmethod
    def display(self):
        pass


# ===== 真实主题 =====
class HighResolutionImage(Image):
    """高分辨率图片 - 加载耗时"""
    def __init__(self, filename: str):
        self._filename = filename
        print(f"  [加载图片] {filename}...")
        time.sleep(1)  # 模拟耗时加载
        print(f"  [图片加载完成] {filename}")

    def display(self):
        print(f"  [显示图片] {self._filename}")


# ===== 代理 =====
class ImageProxy(Image):
    """图片代理 - 延迟加载"""
    def __init__(self, filename: str):
        self._filename = filename
        self._image = None  # 延迟初始化

    def display(self):
        if self._image is None:
            print("  [代理：首次访问，开始加载...]")
            self._image = HighResolutionImage(self._filename)
        self._image.display()


# ===== 保护代理示例 =====
class User:
    """用户"""
    def __init__(self, name: str, is_admin: bool):
        self.name = name
        self.is_admin = is_admin


class Document:
    """文档 - 真实主题"""
    def read(self):
        return "文档内容：机密信息..."


class DocumentProxy:
    """文档代理 - 权限控制"""
    def __init__(self, user: User):
        self._user = user
        self._document = Document()

    def read(self):
        if self._user.is_admin:
            return self._document.read()
        else:
            return "拒绝访问：权限不足"


# ===== 案例演示 =====
if __name__ == "__main__":
    print("=" * 50)
    print("代理模式演示：图片延迟加载")
    print("=" * 50)

    # 创建代理（不立即加载）
    print("\n1. 创建代理对象（不加载图片）:")
    proxy = ImageProxy("photo_4K.jpg")

    print("\n2. 首次调用 display（触发加载）:")
    proxy.display()

    print("\n3. 再次调用 display（复用已加载对象）:")
    proxy.display()

    print("\n" + "=" * 50)
    print("代理模式演示：权限控制")
    print("=" * 50)

    admin = User("管理员", is_admin=True)
    guest = User("访客", is_admin=False)

    admin_doc = DocumentProxy(admin)
    guest_doc = DocumentProxy(guest)

    print(f"\n{admin.name} 访问：{admin_doc.read()}")
    print(f"{guest.name} 访问：{guest_doc.read()}")

    print("\n" + "=" * 50)
    print("实际工程应用：")
    print("  - Spring AOP：方法拦截器")
    print("  - RPC 框架：远程服务代理")
    print("  - 图片/视频延迟加载")
    print("  - 数据库访问代理")
    print("=" * 50)
